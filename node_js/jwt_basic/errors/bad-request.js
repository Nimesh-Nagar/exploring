const CustomAPIError = require('./custom-error')

class BadRequest extends CustomAPIError {
    constructor(message){
        super(message)
        this.statusCode = 500
    }
}

module.exports = BadRequest