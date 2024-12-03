import { Task } from "../models/tasks.model.js";

const getAllTask = (req, res) => {
    res.send("All Task list...")
}

const createTask = async (req, res) => {
    const task = await Task.create(req.body)
    res.status(201).json({ task })

    console.log(req.body)
}

const getTask = (req, res) => {
    res.json({ id : req.params.id } )
    console.log(req.params)
}

const updateTask = (req, res) => {
    res.send("Update Task...")
}

const deleteTask = (req, res) => {
    res.send("Delete Task...")
}


export { getAllTask, createTask, getTask, updateTask, deleteTask }
