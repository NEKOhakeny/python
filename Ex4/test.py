import pandas as pd
import plotly.express as px
import folium
def_staionInfo = pd.read_csv('stationInfo.csv')
grid = pd.DataFrame(columns=['x','y'])
for itr in def_staionInfo['Location']:
    itr = itr.replace('Point(','')
    itr = itr.replace(')','')
    itr = itr.split()
    itr = list(map(float,itr))
    grid.loc[len(grid)] = itr
    
fig = px.scatter_mapbox(
    data_frame=def_staionInfo, 
    lat= grid.y, 
    lon= grid.x, 
    
    hover_name="Location",
    hover_data=["stationId"],
    color="stationId",
    #size="stationId",
    #size_max=30,
    opacity=1.0,
    
    center={"lat": 34.686567, "lon":135.52000},
    zoom=4,
    height=600,
    width=800)
fig.update_layout(mapbox_style='open-street-map')
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_layout(title_text="Station Info")
fig.show()
