# gpxfileutils.py

# Read a GPX  file
def readGPXFile(fname):
    with open(fname, 'r') as gpxFile:
        gpxData = gpxFile.read()
    return gpxData


# Write a GPX file
def writeGPXFile(fname, gpxData):
    with open(fname, 'w') as gpxFile:
        gpxFile.write(gpxData)

# Write a GPX file where input is a list of lines that need '\n' at the end
def writeGPXLinesFile(fname, gpxDataLines):
    with open(fname, 'w') as gpxFile:
        for line in gpxDataLines:
            l = line + '\n'
            gpxFile.write(l)