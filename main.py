#Standard calculator

#Input - active input (values you're inputting right now , stored in input (current computation)

#Memory -- MS (memory store), MR (recall stored numbers), M+ means add presently displayed value to value in memory changing the value in memory, M- substract present value from stored value changing the value in memory, MC (memory clear)

#Modify input -- CE (clear most recenty entry), C (clear all input)

#Calculations class - addition, subtraction, multiplication, division , BIDMAS 

#Output -- print values

# INPUT active input - input a value and arithmetical operator, this is sent to stored 

#can just enter al input at once and have user confirm it is correct? does python account for order of ops? 

active_input = input("Input all operands and operators: ")
stored_input = []

def current_output(active_input):
  try:
    if active_input[1] == '+':
      return int(active_input[0])+int(active_input[2])
  except TypeError:
    pass

def clear_entry(stored_input):
  del stored_input[:-1]
  return print(stored_input)
  

def clear_all(stored_input):
  stored_input.clear()
  return print(stored_input)

## need a while loop here, while ai != calc

if active_input == 'CE':
  stored_input = stored_input[0:-1]
  print(stored_input)
elif active_input == 'C':
  clear_all(stored_input)
elif active_input != 'CE' and 'C':
  for o in active_input:
      stored_input.append(o)
  print(f'Stored input is {stored_input}')
  print(stored_input[0:-1])
  print(f'Current output is {current_output(active_input)}')
  active_input = input("Input all operands and operators: ")