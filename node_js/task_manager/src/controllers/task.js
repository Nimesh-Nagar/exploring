import { Task } from "../models/tasks.model.js";

const getAllTask = async (req, res) => {
    try {
        const getTask = await Task.find(req.body)
        res.status(200).json( {getTask} )
        
    } catch (error) {
        res.status(500).json( {msg : error} )
    }
    
}

const createTask = async (req, res) => {
    
    try {
        const task = await Task.create(req.body)
        console.log("POST Req. ")

        res.status(201).json({ task })
        console.log(req.body)
    
    } catch (error) {
        res.status(500).json( {msg : error} ) 
    }
    
}

const getTask = async (req, res) => {
    try {
        const {id : taskID} = req.params
        const task = await Task.findOne({ _id : taskID })

        if(!task){
            return res.status(404).json({msg : `No Task with id: ${taskID}`})
        }

        res.status(200).json({ task })

    } catch (error) {
        res.status(500).json( {msg : error} )
    }

}

const updateTask = async(req, res) => {
    try{
        const { id: taskID } = req.params;
        const task = await Task.findOneAndUpdate( {_id : taskID}, req.body, {
            new : true,
            runValidators : true
        } );

        if(!task){
            return res.status(404).json({msg : `No task found with id : ${taskID}`});
        }
        res.status(200).json( {task} )

    }catch(error){
        res.status(500).json( {msg : error} )
    }
}

const deleteTask = async (req, res) => {
    try {
        const { id: taskID} = req.params;
        const task = await Task.findOneAndDelete( {_id : taskID });
        if(!task){
            return res.status(404).json( {msg : `No task Found with id : ${taskID}`} );
        }

        res.status(200).json({ task });

    } catch (error) {
        res.status(500).json( {msg : error });
    }
}


export { getAllTask, createTask, getTask, updateTask, deleteTask }
