#!/bin/bash
# newTrkpoint.sh - add a new trackpoint to data.gpx
cat newTrackpoint.gpx >> trackpoints.gpx
cat trackpoints.gpx > data.gpx
cat trackEndLines.gpx >> data.gpx
cat waypoints.gpx >> data.gpx
cat gpxEndLine.gpx >> data.gpx
git add data.gpx
git commit -m "Added new trackpoint"
git push --all
