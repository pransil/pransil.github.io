# gpxpytest.py
import gpxpy
import gpxpy.gpx
import datetime
import pytz

def add_waypt(gpx, lat, lon, name):
    # adding 2 waypoints
    gpx_wps = gpxpy.gpx.GPXWaypoint()
    gpx_wps.latitude = lat
    gpx_wps.longitude = lon
    gpx_wps.symbol = "Marks-Mooring-Float"
    gpx_wps.name = name
    #gpx_wps.time = time
    gpx_wps.description = "T1 description"
    gpx.waypoints.append(gpx_wps)
    return gpx


gpx = gpxpy.gpx.GPX()
now = datetime.datetime.now()
print(now)
print("Local:", now.strftime("%m/%d/%Y, %H:%M:%S"))
one_day = datetime.timedelta(days=1)
yesterday = now - one_day
print("Yesterday:", yesterday.strftime("%m/%d/%Y, %H:%M:%S"))

# Create first track in our GPX:
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)

# Create first segment in our GPX track:
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

# Create points:
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(-17.4234, -149.4234, elevation=1234))
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(-17.5235, -149.5235, elevation=1235))
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(-17.6236, -149.8236, elevation=1236))

# You can add routes and waypoints, too...
add_waypt(gpx, -17.531781, -149.567304, 'This is point 1')
add_waypt(gpx, -17.631781, -149.667304, 'This is point 2')


#print('Created GPX:', gpx.to_xml())

with open('test.gpx', 'w') as f:
    f.write(gpx.to_xml())