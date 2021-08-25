# Imported modules
import imageio, sys, os, numpy as np
from tqdm import tqdm


##### STUDENT SECTION START #####
'''
This section below is where your transformation functions will go.

You have to figure out the parameters and add them
to the function definitions. Then write the functions and only
return the numpy array of the transformed image. The bare
minimum parameter will always be the image and is included already.

Check flip horizontal & vertical functions for examples.
'''

# Translation Function
def translation_trans(img):
	img_new = img.copy()

	### Your Code Goes Here Start ###


	### Your Code Goes Here End ###

	return img_new

# Rotate Function
def rotate_trans(img):
	img_new = img.copy()

	### Your Code Goes Here Start ###


	### Your Code Goes Here End ###

	return img_new

# Similarity Function
def similarity_trans(img):
	img_new = img.copy()

	### Your Code Goes Here Start ###


	### Your Code Goes Here End ###

	return img_new

# Affine Function
def affine_trans(img):
	img_new = img.copy()

	### Your Code Goes Here Start ###


	### Your Code Goes Here End ###

	return img_new

# Projective Function
def projective_trans(img):
	img_new = img.copy()

	### Your Code Goes Here Start ###


	### Your Code Goes Here End ###

	return img_new

# Subtract Function
def subtract_trans(img):
	img_new = img.copy()

	### Your Code Goes Here Start ###


	### Your Code Goes Here End ###

	return img_new
##### STUDENT SECTION END #####



##### EXAMPLES START #####
# Flip image vertically
def flip_vertical_trans(img):
	# Copy numpy array, not needed here but just showing how to do it for future.
	img_new = img.copy()

	# Flip vertically using numpy slices
	img_new = img_new[::-1]

	# This will work as well without the copy in this case, but not in all future cases.
	# img_new = img[::-1]

	return img_new

# Flip image horizontally
def flip_horizontal_trans(img):
	# Copy numpy array, not needed here but just showing how to do it for future.
	img_new = img.copy()

	# Flip horizontally using numpy slices
	img_new = img_new[:, ::-1]

	# This will work as well without the copy in this case, but not in all future cases.
	# img_new = img[:, ::-1]

	return img_new
##### EXAMPLES END #####



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

		# Flip horizontal, no parameters
		trans = 'flip_horizontal'
		img_new = flip_horizontal_trans(img)
		out_path = get_output_path(output_dir, img_path, trans)
		imageio.imwrite(out_path, img_new)

		# Flip vertical, no parameters
		trans = 'flip_vertical'
		img_new = flip_vertical_trans(img)
		out_path = get_output_path(output_dir, img_path, trans)
		imageio.imwrite(out_path, img_new)



		##### STUDENT SECTION START #####
		'''
		You have to figure out the parameters, if needed, and pass 
		them to the functions under each section below.
		Do not change output filename and saving part, just function parameters.
		'''

		# Translation Function
		trans = 'translation'
		img_new = translation_trans(img)
		out_path = get_output_path(output_dir, img_path, trans)
		imageio.imwrite(out_path, img_new)

		# Rotate Function
		trans = 'rotate'
		img_new = rotate_trans(img)
		out_path = get_output_path(output_dir, img_path, trans)
		imageio.imwrite(out_path, img_new)

		# Similarity Function
		trans = 'similarity'
		img_new = similarity_trans(img)
		out_path = get_output_path(output_dir, img_path, trans)
		imageio.imwrite(out_path, img_new)

		# Affine Function
		trans = 'affine'
		img_new = affine_trans(img)
		out_path = get_output_path(output_dir, img_path, trans)
		imageio.imwrite(out_path, img_new)

		# Projective Function
		trans = 'projective'
		img_new = projective_trans(img)
		out_path = get_output_path(output_dir, img_path, trans)
		imageio.imwrite(out_path, img_new)

		# Subtract Function
		trans = 'subtract'
		img_new = subtract_trans(img)
		out_path = get_output_path(output_dir, img_path, trans)
		imageio.imwrite(out_path, img_new)
		##### STUDENT SECTION END #####

if __name__ == '__main__':
	main()