class EarleyParser:
    def _init_(self, grammar):
        self.grammar = grammar
        self.chart = []

    def parse(self, tokens):
        self.chart = [[] for _ in range(len(tokens) + 1)]
        self.chart[0].append(("S'", ["S"], 0, 0))  
        for i in range(len(tokens) + 1):
            for state in self.chart[i]:
                if self._is_complete(state):
                    self._complete(state, i)
                elif not self._is_complete(state) and self._next_symbol(state) in self.grammar:
                    self._predict(state, i)
                elif not self._is_complete(state) and i < len(tokens) and self._next_symbol(state) == tokens[i]:
                    self._scan(state, i)
        for state in self.chart[len(tokens)]:
            if state == ("S'", ["S"], 1, 0):
                return True
        return False
    def _is_complete(self, state):
        _, rule, dot, _ = state
        return dot >= len(rule)

    def _next_symbol(self, state):
        _, rule, dot, _ = state
        if dot < len(rule):
            return rule[dot]
        return None
    def _predict(self, state, index):
        _, rule, dot, _ = state
        next_symbol = rule[dot]
        for production in self.grammar[next_symbol]:
            new_state = (next_symbol, production, 0, index)
            if new_state not in self.chart[index]:
                self.chart[index].append(new_state)
    def _scan(self, state, index):
        _, rule, dot, start = state
        next_symbol = rule[dot]
        if index < len(self.chart) - 1:
            new_state = (state[0], state[1], dot + 1, start)
            self.chart[index + 1].append(new_state)
    def _complete(self, state, index):
        left, rule, dot, start = state
        for prev_state in self.chart[start]:
            if not self._is_complete(prev_state) and self._next_symbol(prev_state) == left:
                new_state = (prev_state[0], prev_state[1], prev_state[2] + 1, prev_state[3])
                if new_state not in self.chart[index]:
                    self.chart[index].append(new_state)

if __name__ == "_main_":
    grammar = {
        'S': [['NP', 'VP']],
        'NP': [['Det', 'N']],
        'VP': [['V', 'NP']],
        'Det': [['the']],
        'N': [['cat'], ['dog']],
        'V': [['chased'], ['saw']]
    }
    parser = EarleyParser(grammar)
    sentence = "the cat chased the dog".split()
    if parser.parse(sentence):
        print("The sentence is valid according to the grammar.")
    else:
        print("The sentence is not valid according to the grammar.")
