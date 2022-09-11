from django.test import TestCase

# Create your tests here.

from keras.models import load_model
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
from skimage.transform import resize
class myres(TestCase):
	def show(self):
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
		#print(type(test_images)) 
		img = plt.imshow(test_images[0]) #show new image
		e=0
		lim=len(test_images)
		probabilities = model.predict(np.array( [test_images[0],] ))
		e=e+1	
		if(e<=lim):
			probabilities1 = model.predict(np.array( [test_images[1],] ))
			e=e+1
		if(e<=lim):
			probabilities2 = model.predict(np.array( [test_images[2],] ))
			e=e+1
		if(e<=lim):
			probabilities3 = model.predict(np.array( [test_images[3],] ))
			e=e+1	


		#print(probabilities)               #nparray type
		
		number_to_class = ['dent', 'scratch', 'smash','bumper_dent','side_dent','destroy','glass_shattered','shattered','lamp_broken','side_mirror','not_damage']
		index = np.argsort(probabilities[0,:])
		inde = np.argsort(probabilities1[0,:])
		ind = np.argsort(probabilities2[0,:])
		inx = np.argsort(probabilities3[0,:])
		
		dc="{\""+number_to_class[index[10]]+"\":\""+str(probabilities[0,index[10]])+"\",\""+number_to_class[inde[10]]+"\":\""+str(probabilities1[0,inde[10]])+"\",\""+number_to_class[ind[10]]+"\":\""+str(probabilities2[0,ind[10]])+"\",\""+number_to_class[inx[10]]+"\":\""+str(probabilities3[0,inx[10]])+"\"}"
		print(dc)
		print(type(dc))
		rs=json.loads(dc) 
		print(rs['dent'])
		print(type(rs))
		cost=0
		for x in rs:
			if("scratch"==x):
				cost=cost+1000
			if("dent"==x):
				cost=cost+2000
			if("shattered"==x):
				cost=cost+5000
			if("glass_shattered"==x):
				cost=cost+6200
			if("bumper_dent"==x):
				cost=cost+5800
			if("side_mirror"==x):
				cost=cost+5300
			if("lamp_broken"==x):
				cost=cost+5700		
			if("side_dent"==x):
				cost=cost+9950
			if("smash"==x):
				cost=cost+20500
			if("destroy"==x):
				cost="Thorough inspection in case of grave damage"	
			
		mes="total cost of repair: "+str(cost)				
		f=open('amrup.txt','w')
		f.write(mes)
		f.close()
		print(cost)

		res="Fourth most likely class:"+number_to_class[index[7]]+"  --   Probability:"+str(probabilities[0,index[7]])+"\nthird most likely class:"+number_to_class[index[8]]+"--       Probability:"+str(probabilities[0,index[8]])+"\nsecond most likely class:"+number_to_class[index[9]]+"--      Probability:"+str(probabilities[0,index[9]])+"\nFirst most likely class:"+number_to_class[index[10]]+"-- Probability:"+str(probabilities[0,index[10]])
		return str(rs)
a=myres()
d=a.show()
file=open('content/data.txt','w')
file.write(d)
file=open('content/data.txt','r')
print(file.read())
file.close()
print(d)