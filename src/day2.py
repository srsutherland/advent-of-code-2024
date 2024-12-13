sample_input = \
"""
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

def part1(input:str) -> int:
    reports = input.strip().split("\n")
    safe = 0
    for report in reports:
        report = list(map(int, report.split()))
        increasing = report[1] - report[0] > 0
        report_is_safe = True
        #print(f'{report} is {"increasing" if increasing else "decreasing"}')
        for i in range(1, len(report)):
            delta = report[i] - report[i-1]
            #print(f"{report[i]} - {report[i-1]} = {delta}")
            if increasing != (delta > 0):
                report_is_safe = False
                #print("Wrong direction")
                break
            if not (1 <= abs(delta) <= 3):
                report_is_safe = False
                #print("Too big of a jump")
                break
        # print debugging
        #print(f"safe: {report_is_safe}")
        if report_is_safe:
            safe += 1
    return safe


def test_part1():
    target = 2
    test_result = part1(sample_input)
    print(f"The sample result of part 1 is {test_result}")


def load_input():
    with open("inputs/day2.txt") as f:
        return f.read()

if __name__ == "__main__":
    test_part1()
    result = part1(load_input())
    print(f"The result of part 1 is {result}")