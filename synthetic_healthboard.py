import csv
from collections import defaultdict
import sys


def summarize(rows):
    totals = defaultdict(lambda: [0, 0])
    for row in rows:
        bucket = totals[row["journey"]]
        bucket[0] += 1
        if row["status"].lower() == "pass":
            bucket[1] += 1
    return {journey: round(passed / total, 3) for journey, (total, passed) in totals.items()}


def degraded(rows, threshold=0.95):
    return sorted(journey for journey, rate in summarize(rows).items() if rate < threshold)


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for journey in degraded(list(csv.DictReader(handle))):
            print(journey)


if __name__ == "__main__":
    main(sys.argv[1])
