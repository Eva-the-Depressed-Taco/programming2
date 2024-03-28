des = int(input("enter designing time"))
cod = int(input("enter coding time"))
deb = int(input("enter debiging time"))
tes = int(input("enter testing time "))

time = des + cod + deb + tes
desP = des / time
codP = cod / time
debP = deb / time
tesP = tes / time
print ("percntage diplayed out")
print("design percntage  =", desP)
print("codeing percntage  =", codP)
print("debug percntage  =", debP)
print("test percntage  =", tesP)