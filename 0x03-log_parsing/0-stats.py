#!/usr/bin/python3
'''Script reads stdin line by line and computes metrics
'''
import re
import sys


def parse_line(line):
    '''Split line to tokens'''
    pattern = r'(?P<ip>^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - ' \
        r'\[(?P<date>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})] ' \
        r'"(?P<req>.*)" (?P<code>\d{3}) (?P<file_size>\d{1,9})$'
    tokens = re.match(pattern, line)
    return tokens


def print_static(status, size):
    '''Print statistic logs'''
    print(f'File size: {size}')
    for k in status:
        if status[k] != 0:
            print('{}: {}'.format(k, status[k]), flush=True)


def stats():
    '''Parse stdin line by line'''
    counter = 0
    size = 0
    status = {'200': 0, '301': 0, '400': 0, '401': 0,
              '403': 0, '404': 0, '405': 0, '500': 0}

    try:
        for line in sys.stdin:
            counter += 1
            parse = parse_line(line)
            if not parse:
                continue
            tokens = parse.groupdict()
            if tokens['code'] in status:
                status[tokens['code']] += 1
                size += int(tokens['file_size'])
            if counter % 10 == 0:
                print_static(status, size)
        else:
            print_static(status, size)

    except (KeyboardInterrupt, SystemExit):
        print_static(status, size)
        raise


if __name__ == '__main__':
    stats()
