const Product = require("../models/product.models")

// for Static data (hard-coded)
const getAllProductsStatic = async (req, res) =>{
    // throw new Error('Testing async error')
    // const products  = await Product.find({ featuredd : true }) 
    // const products  = await Product.find({ name : 'entertainment center' }) //find by name

    const products  = await Product.find({}).sort('-name, price') //sort product by name
    res.status(200).json({ products, count : products.length })
}

// for Dynamic data
const getAllProducts = async (req, res) =>{
    // console.log(req.query)
    const { featured, company, name, sort } = req.query;
    console.log(req.query)
    const queryObject = {}

    if(featured) {
        queryObject.featured = featured === 'true' ? true : false   
    }
    console.log(queryObject)

    if(company){
        queryObject.company = company
    }

    if(name){
        queryObject.name = { $regex: name, $option: 'i' }
    }    
    // console.log(queryObject)

// sort the data 
    let result = Product.find(queryObject)
    if(sort){
        const sortList = sort.split(',').join(' ')
        result = result.sort(sortList)
    }
    else{
        result = result.sort('createdAt')
    }

    const products = await result
    res.status(200).json({ products, count : products.length })

}


module.exports = {
    getAllProductsStatic, 
    getAllProducts
}

