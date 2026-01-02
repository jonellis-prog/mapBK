import folium
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

## webbrowser.open(map_file)
@app.route('/')
def index():
    m = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

    folium.Marker([40.7128, -74.0060], popup='New York City').add_to(m)

    map_file = "./map.html"
    m.save(map_file)
    return render_template(map_file)

@app.route('/Goto/', methods=['GET', 'POST'])
def goto():
    lat =  request.args.get('lat') if request.args.get('lat') is not None else 40.7128
    lon =  request.args.get('lon') if request.args.get('lon') is not None else -74.0060
    m = folium.Map(location=[lon, lat], zoom_start=12)
    map_file = "./map.html"
    m.save(map_file)
    return render_template(map_file)

if __name__ == '__main__':
    app.run(debug=True)
