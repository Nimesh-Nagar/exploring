const startEl = document.getElementById("start")
const pauseEl = document.getElementById("pause")
const resetEl = document.getElementById("reset")
const timerEl = document.getElementById("timer")

let interval;
let timeLeft = 1500;  // Start Time for pomodoro in seconds

function updateTimer(){
    let minutes = Math.floor(timeLeft / 60);
    let seconds = timeLeft % 60;
    let formattedTime = `${minutes.toString().padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`

    timerEl.innerHTML = formattedTime
}

function startTimer(){
    interval = setInterval(() => {
        timeLeft--; 
        updateTimer();

        if (timeLeft === 0){
            clearInterval(interval);
            alert("Time's Up !");
            timeLeft = 1500;
            updateTimer();
        }

    }, 1000);
}

function pauseTimer(){
    clearInterval(interval);
}

function resetTimer(){
    clearInterval(interval);
    timeLeft = 1500;
    updateTimer();
}

startEl.addEventListener("click", startTimer)
pauseEl.addEventListener("click", pauseTimer)
resetEl.addEventListener("click", resetTimer)


