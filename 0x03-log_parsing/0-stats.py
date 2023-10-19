#!/usr/bin/python3
'''Script reads stdin line by line and computes metrics
'''
import sys


def parse_line(line):
    '''Split line to tokens'''
    tokens = line.split(' ')
    return tokens


def print_static(status, size):
    '''Print statistic logs'''
    print(f'File size: {size}')
    for k in sorted(status.keys()):
        if status[k] != 0:
            print('{}: {}'.format(k, status[k]))


def stats():
    '''Parse stdin line by line'''
    counter = 0
    size = 0
    status = {'200': 0, '301': 0, '400': 0, '401': 0,
              '403': 0, '404': 0, '405': 0, '500': 0}

    try:
        for line in sys.stdin:
            counter += 1
            tokens = parse_line(line)
            if not tokens[-1].strip().isdigit():
                continue
            file_size = int(tokens[-1])
            code = tokens[-2]
            if code in status:
                status[code] += 1
            size += file_size
            if counter % 10 == 0:
                print_static(status, size)

        print_static(status, size)

    except KeyboardInterrupt:
        print_static(status, size)
        raise


if __name__ == '__main__':
    stats()
