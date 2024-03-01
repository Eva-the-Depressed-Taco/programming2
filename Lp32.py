slices = int(input("enter slices"))
dia = int(input("enter daimter"))
Laborcosts = 0.75 * slices
rent = 1 * slices
mat = dia * 0.05
total = mat + rent + Laborcosts
print("cost =", total)