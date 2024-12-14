import os
import sys

global logging
logging = False
def log(message):
    if log.enabled:
        print(message)
log.enabled = False

class AdventDay:
    def __init__(self, sample_input:str=None):
        self.sample_input = None
        self.sample_input2 = None
        self.set_sample_input(sample_input)
        try:
            self.input = self.load_input()
        except FileNotFoundError:
            self.input = None
            print("No input file found")
    
    def load_input(self):
        # change to the dir of the file calling this function
        cur_dir = os.getcwd()
        filename = os.path.abspath(sys.argv[0])
        new_dir = os.path.dirname(filename)
        os.chdir(new_dir)
        with open('input.txt') as f:
            return f.read()
    
    def set_sample_input(self, sample_input:str):
        self.sample_input = sample_input
        if self.sample_input2 is None:
            self.sample_input2 = sample_input
    
    def set_sample_input2(self, sample_input:str):
        self.sample_input2 = sample_input
    
    def run(self, test_part1=True, run_part1=True, test_part2=True, run_part2=True):
        if test_part1:
            self.test_part1()
        if run_part1 and self.input:
            self.run_part1()
        if test_part2:
            self.test_part2()
        if run_part2 and self.input:
            self.run_part2()
    
    def test_part1(self):
        test_result = self.part1(self.sample_input)
        print(f"The sample result of part 1 is {test_result}")
    
    def test_part2(self):
        test_result = self.part2(self.sample_input2)
        print(f"The sample result of part 2 is {test_result}")
    
    def run_part1(self):
        result = self.part1(self.input)
        print(f"The answer to part 1 is: {result}")
    
    def run_part2(self):
        result = self.part2(self.input)
        print(f"The answer to part 2 is: {result}")