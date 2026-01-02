from flask import Flask, render_template, redirect, url_for
import openlayers as ol

app = Flask(__name__)
m = ol.Map(
    center=[-0.1276, 51.5072],
    zoom=10
    
)

m.save("./templates/map.html")

@app.route('/')
def index():
    return render_template('map.html')

# Create a map instance

if __name__ == '__main__':
    app.run(debug=True)