'''
lsho = 0
lelb = 1
lwri = 2
rsho = 3
relb = 4
rwri = 5
lhip = 6
rhip = 9
leye = 12
reye = 13
nose = 16
'''


from scipy import io
import random
import os
from scipy import misc
import matplotlib.pyplot as plt
img_dir = './dataset/person_0/imgs'

example = io.loadmat('examples.mat')['examples'][0]
i = random.randint(0, len(example))
img = misc.imread(os.path.join(img_dir, example[i]['filepath'][0]))
coords = example[i]['coords']
plt.figure()
plt.imshow(img)
plt.plot(coords[:,[0,1,2]][0],coords[:,[0,1,2]][1]) # left arm
plt.plot(coords[:,[3,4,5]][0],coords[:,[3,4,5]][1]) # right arm
plt.plot(coords[:, [6,9]][0], coords[:, [6,9]][1])  # hip
plt.plot(coords[:,[12,13,16,12]][0], coords[:,[12,13,16,12]][1])

plt.show()