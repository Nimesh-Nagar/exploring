# Greengrass v2 — learning roadmap

Companion to `claude/greengrass-local-setup.md` (which covers the working local
setup and the failure modes already hit). Written 2026-10-28.

Starting point: local deployment of `com.example.HelloWorld` works. Cloud
deployment walked through but not confirmed.

Each stage has something to build — Greengrass concepts don't stick from reading.

---

## Stage 0 — Close the cloud loop

**Concepts:** component registry vs S3 vs deployment; immutable versions; a
deployment is a declarative desired state, not a push.

**Build:**

1. Upload artifact to S3 under `artifacts/<Name>/<Version>/`
2. Recipe gains an `Artifacts:` section with the `s3://` URI
3. `s3:GetObject` inline policy on the role behind
   `GreengrassV2TokenExchangeCoreDeviceRoleAlias` (NOT on your IAM user)
4. `aws greengrassv2 create-component-version --inline-recipe fileb://<recipe>`
5. Wait for `componentState: DEPLOYABLE`
6. Console → Deployments → **Revise** the existing one (keep `aws.greengrass.Cli`
   ticked — a revision replaces the entire component set for the target)

**Done when:** a configuration merge from the console (`{"Iterations": 3}`)
changes the component's behaviour with no device-side action.

**Key trap:** overwriting the same S3 key does NOT update devices. The version is
already resolved and cached. New code = new version number, always.

---

## Stage 1 — GDK (Greengrass Development Kit)

Turns Stage 0's six manual steps into `gdk component publish`.
`"version": "NEXT_PATCH"` in `gdk-config.json` auto-bumps.

```bash
pip3 install --break-system-packages \
  git+https://github.com/aws-greengrass/aws-greengrass-gdk-cli.git@v<latest-tag>
gdk component init -l python -t HelloWorld -n com.example.HelloWorld
gdk component build
gdk component publish
```

Do this BEFORE Stage 2 — IPC work means dozens of version bumps.

---

## Stage 2 — IPC (the actual programming model)

Where Greengrass stops being a deployment system and becomes an edge runtime.

**Concepts:**

- `PublishToTopic` / `SubscribeToTopic` — local pub/sub, works with WAN down
- `PublishToIoTCore` / `SubscribeToIoTCore` — the cloud hop
- `GetConfiguration` / `SubscribeToConfigurationUpdate` — reconfigure a running
  component without restarting it
- `accessControl` in `ComponentConfiguration.DefaultConfiguration` — gates all of
  the above; denied by default

**Build:** producer component simulating sensor readings → local bus → consumer
component that aggregates and publishes a rolling summary to IoT Core.

**Needs:** `pip3 install awsiotsdk`, and the core device's IoT policy must allow
`iot:Publish` on the topic (separate from `accessControl`, which only governs the
component→nucleus hop).

---

## Stage 3 — Offline-first

**Concepts:** `StreamManager` (store-and-forward to S3/Kinesis/IoT Analytics),
local shadows, `ShadowManager` sync strategies.

**Build / test:** cut the VM's network, keep the producer running, restore the
network, confirm nothing was lost. This property is the reason Greengrass exists.

---

## Stage 4 — AWS-managed components

- `aws.greengrass.LogManager` — component logs → CloudWatch
- `aws.greengrass.LocalDebugConsole` — port 1441, needs a Lima port forward to
  reach from macOS
- `aws.greengrass.SecretManager` — pull secrets to the edge
- `aws.greengrass.ShadowManager` + MQTT bridge
- `aws.greengrass.clientdevices.*` (ClientDeviceAuth, IPDetector, MQTT broker) —
  other LAN devices connect _through_ the core instead of directly to AWS. The
  real fleet-architecture unlock.
- `aws.greengrass.DockerApplicationManager` — how most teams ship non-Python work

---

## Stage 5 — Fleet operations

Thing groups instead of single-thing targeting; deployment policies (failure
handling / rollback, component update policy, configuration validation); OTA
nucleus upgrades; Fleet Status Service + CloudWatch alarms.

**Build:** a second Lima VM as a two-device fleet. Most of this is invisible with
one device.

---

## Stage 6 — Infrastructure as code

Component versions and deployments are CDK/CloudFormation resources
(`AWS::GreengrassV2::ComponentVersion`, `AWS::GreengrassV2::Deployment`).
Likely the fastest stage given existing CDK experience, and the one that makes
everything reproducible instead of console clicks. Pair with a CI pipeline that
runs `gdk component publish` on merge.

---

## Stage 7 — Capstone: industrial edge

Modbus / OPC-UA ingestion → local rule evaluation → buffered sync upward, with
Node-RED running as a Greengrass component. The architecture behind real
shop-floor deployments: local control that never depends on the WAN, with managed
deployment and versioned rollback on top.

---

## Notes

- Lambda components exist but are legacy — learn only if inherited in an existing
  stack.
- Docker components slot in anywhere after Stage 2.
- Stages 2, 3 and 7 have the thinnest public material — most Greengrass content
  stops at Hello World.
