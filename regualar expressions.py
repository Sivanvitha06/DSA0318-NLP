def fsa_accepts(string):
    state = 'q0'
    for char in string:
        if state == 'q0':
            if char == 'a':
                state = 'q1'
            else:
                state = 'q0' 
        elif state == 'q1':
            if char == 'b':
                state = 'q2'
            elif char == 'a':
                state = 'q1'  
            else:
                state = 'q0' 
        elif state == 'q2':
            if char == 'a':
                state = 'q1'
            else: 
                state = 'q0'
    return state == 'q2'
test_strings = ["ab", "aab", "bbaab", "abc", "aabb", "cabb"]
for s in test_strings:
    result = fsa_accepts(s)
    print(f"The string '{s}' is {'accepted' if result else 'rejected'} by the automaton.")
