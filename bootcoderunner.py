from instruction import Instruction


class BootCodeRunner:

    def __init__(self, raw_instructions):
        self.instructions = self.parse_instructions(raw_instructions)
        self.accumulator = 0
        self.execution_index = 0
        self.operations = {
            'acc': self.acc,
            'jmp': self.jmp,
            'nop': self.nop,
        }

    def parse_instructions(self, raw_instructions):
        result = []
        for raw_instruction in raw_instructions:
            result.append(Instruction(raw_instruction))
        return result

    def execute_safe(self):
        try:
            return self.execute()
        except Exception as error:
            print(error)
            return None

    def execute(self):
        self.accumulator = 0
        self.execution_index = 0

        execution_set = set()
        while self.execution_index < len(self.instructions):
            if self.execution_index in execution_set:
                raise Exception(
                    f"Exception: program is executing instruction more then once, current value {self.accumulator}")

            instruction = self.instructions[self.execution_index]

            if instruction.operation not in self.operations:
                raise Exception(f"Exception: operation {instruction.operation} is not supported, current value {self.accumulator}")

            execution_set.add(self.execution_index)
            self.operations[instruction.operation](instruction.argument)

        return self.accumulator

    def acc(self, value):
        self.accumulator += value
        self.execution_index += 1

    def jmp(self, value):
        self.execution_index += value

    def nop(self, value):
        self.execution_index += 1

    def repair(self):
        for index in range(len(self.instructions)):
            operation = self.instructions[index].operation
            replacement_operation = self.get_replacement_operation(operation)

            if replacement_operation is not None:
                self.instructions[index].operation = replacement_operation

                try:
                    self.execute()
                    return True
                except:
                    self.instructions[index].operation = operation

        return False

    def get_replacement_operation(self, operation):
        if operation == 'nop':
            return 'jmp'
        if operation == 'jmp':
            return 'nop'
        return None
