# -*- coding: utf-8 -*-
"""imageprediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pD87pexdVHE9h6zX5CPc16V9v3QPRKrZ
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
from google.colab.patches import cv2_imshow
from PIL import Image
import tensorflow as tf
tf.random.set_seed(3)
from tensorflow import keras
from keras.datasets import mnist
from tensorflow.math import confusion_matrix

(x_train,y_train ),(x_test, y_test) = mnist.load_data()

type(x_train)

print(x_train.shape, y_train.shape,x_test.shape, y_test.shape)

print(x_train[10])

plt.imshow(x_train[10])
plt.show()

print(y_train[10])

print(np.unique(y_train))
print(np.unique(y_test))

x_train = x_train/255
x_test = x_test/255

print(x_train[10])

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(50,activation='relu'),
    keras.layers.Dense(50,activation='relu'),
    keras.layers.Dense(10,activation='sigmoid')
])

model.compile(optimizer='adam',
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train,y_train,epochs=10)

loss , accuracy = model.evaluate(x_test, y_test)
print(accuracy)

print(x_test.shape)

plt.imshow(x_test[7])

print(y_test[7])

y_pred = model.predict(x_test)

print(y_pred[7])
y_pred.shape

"""model.predict() gives the prediction probability of each class for that data point

"""

label_for_text_image = np.argmax(y_pred[7])
print(label_for_text_image)

y_pred_labels = [np.argmax(i) for i in y_pred]
print(y_pred_labels)

"""Y_test --> True labels

Y_pred_labels --> Predicted Labels
"""

conf_mat = confusion_matrix(y_test, y_pred_labels)

plt.figure(figsize=(15,7))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues')
plt.ylabel('True Labels')
plt.xlabel('Predicted Labels')

!wget https://miro.medium.com/v2/resize:fit:451/0*kKxxK1YXSyWMEBtS.PNG

input_img = cv2.imread('/content/mnist.PNG')

type(input_img)

plt.imshow(input_img)

input_img.shape

gray_img = cv2.cvtColor(input_img,cv2.COLOR_RGB2GRAY)

gray_img.shape

input_image_resize = cv2.resize(gray_img, (28, 28))

plt.imshow(input_image_resize)

input_image_resize.shape

input_image_resize = input_image_resize/255

image_reshaped = np.reshape(input_image_resize, [1,28,28])

input_prediction = model.predict(image_reshaped)
print(input_prediction)

input_pred_label = np.argmax(input_prediction)

print(input_pred_label)

