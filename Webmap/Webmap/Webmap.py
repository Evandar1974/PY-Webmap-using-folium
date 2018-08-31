import folium
import pandas


data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
nme = list(data["NAME"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], popup=str(el)+ " m", radius=12, fill_color=color_producer(el), fill=True, fill_opacity=0.7, color='grey'))

fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))
map.add_child(fg)

map.save("Map1.html")
