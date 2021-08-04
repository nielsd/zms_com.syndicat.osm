class osm_map_link:
	"""
	python-representation of osm_map_link
	"""

	# Access
	access = {"delete_custom":""
		,"delete_deny":[""
			,""
			,""
			,"ZMSAuthor"]
		,"insert_custom":"{$}"
		,"insert_deny":[""
			,""
			,""
			,"ZMSAuthor"]}

	# Enabled
	enabled = 1

	# Id
	id = "osm_map_link"

	# Name
	name = "OpenStreetMap Map / Link"

	# Package
	package = "com.syndicat.osm"

	# Revision
	revision = "2.0.1"

	# Type
	type = "ZMSObject"

	# Attrs
	class Attrs:
		icon_clazz = {"custom":"fa fa-map"
			,"default":""
			,"id":"icon_clazz"
			,"keys":[]
			,"mandatory":0
			,"multilang":0
			,"name":"Icon Class (css)"
			,"repetitive":0
			,"type":"constant"}

		title = {"default":""
			,"id":"title"
			,"keys":[]
			,"mandatory":1
			,"multilang":1
			,"name":"DC.Title"
			,"repetitive":0
			,"type":"string"}

		map_width = {"default":"100%"
			,"id":"map_width"
			,"keys":[]
			,"mandatory":1
			,"multilang":0
			,"name":"Map Width"
			,"repetitive":0
			,"type":"string"}

		map_height = {"default":"450"
			,"id":"map_height"
			,"keys":[]
			,"mandatory":1
			,"multilang":0
			,"name":"Map Height (Pixel)"
			,"repetitive":0
			,"type":"int"}

		label1 = {"default":""
			,"id":"label1"
			,"keys":[]
			,"mandatory":0
			,"multilang":0
			,"name":"label1"
			,"repetitive":0
			,"type":"interface"}

		map_long = {"default":"10.077134370803833"
			,"id":"map_long"
			,"keys":[]
			,"mandatory":1
			,"multilang":0
			,"name":"Logintude"
			,"repetitive":0
			,"type":"float"}

		map_lat = {"default":"51.3624596740495"
			,"id":"map_lat"
			,"keys":[]
			,"mandatory":1
			,"multilang":0
			,"name":"Latidude"
			,"repetitive":0
			,"type":"float"}

		map_zoom = {"default":""
			,"id":"map_zoom"
			,"keys":["19"
				,"18"
				,"17"
				,"16"
				,"15"
				,"14"
				,"13"
				,"12"
				,"11"
				,"10"
				,"9"
				,"8"
				,"7"
				,"6"
				,"5"
				,"4"
				,"3"
				,"2"
				,"1"]
			,"mandatory":1
			,"multilang":0
			,"name":"Zoom Level"
			,"repetitive":0
			,"type":"select"}

		map_max_zoom = {"default":""
			,"id":"map_max_zoom"
			,"keys":["19"
				,"18"
				,"17"
				,"16"
				,"15"
				,"14"
				,"13"
				,"12"
				,"11"
				,"10"
				,"9"
				,"8"
				,"7"
				,"6"
				,"5"
				,"4"
				,"3"
				,"2"
				,"1"]
			,"mandatory":0
			,"multilang":1
			,"name":"Max Zoom"
			,"repetitive":0
			,"type":"select"}

		map_marker_delim1 = {"default":""
			,"id":"map_marker_delim1"
			,"keys":[]
			,"mandatory":0
			,"multilang":1
			,"name":"Marker"
			,"repetitive":0
			,"type":"delimiter"}

		map_markers = {"default":""
			,"id":"map_markers"
			,"keys":[]
			,"mandatory":0
			,"multilang":0
			,"name":"Map Marker"
			,"repetitive":1
			,"type":"osm_map_marker"}

		standard_html = {"default":""
			,"id":"standard_html"
			,"keys":[]
			,"mandatory":0
			,"multilang":0
			,"name":"standard_html"
			,"repetitive":0
			,"type":"zpt"}

		getleafletmapscript = {"default":""
			,"id":"getLeafletMapScript"
			,"keys":[]
			,"mandatory":0
			,"multilang":0
			,"name":"getLeafletMapScript"
			,"repetitive":0
			,"type":"py"}

		rendershort = {"default":""
			,"id":"renderShort"
			,"keys":[]
			,"mandatory":0
			,"multilang":0
			,"name":"renderShort"
			,"repetitive":0
			,"type":"zpt"}
