import folium
import pandas

data = pandas.read_csv("original.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
status = list(data["STATUS"])
elev = list(data["ELEV"])

html_popup = """
<h4 style="text-align:center">Volcano information:</h4>
<h3 style="text-align:center"> %s </h3>
Height: %s 
</br>
Status: %s 
"""

homes_popup = """
<h4 style="text-align:center">%s</h4> 
"""

feature = {
    "color": "red",
    "weight": 5,
    "opacity": 0.9
}

def geoStyle(feature):
    return {
    "color": "blue",
    "weight": 1,
    "opacity": 0.5
}

multiCoordinates = [[51.130197, 16.961561], [51.072835, 16.989717], [51.061847, 16.978033], [51.098237, 17.668597], [51.043037, 16.198196]]
popups = ['Nasz dom :-)', 'Dom Mamy Kuby', 'Dom Taty Kuby', 'Dom Rodziców Izy', 'Dom Dziadków Kuby']

def color_elevation(elevation):
    if elevation < 1000:
        return 'orange'
    elif 1000 <= elevation < 3000:
        return 'red'
    else:
        return 'darkred'

i = 0
map = folium.Map(location=[51.130197, 16.961561], zoom_start=12)

fg = folium.FeatureGroup(name="My Map")


for coordinates in multiCoordinates:
    iframe = folium.IFrame(html=homes_popup % (popups[i]), width=150, height=50)
    fg.add_child(folium.Marker(location=coordinates, popup=folium.Popup(iframe), icon=folium.Icon(color='green', icon='glyphicon-home', prefix='glyphicon')))
    i += 1

for lt, ln, nm, st, ev in zip(lat, lon, name, status, elev):
    iframe = folium.IFrame(html=html_popup % (nm, str(ev), st), width=150, height=200)
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=folium.Popup(iframe), color=color_elevation(ev), fill=True, fill_color=color_elevation(ev), fill_opacity=0.8))

fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()), style_function=geoStyle))

map.add_child(fg)

map.save("Map3.html")