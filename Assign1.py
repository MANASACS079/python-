#Define a grid as shown above
grid=[[1,2,3,2,3,1,3,2,1],
      [4,5,6,4,5,6,4,6,5],
      [7,8,9,7,8,9,8,9,7],
      [4,5,6,2,3,1,2,3,1],
      [1,2,3,5,4,6,4,5,6],
      [7,8,9,7,8,9,7,8,9],
      [8,7,9,1,3,2,3,1,2],
      [4,5,6,6,5,4,9,8,7],
      [2,3,1,7,9,8,4,6,5]]
# for row in grid:
#      for element in row:
#         print(element)
 

for i in range(0,9):
  for j in range(0,9):
    print(grid[i][j],end=' ')
  print()  
  
