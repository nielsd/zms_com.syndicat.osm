class osm_map_marker:
	"""
	python-representation of osm_map_marker
	"""

	# Access
	access = {"delete_custom":""
		,"delete_deny":[""
			,""
			,""
			,""]
		,"insert_custom":"{$}"
		,"insert_deny":[""
			,""
			,""
			,""]}

	# Enabled
	enabled = 0

	# Id
	id = "osm_map_marker"

	# Name
	name = "OSM Map Marker"

	# Package
	package = "com.syndicat.osm"

	# Revision
	revision = "2.0.1"

	# Type
	type = "ZMSObject"

	# Attrs
	class Attrs:
		icon_clazz = {"custom":"fas fa-map-marker-alt"
			,"default":""
			,"id":"icon_clazz"
			,"keys":[]
			,"mandatory":0
			,"multilang":1
			,"name":"Icon Class (css)"
			,"repetitive":0
			,"type":"constant"}

		map_marker_title = {"default":""
			,"id":"map_marker_title"
			,"keys":[]
			,"mandatory":1
			,"multilang":1
			,"name":"DC.Title"
			,"repetitive":0
			,"type":"string"}

		map_marker_text = {"default":""
			,"id":"map_marker_text"
			,"keys":[]
			,"mandatory":0
			,"multilang":1
			,"name":"Map text"
			,"repetitive":0
			,"type":"string"}

		mark_long = {"default":""
			,"id":"mark_long"
			,"keys":[]
			,"mandatory":1
			,"multilang":1
			,"name":"Longitude"
			,"repetitive":0
			,"type":"float"}

		mark_lat = {"default":""
			,"id":"mark_lat"
			,"keys":[]
			,"mandatory":1
			,"multilang":1
			,"name":"Latitude"
			,"repetitive":0
			,"type":"float"}

		standard_html = {"default":""
			,"id":"standard_html"
			,"keys":[]
			,"mandatory":0
			,"multilang":0
			,"name":"Template: OSM Map Marker"
			,"repetitive":0
			,"type":"zpt"}
