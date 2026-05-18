// === CLOCK ===
function getDate() {
    return new Date().toLocaleTimeString("en-KE", {timeZone: "Africa/Nairobi"});
}

function updateClock() {
    const clockElement = document.getElementById("clock");
    clockElement.textContent = getDate();
}

updateClock();
setInterval(updateClock, 1000);

// === BIO TEXT ANIMATION ===
setTimeout(() => {
    document.querySelectorAll("#bio p span").forEach(el => {
        el.classList.add("text-visible");
    });
}, 800);

// === WEATHER ===
const nairobiCoordinates = [-1.2302285, 36.866615]
const openMeteoApi = "https://api.open-meteo.com/v1/"

const link = `${openMeteoApi}forecast?latitude=${nairobiCoordinates[0]}&longitude=${nairobiCoordinates[1]}&current=temperature_2m,weathercode&timezone=Africa/Nairobi`;


