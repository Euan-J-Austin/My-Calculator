#next, using memory on stored input, append operand then integer value of memory

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
            print(stored)
            activeInput.enter(input('Enter: '))
    except IndexError: #deals with case of single operand or operator, where elif i[-2] == 'M' forces IndexError 
      stored.append(i)
      print(stored)
      activeInput.enter(input('Enter: '))

class activeMemory:
  def __init__(self):
    pass
  def modify_memory(x):
    if x == 'MS':
      MR = stored
      print(f'test {MR}')
      activeInput.enter(input('Enter: '))
    elif x == 'MC':
      MR = []
      print(f'test1 {MR}')
      activeInput.enter(input('Enter: '))

class storedInput:
  def __init__(self):
    pass
  def modify_stored(x):
    if x == 'C':
      stored.clear()
      print(f'test stored C {stored}')
      activeInput.enter(input('Enter: '))
    if x == 'CE':
      del stored[-1]
      print(f'test stored CE {stored}')
      activeInput.enter(input('Enter: '))

class Output:
  def __init__(self):
    pass
  def eval_output(x):
    if x == 'E':
      return print(eval(''.join(stored)))

MR = []
stored = []

activeInput.enter(input('Enter: ')) #must input single operand or operator 