import { Router } from "express";
import { getAllTask, createTask, getTask, updateTask, deleteTask } from "../controllers/task.js";

const router = Router();

router.route("/").get(getAllTask).post(createTask);
router.route("/:id").get(getTask).patch(updateTask).delete(deleteTask);


// module.exports = router
export default router

