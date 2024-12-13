sample_input = \
"""
3   4
4   3
2   5
1   3
3   9
3   3
"""
def get_lists(input=sample_input):
    lines = input.strip().split('\n')
    left, right  = [], []
    for line in lines:
        a, b = map(int, line.split())
        left.append(a)
        right.append(b)
    return left, right

def part1(input=sample_input):
    left, right = get_lists(input)
    distance = 0
    left.sort()
    right.sort()
    for a, b in zip(left, right):
        d = abs(a - b)
        distance += d
        # print(d)
    return distance

def load_input():
    with open('inputs/day1.txt') as f:
        return f.read()
    
def part2(input=sample_input):
    left, right = get_lists(input)
    similarity = 0
    # count items in right
    right_counts = {}
    for item in right:
        right_counts[item] = right_counts.get(item, 0) + 1
    for item in left:
        if item in right_counts:
            similarity += item * right_counts[item]
    return similarity
    

if __name__ == '__main__':
    input = load_input()
    result = part1(input)
    print(f"The answer to part 1 is: {result}")
    result = part2(input)
    print(f"The answer to part 2 is: {result}")