// check username, password in post(login) request
// if exist create new JWT
// send back to fron-end
// setup authentication so only the request with JWT can access the dasboard

const jwt = require('jsonwebtoken')
const BadRequest = require('../errors')

//login
const login = (req,res) => {
    const {username, password} = req.body
    // mongoose validation
    // Joi
    // check in the controller
    if (!username || !password){
        throw new BadRequest('Please Provide Email and Password')
    }

    //just for demo, normally provided by DB!!!!
    const id = new Date().getDate()

    // try to keep payload small, better experience for user
    // just for demo, in production use long, complex and unguessable string value!!!!!!!!!
    const token = jwt.sign({ id, username }, process.env.JWT_SECRET, {
        expiresIn: '30d',
    })
    
    res.status(200).json({ msg: 'user created', token})

}

//dashboard 
const dashboard = async (req,res) => {
    const luckyNumber = Math.floor( Math.random()*100 )
    // console.log("REQUEST Dashboard : ",req)

    res.status(200).json({
        msg : `Hello, ${req.user.username} `,
        secret: `Here is your authorized data, your lucky number is ${luckyNumber}`,
    })
    
}


module.exports = {
    login,
    dashboard
}