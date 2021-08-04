## Script (Python) "osm_map_link.getLeafletMapScript"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=zmscontext=None,options=None
##title=py: getMapScript
##
# --// getMapScript //--
# get LeafLet Script

request          = container.REQUEST

map_id           = zmscontext.getId()
map_title        = zmscontext.attr('title')
map_div_id       = 'mymap_'+str(map_id)
map_access_token = zmscontext.content.attr('osm_mapbox_token')
map_lat          = zmscontext.attr('map_lat')
map_long         = zmscontext.attr('map_long')
map_zoom         = str(zmscontext.attr('map_zoom'))
map_max_zoom     = str(zmscontext.attr('map_max_zoom'))

map_markers      = zmscontext.getObjChildren('map_markers',request)



my_script= """
var mymap = L.map('%s').setView([%s, %s], %s);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=%s', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OSM</a> | <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: %s,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: '%s'
}).addTo(mymap);
""" % (map_div_id, map_lat, map_long, map_zoom, map_access_token, map_max_zoom, map_access_token)


i                   = 0
for my_marker in map_markers:
   i                = i + 1
   mark_long        = my_marker.attr('mark_long')
   mark_lat         = my_marker.attr('mark_lat')
   map_marker_title = my_marker.attr('map_marker_title')

   map_marker_text  = my_marker.attr('map_marker_text').replace('\n','<br />')
   map_marker_text_line = ""
   for line in map_marker_text:
      line.replace('\t','')
      line.replace('\n','<br />')
      map_marker_text_line = map_marker_text_line + line

   my_script = my_script + """
  
   var marker%s = L.marker([%s, %s]).addTo(mymap);
   marker%s.bindPopup(`<h5>%s</h5> %s`).openPopup();

   var popup = L.popup()

   """ % (i, mark_lat, mark_long, i, map_marker_title, map_marker_text_line)

return my_script

# --// /getMapScript //--
