def dir_reduc(arr):
​
    final_dir = []
  
    directions = {
      'NORTH' : 'SOUTH',
      'SOUTH' : 'NORTH',
      'WEST' : 'EAST',
      'EAST' : 'WEST'
    }
​
    for i in range(0,len(arr)):
      if len(final_dir) and directions[final_dir[len(final_dir) - 1]] == arr[i]:
        final_dir.pop()
      else:
        final_dir.append(arr[i])
​
​
    return final_dir
      
        