def get_trajectory_drivers_info(fpath):
	"""
	
	Function reads the modeling file and returns the idx of the trajectory drivers of the model
	
	
	Parameters:
	fpath							:	string
										absolute path of the modeling file
			
	Returns	: 
	trajectory_drivers_idxs_info:	list
									indexes of trajectory drivers in jacobian matrix
	"""
	import numpy as np
	import os

#	try:

	trajectory_drivers_idxs_info = []

	modeling_file_data = np.loadtxt(fpath,
									dtype='float',
									delimiter=',',
									comments="#")

	for row in modeling_file_data:
		if row[0] == 6:
			trajectory_drivers_idxs_info.append(int(row[1]))
			trajectory_drivers_idxs_info.append(int(row[1]+1))

	return trajectory_drivers_idxs_info

#	except exception as e:
#		print(e)


if __name__ == '__main__' :

	import os
	import numpy as np


	input_folder = r'C:\Documentos\IST\PhD\Thesis'
	model = r'SimplePendulum_hrz_IDA_MC'

	fpath = os.path.join(input_folder, model, 'Modeling_File.mod')

	trajectory_drivers_idxs_info = get_trajectory_drivers_info(fpath)

	# print(trajectory_drivers_idxs_info )

	np.random.seed(42)
	test_array = np.random.rand(7,5)
	print('test_array_before', test_array.shape, test_array)

	updated_test_array = np.delete(test_array, trajectory_drivers_idxs_info[2::], axis=0)
	print('test_array_after', updated_test_array.shape, updated_test_array)



