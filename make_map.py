import folium

pos = [35.69158, 139.69696]
map = folium.Map(location=pos, zoom_start=15)
map.save("西新宿周辺地図.html")
