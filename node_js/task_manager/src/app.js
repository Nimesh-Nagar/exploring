import express from "express";
const app = express();

import tasks from "./routes/task.routes.js"

//middleware
app.use(express.json());

//routes
app.get("/hello", (req, res) => {
    res.send(`<h1> Task Manager App is Running </h1>`);
});

app.use("/api/v1/tasks", tasks)
    


const port = 3000;

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);

});