require('dotenv').config()
//async errors

const express = require('express');
const app = express();

const notFoundMiddleware = require('./middleware/not-found');
const errorMiddleware = require('./middleware/error-handler');

const connectDB = require("./db/connect")
const products = require("./routes/products.routes.js")

//middleware
app.use(express.json())

const port = process.env.PORT || 3000;
const mongo_url = process.env.MONGO_URI; 

//routes
app.get('/', (req, res) => {
    res.send("<h1> Store API</h1> <a href='/api/v1/products'>Products Route </a>")
})

app.use('/api/v1/products', products)

//product route
app.use(notFoundMiddleware);
app.use(errorMiddleware);

const start = async () => {
    try {
        //connect to DB
        await connectDB(process.env.MONGO_URI); 
        app.listen(port, () => {
            console.log(`Server is running on port : ${port}`)
        })
    } catch (error) {
        console.log(error)
    }
}

start()