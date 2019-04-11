import numpy as np
import matplotlib.pyplot as plt

sample_vectors = np.random.uniform(-1,1,[100,2])

print(sample_vectors) #1 sample per row

#function for computing the mean of min angles
def compute_angles(dimension):
	#random vector samples with values ranging from -1 to 1
	sample_vectors = np.random.uniform(-1,1,[100,dimension])
	'''
	Resulting array would be of this form for e.g sample size = 2
	[[-0.1 0.2 ..... d]
	 [-0.9,0.4 ..... d]]
	'''

	min_angles = []

	#computing min angles
	'''
	   Outerloop iterates over each vector in the sample vector list and then computes the angles
	   between this vector and all other vectors inside the innerloop,
	   resulting in a list of minimum angles for each vector
	'''
	for index_1,vector_1 in enumerate(sample_vectors):
		angle_list = []
		for index_2,vector_2 in enumerate(sample_vectors):
			#check to vector does not compute angle with itself
			if index_1 != index_2:
				#compute unit vectors/ divide the vector by its length
				unit_vector_1 = vector_1/np.linalg.norm(vector_1)
				unit_vector_2 = vector_2/np.linalg.norm(vector_2)
				#angle is computed by taking dot product of both vectors
				angle = np.arccos(np.dot(unit_vector_1,unit_vector_2))
				angle_list.append(angle)
		#get the minimum angle from the list of computed angles for the current vector
		min_angles.append(min(angle_list))

	avg = np.mean(min_angles)
	return avg

print(compute_angles(2))

#repeated for dimension 1-1000
#may run for a few minutes, pick a larger step or smaller d_high for faster execution

d_low = 1
d_high = 1000
step = 1;
average = []
for d in range(d_low, d_high+1, step):
	average.append(compute_angles(d))

#plot of average angle values against dimensions
plt.plot(np.arange(d_low, d_high+1, step),average)
plt.xlabel('dimension')
plt.ylabel('avg min angle (rad)')
plt.show()
