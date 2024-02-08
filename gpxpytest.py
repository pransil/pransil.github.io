# gpxpytest.py
import gpxpy
import gpxpy.gpx
import datetime
import pytz
import gpxptutils
import gpxfileutils
import random


gpx = gpxpy.gpx.GPX()
now = datetime.datetime.now()
print(now)
print("Local:", now.strftime("%Y/%d/%m, %H:%M:%S"))
one_day = datetime.timedelta(days=1)
yesterday = now - one_day
tomorrow = now + one_day
print("Yesterday:", yesterday.strftime("%Y/%d/%m, %H:%M:%S"))
print("Tomorrow:", tomorrow.strftime("%Y/%d/%m, %H:%M:%S"))

# Create first track in our GPX:
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)

# Create first segment in our GPX track:
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

# Create track points with random increments 
lat = [-17.4234]
lon = [-149.4234]

for i in range (1, 10):
    lat.append(random.random() * 0.1 + lat[i-1])
    lon.append(random.random() * 0.1 + lon[i-1])
    gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(lat[i], lon[i], time=yesterday))

#print('tst.gpx track points:', gpx.to_xml())

# You can add routes and waypoints, too...
gpx = gpxptutils.add_waypt(gpx, lat[2], lon[2], name='Noonsite 2023-12-15', time=yesterday, type='In Marina', desc='Marina Taina')
gpx = gpxptutils.add_waypt(gpx, lat[5], lon[5],name='Noonsite 2023-12-16', time=now, type='At Anchor', desc='Opuhonu Bay')
gpx = gpxptutils.add_waypt(gpx, lat[9], lon[9], name='Noonsite 2023-12-17', time=tomorrow, type='On Passage', desc='Day four')


#print('Created GPX:', gpx.to_xml())

with open('tst.gpx', 'w') as f:
    f.write(gpx.to_xml())

# Make a gpx file from
# - lat_start, lon_start, lat_end, lon_end
# - time_start, time_end
lat_start = -17.5
lon_start = -149.5
lat_end = -19.4
lon_end = -151.4
time_start = datetime.datetime.now()
time_end = time_start + datetime.timedelta(days=10)
