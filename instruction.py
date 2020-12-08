class Instruction:

    def __init__(self, raw):
        instruction = raw.split(' ')
        self.operation = instruction[0]
        self.argument = int(instruction[1])
