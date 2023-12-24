# gpxpytest.py
import gpxpy
import gpxpy.gpx
import datetime
import pytz
import gpxptutils
import gpxfileutils


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

# Create points:
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(-17.4234, -149.4234, time=yesterday))
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(-17.5235, -149.5235, time=now))
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(-17.6236, -149.8236, time=tomorrow))

# You can add routes and waypoints, too...
gpxptutils.add_waypt(gpx, -17.531781, -149.567304, name='Noonsite 2023-12-15', time=yesterday, type='In Marina', desc='Marina Taina')
gpxptutils.add_waypt(gpx, -17.631781, -149.667304, name='Noonsite 2023-12-16', time=now, type='At Anchor', desc='Opuhonu Bay')
gpxptutils.add_waypt(gpx, -17.731781, -149.667304, name='Noonsite 2023-12-17', time=tomorrow, type='On Passage', desc='Day four')


#print('Created GPX:', gpx.to_xml())

with open('tst.gpx', 'w') as f:
    f.write(gpx.to_xml())