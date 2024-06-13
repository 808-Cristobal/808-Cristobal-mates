#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Simulación de una máquina de Turing en Python

class TuringMachine:
    def __init__(self, tape="", blank_symbol=" ", initial_state="", final_states=None, transition_function=None):
        self.tape = dict(enumerate(tape))  # La cinta se almacena 
        self.blank_symbol = blank_symbol
        self.head_position = 0
        self.current_state = initial_state
        self.final_states = final_states if final_states else set()
        self.transition_function = transition_function if transition_function else {}

    def get_tape(self):
       
        min_used_index = min(self.tape.keys())
        max_used_index = max(self.tape.keys())
        return "".join(self.tape.get(i, self.blank_symbol) for i in range(min_used_index, max_used_index + 1))

    def step(self):
        
        current_symbol = self.tape.get(self.head_position, self.blank_symbol)

        
        action = self.transition_function.get((self.current_state, current_symbol))
        if action is None:
            return False  

        new_state, new_symbol, direction = action

        # Escribir el nuevo símbolo 
        self.tape[self.head_position] = new_symbol

        
        if direction == "R":
            self.head_position += 1
        elif direction == "L":
            self.head_position -= 1

        
        self.current_state = new_state

        return True

    def run(self, max_steps=1000):
        steps = 0
        while self.current_state not in self.final_states and steps < max_steps:
            if not self.step():
                break
            steps += 1
        return self.get_tape()

#Definición 
tape = "1011"  
initial_state = "q0"
final_states = {"qf"}
blank_symbol = " "


transition_function = {
    ("q0", "0"): ("q0", "0", "R"),
    ("q0", "1"): ("q0", "1", "R"),
    ("q0", " "): ("qf", " ", "N"), 
}

tm = TuringMachine(tape=tape, blank_symbol=blank_symbol, initial_state=initial_state, final_states=final_states, transition_function=transition_function)


result = tm.run()

print(f"Resultado final en la cinta: {result}")


# In[ ]:




