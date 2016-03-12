function loadMap() {
    L.mapbox.accessToken = 'pk.eyJ1IjoiYWtpZXZldCIsImEiOiJjaWp5OGpicWUxb3o1dmdsejBmc3FtaTdzIn0.qYjA6WKb3HwbpS33GAEqZA';

    var mapContainer = document.getElementsByClassName('map__container')[0];
    var mapBoxId = mapContainer.getAttribute('data-map');
    var mapId = mapContainer.children[0].id;

    L.mapbox.map(mapId, mapBoxId);
}

document.addEventListener("DOMContentLoaded", function() {
    console.log('js loaded');
    loadMap();
});
