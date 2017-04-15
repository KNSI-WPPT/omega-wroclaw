var map;

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

    jQuery("#map_button").click(function () {
        // new google.maps.Marker({
        //     position: new google.maps.LatLng(51.14058982 ,16.95920382),
        //     map: map
        // });
        getStops();
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


            new google.maps.Marker({
                position: new google.maps.LatLng(stopsPositions[i][1], stopsPositions[i][0]),
                map: map
            })
        }
    }


});
