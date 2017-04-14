#!/usr/bin/env python

import re
import sys

TIME_REGEX = re.compile('(\d{1,2}):(\d{1,2}):(\d{1,2}),(\d{1,3})')

def match_to_milliseconds(match):
    h = int(match.group(1))
    m = int(match.group(2))
    s = int(match.group(3))
    ms = int(match.group(4))
    return ms + s * 1000 + m * 60000 + h * 3600000

def milliseconds_to_time_string(ms):
    s, ms = divmod(ms, 1000)
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    return '%02d:%02d:%02d,%03d' % (h, m, s, ms)

def offset_times(line, offset):
    def offset_match(match):
        ms = match_to_milliseconds(match) + offset
        return milliseconds_to_time_string(ms)

    line = TIME_REGEX.sub(offset_match, line)
    return line

def main(argv):
    if (len(argv) != 3):
        print 'usage: %s input.srt offset > out.srt' % argv[0]
        exit()

    filename = argv[1]
    offset = int(argv[2])

    lines = open(filename, 'r').readlines()
    for line in lines:
        print offset_times(line, offset),

if __name__ == '__main__':
    main(sys.argv)
