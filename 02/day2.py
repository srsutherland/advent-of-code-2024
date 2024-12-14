import sys
sys.path.insert(0, '.')
sys.path.insert(0, '..')
from base import AdventDay, log

sample_input = \
"""
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

global logging
logging = False

class Day2(AdventDay):
    def part1(self, input:str) -> int:
        reports = input.strip().split("\n")
        safe = 0
        for report in reports:
            report = list(map(int, report.split()))
            report_is_safe = self.is_report_safe(report)
            if report_is_safe:
                safe += 1
        return safe

    def is_report_safe(self, report: list[int]) -> bool:
        increasing = report[1] - report[0] > 0
        log(f'{report} is {"increasing" if increasing else "decreasing"}')
        for i in range(1, len(report)):
            delta = report[i] - report[i-1]
            log(f"{report[i]} - {report[i-1]} = {delta}")
            if increasing != (delta > 0):
                log("Wrong direction")
                return False
            if not (1 <= abs(delta) <= 3):
                log("Too big of a jump")
                return False
        return True

    def part2(self, input:str) -> int:
        reports = input.strip().split("\n")
        safe = 0
        for report in reports:
            report = list(map(int, report.split()))
            report_is_safe = self.is_report_safe(report)
            if not report_is_safe:
                for i in range(len(report)):
                    # Remove one element from the list
                    dampened_report = report[:i] + report[i+1:]
                    report_is_safe = self.is_report_safe(dampened_report)
                    if report_is_safe:
                        break
            if report_is_safe:
                safe += 1
        return safe



def load_input():
    with open("inputs/day2.txt") as f:
        return f.read()

if __name__ == "__main__":
    day2 = Day2(sample_input)
    day2.run()