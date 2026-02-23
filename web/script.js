function startJarvis() {
    eel.start_jarvis();
}

function stopJarvis() {
    eel.stop_jarvis();
    window.close();
}

eel.expose(updateStatus);
function updateStatus(text) {
    const status = document.getElementById("status");
    status.innerText = "● " + text;

    status.className = "status " +
        (text === "Listening" ? "listening" : "sleeping");
}
