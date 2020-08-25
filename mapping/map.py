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

multiCoordinates = [[51.130197, 16.961561], [51.072835, 16.989717], [51.061847, 16.978033], [51.098237, 17.668597], [51.043037, 16.198196]]
popups = ['Nasz dom :-)', 'Dom Mamy Kuby', 'Dom Taty Kuby', 'Dom Rodziców Izy', 'Dom Dziadków Kuby']

def color_elevation(elevation):
    if elevation < 1000:
        return 'orange'
    elif 1000 <= elevation < 3000:
        return 'red'
    else:
        return 'darkred'

def fillColor(x):
    if x['properties']['POP2005'] < 10000000:
        return '#ADFF2F'
    elif 10000000 <= x['properties']['POP2005'] < 20000000:
        return '#9ACD32	'
    elif 20000000 <= x['properties']['POP2005'] < 30000000:
        return '#FFFF00'
    elif 30000000 <= x['properties']['POP2005'] < 40000000:
        return '#FFA500'
    elif 40000000 <= x['properties']['POP2005'] < 70000000:
        return '#FF8C00'
    elif 70000000 <= x['properties']['POP2005'] < 120000000:
        return '#FA8072'
    elif 120000000 <= x['properties']['POP2005'] < 250000000:
        return '#FF0000'
    else:
        return '#800000'
        
i = 0
m = folium.Map(location=[51.130197, 16.961561], zoom_start=12)

fgv = folium.FeatureGroup(name="Volcanoes & Houses")


for coordinates in multiCoordinates:
    iframe = folium.IFrame(html=homes_popup % (popups[i]), width=150, height=50)
    fgv.add_child(folium.Marker(location=coordinates, popup=folium.Popup(iframe), icon=folium.Icon(color='green', icon='glyphicon-home', prefix='glyphicon')))
    i += 1

for lt, ln, nm, st, ev in zip(lat, lon, name, status, elev):
    iframe = folium.IFrame(html=html_popup % (nm, str(ev), st), width=150, height=200)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=folium.Popup(iframe), color=color_elevation(ev), fill=True, fill_color=color_elevation(ev), fill_opacity=0.8))


fgp = folium.FeatureGroup(name="Popoulation")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor': fillColor(x),
                          'weight': 1 }))

m.add_child(fgv)
m.add_child(fgp)
m.add_child(folium.LayerControl())
m.save("Map3.html")