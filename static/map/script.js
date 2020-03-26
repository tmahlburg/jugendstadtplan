
var map = L.map('stadtplan', {zoomControl: false}).setView([54.095166, 13.3710154], 17);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

function onMapClick(e) {
    alert("You clicked the map at " + e.latlng);
}

L.control.zoom({
     position:'bottomleft'
}).addTo(map);

map.on('click', onMapClick);
