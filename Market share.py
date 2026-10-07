from random import random
import matplotlib.pyplot as plt

times = []
Volture_owners = []
NeonDrive_owners = []

Volture = 0
NeonDrive = 0

for i in range(10000):
    if i < 5:
        if random() < 0.5:
            Volture += 1
        else:
            NeonDrive += 1
    else:
        if random() < Volture/(Volture+NeonDrive):
            Volture += 1
        else:
            NeonDrive += 1
    times.append(i)
    Volture_owners.append(Volture)
    NeonDrive_owners.append(NeonDrive)

plt.plot(times,Volture_owners)
plt.plot(times,NeonDrive_owners)
plt.xlabel('Time')
plt.ylabel('No. owners')
plt.legend(['Volture', 'NeonDrive'])
plt.show()

print(Volture,":",NeonDrive)

