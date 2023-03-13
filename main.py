MR = ['0']
stored = []

class activeInput:
  def __init__(self):
    pass
  def enter(i):
    #evaluates to numeric is true?
    if i[0] == 'C':
      storedInput.modify_stored(i)
    if i[-2:] == 'M':
      activeMemory.modify_memory(i)
    if i[0] != 'C' or i[-2:] != 'M':
      for x in i:
        if x != ' ':
          stored.append(x)
      print(stored)
      print(eval(''.join(stored)))
      activeInput.enter(input('Enter: '))
  
class activeMemory:
  def __init__(self):
    pass
  def modify_memory(self, x):
    if x == 'MS':
      MR.clear()
      for n in stored:
        MR.append(stored)
      print(MR)
    if x == 'MC':
      MR.clear()

class storedInput:
  def __init__(self):
    pass
  def modify_stored(self, x):
    if x == 'C':
      stored.clear()
    if x == 'CE':
      del stored[-1]
                 
activeInput.enter(input('Enter: '))