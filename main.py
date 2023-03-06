#Standard calculator

#Input - active input (values you're inputting right now , stored in input (current computation)

#Modify input -- CE (clear most recenty entry), C (clear all input)

#Memory -- MS (memory store), MR (recall stored numbers), M+ means add presently displayed value to value in memory changing the value in memory, M- substract present value from stored value changing the value in memory, MC (memory clear)

#Calculations class - addition, subtraction, multiplication, division , BIDMAS 

#Output -- print values

# INPUT active input - input a value and arithmetical operator, this is sent to stored 

active_input = input("Input sinlge operand or operator: ")
#this allows for order of operations?
stored_input = []

while active_input != 'Calculate':
  stored_input.append(active_input)
  print(f'Stored input is {stored_input}')
  active_input = input("Input single operand or operator: ")
else:
  pass

print(stored_input)
