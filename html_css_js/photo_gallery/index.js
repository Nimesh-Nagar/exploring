const btnEl = document.getElementById("btn")
const errorMessageEl = document.getElementById("errorMsg")

function fetchImage(){

    const inputValue = document.getElementById('input').value;

    if(inputValue > 10 || inputValue < 1){
        errorMessageEl.style.display = "block"
        return
    }

    fetch(`https://api.unsplash.com/photos?per_page=${inputValue}&page=1&client_id=YwZe_1GYXWVbPWhbwX16O4j9EtVUYNuQ1aYtu-GyAmU`).then((res)=>res.json().then((data)=>{
        console.log(data);
    }))


}


btnEl.addEventListener("click", fetchImage)