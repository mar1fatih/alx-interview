#!/usr/bin/python3
""" log parsing """
import sys


i = 0
files_size = 0
codes = {'200': 0, '301': 0, '400': 0, '401': 0,
           '403': 0, '404': 0, '405': 0, '500': 0}


def output(total):
    """ function to print """
    print('File size: {}'.format(total))
    for key, value in sorted(codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


try:
    for line in sys.stdin:
        split_line = line.split(" ")
        if len(split_line) > 4:
            code = split_line[-2]
            if code in codes.keys():
                codes[code] += 1
            filesize = int(split_line[-1])
            files_size += filesize
            i += 1
        if i % 10 == 0:
            output(files_size)
except Exception as e:
    pass
finally:
    output(files_size)
