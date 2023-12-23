I have a WordPress blog at SailingCalista.net. It uses a Waymark maps pluggin with which some of the maps 
read a gpx file each time they are viewed. Those gpx files are stored here and served from
pransil.github.io/pub-pages/some-gpx-file.gpx

These files will come from my RaspberryPI system on Calista. 
 - Waypoints will be taken (automatically) at noon each day. 
 - Trackpoints will be every hour.
 - Calista spend most of her time at anchor or docked. I don't want to keep adding points for this so
     - Trackpoints will only be added if they are ~ 0.2 nm from the last one added.
     - The new waypoint each day will replace the waypoint from the prior day if it is LT ~0.2 nm from the prior day's waypoint.

These file updates will be pushed from my RPI system on Calista.
