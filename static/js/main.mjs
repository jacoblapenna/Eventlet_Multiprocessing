
var socket =  io.connect(location.origin);
var button = document.getElementById("start");
var span = document.getElementById("data")

button.addEventListener("click", evnet_handler);

function evnet_handler() {
    button.removeEventListener("click", event_handler);
    socket.emit("start_data");
});

socket.on("new_data", function(data) {
    span.innerHTML = data.value;
});