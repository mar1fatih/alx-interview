#!/usr/bin/python3
""" interviews tests """
import sys
import re
import signal


i = 0
file_size = 0
list_codes = []


def output(size, list_codes):
    """ show the output """
    codes = {}
    for code in list_codes:
        codes[code] = codes.get(code, 0) + 1

    sorted_codes = {k: codes[k] for k in sorted(codes)}
    print('File size:', size)
    for k, v in sorted_codes.items():
        print('{}: {}'.format(k, v))


def signal_handler(sig, frame):
    """ signal_handler Ctrl+C """
    output(file_size, list_codes)


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    if i % 10 == 0 and i != 0:
        output(file_size, list_codes)
    pattern = r'^(?:\d{1,3}\.){3}\d{1,3} - \[\d{4}-\d{2}-\d{2} ' +\
              r'.{15}\] \"GET /projects/260 HTTP/1\.1\" ' +\
              r'(200|301|400|401|403|404|405|500) \d+$'
    if re.match(pattern, line):
        splited_code = line.split('"')[-1].split(' ')[1]
        split_size = line.split('"')[-1].split(' ')[2][:-1]
        list_codes.append(splited_code)
        file_size += int(split_size)

    i += 1
