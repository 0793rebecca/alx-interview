#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""

import sys


def compute_metrics():
    total_size = 0
    status_count = {
        code: 0
        for code in [200, 301, 400, 401, 403, 404, 405, 500]
    }

    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_count)
                total_size = 0
                status_count = {
                    code: 0
                    for code in [200, 301, 400, 401, 403, 404, 405, 500]
                }

            try:
                parts = line.split()
                file_size = int(parts[-1])
                status_code = int(parts[-2])
                total_size += file_size
                if status_code in status_count:
                    status_count[status_code] += 1
            except (IndexError, ValueError):
                continue

    except KeyboardInterrupt:
        print_statistics(total_size, status_count)


def print_statistics(total_size, status_count):
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_count.keys()):
        count = status_count[status_code]
        if count > 0:
            print(f"{status_code}: {count}")


if __name__ == "__main__":
    compute_metrics()
