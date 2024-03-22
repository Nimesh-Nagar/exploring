const btnEl = document.getElementById("btn")
const errorMessageEl = document.getElementById("errorMsg")

const galleryEl = document.getElementById("gallery")

async function fetchImage(){

    const inputValue = document.getElementById('input').value;

    if(inputValue > 10 || inputValue < 1){
        errorMessageEl.style.display = "block"
        errorMessageEl.innerText = "Number Should be between 0 and 11"
        return
    }

    let imgs = "";

    try {
        btnEl.style.display = "none";
        const loading = `<img src="spinner.svg" />` ;
        galleryEl.innerHTML = loading;

        await fetch(`https://api.unsplash.com/photos?per_page=${inputValue}&page=${Math.round(Math.random() * 1000)}&client_id=YwZe_1GYXWVbPWhbwX16O4j9EtVUYNuQ1aYtu-GyAmU`).then((res)=>res.json().then((data)=>{
        // console.log(data);
        if(data){
           data.forEach((pic)=>{
            // console.log(pic.urls.small);

            imgs += `<img src=${pic.urls.small} alt="Image"/>`;
            galleryEl.style.display = "block";
            galleryEl.innerHTML = imgs;
            btnEl.style.display = "block";
            errorMessageEl.style.display = "none"
           });
        }
    }))

        
    } catch (error) {
        console.log(error);
        errorMessageEl.style.display = "block";
        errorMessageEl.innerHTML = "An Error occured! Try Again Later"

        btnEl.style.display = "block";
        galleryEl.style.display = "none"
        
    }

}

btnEl.addEventListener("click", fetchImage)
