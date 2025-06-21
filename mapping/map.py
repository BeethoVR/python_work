import pandas as pd
from os import system
from os import path as os_path
import folium

map = folium.Map(location=[42.58, -113.29],    # +/- Centro/Oeste de USA
                 zoom_start=5.2)
                 
fgv = folium.FeatureGroup(name='Volcanes')

system("clear")

def getPath():
    sPath = './mapping/'                # Path si estoy en la carpeta global
    if os_path.isdir('../mapping/'): 
        sPath = ''                      # Path si estoy en la carpeta del Proyecto
    return(sPath)    

sPath = getPath()
print(f"\n\n->{sPath}<-\n\n")

def getColorMarker(Elevation):
    color = 'green'
    if (Elevation > 3000):
        color = 'red'
    elif (Elevation > 2000):
        color = 'orange'    
    elif (Elevation > 1000):
        color = '#3388ff' 

    return(color)    

if (os_path.isfile(sPath + 'Volcanoes.txt')):
    data = pd.read_csv(sPath + 'Volcanoes.txt')
    print(data)

    # Trabajar con LISTAS es más eficiente y rápido que trabajar con Pandas.FrameSets
    Name    = data['NAME']
    Lat     = data['LAT']
    Lon     = data['LON']
    Elev    = data['ELEV']
    #print(Lat)
    #print(Lon)

    html = """<h4>Volcano information:</h4>
                    Name: %s <br/>
                    Height: %4.0f m
           """
    for lt, ln, Nm, El in zip(Lat,Lon, Name, Elev): # Zip - Une las listas para sacar de uno en uno por cada vuelta
        iframe = folium.IFrame(html=html % (Nm, El), width=200, height=100)
        #fgv.add_child(folium.Marker(location=[lt, ln], popup=(Nm + '\n(Elev:' + str(El) + 'm)'), icon=folium.Icon(color='red')))
        #fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='red')))
        #fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=getColorMarker(El))))
        fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=5, popup=folium.Popup(iframe), 
                                         color='grey', #getColorMarker(El), 
                                         fill=True, 
                                         fillColor=getColorMarker(El),
                                         fillOpacity=1.0))

    ## Forma que YO Invente o Cree, directamente del Pandas.FrameSet
    #for volcan in data.iterrows():
    #    #print(f"%2.7f , %2.7f" % (volcan[1][8], volcan[1][9]))
    #    ESTABA PROBANDO ESTO bf1.iloc
    #    fg.add_child(folium.Marker(location=[volcan[1][8], volcan[1][9]], popup=volcan[1][2], icon=folium.Icon(color='green')))

fgp = folium.FeatureGroup(name='Población')
if (os_path.isfile(sPath + 'world.json')):
    fgp.add_child(folium.GeoJson(data=open(sPath + 'world.json', encoding='utf-8-sig').read(), 
                                style_function=lambda x: {'fillColor':
                                                                'green' if x['properties']['POP2005'] < 10000000 
                                                          else 'orange' if x['properties']['POP2005'] < 20000000
                                                          else 'red'}))

map.add_child(fgp)
map.add_child(fgv)

map.add_child(folium.LayerControl())

map.save(sPath + 'Map.html')
