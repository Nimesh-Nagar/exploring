const apikey =  "5c2320ed72ed629f598cba365eca1e9f";
//const apikey =  "60d07b366f18b29246ed0eb41fb6bc20";


const weatherDataEl = document.getElementById('weather-data')

const cityEventEl = document.getElementById('city-input')

const formEl = document.querySelector("form")


formEl.addEventListener("submit", (event)=>{
    event.preventDefault();
    const cityName = cityEventEl.value;
    console.log(cityName)
    getWeatherData(cityName)

});

async function getWeatherData(cityValue){
    try{
        const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${cityValue}&appid=${apikey}&units=metric`)

        if(!response.ok){
            throw new Error("Network Resonce is not Ok")
        }

        const data = await response.json()
        console.log(data)

        const temperature = Math.round(data.main.temp)

        const description = data.weather[0].description

        const icon = data.weather[0].icon

        const details = [
            `Feels Like : ${Math.round(data.main.feels_like)} °C`,
            `Humidity : ${data.main.humidity} %`,
            `Wind Speed : ${data.wind.speed} m/s` 

        ]

        // Dynamically changing data in website
        weatherDataEl.querySelector('.icon').innerHTML = `<img src="https://openweathermap.org/img/wn/${icon}.png" alt="Weather Icon">`;

        weatherDataEl.querySelector('.temperature').textContent = `${temperature} °C`;
        weatherDataEl.querySelector('.description').textContent = description ;

        weatherDataEl.querySelector('.details').innerHTML = details.map((detail)=> `<div>${detail}</div>`).join(""); 

        
    }catch (error){
        weatherDataEl.querySelector('.icon').innerHTML = ""
        weatherDataEl.querySelector('.temperature').textContent = "";
        weatherDataEl.querySelector('.description').textContent = "Error Occured ! Please Try Again Later" ;
        weatherDataEl.querySelector('.details').innerHTML = ""; 


    }
}

