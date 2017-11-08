var map;
var markers = [];
var wroclawCoords = new google.maps.LatLng(51.110679, 17.036151);
var busToDisplay = ["100","103"];
var LastBusData = [];
var CurrentBusData = [];
var socket = io('http://localhost:5000');
var busPositions = [];

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

    jQuery("#100").click(function () {
        if(busToDisplay.indexOf(this.id)===-1) {
            busToDisplay.push(this.id);
            displayBus();
            console.log("bus number 100 added");
        }
        else {
            console.log("bus number 100 removed");
        }
    });

    jQuery("#103").click(function () {
        if(busToDisplay.indexOf(this.id)===-1) {
            busToDisplay.push(this.id);
            displayBus();
            console.log("bus number 103 added");
        }
        else {
            console.log("bus number 103 removed");
        }
    });

    jQuery("#display_buses_button").click(function () {
        CalculateActualBusPositions();
        deployBuses();
    });

    function getStops() {
        $.ajax({
            type: 'GET',
            url: '/resources/stops',
            async: true,
            dataType: 'json',
            success: function (response) {
                parseStops(response);
            },
            error: function () {
                alert("There was an error while fetching bus positions");
            }
        });
    }

    function parseStops(data) {
        var stops = data.stops;
        for (var i = 0; i < stops.length; i++) {

            var stopType = stops[i].type;
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


socket.on('connect',function() {
    console.log("polaczono");
});

socket.on('disconnect',function () {
    console.log("disconect");
});

socket.on('serial data',function (data) {
    JSONtoArray(data.bus_location_data);
    //if(CurrentBusData.length !== 0 && LastBusData.length !== 0)

});

function JSONtoArray(data) {
    CurrentBusData = LastBusData.slice(0);
    LastBusData = [];
    for(var i = 0;i<data.length;i++) {
        LastBusData[i] = data[i];
        console.log(LastBusData[i])
    }
}

function CalculateActualBusPositions() {

    var tmplong = 0;
    var tmplat = 0;

    for(var i = 0;i<LastBusData.length; i++){
        busPositions[i] = [];
        var k =0;
        while(k <= 500){
            tmplong = k*((LastBusData[i].longitude-CurrentBusData[i].longitude)/500)+parseFloat(CurrentBusData[i].longitude);
            tmplat = k*((LastBusData[i].latitude-CurrentBusData[i].latitude)/500)+parseFloat(CurrentBusData[i].latitude);
            busPositions[i].push({id:LastBusData[i].id,position:new google.maps.LatLng(tmplat,tmplong)});
            k++;
        }
    }
}

function deployBuses() {
    var pinIcon = new google.maps.MarkerImage(
        "http://localhost:5000/resources/bus-circle.png",
        null, /* size is determined at runtime */
        null, /* origin is 0,0 */
        null, /* anchor is bottom center of the scaled image */
        new google.maps.Size(20, 20)
    );
    var markers = [];
    for(var i = 0; i<busPositions.length;i++) {
        markers.push(new google.maps.Marker({
            position: busPositions[i][0].position,
            map: map,
            icon: pinIcon
        }));
    }

    var n = 1;
    var myInterval = setInterval(function () {
        if(n>=50) {
            breakInterval(myInterval);
            for(var i = 0; i < markers.length; i++)
                markers[i].setMap(null)
            CalculateActualBusPositions();
            deployBuses();
        }
        for(var i = 0; i<markers.length;i++)
            markers[i].setPosition(busPositions[i][n].position)
        n++;
    },10)
}

function breakInterval(interval){
    clearInterval(interval);
}

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

// Page style functions
$("#mobile-button").on("click", function () {
    $("#debug_panel").toggle()
    $("#mobile-button-lines").toggle()
    $("#mobile-button-close-panel").toggle()
})