#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""

import sys
import re
from collections import defaultdict


def print_stats(total_size, status_codes):
    """
    Print the accumulated statistics.

    Args:
        total_size (int): The total file size processed.
        status_codes (dict): A dictionary of status codes and their counts.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """
    Parse a single line of log input.

    Args:
        line (str): A line from the log file.

    Returns:
        tuple: A tuple containing the status code and file size,
        or (None, None) if the line is invalid.
    """
    pattern = (
        r'(\d+\.\d+\.\d+\.\d+) - '
        r'\[(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
    )
    match = re.match(pattern, line)
    if match:
        ip, date, status, file_size = match.groups()
        return int(status), int(file_size)
    return None, None


def main():
    """
    Main function to process the log input and print statistics.
    """
    total_size = 0
    line_count = 0
    status_codes = defaultdict(int)

    try:
        for line in sys.stdin:
            status, file_size = parse_line(line.strip())
            if status and file_size:
                total_size += file_size
                status_codes[status] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
