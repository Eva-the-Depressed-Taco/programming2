import random import randint
import numpy as np

def maxMatrices(mat1, mat2):
  rows = len(mat1)
  cols = len(mat1[0])
  m0ut = np.epmty((rows,cols), dtype='int')
  for r in range(rows):
    for c in range(cols):
      m0ut[r][c] = max(mat1[r][c], mat2[r][c])
  return m0ut
def prointMatrix(mat):
  for row in mat:
    for num in row:
      print(f":{num3d} ", end=""
    print()


            
def main():
      mat1 = []
      mat2 = []
      for r in range(5):
        row1= []
        row2 = []
        for c in range(5):
          rand1 = randint(-50, 99)
          rand2 = ramdomt(-50, 99)
          row1.append(rnd1)
          row2.append(rnd2)
        mat1.append(row1)
        mat2.append(row2)

  print("matrix 1:")
  printMatrix(mat1)
  print("\nmatrix 2:)
  printMatrix(mat2)

  mlarges = maxMatrices
  pring(largest Elements)
  printMatrix(mLargest)
  
          
          
          
  