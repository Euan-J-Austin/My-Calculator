import os 

class activeInput:
  def __init__(self):
    pass
  def enter(i):
    try:
      if i[0] == 'C':
        storedInput.modify_stored(i)
      elif i == 'E':
        Output.eval_output(i)
      elif i[-2] == 'M':
        activeMemory.modify_memory(i)
      else:
        for x in i:
          if x != ' ':
            stored.append(x)
            activeInput.enter(Output.general_output())
    except IndexError: #deals with case of single operand or operator, where elif i[-2] == 'M' forces IndexError
      stored.append(i)
      activeInput.enter(Output.general_output())

class activeMemory:
  def __init__(self):
    pass
  def modify_memory(x):
    global MR #or will be assumed to be local as assigned a value in the function's body
    global stored
    if x == 'MS':
      MR = stored.copy()
      activeInput.enter(Output.general_output())
    elif x == 'MC':
      MR = []
      activeInput.enter(Output.general_output())
    elif x[-2:] == 'MR':
      operand = str(eval(''.join(MR))) #assign to a new variable as appending to stored affects MR for some reason
      stored.append(x[:-2])  #operator
      stored.append(operand) #operand
      activeInput.enter(Output.general_output())

class storedInput:
  def __init__(self):
    pass
  def modify_stored(x):
    if x == 'C':
      stored.clear()
      activeInput.enter(Output.general_output())
    if x == 'CE':
      del stored[-1]
      activeInput.enter(Output.general_output())

class Output:
  def __init__(self):
    pass
  def eval_output(x):
    if x == 'E':
      return print(eval(''.join(stored)))
  def general_output():
    os.system('clear')
    try:
      general_stored = eval(''.join(stored))
    except SyntaxError:
      general_stored = 0
    try:
      general_MR = eval(''.join(MR))
    except SyntaxError:
      general_MR = 0
    return input(f"""
STORED is {general_stored}.
[CE] [C]
MEMORY is {general_MR}.
[MS] [MC] [+MR] [-MR] [*MR] [/MR] [**MR]

ENTER: """)
      
MR = []
stored = []

activeInput.enter(Output.general_output())