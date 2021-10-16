parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:

def get_parking_lot():
    state ={}
    state['total_Slots']=0
    state['available_Slots']=0
    state['occupied_Slots']=0
    for i in range(0,3):
      for j in range(0,3):
        if parking_state[i][j]==1:
          state['total_Slots']+=1
          state['occupied_Slots']+=1
        elif parking_state[i][j]==2:
            state['total_Slots']+=1
            state['available_Slots']+=1
        else:
          pass
        #print(j)
    return state

print(get_parking_lot())    


