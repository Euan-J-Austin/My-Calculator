#Standard calculator

#Input - active input (values you're inputting right now , stored in input (current computation)

#Memory -- MS (memory store), MR (recall stored numbers), M+ means add presently displayed value to value in memory changing the value in memory, M- substract present value from stored value changing the value in memory, MC (memory clear)

#Modify input -- CE (clear most recenty entry), C (clear all input)

#Calculations class - addition, subtraction, multiplication, division , BIDMAS 

#Output -- print values

#aesthetics --- clearing screen with every active_input entry? 


stored_input = []
memory = []

class calculateOutput:
  def __init__(self):
    pass

  def current_output(si):
    #need try test here 
    return eval(''.join(si))

class modifyStoredInput:
  def __init__(self):
    pass
  def modify(actinp):
    if actinp == 'CE':
      del stored_input[-1]
      print(stored_input[0:])
      active.entry(input("Enter all operands and operators: "))
    else:
      stored_input.clear()
      print(stored_input)
      active.entry(input("Enter all operands and operators: "))

class memoryUtility:
  def __init(self):
    pass
  def modify(actinp):
    if actinp == 'MC':
      memory.clear()
    elif actinp == 'MR':
      pass
    elif actinp == 'M+':
      sum(actinp)
    elif actinp == 'M-':
      pass
    elif actinp == 'MS':
      pass

class activeEntry(modifyStoredInput, calculateOutput):
  def __init__(self):
    pass
  def entry(self, actinp):
      if actinp[0] == 'C':
        modifyStoredInput.modify(actinp)
      elif actinp[0] == 'M':
        memoryUtility.modify(actinp)
        pass
      elif actinp == 'Execute':
        pass
        #use map function? 
      elif actinp != 'CE' and 'C' and 'Execute':
        for o in actinp:
          if o != ' ':
            stored_input.append(o)
        print(f'Stored input is {stored_input}')
        print(f'Current output is {calculateOutput.current_output(stored_input)}')
        self.entry(input("Enter all operands and operators: "))

active = activeEntry()
modify = modifyStoredInput()
calculate = calculateOutput()

active.entry(input("Enter all operands and operators: "))

