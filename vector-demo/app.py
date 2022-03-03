import geopandas as gpd
from greppo import app

app.display(name="Title", value='Kenyan Counties, and Road Network')
app.display(
    name='description',
    value='A base app for vector data using GeoJSON data'
)

text_1 = """
## About the web-app
The dashboard shows the boundaries of the countirs of Kenya as polygons, and 
the major arterial highways as lines.
"""

app.display(name='text-1', value=text_1)

counties = gpd.read_file("./kenyan-counties.geojson")
roads = gpd.read_file("/Users/jobdulo/Documents/geo_data/Kenya_roads.json")

app.vector_layer(
    data = counties,
    name = "Counties of Kenya",
    description = "Boundaries of the counties of Kenya",
    style = {"fillColor":"#4daf4a"}
)

app.vector_layer(
    data = roads,
    name = "Main Roads and Highways in Kenya",
    description = "Major roads and highways of Kenya",
    style = {"fillColor":"#377eb8"}
)

app.display(name='text-2',
            value='The following displays the count of polygons, lines and points as a barchart.')

app.bar_chart(name='Geometry count', description='A bar-cart showing the count of each geometry-type in the datasets.',
              x=['polygons', 'lines (x1000)'], y=[len(counties), len(roads)/1000], color='#984ea3')

app.base_layer(
    name="Open Stree Map",
    visible=True,
    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    subdomains=None,
    attribution='(C) OpenStreetMap contributors',
)

app.base_layer(provider="CartoDB Positron")