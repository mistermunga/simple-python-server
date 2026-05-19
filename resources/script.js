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
async function fetchWeather() {
    const response = await fetch("/weather");
    return await response.json();
}

async function updateWeather() {
    try {
        const data = await fetchWeather();
        document.getElementById("weather").textContent =
            `${data.temperature}°C`;
    } catch (error) {
        document.getElementById("weather").textContent = "–";
    }
}

updateWeather();
setInterval(updateWeather, 60000); // refresh display every minute
