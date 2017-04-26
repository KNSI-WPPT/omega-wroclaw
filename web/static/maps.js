var map;
var markers = [];
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
            url: "/stops",
            async: true,
            success: function (data) {
                parseStops(data);
            }
        });
    }

    function parseStops(data) {
        var stopsPositions = data.split("\n");

        for (var i = 0; i < stopsPositions.length; i++) {
            stopsPositions[i] = stopsPositions[i].split(';');
            stopsPositions[i][0] = stopsPositions[i][0].replace(",", ".");
            stopsPositions[i][1] = stopsPositions[i][1].replace(",", ".");


            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(stopsPositions[i][1], stopsPositions[i][0]),
                map: map
            });
            markers.push(marker);
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
