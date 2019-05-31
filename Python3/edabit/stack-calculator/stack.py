class StackCalc:

    def __init__(self):
        self.instructions = []

    def run(self, instructions):
        self.instructions = instructions.split()

    def getValue(self):
        two_number_operations = ['+', '-', "*", "/"]
        answer, stack = 0, []
        for i in self.instructions:
            if i.isdecimal():
                stack.append(int(i))
            elif i in two_number_operations:
                stack.append(
                    eval(
                        str(max(stack[-2:])) 
                        + i 
                        + str(min(stack[-2:]))
                    )
                )
                stack.pop(-3)
                stack.pop(-2)    
            elif i == "DUP":
                stack.append(stack[-1])
            elif i == "POP":
                stack.pop(-1)    
            else:
                return "Invalid instruction: " + i
        if len(stack) >= 1:
            answer = stack[-1]
        return answer
