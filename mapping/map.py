import folium
import pandas

data = pandas.read_csv("original.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
status = list(data["STATUS"])
elev = list(data["ELEV"])

multiCoordinates = [[51.130197, 16.961561], [51.072835, 16.989717], [51.061847, 16.978033], [51.098237, 17.668597], [51.043037, 16.198196]]
popups = ['Nasz dom :-)', 'Dom Mamy Kuby', 'Dom Taty Kuby', 'Dom Rodziców Izy', 'Dom Dziadków Kuby']
i = 0
map = folium.Map(location=[51.130197, 16.961561], zoom_start=12)

fg = folium.FeatureGroup(name="My Map")


for coordinates in multiCoordinates:
    fg.add_child(folium.Marker(location=coordinates, popup=popups[i], icon=folium.Icon(color='green', icon='glyphicon-home', prefix='glyphicon')))
    i += 1

for lt, ln, nm, st, ev in zip(lat, lon, name, status, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=f'Name:{nm} \n Status:{st} \n Elev:{ev} m', icon=folium.Icon(color='red', icon='glyphicon-picture', prefix='glyphicon')))

map.add_child(fg)

map.save("Map3.html")