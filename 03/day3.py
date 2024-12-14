import re
import sys
sys.path.insert(0, '.')
sys.path.insert(0, '..')
from base import AdventDay, log

sample_input = \
"""xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

log.enabled = False

class Day3(AdventDay):
    def part1(self, input:str) -> int:
        mul_re_str = r"mul\((\d+),(\d+)\)"
        mul_re = re.compile(mul_re_str)
        mul_matches = mul_re.findall(input)
        total = 0
        for match in mul_matches:
            left = int(match[0])
            right = int(match[1])
            total += left * right
        return total

    def part2(self, input:str) -> int:
        re_str = r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)"
        re_ = re.compile(re_str)
        # matches = re_.findall(input) # need match objects, not tuples
        matches = re_.finditer(input)
        total = 0
        do = True
        for match in matches:
            log(match)
            if match.group(0) == "do()":
                do = True
                log("do")
            elif match.group(0) == "don't()":
                do = False
                log("dont")
            else:
                left = int(match.group(1))
                right = int(match.group(2))
                do_str = "do" if do else "don't"
                log(f"{do_str} mul({left},{right})")
                if do:
                    total += left * right
        return total

if __name__ == '__main__':
    day3 = Day3()
    day3.set_sample_input(sample_input)
    day3.set_sample_input2(
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )
    day3.run()