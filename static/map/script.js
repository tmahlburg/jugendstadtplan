var map;

function setup_map(viewpoint = [54.095166, 13.3710154]) {
    map = L.map('map', {zoomControl: false}).setView(viewpoint, 17);
	L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
	}).addTo(map);

	L.control.zoom({position:'bottomleft'}).addTo(map);
	map.on('click', onMapClick);
}

var popup = L.popup();
function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("Aktuelle Position: " + e.latlng.toString())
        .openOn(map);
}
