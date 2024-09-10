class FSM:
    def __init__(self):
        self.state = 'start'

    def transition(self, letter):
        if self.state == 'start':
            if letter in 'sxz':
                self.state = 'add_es'
            elif letter == 'y':
                self.state = 'change_y_to_ies'
            elif letter in 'h' and self.word[-2] in 'cs':
                self.state = 'add_es'
            else:
                self.state = 'add_s'

    def pluralize(self, word):
        self.word = word
        for letter in word:
            self.transition(letter)
        if self.state == 'add_es':
            return word + 'es'
        elif self.state == 'change_y_to_ies':
            return word[:-1] + 'ies'
        else:
            return word + 's'

fsm = FSM()
words = ["cat", "dog", "box", "church", "baby", "fox", "bush"]
for word in words:
    print(f"Plural of {word} is {fsm.pluralize(word)}")
