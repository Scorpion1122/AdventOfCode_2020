import fileutility
from bootcoderunner import BootCodeRunner


def solve():
    instructions = fileutility.read_lines_file("input_day8.txt")

    boot_code_runner = BootCodeRunner(instructions)

    print ("Part 1:")
    boot_code_runner.execute_safe()

    print(f"Part 2:")
    print(f"repair? {boot_code_runner.repair()}")
    print(f"result = {boot_code_runner.execute_safe()}")



