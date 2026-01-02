import folium
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Create a map centered at a specific location (e.g., New York City)
m = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

# Add a marker
folium.Marker([40.7128, -74.0060], popup='New York City').add_to(m)

# Save the map to an HTML file
map_file = "./nyc_map.html"
m.save(map_file)
mapframe_file = "./mapframe_file.html"
## webbrowser.open(map_file)

@app.route('/')
def index():
    return render_template(map_file)

if __name__ == '__main__':
    app.run(debug=True)
