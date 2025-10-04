#!/usr/bin/env python3
# This is a translator for a brainfuck inspired conlang
Memory = [0,0,0] # 0 is position in memory, all others is just memory
program = input('Hello, welcome to this brainfuck inspire conlang.\nPlease input the program you want to run. (only a single line)\n')
position = 0 # position in program
loops = [0]

def run(pos):
    global position
    global Memory
    global program
    if pos == '>':
        if Memory[0] + 3 > len(Memory):
            Memory.append(0)
        Memory[0] += 1
    elif pos == '<':
        if Memory[0] != 0:
            Memory[0] -= 1
    elif pos == '+':
        Memory[Memory[0] + 1] += 1
    elif pos == '-':
        Memory[Memory[0] + 1] -= 1
    elif pos == '[':
        loops.append(position)
        loops[0] += 1
    elif pos == ']':
        if Memory[Memory[0] + 1] != 0:
            position = loops[loops[0]]
        else:
            del loops[1]
            loops[0] -= 1

while position < len(program):
    run(program[position])
    position += 1

Final_output = ''
position = 1

while position < len(Memory):
    Final_output += str(Memory[position])
    Final_output += '_'
    position += 1
print(Final_output)