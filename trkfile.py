# trkfile.py - read and write GPX track files

# Read a GPX track file
def readTrackFile(fname):
    gpxFile = open(fname, 'r')
    gpxData = gpxFile.read()
    gpxFile.close()
    return gpxData

# Write a GPX track file
def writeTrackFile(fname, gpxData):
    gpxFile = open(fname, 'w')
    gpxFile.write(gpxData)
    gpxFile.close()

def writeTrackFileLines(fname, gpxDataLines):
    for line in gpxDataLines:
        print(line)
    print('Done writing track file')
    with open(fname, 'w') as gpxFile:
        for line in gpxDataLines:
            l = line + '\n'
            gpxFile.write(l)
    #gpxFile.write('\n')
    gpxFile.close()


def count_lines_in_data(file_data):
    # Convert the file data to a string
    #file_content = file_data.decode()

    # Split the string into lines
    lines = file_data.split('\n')

    # Count the lines
    line_count = len(lines)

    return line_count

data_in = readTrackFile('t1.gpx')
lines = data_in.split('\n')
line_count = len(lines)
print ("There are", line_count, "lines in the file.")
print (lines[22])

lines.insert(-3, '<trkpt lat="48.782047" lon="-129.425431">')
lines.insert(-3, '</trkpt>')

writeTrackFileLines('t2.gpx', lines)
