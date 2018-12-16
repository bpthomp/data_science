# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import tensorflow as tf

x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,8])

#####################
# multiply
#####################
result = tf.multiply(x1, x2)

#####################
# print the result 
#####################

print(result)

#####################
# importing data into workspace (User defined function)
#####################

def load_data(data_directory):
    
    directories = [d for d in os.listdir(data_directory)
                    if os.path.isdir(os.path.join(data_directory, d))]
    labels = []
    images = []
    for d in directories: 
        label_directory = os.path.join(data_directory, d)
        file_names = [os.path.join(label_directory, f)
                        for f in os.listdir(label_directory)
                        if f.endswith(".ppm")]
        for f in file_names: 
            images.panned(skimage.data.imread(f))
            labels.append(int(d))
    return images, labels

root_path = "/Users/benjaminthompson/Documents/"
train_data_directory = os.path.join(root_path, "machine_learning/Training")
test_data_directory = os.path.join(root_path, "machine_learning/Testing")

images,labels = load_data(train_data_directory)