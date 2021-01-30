var map;
function setup_map(viewpoint = [54.08950301403954, 13.40512275695801], zoom = 14) {
    map = L.map('map', {zoomControl: false}).setView(viewpoint, zoom);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.control.zoom({position:'bottomright'}).addTo(map);
    map.on('click', onMapClick);
}

var popup = L.popup();
function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("<a href=\"/suggestion/?lat=" + e.latlng.lat + "&lng=" + e.latlng.lng + "\">Hier einen neuen Ort vorschlagen</a>")
        .openOn(map);
}

function close_toast(btn) {
    ((btn.parentNode).parentNode).removeChild(btn.parentNode);
}
