#!/usr/bin/python3
import sys
import re
from collections import defaultdict

def parse_line(line):
    # Define the regex pattern for the expected log format
    pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
    match = re.match(pattern, line)
    if match:
        return match.group(2), int(match.group(3))
    return None, None

def print_metrics(file_size_total, status_counts):
    print(f"File size: {file_size_total}")
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    file_size_total = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code and file_size is not None:
                file_size_total += file_size
                status_counts[status_code] += 1

            line_count += 1

            # Print metrics after every 10 lines
            if line_count % 10 == 0:
                print_metrics(file_size_total, status_counts)

    except KeyboardInterrupt:
        # Print metrics on keyboard interruption
        print_metrics(file_size_total, status_counts)

if __name__ == "__main__":
    main()

