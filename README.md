# Convolutional Pose Machines
Original repository: [Convolutional Pose Machines - Tensorflow](https://github.com/timctho/convolutional-pose-machines-tensorflow)
## Environments
- Windows 10
- Anaconda3(64bit)
- tensorflow 1.3.0 
    - https://www.tensorflow.org/
- OpenCV 3.3
    - http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv

## Dataset
[FLIC Dataset](http://bensapp.github.io/datasets.html)
### Create dataset
Prepare data like
- dataset/person_0/imgs/
- dataset/person_0/labels.txt

And in **labels.txt**, the data format is *xxx.png, joint_0_x, joint_0_y, joint_1_x, joint_1_y, ...* 

And then run **create_cpm_tfr_fulljoints.py**.

    Please refer to genDataDemo.py to know how to generate labels.txt
## Training
See **train.py** for an example.

