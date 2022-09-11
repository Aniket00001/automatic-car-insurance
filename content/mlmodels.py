from keras.models import load_model
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
from skimage.transform import resize


class MyRes():
	def show(self):
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		y = os.path.join(BASE_DIR, 'content\\car2_final_model.h5')
		model = load_model(y)
		upload='./static/'  #os.path.dirname(os.path.dirname(os.path.abspath('0021.jpg')))
		x = os.path.join(BASE_DIR, 'media\\documents')
		def load_image(file_path): 
		    return cv2.imread(file_path)
		test_path = x                     #'./static/upload/'
		ima_files = os.listdir(test_path)
		test_images = [load_image(test_path + file) for file in ima_files]


		#print(test_images)
		#print(ima_files)

		my_image_resized =[] #resize the image to 32x32 pixel with depth = 3
		for i in range(len(test_images)):
		    test_images[i] =  resize(test_images[i], (90,90,3))
		#print(type(test_images)) 
		img = plt.imshow(test_images[0]) #show new image


		probabilities = model.predict(np.array( [test_images[0],] ))
		#print(probabilities)
		number_to_class = ['dent', 'scratch', 'smash','bumper_dent','side_dent','destroy','glass_shattered','shattered','lamp_broken','side_mirror','not_damage']
		index = np.argsort(probabilities[0,:])


		res="Fourth most likely class:"+number_to_class[index[7]]+"  --   Probability:"+str(probabilities[0,index[7]])+"\nthird most likely class:"+number_to_class[index[8]]+"--       Probability:"+str(probabilities[0,index[8]])+"\nsecond most likely class:"+number_to_class[index[9]]+"--      Probability:"+str(probabilities[0,index[9]])+"\nFirst most likely class:"+number_to_class[index[10]]+"-- Probability:"+str(probabilities[0,index[10]])
		return res
a=MyRes()
d=a.show()
file=open('data.txt','w')
file.write(d)
file=open('data.txt','r')
print(file.read())
file.close()
print(d)