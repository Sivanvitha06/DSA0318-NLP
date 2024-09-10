class Parser:
    def __init__(self, tokens):
        self.tokens = tokens 
        self.pos = 0          

    def eat(self, token_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos] == token_type:
            self.pos += 1
        else:
            raise SyntaxError(f"Expected {token_type} but found {self.tokens[self.pos]}")

    def parse_E(self):
        """Parse E → T + E | T"""
        node = self.parse_T()
        if self.pos < len(self.tokens) and self.tokens[self.pos] == '+':
            self.eat('+')
            node = ('+', node, self.parse_E())  # E → T + E
        return node

    def parse_T(self):
        """Parse T → F * T | F"""
        node = self.parse_F()
        if self.pos < len(self.tokens) and self.tokens[self.pos] == '*':
            self.eat('*')
            node = ('*', node, self.parse_T())  # T → F * T
        return node

    def parse_F(self):
        """Parse F → (E) | num"""
        if self.tokens[self.pos] == '(':
            self.eat('(')
            node = self.parse_E()
            self.eat(')')
            return node
        else:  # Assume it's a number
            num = self.tokens[self.pos]
            self.eat(num)
            return num

# Example usage
def tokenize(expression):
    """Simple tokenizer to split expression into tokens."""
    return expression.replace('(', ' ( ').replace(')', ' ) ').split()

# Test the parser
expression = "3 * ( 5 + 2 )"
tokens = tokenize(expression)
parser = Parser(tokens)
parse_tree = parser.parse_E()
print("Parse tree:", parse_tree)
