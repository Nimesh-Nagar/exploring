
const getAllTask = (req, res) => {
    res.send("All Task list...")
}

const createTask = (req, res) => {
    res.json(req.body)
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
