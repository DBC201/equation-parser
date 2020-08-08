from equation.queue import Queue
from equation.stack import Stack


class Parser:
    operators = {  # precedence values
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    def __init__(self, equation=None):
        self.equation = ''
        if equation:
            self.equation = equation

    def __evaluate_post_fix(self, inp):
        def operate(a, b, operand):
            if operand == '+':
                return a + b
            elif operand == '-':
                return a - b
            elif operand == '*':
                return a * b
            elif operand == '/':
                return a / b
            elif operand == '^':
                return a ** b
            else:
                raise RuntimeError(f"Wrong operand: {operand}")

        post_fix = Stack()
        while not inp.isEmpty():
            e = inp.dequeue()
            if e in self.operators:
                n2 = post_fix.pop()
                n1 = post_fix.pop()
                post_fix.push(operate(n1, n2, e))
            else:
                post_fix.push(e)
        if post_fix.size() > 1:
            raise RuntimeError(f"Invalid equation: {self.equation}")
        return post_fix.pop()

    def parse(self, variables=None, equation=None):
        if equation:
            self.equation = equation

        output = Queue()
        operator_stack = Stack()

        def is_number(inp):
            try:
                float(inp)
            except ValueError:
                return False
            return True

        token_index = 0

        while token_index < len(self.equation):
            token = self.equation[token_index]
            if is_number(token):
                number_str = ''
                while is_number(self.equation[token_index]):
                    number_str += str(self.equation[token_index])
                    token_index += 1
                    if token_index >= len(self.equation):
                        break
                output.enqueue(float(number_str))
                continue
            elif token in self.operators:
                if not operator_stack.isEmpty():
                    top_operator = operator_stack.peek()
                    if not top_operator == '(':
                        while self.operators[top_operator] >= self.operators[token]:
                            if operator_stack.isEmpty() or operator_stack.peek() == '(':
                                break
                            output.enqueue(operator_stack.pop())
                operator_stack.push(token)
            elif variables and token in variables:
                if token_index == 0 or not is_number(self.equation[token_index - 1]):
                    output.enqueue(1)
                operator_stack.push('*')
                output.enqueue(variables[token])
            elif token == '(':
                operator_stack.push(token)
            elif token == ')':
                while operator_stack.peek() != '(':
                    output.enqueue(operator_stack.pop())
                if operator_stack.peek() == '(':
                    operator_stack.pop()
                else:
                    raise RuntimeError("Mismatched parentheses!")
            else:
                raise RuntimeError(f"Undeclared variable: {token}")
            token_index += 1

        while not operator_stack.isEmpty():
            output.enqueue(operator_stack.pop())

        return self.__evaluate_post_fix(output)
