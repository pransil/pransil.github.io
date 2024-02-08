# gpxptutils.py
import gpxpy
import gpxpy.gpx
import datetime
import pytz
from haversine import haversine, Unit

def add_waypt(gpx, lat, lon, type, name, time, desc):
    gpx_wps = gpxpy.gpx.GPXWaypoint()
    gpx_wps.latitude = lat
    gpx_wps.longitude = lon
    gpx_wps.type = type
    gpx_wps.time = time
    gpx_wps.name = name
    gpx_wps.description = desc
    gpx.waypoints.append(gpx_wps)
    return gpx

def add_waypt_from_dict(gpx, gd):
    # adding 2 waypoints
    gpx_wps = gpxpy.gpx.GPXWaypoint()
    gpx_wps.latitude = gd['lat']
    gpx_wps.longitude = gd['lon']
    gpx_wps.type = gd['type']
    gpx_wps.time = gd['time']
    gpx_wps.name = gd['name']
    desc = gd['desc'] + ' ' + gd['passage_day'] + ' ' + gd['current_speed'] + ' ' + gd['current_heading'] + ' ' + gd['24-hr_Distance'] + ' ' + gd['24-hr_Avg_Speed']    
    gpx_wps.description = desc
    gpx.waypoints.append(gpx_wps)
    return gpx

waypoint_dict = {
    'lat': -17.531781,
    'lon': -149.613281,
    'type': 'In Marina',
    'name': 'Noonsite 2023-12-15',
    'time': datetime.datetime.now(),
    'desc': 'P1 description',
    'passage_day': 0,
    'current_speed': 5.4,
    'current_heading': 270,
    '24-hr_Distance': 168,
    '24-hr_Avg_Speed': 5.3,
}

def make_waypoint_dict(track_dict, track_dict_previous=None, current_speed=None, current_heading=None):
    waypoint_dict['lat'] = track_dict['lat']
    waypoint_dict['lon'] = track_dict['lon']
    waypoint_dict['type'] = 'On Passage'
    time_str = track_dict['time'].strftime('%Y-%m-%d')
    waypoint_dict['name'] = 'Noonsite ' + time_str
    waypoint_dict['time'] = track_dict['time']
    waypoint_dict['desc'] = 'Calista is on passage'
    if track_dict_previous is not None:
        waypoint_dict['passage_day'] = track_dict_previous['passage_day'] + 1
        dist = haversine(track_dict['lat'], track_dict['lon'], track_dict_previous['lat'], track_dict_previous['lon'])
        waypoint_dict['24-hr_Distance'] = dist
        waypoint_dict['24-hr_Avg_Speed'] = dist / 24.0
    else:
        waypoint_dict['passage_day'] = 0
        waypoint_dict['24-hr_Distance'] = 0
        waypoint_dict['24-hr_Avg_Speed'] = 0
    waypoint_dict['current_speed'] = current_speed
    waypoint_dict['current_heading'] = current_heading
    return waypoint_dict

track_dict = {
    'lat': -17.531781,
    'lon': -149.613281,
    'time': datetime.datetime.now(),
}

track_dict_list = track_dict   
tdl0 = track_dict_list
# make_track_dict_list() from lat_start, lon_start, time_start
# to lat_end, lon_end, time_end
# with one track_dict every hour
def make_track_dict_list(lat_start, lon_start, time_start, lat_end, lon_end, time_end):
    lat_step = lat_end - lat_start
    lon_step = lon_end - lon_start
    tdl = []
    tdl0 = {
        'lat': lat_start,
        'lon': lon_start,
        'time': time_start,
    }
    tdl.append(tdl0)
    i = 0
    while time_now < time_end:
        time_now = time_now + datetime.timedelta(hours=1)
        tdl_next = {
            'lat': lat_start + lat_step*i + random.uniform(-1.0, 1.0) * lat_step,
            'lon': lon_end + lon_step*i + random.uniform(-1.0, 1.0) * lon_step,
            'time': time_now + datetime.timedelta(hours=1),
        }
        tdl.append(tdl_next)
    return tdl  

track_dict_list = make_track_dict_list(-17.531781, -149.613281, datetime.datetime.now(),
                                        -19.531781, -152.613281, datetime.datetime.now() + datetime.timedelta(days=10))
# make_waypoints_list_from_track_list() 
# Starting from track_dict_list[] add a waypoint_dict for every track_dict where time = noon
# Each waypoint_dict has lat, lon, type, name, time, desc, passage_day, current_speed, 
# current_heading, 24-hr_Distance, 24-hr_Avg_Speed
# where passage_day is the number of days since the start of the track
# 24-hr_Distance and 24-hr_Avg_Speed are calculated from the track_dict_list
def make_waypoints_list_from_track_list(track_dict_list):
    track_dict_previous = None
    way_dict_list = []
    for track_dict in track_dict_list:
        if track_dict['time'].hour == 12:
            current_speed = 5.0 + random.uniform(-3.0, 5.0)
            current_heading = 260 + random.uniform(-10, 10)
            way_dict_list.append(make_waypoint_dict(track_dict, track_dict_previous, current_speed, current_heading))
    return way_dict_list        

# make_gpx_from_waypoints_list_track_list()
# Create a GPX xmlstruct from a waypoint_dict_list and a track_dict_list
def make_gpx_from_waypoints_list_track_list(way_dict_list, track_dict_list):
    
def make_gpx_from_waypoints_list(way_dict_list):
    gpx = gpxpy.gpx.GPX()
    for way_dict in way_dict_list:
        gpx_wps = gpxpy.gpx.GPXWaypoint()
        gpx_wps.latitude = way_dict['lat']
        gpx_wps.longitude = way_dict['lon']
        gpx_wps.type = way_dict['type']
        gpx_wps.time = way_dict['time']
        gpx_wps.name = way_dict['name']
        gpx_wps.description = way_dict['desc']
        gpx.waypoints.append(gpx_wps)
    return gpx