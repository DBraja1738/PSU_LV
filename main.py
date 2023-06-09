import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image_dataset_from_directory
from keras import layers
import numpy as np
train_ds = image_dataset_from_directory(
 directory='C:/Users/student/Documents/lv8psu/Train',
 labels='inferred',
 label_mode='categorical',
 batch_size=32,
 image_size=(48, 48))


model=keras.Sequential()
model.add(layers.Conv2D(32,(3,3),activation='relu', input_shape=(48,48,3)))
model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Flatten())

model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(43, activation='softmax'))


model.summary()
model.compile(optimizer='adam',
loss='categorical_crossentropy',
metrics=['accuracy'])


model.fit(train_ds, epochs=3)

model.save('dbmodel')