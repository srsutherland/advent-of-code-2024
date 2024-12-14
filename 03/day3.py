import re
import sys
sys.path.insert(0, '.')
sys.path.insert(0, '..')
from base import AdventDay, log

sample_input = \
"""xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

global logging
logging = True

class Day3(AdventDay):
    mul_re_str = r"mul\((\d+),(\d+)\)"

    def part1(self, input:str) -> int:
        # find all instances of mul(x,y)
        mul_re = re.compile(self.mul_re_str)
        mul_matches = mul_re.findall(input)
        total = 0
        for match in mul_matches:
            left = int(match[0])
            right = int(match[1])
            total += left * right
        return total

    def part2(self, input:str) -> int:
        return 0

if __name__ == '__main__':
    day3 = Day3(sample_input)
    day3.run()