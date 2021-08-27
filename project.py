# Imported modules
import imageio, sys, os, numpy as np
from tqdm import tqdm


##### STUDENT SECTION START #####
'''
This section below is where your transformation functions will go.

You have to figure out the parameters. Then write the functions and only
return the numpy array of the transformed image. The bare
minimum parameter will always be the image and is included already.
'''

# Flip image vertically
def flip_vertical_trans(img, params):
	### Your Code Goes Here Start ###
	img_new = img.copy()
	
	return img_new
	### Your Code Goes Here End ###

# Flip image horizontally
def flip_horizontal_trans(img, params):
	### Your Code Goes Here Start ###
	img_new = img.copy()
	
	return img_new
	### Your Code Goes Here End ###

# Translation Function
def translation_trans(img, params):
	### Your Code Goes Here Start ###
	img_new = img.copy()
	
	return img_new
	### Your Code Goes Here End ###

# Rotate Function
def rotate_trans(img, params):
	### Your Code Goes Here Start ###
	img_new = img.copy()
	
	return img_new
	### Your Code Goes Here End ###

# Similarity Function
def similarity_trans(img, params):
	### Your Code Goes Here Start ###
	img_new = img.copy()
	
	return img_new
	### Your Code Goes Here End ###

# Affine Function
def affine_trans(img, params):
	### Your Code Goes Here Start ###
	img_new = img.copy()
	
	return img_new
	### Your Code Goes Here End ###

# Projective Function
def projective_trans(img, params):
	### Your Code Goes Here Start ###
	img_new = img.copy()
	
	return img_new
	### Your Code Goes Here End ###

# Subtract Function
def subtract_trans(img, params):
	### Your Code Goes Here Start ###
	img_new = img.copy()
	
	return img_new
	### Your Code Goes Here End ###
##### STUDENT SECTION END #####



##### HELPERS START #####
# Create output filename and path
def get_output_path(output_dir, img_path, trans):
	# Captures full fname from path and splits at fname and extension
	img_fname, img_ext = os.path.split(img_path)[-1].rsplit('.', 1)

	# Creates new fname with extension and adds full output path
	new_fname_ext = f'{img_fname}-{trans}.{img_ext}'
	out_path = os.path.join(output_dir, new_fname_ext)

	return out_path

# Gets paths to images in data directory
def get_image_paths(data_dir):
	# Pull image files in dir, must be png, jpg, jpeg
	img_exts = ['png', 'jpg', 'jpeg']
	img_list = os.listdir(data_dir)
	img_list = [f for f in img_list if f.rsplit('.', 1)[-1] in img_exts]

	# Check to make sure it found images, exit if not
	if not img_list:
		print(f'No images found in {data_dir}. Exiting program...\n') 
		sys.exit(1)

	# Add directory to path of image files
	img_path_list = [os.path.join(data_dir, f) for f in img_list]
	img_path_list = [f for f in img_path_list if os.path.isfile(f)]

	# Check to make sure it found image paths, exit if not
	if not img_path_list:
		print(f'No images found in {data_dir}. Exiting program...\n')
		sys.exit(1)

	return img_path_list
##### HELPERS END #####



# Main Function, in Python, ALWAYS use a main function
def main():
	# CLI Positional Args
	# data_dir = sys.argv[1]
	# output_dir = sys.argv[2]

	# Args, no command line args. Comment out to use cli args above.
	data_dir = 'data'
	output_dir = 'output'

	# Make sure data directory exists
	if not os.path.exists(data_dir):
		print(f'data_dir: {data_dir} does not exist. Exiting program...\n')
		sys.exit(1)

	# Make sure output directory exists and create it if it doesn't
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)

	# Read images in data directory
	img_path_list = get_image_paths(data_dir)

	# Run transformations on images
	for img_path in tqdm(img_path_list):
		# Open image with imageio as numpy array
		img = imageio.imread(img_path)


		##### STUDENT SECTION START #####
		'''
		You have to figure out the parameters, if needed, and pass 
		them to the functions under each section below.
		Do not change output filename and saving part, just function parameters.
		'''

		# Flip horizontal, no parameters
		## Enter needed parameters here in list
		params = [None]
		trans = 'flip_horizontal'
		img_new = flip_horizontal_trans(img, params)
		out_path = get_output_path(output_dir, img_path, trans)
		imageio.imwrite(out_path, img_new)

		# Flip vertical, no parameters
		## Enter needed parameters here in list
		params = [None]
		trans = 'flip_vertical'
		img_new = flip_vertical_trans(img, params)
		out_path = get_output_path(output_dir, img_path, trans)
		imageio.imwrite(out_path, img_new)

		# Translation Function
		## Enter needed parameters here in list
		params = [None]
		trans = 'translation'
		img_new = translation_trans(img, params)
		out_path = get_output_path(output_dir, img_path, trans)
		imageio.imwrite(out_path, img_new)

		# Rotate Function
		## Enter needed parameters here in list
		params = [None]
		trans = 'rotate'
		img_new = rotate_trans(img, params)
		out_path = get_output_path(output_dir, img_path, trans)
		imageio.imwrite(out_path, img_new)

		# Similarity Function
		## Enter needed parameters here in list
		params = [None]
		trans = 'similarity'
		img_new = similarity_trans(img, params)
		out_path = get_output_path(output_dir, img_path, trans)
		imageio.imwrite(out_path, img_new)

		# Affine Function
		## Enter needed parameters here in list
		params = [None]
		trans = 'affine'
		img_new = affine_trans(img, params)
		out_path = get_output_path(output_dir, img_path, trans)
		imageio.imwrite(out_path, img_new)

		# Projective Function
		## Enter needed parameters here in list
		params = [None]
		trans = 'projective'
		img_new = projective_trans(img, params)
		out_path = get_output_path(output_dir, img_path, trans)
		imageio.imwrite(out_path, img_new)

		# Subtract Function
		## Enter needed parameters here in list
		params = [None]
		trans = 'subtract'
		img_new = subtract_trans(img, params)
		out_path = get_output_path(output_dir, img_path, trans)
		imageio.imwrite(out_path, img_new)
		##### STUDENT SECTION END #####

if __name__ == '__main__':
	main()