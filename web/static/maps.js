var map;
var stopMarkers = [];
var busMarkers = [];
var wroclawCoords = new google.maps.LatLng(51.110679, 17.036151);
var busToDisplay = [100,103];
var LastBusData = [];
var CurrentBusData = [];
var socket = io('http://localhost:5000');
var counter=0;
var myInterval;
var hide = false;
var start = false;
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
        stopMarkers = [];
    });

    jQuery("#100").click(function () {
        if(busToDisplay.indexOf(parseInt(this.id))===-1) {
            busToDisplay.push(parseInt(this.id));
            console.log("bus number 100 added");
        }
        else {
            console.log("bus number 100 removed");
            busToDisplay.splice(busToDisplay.indexOf(parseInt(this.id)),1);
        }
    });

    jQuery("#103").click(function () {
        if(busToDisplay.indexOf(parseInt(this.id))===-1) {
            busToDisplay.push(parseInt(this.id));
            console.log("bus number 103 added");
        }
        else {
            console.log("bus number 103 removed");
            busToDisplay.splice(busToDisplay.indexOf(parseInt(this.id)),1);
        }
    });

    jQuery("#display_buses_button").click(function () {
        hide = false;
    });

    jQuery("#hide_buses_button").click(function () {
        hide = true;
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
            stopMarkers.push(marker);

            var infoWindow = new google.maps.InfoWindow();

            stopMarkers[i].addListener('click', function () {
                infoWindow.setContent(this.content);
                infoWindow.open(map, this);
            });
        }
    }
});


socket.on('connect',function() {
    console.log("connect");
});

socket.on('disconnect',function () {
    console.log("disconect");
});

socket.on('serial data',function (data) {
    JSONtoArray(data.bus_location_data);
});

function JSONtoArray(data) {
    counter=0;
    CurrentBusData = LastBusData.slice(0);
    LastBusData = [];
    for(var i = 0;i<data.length;i++) {
        LastBusData[i] = data[i];
    }
    if(CurrentBusData.length !== 0 && LastBusData.length !== 0 && !start) {
        init();
        start=true;
    }
}

function init() {

    var infoWindow = new google.maps.InfoWindow();
    var pinIcon = new google.maps.MarkerImage(
        "http://localhost:5000/resources/bus-circle.png",
        null, /* size is determined at runtime */
        null, /* origin is 0,0 */
        null, /* anchor is bottom center of the scaled image */
        new google.maps.Size(20, 20)
    );

    for(var i = 0; i<LastBusData.length;i++) {
        busMarkers.push(new google.maps.Marker({
            position: new google.maps.LatLng(LastBusData[i].latitude,LastBusData[i].longitude),
            map: map,
            icon: pinIcon
        }));
        busMarkers[i].content = 'Bus: ' + LastBusData[i].id;

        busMarkers[i].addListener('click', function () {
            infoWindow.setContent(this.content);
            infoWindow.open(map, this);
        });
    }

    var tmplong;
    var tmplat;

    myInterval = setInterval(function () {

        for(var i = 0;i<LastBusData.length; i++) {
            if (!hide) {
                if (busToDisplay.indexOf(parseInt(LastBusData[i].id)) !== -1) {
                    tmplong = counter * ((LastBusData[i].longitude - CurrentBusData[i].longitude) / 500) + parseFloat(CurrentBusData[i].longitude);
                    tmplat = counter * ((LastBusData[i].latitude - CurrentBusData[i].latitude) / 500) + parseFloat(CurrentBusData[i].latitude);
                    busMarkers[i].setPosition(new google.maps.LatLng(tmplat, tmplong));
                }
                else {
                    busMarkers[i].setPosition(null);
                }
            }
            else {
                busMarkers[i].setPosition(null);
            }
        }
        counter++;
    },9)

}

function setMapOnAll(map) {
    for (var i = 0; i < stopMarkers.length; i++) {
        stopMarkers[i].setMap(map);
    }
}

// Removes the stopMarkers from the map, but keeps them in the array.
function clearMarkers() {
    setMapOnAll(null);
}

// Shows any stopMarkers currently in the array.
function showMarkers() {
    setMapOnAll(map);
}

// Deletes all stopMarkers in the array by removing references to them.
function deleteMarkers() {
    clearMarkers();
    stopMarkers = [];
}

// Page style functions
$("#mobile-button").on("click", function () {
    $("#debug_panel").toggle();
    $("#mobile-button-lines").toggle();
    $("#mobile-button-close-panel").toggle();
});