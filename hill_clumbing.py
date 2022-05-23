# -*- coding: utf-8 -*-
"""hill clumbing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1clg75XiAOygM3kzl2SSLtqgWqNvudmqi
"""

state=[2, 1, 5, 0, 8, 4, 10, 0, 20, 10]

def calc_cost(state):
  a=len(state)
  
  add=0;
  for i in range(0,a):
    for j in range(i+1,a):
      if state[i]>state[j]:
        add+=1
  
  return add

def state_generation(current_state,current_state_cost):
  ab=len(current_state)
  
  
  temp=[]
  temp1=[]
  
  for k in current_state:
    temp.append(k)

  for k in current_state:
    temp1.append(k)
  min_cost=99999
  for i in range(0,ab):
    
    for j in range(i+1,ab):
      l=0
      for k in current_state:
          temp[l]=k
          l+=1
      
      g=temp[j]
      temp[j]=temp[i]
      temp[i]=g
     
      
      e=calc_cost(temp)
      
      
      if(e<min_cost):
        min_cost=e
        l=0
        for k in temp:
          temp1[l]=k
          l+=1
        
        
        
        
  
  if min_cost < current_state_cost:
    
    return temp1,min_cost
  else:
    
    return current_state,None

def goal_test(state):
 
  if calc_cost(state) == 0:
    return True
  else:
    return False

while(not goal_test(state)):
   cost=calc_cost(state)
   state,cost=state_generation(state,cost)
  
   if cost==None:
     print(state)
     break

print(state)