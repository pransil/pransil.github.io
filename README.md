I have a WordPress blog at SailingCalista.net where I blog about our sailing adventures on our 46 ft catamaran, Calista. The blog uses a Waymark maps pluggin with which some of the maps read a gpx file each time they are viewed. Those gpx files are stored here and served from
pransil.github.io/pub-pages/some-gpx-file.gpx

These files will come from my RaspberryPI system on Calista. 
 - Trackpoints will be generated (automatically) every minute and written into an influxdb database and containing
    - datetime
    - lat / lon
    - current speed
    - current heading
    - maybe some other stuff (weather, sea state, ...)?  
 - A "noon-site" waypoint will be generated at noon each day containing all the trackpoint data plus 24 hour distance and 24 hour avg speed.
 - The noon-site data will be appended to a file here that will be used by the map on the blog showing our current location and track.
 - Calista spends most of her time at anchor or docked. I don't want to keep adding points for this so I may over-write the previous noon-site if Calista has not moved

These file updates will be pushed from my RPI system on Calista.
