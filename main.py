stored_input = []
memory = ['0']

class calculateOutput:
  pass
  # def __init__(self, si):
  #   self.x = eval(''.join(si))

  # def current_output(self, si):
  #   #need try test here 
  #   return self.si
  
  # def execute(self, si):
  #   return print(f'The final value is: {self.x}.')

class modifyStoredInput:
  def __init__(self):
    pass
  def modify(actinp):
    if actinp == 'CE':
      del stored_input[-1]
      print(stored_input[0:])
      active.entry(input("Enter all operands and operators: "))
    else: #if actinp is equal to C
      stored_input.clear()
      print(stored_input)
      active.entry(input("Enter all operands and operators: "))

class memoryUtility:
  def __init(self):
    pass
  def modify(actinp):
    if actinp == 'MC':
      memory.clear()
    if actinp == '+MR' or '-MR' or '*MR' or '/MR' or '**MR':
      #either operating on stored input e.g. actinp = '+MR' or operation producing value
      #for stored_input e.g. '+7*MR'
      if actinp == '+MR':
        stored_input.append('+')
        stored_input.append(eval(''.join(actinp[0:-3])) + eval(''.join(memory)))
      if actinp == '-MR':
        stored_input.append(eval(''.join(actinp[0:-3])) - eval(''.join(memory)))
      if actinp == '*MR':
        stored_input.append(eval(''.join(actinp[0:-3])) * eval(''.join(memory)))
      if actinp == '/MR':
        stored_input.append(eval(''.join(actinp[0:-3])) / eval(''.join(memory)))
      if actinp == '**MR':
        stored_input.append(eval(''.join(actinp[0:-4])) ** eval(''.join(memory)))
    if actinp == 'M+':
      new_mem= eval(''.join(memory)) + eval(''.join(stored_input))
      memory.clear()
      memory.append(new_mem)
      print(memory)
      active.entry(input("Enter all operands and operators: "))
    if actinp == 'M-':
      new_mem = eval(''.join(memory)) - eval(''.join(stored_input))
      memory.clear()
      memory.append(new_mem)
      print(memory)
      active.entry(input("Enter all operands and operators: "))
    if actinp == 'MS':
      memory.clear()
      memory.append(eval(''.join(stored_input)))
      print(memory)
      active.entry(input("Enter all operands and operators: "))

class activeEntry(modifyStoredInput): # calculateOutput
  def __init__(self):
    pass
  def entry(self, actinp):
      if actinp[0] == 'C':
        modifyStoredInput.modify(actinp)
      if actinp[-1:] or actinp[-2:] == 'M':
        memoryUtility.modify(actinp)
      # elif actinp == 'Execute':
      #   calculateOutput.current_output(stored_input)
      if actinp[0].isnumeric() or actinp[1].isnumeric() or actinp[2].isnumeric() is True:
        for o in actinp:
          if o != ' ':
            stored_input.append(o)
        print(f'Stored input is {stored_input}')
        print(f"Current output is {eval(''.join(stored_input))}")
        self.entry(input("Enter all operands and operators: "))

active = activeEntry()
modify = modifyStoredInput()
# calculate = calculateOutput()

active.entry(input("Enter all operands and operators: "))

      #this solves the memory recall operations issues 

# si = ['1']

# memory = ['1']

# actinp = '+1+MR'

# if actinp[0] == '+' or '-' or '*' or '/' or '**':
#   si.append(actinp[0])
# if actinp[-3:] == '+MR':
#   try:
#     si.append(str(eval(''.join(actinp[0:-3])) + eval(''.join(memory))))
#   except SyntaxError:
#     si.append(str(eval(''.join(memory))))
#   print(si)
#   print(type(si))
#   print(eval(''.join(si)))