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

import codecs
from scipy import io
import random
import os
from scipy import misc
import matplotlib.pyplot as plt

img_dir = './dataset/person_0/imgs'

f = codecs.open('./dataset/person_0/labels.txt', 'wb', encoding='utf-8')

example = io.loadmat('examples.mat')['examples'][0]

for i in range(500):
    coords = example[i]['coords']
    loc = []
    # loc = [coords[:, 16][0], coords[:, 16][1]]
    # loc = [str(x) for x in loc]
    for x, y in zip(coords[:, [0, 1, 2, 3, 4, 5, 6, 9, 12, 13, 16]][0],
                    coords[:, [0, 1, 2, 3, 4, 5, 6, 9, 12, 13, 16]][1]):
        loc.append(x)
        loc.append(y)
    bbox_top_left_y = (min(loc[0:22:2])) - 60
    bbox_top_left_x = (min(loc[1:22:2])) - 60
    bbox_bot_right_y = (max(loc[0:22:2])) + 60
    bbox_bot_right_x = (max(loc[1:22:2])) + 60
    img = misc.imread(os.path.join(img_dir, example[i]['filepath'][0]))
    if bbox_top_left_x < 0:
        bbox_top_left_x = 0
    if bbox_top_left_y < 0:
        bbox_top_left_y = 0
    if bbox_bot_right_x > img.shape[0]: bbox_bot_right_x = img.shape[0]
    if bbox_bot_right_y > img.shape[1]: bbox_bot_right_y = img.shape[1]
    # plt.figure()
    # plt.imshow(img[int(bbox_top_left_x):int(bbox_bot_right_x), int(bbox_top_left_y):int(bbox_bot_right_y), :])
    # plt.figure()
    # plt.imshow(img)
    # plt.show()
    bbox = [bbox_top_left_x, bbox_top_left_y, bbox_bot_right_x, bbox_bot_right_y]
    loc = [str(i) for i in loc]
    bbox = [str(i) for i in bbox]
    f.write('{} {} {}\n'.format(example[i]['filepath'][0], ' '.join(bbox), ' '.join(loc)))

f.close()


# i = random.randint(0, len(example))
# img = misc.imread(os.path.join(img_dir, example[i]['filepath'][0]))
# coords = example[i]['coords']
# plt.figure()
# plt.imshow(img)
# plt.plot(coords[:,[0,1,2]][0],coords[:,[0,1,2]][1]) # left arm
# plt.plot(coords[:,[3,4,5]][0],coords[:,[3,4,5]][1]) # right arm
# plt.plot(coords[:, [6,9]][0], coords[:, [6,9]][1])  # hip
# plt.plot(coords[:,[12,13,16,12]][0], coords[:,[12,13,16,12]][1])

# plt.show()
