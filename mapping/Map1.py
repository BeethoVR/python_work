import folium

#map = folium.Map(location=[80, -100])  # Isla arriba de Canada
map = folium.Map(location=[38.58, -99.09],    # +/- Centro de USA
                 zoom_start=6)
                 #tiles='Open topo Map',
                 #attr='Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)')
                 #) # Solo 3 Tiles Build IN
#folium.TileLayer('openstreetmap').add_to(map)  # OpenStreetMap
#folium.TileLayer('cartodbdark_matter').add_to(map)    # Cartodb dark_matter
#folium.TileLayer('cartodbpositron').add_to(map)       # Cartodb Positron 
#folium.LayerControl().add_to(map)                   

fg = folium.FeatureGroup(name='My Map')
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save('./mapping/Map1.html')

m = folium.Map(location=[40.965, -5.664], 
               zoom_start=16, 
               tiles = "CartoDB Positron"
              ) 
tooltip = 'plaza Mayor'
folium.Marker([40.965, -5.664], popup='Plaza Mayor', tooltip=tooltip).add_to(m) 
m.save('./mapping/Map2.html')

# Tiles personalizados
# Plain JavaScript:
#
#var OpenTopoMap = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
#	maxZoom: 17,
#	attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
#});
map2 = folium.Map(location=[37, -99],    # +/- Centro de USA
                 zoom_start=6,
                 tiles='https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
                 attr='Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)')
map2.save('./mapping/Map3.html')

