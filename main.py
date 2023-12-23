# main.py
import trkfile as trk

if __name__ == '__main__':
    data_in = trk.readTrackFile('t1.gpx')
    lines = data_in.split('\n')
    line_count = len(lines)
    print ("There are", line_count, "lines in the file.")
