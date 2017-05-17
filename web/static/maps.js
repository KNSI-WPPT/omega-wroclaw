var map;
var markers = [];
var infoWindows = [];
var wroclawCoords = new google.maps.LatLng(51.110679, 17.036151);

function initialize() {
    var mapOptions = {
        zoom: 14,
        center: wroclawCoords,
        max: 12
    };
    map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
    map.setMapTypeId(google.maps.MapTypeId.ROADMAP);
}


$(document).ready(function () {
    initialize();

    jQuery("#stops_button").click(function () {
        getStops();
    });


    jQuery("#hide_stops_button").click(function () {
        clearMarkers();
        markers = [];
    });
    function getStops() {
        $.ajax({
            type: 'GET',
            url: '/resources/stops',
            async: true,
            dataType: 'json',
            success: function (response) {
                parseStops(response);
            }
        });
    }

    function parseStops(data) {
        var stops = data.stops;
        for (var i = 0; i < stops.length; i++) {

            var stopType =  stops[i].type;
            var stopId = stops[i].id;
            var stopLat = stops[i].lat;
            var stopLng = stops[i].lng;
            
            var pinType;
            if (stopType === 2) {
                pinType = 'mixed-circle.png';
            } else if (stopType === 1) {
                pinType = 'red-circle.png';
            } else {
                pinType = 'blu-circle.png';
            }

            // this could be moved outside the loop
            var pinIcon = new google.maps.MarkerImage(
                "http://localhost:5000/resources/" + pinType,
                null, /* size is determined at runtime */
                null, /* origin is 0,0 */
                null, /* anchor is bottom center of the scaled image */
                new google.maps.Size(20, 20)
            );
            // or https://chart.googleapis.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2%7C870f57
            // for custom symbols and RGB colors

            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(stopLat, stopLng),
                map: map,
                icon: pinIcon
            });
            marker.content = 'Stop: ' + stopId;
            markers.push(marker);

            var infoWindow = new google.maps.InfoWindow();

            markers[i].addListener('click', function () {
                infoWindow.setContent(this.content);
                infoWindow.open(map, this);
            });
        }
    }
});

function setMapOnAll(map) {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(map);
    }
}

// Removes the markers from the map, but keeps them in the array.
function clearMarkers() {
    setMapOnAll(null);
}

// Shows any markers currently in the array.
function showMarkers() {
    setMapOnAll(map);
}

// Deletes all markers in the array by removing references to them.
function deleteMarkers() {
    clearMarkers();
    markers = [];
}
