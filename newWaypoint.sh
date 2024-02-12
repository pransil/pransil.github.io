#!/bin/bash
# newWaypoint.sh - add a new waypoint to data.gpx
# First get the track points and add its termination lines
cat trackpoints.gpx > data.gpx
cat trackEndLines.gpx >> data.gpx

# Add new waypoint to waypoints.gpx
cat newWaypoint.gpx >> waypoints.gpx
# Add waypoints to data.gpx and terminate
cat waypoints.gpx >>data.gpx
cat gpxEndLine.gpx >> data.gpx

# Push to github
git add data.gpx
git commit -m "Added new trackpoint"
git push --all
