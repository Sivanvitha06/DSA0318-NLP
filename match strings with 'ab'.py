q0 = 0
q1 = 1
q2 = 2
current_state = q0
accepting_state = q2
transition_function = {
    (q0, 'a'): q1,
    (q1, 'b'): q2,
    (q0, 'b'): q0,
    (q1, 'a'): q1,
    (q2, 'a'): q1,
    (q2, 'b'): q0
}
test_strings = ["aab", "bbab", "ab", "bbaa", "abab"]
results = {}
for input_string in test_strings:
    current_state = q0
    for char in input_string:
        if (current_state, char) in transition_function:
            current_state = transition_function[(current_state, char)]
        else:
            current_state = q0
    results[input_string] = current_state == accepting_state
print(results)
