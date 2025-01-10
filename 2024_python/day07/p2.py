from itertools import product
import time


class Instruction():

    def __init__(self, line) -> None:
        self.arit_sum, self.digits = line.split(":")
        self.arit_sum = int(self.arit_sum.strip())
        self.digits = self.digits.strip().split(" ")
        self.digits = [int(x) for x in self.digits]
        self.permutations = []
        self.build_config()

    def build_config(self) -> None:
        self.expand_with_choices(choices=['*', '+', '||'])

    def expand_with_choices(self, choices):
        results = []
        for combo in product(choices, repeat=len(self.digits) - 1):
            temp = []
            for x, c in zip(self.digits, combo):
                temp.append(x)
                temp.append(c)
            temp.append(self.digits[-1])
            results.append(temp)
        self.permutations = results

    def compute_ltr(self) -> bool:

        for permut in self.permutations:
            permut_val = 0
            for i, ins in enumerate(permut):
                if i == 0:
                    permut_val += ins
                if i % 2 == 0 and i != 0:
                    if permut[i - 1] == '+':
                        permut_val += ins
                    elif permut[i - 1] == '*':
                        permut_val *= ins
                    elif permut[i - 1] == '||':
                        pre_str = str(permut_val)
                        post_str = str(ins)
                        permut_val = int(pre_str + post_str)
            if permut_val == self.arit_sum:
                print(f"Found correct")
                return True
        return False
    

def main(data):
    start = time.perf_counter()
    score = 0
    lines = data.splitlines()
    for line in lines:
        instruction = Instruction(line)
        if instruction.compute_ltr():
            score += instruction.arit_sum
        print(f"Current Scpre = {score}")
    elapsed = time.perf_counter() - start
    print(f"Elpased time: {elapsed:.4f}")
    return score

