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



