class activeInput:
  def __init__(self):
    pass
  def enter(i):
    try: 
      if i[0] == 'C':
        storedInput.modify_stored(i)
      elif i[-2] == 'M':
          activeMemory.modify_memory(i)
      else:
        for x in i:
          if x != ' ':
            stored.append(x)
            print(stored)
            activeInput.enter(input('Enter: '))
    except IndexError: #deals with case of single operand or operator
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
    if x == 'MC':
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

MR = []
stored = []

activeInput.enter(input('Enter: '))