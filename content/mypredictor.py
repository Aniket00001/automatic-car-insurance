

from keras.models import load_model
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
from skimage.transform import resize

model = load_model('content/car2_final_model.h5')
upload='./static/'  #os.path.dirname(os.path.dirname(os.path.abspath('0021.jpg')))

def load_image(file_path): 
    return cv2.imread(file_path)
test_path ='content/static/upload/'
ima_files = os.listdir(test_path)
test_images = [load_image(test_path + file) for file in ima_files]


#print(test_images)
#print(ima_files)

my_image_resized =[] #resize the image to 32x32 pixel with depth = 3
for i in range(len(test_images)):
    test_images[i] =  resize(test_images[i], (90,90,3))
print(type(test_images)) 
img = plt.imshow(test_images[0]) #show new image


probabilities = model.predict(np.array( [test_images[0],] ))
#print(probabilities)
number_to_class = ['dent', 'scratch', 'smash','bumper_dent','side_dent','destroy','glass_shattered','shattered','lamp_broken','side_mirror','not_damage']
index = np.argsort(probabilities[0,:])


res="Fourth most likely class:"+number_to_class[index[7]]+"-- Probability:"+str(probabilities[0,index[7]])+"\nthird most likely class:"+number_to_class[index[8]]+"-- Probability:"+str(probabilities[0,index[8]])+"\nsecond most likely class:"+number_to_class[index[9]]+"-- Probability:"+str(probabilities[0,index[9]])+"\nFirst most likely class:"+number_to_class[index[10]]+"-- Probability:"+str(probabilities[0,index[10]])

file=open('data.txt','w')
file.write(res)
file=open('data.txt','r')
print(file.read())
file.close()
print("\n\n",res)
'''
print("least most likely class:", number_t o_class[index[0]], "-- Probability:", probabilities[0,index[0]])
print("least likely class:", number_to_class[index[1]], "-- Probability:", probabilities[0,index[1]])
print("ninth most likely class:", number_to_class[index[2]], "-- Probability:", probabilities[0,index[2]])
print("eight most likely class:", number_to_class[index[3]], "-- Probability:", probabilities[0,index[3]])
print("seventh most likely class:", number_to_class[index[4]], "-- Probability:", probabilities[0,index[4]])
print("sixth most likely class:", number_to_class[index[5]], "-- Probability:", probabilities[0,index[5]])
print("Fifth most likely class:", number_to_class[index[6]], "-- Probability:", probabilities[0,index[6]])
print("Fourth most likely class:", number_to_class[index[7]], "-- Probability:", probabilities[0,index[7]])
print("third most likely class:", number_to_class[index[8]], "-- Probability:", probabilities[0,index[8]])
print("second most likely class:", number_to_class[index[9]], "-- Probability:", probabilities[0,index[9]])
print("First most likely class:", number_to_class[index[10]], "-- Probability:", probabilities[0,index[10]])

'''