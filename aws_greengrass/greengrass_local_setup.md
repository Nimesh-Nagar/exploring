# Greengrass v2 — working local setup (Lima Ubuntu VM on macOS M1)

Status as of 2026-09-07: Nucleus running, Greengrass CLI 2.18.3, first custom
component `com.example.HelloWorld` 1.0.0 deployed successfully via local deployment.

## Environment

| Thing                   | Value                                             |
| ----------------------- | ------------------------------------------------- |
| Core device thing name  | `GGCoreMacOS-2108`                                |
| Region                  | `ap-south-1`                                      |
| Nucleus root            | `/greengrass/v2`                                  |
| Installer files         | `~/cloud/GreengrassInstaller`                     |
| Component dev workspace | `~/cloud/gg_workspace` (`recipes/`, `artifacts/`) |
| IoT role alias          | `GreengrassV2TokenExchangeCoreDeviceRoleAlias`    |

## The command that works

```bash
sudo /greengrass/v2/bin/greengrass-cli deployment create \
  --recipeDir /home/nimesh/cloud/gg_workspace/recipes \
  --artifactDir /home/nimesh/cloud/gg_workspace/artifacts \
  --merge "com.example.HelloWorld=1.0.0"
```

Absolute paths are required in practice — the CLI resolves relative paths against
the JVM cwd, which is easy to get wrong under `sudo`.

Remove:

```bash
sudo /greengrass/v2/bin/greengrass-cli deployment create --remove "com.example.HelloWorld"
```

## Required layout

```
~/cloud/gg_workspace/
  recipes/com.example.HelloWorld-1.0.0.yaml      # <ComponentName>-<Version>.yaml
  artifacts/com.example.HelloWorld/1.0.0/hello_world.py   # <Name>/<Version>/<files>
```

Both conventions are strict. Local deployments copy artifacts by directory
convention only — the recipe needs no `Artifacts:` section, and if the
`<Name>/<Version>/` path is absent nothing is copied and no error is raised at
deploy time.

## Working recipe

```yaml
RecipeFormatVersion: "2020-01-25"
ComponentName: com.example.HelloWorld
ComponentVersion: "1.0.0"
ComponentDescription: "My first custom Python Hello World component."
ComponentPublisher: "Nimesh"
Manifests:
  - Platform:
      os: linux
    Lifecycle:
      Run: python3 -u {artifacts:path}/hello_world.py
```

## Failures hit and what each meant

1. `recipeFormatVersion is marked non-null but is null` — recipe used lowercase
   keys and `recipeFormatVersion: '2.0'`. The schema is PascalCase and the only
   valid format version is the literal `2020-01-25`.
2. `NoSuchFileException: /home/nimesh/gg_workspace/recipes` — wrong `--recipeDir`;
   the workspace lives under `~/cloud/`.
3. `python3: can't open file '.../packages/artifacts/com.example.HelloWorld/1.0.0/hello_world.py': [Errno 2]`
   — artifact source layout didn't match `<artifactDir>/<Name>/<Version>/`, so the
   copy into the component store was a no-op.
4. Errno 2 vs Errno 13: ENOENT means the artifact genuinely wasn't copied;
   EACCES/Permission denied would instead point at `ggc_user` permissions.

## Notes

- `Run` lifecycle scripts that exit 0 land in state `FINISHED`, not an error.
  Use `Startup`/`Shutdown` for long-lived services the nucleus supervises.
- Bump `ComponentVersion` (and rename the recipe file) on every edit — re-merging
  the same version against changed files is the main source of "my change didn't
  take effect".
- `stdout` from the component goes to `/greengrass/v2/logs/<ComponentName>.log`,
  not the terminal. Deployment/resolution errors go to `greengrass.log`.
- Local deployments are NOT cloud deployments: the component does not appear under
  Greengrass → Components → My components. It does appear on the core device's
  Components tab, reported by the Fleet Status Service.

## Next steps

- Register the component in the cloud (S3 artifact + `Artifacts:` URI + IAM
  `s3:GetObject` on the token exchange role), then deploy from the console.
- When revising the console deployment, keep `aws.greengrass.Cli` selected — a
  revision replaces the whole component set for the target.
- IPC pub/sub (`awsiotsdk`, `aws.greengrass.ipc.mqttproxy` accessControl) to see
  component output in the IoT Core MQTT test client.
- `aws.greengrass.LocalDebugConsole` on port 1441 — needs a Lima port forward to
  reach from macOS.
