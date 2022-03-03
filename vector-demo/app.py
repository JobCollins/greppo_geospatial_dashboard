import geopandas as gpd
from greppo import app

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

app.base_layer(
    name="Open Stree Map",
    visible=True,
    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    subdomains=None,
    attribution='(C) OpenStreetMap contributors',
)

app.base_layer(provider="CartoDB Positron")