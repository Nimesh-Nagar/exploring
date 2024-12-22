import mongoose, { Schema } from "mongoose";

const TaskSchema = new mongoose.Schema({
    name : {
        type: String,
        required : [true, 'must provide name'],  // array indicate validator and message 
        tirm : true,
        maxlength : [20, 'Name can not be more than 20 character']
    },
    completed : {
        type : Boolean,
        default : false
    }
});

const Task = mongoose.model("Task", TaskSchema)

export { Task }