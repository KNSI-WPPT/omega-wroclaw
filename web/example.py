
from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons

app = Flask(__name__, template_folder="templates")

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4"

# you can also pass key here
GoogleMaps(app, key="AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4")


@app.route("/example")
def mapview():

    trdmap = Map(
        identifier="trdmap",
        varname="trdmap",
        style=(
            "height:80%;"
            "width:80%;"
            "top:100;"
            "left:0;"
            "position:absolute;"
            "z-index:200;"
        ),
        lat=51.11,
        lng=17.05,
        markers=[
            {
                'icon': icons.dots.green,
                'lat': 51.11045088,
                'lng': 17.05844119,
                'title': "Tu jesteśmy!",
                'infobox': (
                    "<h2><b style='color:#ffcc00;'>Politechnika Wrocławska</b></h2>"
                    "Tu jesteśmy!"
                )
            }
        ],
        maptype = "HYBRID", # ROADMAP(default), SATELLITE, HYBRID, TERRAIN
        zoom="15"
    )


    return render_template(
        'example.html',
        trdmap=trdmap,
    )

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
