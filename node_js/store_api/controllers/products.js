const Product = require("../models/product.models")

// for Static data (hard-coded)
const getAllProductsStatic = async (req, res) =>{
    // throw new Error('Testing async error')
    // const products  = await Product.find({ featuredd : true }) 
    // const products  = await Product.find({ name : 'entertainment center' }) //find by name
    // const products  = await Product.find({}).sort('-name price') //sort product by name and price
    // const products  = await Product.find({}).select('name price') //select product by name and price

    // const products  = await Product.find({})
    // .sort('name')         // sort in accending or decendiong order
    // .select('name price') // shows only specified feild 
    // .limit(4)       //show ony limited items
    // .skip(1)        // skips first item

    const products = await Product.find({ price : { $gt : 30 } }).sort('price').select('price name'); 


    res.status(200).json({ products, count : products.length })
}

// for Dynamic data
const getAllProducts = async (req, res) =>{
    // console.log(req.query)
    const { featured, company, name, sort, fields, numericFilters } = req.query;
    console.log("Query parameters : ",req.query)
    const queryObject = {}

    if(featured) {
        queryObject.featured = featured === 'true' ? true : false   
    }

    if(company){
        queryObject.company = company
    }

    if(name){
        queryObject.name = { $regex: name, $option: 'i' }
    }    

    if(numericFilters){
        const operatorMap = {
            ">" : "$gt",
            ">=" : "$gte",
            "=" : "$eq",
            "<" : "$lt",
            "<=" : "$lte",
        };
        const regEx = /\b(<|>|>=|=|<=)\b/g;
        let filters = numericFilters.replace(regEx, (match) => `-${operatorMap[match]}-`); 
        // console.log(filters)

        const options = ['price', 'rating'];

        filters = filters.split(',').forEach(item => {
            const [field, operator, value] = item.split('-')
            if(options.includes(field)){
                queryObject[field] = { [operator] : Number(value)};
            }
        });
        // console.log(queryObject)

    }
    console.log(queryObject)

    // sort the data 
    let result = Product.find(queryObject)
    if(sort){
        const sortList = sort.split(',').join(' ')
        result = result.sort(sortList)   
    }
    else{
        result = result.sort('createdAt')
    }

    //select particilar field
    if(fields){
        const fieldsList = fields.split(',').join(' ')
        result = result.select(fieldsList)
    }

    const page = Number(req.query.page) || 1
    const limit = Number(req.query.limit) || 10
    const skip = (page - 1) * limit
    
    result = result.skip(skip).limit(limit) 
    // eg. we have 23 products
    // limit is 7 number of pages required ?
    // 7,7,7,2 = 4 pages

    const products = await result
    res.status(200).json({ products, count : products.length })

}


module.exports = {
    getAllProductsStatic, 
    getAllProducts
}

