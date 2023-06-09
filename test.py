import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
image_path='D:/New folder/stop.png'
image=load_img(image_path, target_size=(48,48))
imagearray=img_to_array(image)


model=tf.keras.models.load_model('C:/Users/student/Documents/lv8psu/dbmodel')
prediction=model.predict(imagearray.reshape(1,48,48,3))
class_index=np.argmax(prediction)

print("prediction:class",class_index)