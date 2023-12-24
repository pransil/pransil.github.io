# gpxptutils.py
import gpxpy
import gpxpy.gpx
import datetime
import pytz

def add_waypt(gpx, lat, lon, type, name, time, desc):
    # adding 2 waypoints
    gpx_wps = gpxpy.gpx.GPXWaypoint()
    gpx_wps.latitude = lat
    gpx_wps.longitude = lon
    gpx_wps.type = type
    gpx_wps.time = time
    gpx_wps.name = name
    gpx_wps.description = desc
    gpx.waypoints.append(gpx_wps)
    return gpx
