#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""

import sys
from collections import defaultdict

def parse_line(line):
    try:
        parts = line.split()
        ip_address, date, method, path, protocol = parts[:5]
        status_code, file_size = int(parts[5]), int(parts[6])
        return ip_address, date, method, path, protocol, status_code, file_size
    except (ValueError, IndexError):
        return None

def print_statistics(total_file_size, status_code_counts):
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")

def main():
    total_file_size = 0
    status_code_counts = defaultdict(int)
    lines_processed = 0

    try:
        for line in sys.stdin:
            parsed_line = parse_line(line.strip())
            if parsed_line:
                _, _, _, _, _, status_code, file_size = parsed_line
                total_file_size += file_size
                status_code_counts[status_code] += 1

                lines_processed += 1
                if lines_processed % 10 == 0:
                    print_statistics(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_code_counts)

if __name__ == "__main__":
    main()
