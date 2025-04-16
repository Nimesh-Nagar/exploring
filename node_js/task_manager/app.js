import express from "express";
import mongoose from "mongoose";
import dotenv from "dotenv";
import tasks from "./routes/task.routes.js"
import cors from "cors";

// Load environment variables from .env file
dotenv.config();

const app = express();

//middleware
// console.log("-----------------------------------")
app.use(cors())
app.use(express.static("./public"))
app.use(express.json());

//routes
// app.get("/hello", (req, res) => {
//     res.send(`<h1> Task Manager App is Running </h1>`);
// });

app.use("/api/v1/tasks", tasks)
app.use("*", (req, res) => {
    res.status(404).send("Route does not exist")
})
    
const port = process.env.PORT || 3000;
const mongoUrl = process.env.MONGO_URI;

console.log(port)
console.log(mongoUrl)

const start = async () => {
    try{
        const connectionDb = await mongoose.connect(mongoUrl)
        console.log(`MONGODB connected to DB : ${connectionDb.connection.host}`) 

        app.listen(port, () =>{
            console.log(`Server is running on port ${port}`);
        });
    }catch(err){
        console.log(err)
    }
}

start()
