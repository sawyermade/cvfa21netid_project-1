##### IMPORTS START #####
# Imported modules, do not change or add anything
import imageio, sys, os, numpy as np, zipfile
from tqdm import tqdm
from skimage.color import rgb2lab, lab2rgb
##### IMPORTS END #####

# Check if using Colab, do not change
try:
    # Mount google drive
    from google.colab import drive
    drive_dir = '/content/drive'
    drive.mount(drive_dir)

    # Create output directory
    output_dir = '/content/drive/MyDrive/Colab Notebooks/computer_vision_fa21/project-1/output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Download image data
    import gdown
    data_dir_parent = '/content'
    data_dir = os.path.join(data_dir_parent, 'data')
    data_zip = '/content/data.zip'
    url = 'https://drive.google.com/uc?id=1S6tO3qWtbmYS91RnRvI_KeyjGGyvG-sU'
    gdown.download(url, data_zip, quiet=False)

    # Extract image data
    with zipfile.ZipFile(data_zip, 'r') as zf:
        zf.extractall(data_dir_parent)
        print(f'\nlist of {data_dir} directory: {os.listdir(data_dir)}\n')

    # Set colab flag
    COLAB = True

except Exception as e:
    COLAB = False
    data_dir = None
    output_dir = None

##### HELPERS START #####
# My helper functions, do not change or add anthing

# Converts degrees to radians
def degree_to_radian(degree):
    return degree * np.pi / 180.0

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
    img_path_list.sort()

    # Check to make sure it found image paths, exit if not
    if not img_path_list:
        print(f'No images found in {data_dir}. Exiting program...\n')
        sys.exit(1)

    return img_path_list
##### HELPERS END #####


##### TRANSFORMATION CLASS START #####
# Tranformation Class with all transformation functions
class transformations:
    # Image setup function
    def __setup_image(self, img_path):
        # Open Image
        self.img = imageio.imread(img_path)

        # Set width and height of original image
        self.width = self.img.shape[1]
        self.height = self.img.shape[0]

        # Check if rgb or grayscale
        if self.img.ndim < 3:
            self.isgray = True
            self.isrgb  = False
            self.img = self.img.reshape((self.height, self.width, 1))
        elif self.img.shape[2] == 1:
            self.isgray = True
            self.isrgb  = False
        else:
            self.isgray = False
            self.isrgb  = True

        # Check for alpha channel and remove if there
        if self.isrgb and self.img.shape[2] > 3:
            self.img = self.img[..., :3]

        # Get number of channels, 1 is grayscale, 3 is RGB
        self.channels = self.img.shape[2]

        # Shape tuple
        self.shape = self.img.shape 

    # Get batch array function
    def __get_batch_array_list(self, batch_paths):
        # Goes through images adds to batch list
        batch_paths.sort()
        batch_img_list = []
        for img_path in batch_paths:
            self.__setup_image(img_path)
            batch_img_list.append(self.img.copy())

        # Saves batch
        self.batch = batch_img_list

    # Constructor
    def __init__(self, img_path, batch_paths=None):
        # Sets up image
        if img_path:
            self.__setup_image(img_path)

        # Batch array list
        if batch_paths:
            self.__get_batch_array_list(batch_paths)


    ### HELPERS START ###
    '''
    Create any additional helper functions here 
    that you use in your functions.
    '''
    # Inverse Warp A
    def inverse_warp_a(self, h, h_inv):
        # Get 4 corner points
        cx, cy = [], []
        for fx in [0, self.width - 1]:
            for fy in [0, self.height - 1]:
                x, y = h(fx, fy)
                x, y = int(x), int(y)
                cx.append(x)
                cy.append(y)

        # Get min and max, then new width and height
        min_x, max_x = int(min(cx)), int(max(cx))
        min_y, max_y = int(min(cy)), int(max(cy))
        width_g = max_x - min_x + 1
        height_g = max_y - min_y + 1

        # Creates empty new image
        img_new = np.zeros((height_g, width_g, self.channels))

        # Find pixel values and map to new image
        for gy in range(min_y, max_y + 1):
            for gx in range(min_x, max_x + 1):
                fx, fy = h_inv(gx, gy)
                fx, fy = int(fx), int(fy)
                img_new[gy - min_y, gx - min_x] = self.img[fy, fx]

        # Returns new image
        return img_new

    # Inverse Warp B
    def inverse_warp_b(self, h_inv, output_shape):
        # Create empty new image
        if len(output_shape) < 3:
            output_shape = output_shape + (self.channels,)
        img_new = np.zeros(output_shape)

        # Find pixel values and map to new image
        for gy in range(output_shape[0]):
            for gx in range(output_shape[1]):
                fx, fy = h_inv(gx, gy)
                fx, fy = int(fx), int(fy)
                img_new[max(0, gy), max(0, gx)] = self.img[fy, fx]

        # Returns new image
        return img_new

    ### HELPERS END ###


    ### EXAMPLES START ###
    # Flip vertical
    def flip_vertical(self):
        # h and h inverse using nested functions
        def h(x, y):
            gx = x
            gy = abs(y - (self.height - 1))
            return (gx, gy)
        def h_inv(x, y):
            fx = x
            fy = abs(y - (self.height - 1))
            return (fx, fy)

        # Warp image
        img_new = self.inverse_warp_a(h, h_inv)
        # img_new = self.inverse_warp_b(h_inv, self.shape)

        # Return new image
        return img_new.astype(np.uint8)

    # Flop Horizontal
    def flip_horizontal(self):
        # h and h inverse using lambda functions instead
        h = lambda x, y: (abs(x - (self.width - 1)), y)
        h_inv = lambda x, y: (abs(x - (self.width - 1)), y)

        # Warp image
        # img_new = self.inverse_warp_a(h, h_inv)
        img_new = self.inverse_warp_b(h_inv, self.shape)

        # Return new image
        return img_new.astype(np.uint8)

    ### EXAMPLES END ###


    ### STUDENT SECTION START ###
    '''
    Finish functions without creating any new functions here.
    If you need to create new functions, place them in the helpers
    section of the transformations class.
    The only thing your functions should return is the new image as uint8.
    '''

    # Translation
    def translation(self, shift_x, shift_y):
        # You can delete this, this just makes all black image.
        img_new = np.zeros(self.shape)


        # Only return new image as uint8
        return img_new.astype(np.uint8)


    # Rotate
    def rotate(self, theta):
        # You can delete this, this just makes all black image.
        img_new = np.zeros(self.shape)


        # Only return new image as uint8
        return img_new.astype(np.uint8)


    # Scale
    def scale(self, scale_percent):
        # You can delete this, this just makes all black image.
        img_new = np.zeros(self.shape)


        # Only return new image as uint8
        return img_new.astype(np.uint8)


    # Affine
    def affine(self, A):
        # You can delete this, this just makes all black image.
        img_new = np.zeros(self.shape)


        # Only return new image as uint8
        return img_new.astype(np.uint8)


    # Projection
    def projective(self, H):
        # You can delete this, this just makes all black image.
        img_new = np.zeros(self.shape)


        # Only return new image as uint8
        return img_new.astype(np.uint8)


    # Brightness and Contrast
    def brightness_contrast(self, a, b):
        # You can delete this, this just makes all black image.
        img_new = np.zeros(self.shape)


        # Only return new image as uint8
        return img_new.astype(np.uint8)


    # Gamma Correction
    def gamma_correction(self, a, b):
        # You can delete this, this just makes all black image.
        img_new = np.zeros(self.shape)


        # Only return new image as uint8
        return img_new.astype(np.uint8)


    # Histogram Equalization
    def histogram_equalization(self, a, b):
        # You can delete this, this just makes all black image.
        img_new = np.zeros(self.shape)


        # Only return new image as uint8
        return img_new.astype(np.uint8)


    # Mean and Standard Deviation
    def mean_sd(self, resize_w, resize_h):
        # You can delete this, just copies images from batch
        batch = self.batch
        img_mean = batch[0]
        img_sd = batch[1]

        # Return only mean and sd images as uint8
        return (
            img_mean.astype(np.uint8),
            img_sd.astype(np.uint8)
        )

    # Batch Normalization
    def batch_norm(self, resize_w, resize_h):
        # You can delete this, just copies images from batch
        batch = self.batch
        batch_new = []
        for img in tqdm(batch):
            batch_new.append(img)

        # Return batch normalized images as uint8
        batch_new = [img.astype(np.uint8) for img in batch_new]
        return batch_new

    ### STUDENT SECTION END ###
##### TRANSFORMATION CLASS END #####

##### MAIN FUNCTION START #####
def main():
    # Args, checks if colab or not
    if COLAB:
        global data_dir
        global output_dir
    else:
        data_dir = 'data'
        output_dir = 'output'

    # Batch input and output directories
    data_batch_dir = os.path.join(data_dir, 'batch')
    output_batch_dir = os.path.join(output_dir, 'batch')

    # Make sure data directory exists
    if not os.path.exists(data_dir):
        print(f'data_dir: {data_dir} does not exist. Exiting program...\n')
        sys.exit(1)

    # Make sure output directory exists and create it if it doesn't
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Make sure output batch directory exists and create it if it doesn't
    if not os.path.exists(output_batch_dir):
        os.makedirs(output_batch_dir)

    # Read images in data directory
    img_path_list = get_image_paths(data_dir)

    # Read images in batch dir
    img_path_batch_list = get_image_paths(data_batch_dir)

    ### RUN TRANSFORMATIONS ###
    print('\nTransformations...')
    for img_path in tqdm(img_path_list):
        # Opens image into transformations object
        img_trans = transformations(img_path)
        
        ### Examples ###

        # Flip vertically
        trans = 'flip_vertical'
        img_new = img_trans.flip_vertical()
        out_path = get_output_path(output_dir, img_path, trans)
        imageio.imwrite(out_path, img_new)

        # Flip horizontally
        trans = 'flip_horizontal'
        img_new = img_trans.flip_horizontal()
        out_path = get_output_path(output_dir, img_path, trans)
        imageio.imwrite(out_path, img_new)


        ### STUDENT SECTION START ###

        # Translation function
        ''' 
        Pecent to shift x & y by. Positive shifts right and down,
        negative shifts left and up.
        '''
        ## Parameters you can change
        shift_x, shift_y = 0.0, 0.0

        ## Dont change
        trans = 'translation'
        img_new = img_trans.translation(shift_x, shift_y)
        out_path = get_output_path(output_dir, img_path, trans)
        imageio.imwrite(out_path, img_new)


        # Rotate function
        '''
        Rotate image by degree theta. Positive is clockwise,
        negative is counterclockwise.
        '''
        ## Paremeters you can change
        theta_degree = 0
        theta_radian = degree_to_radian(theta_degree)

        ## Dont change
        trans = 'rotate'
        img_new = img_trans.rotate(theta_radian)
        out_path = get_output_path(output_dir, img_path, trans)
        imageio.imwrite(out_path, img_new)


        # Scaling function
        '''
        Scale the image by percent. Over 100% expands the image,
        while under 100% contracts the image. 
        '''
        ## Parameters you can change
        scale_percent = 1.00

        ## Dont change
        trans = 'scale'
        img_new = img_trans.scale(scale_percent)
        out_path = get_output_path(output_dir, img_path, trans)
        imageio.imwrite(out_path, img_new)


        # Affine function
        '''
        User specified vector of 6 parameters for affine transformation.
        '''
        ## Parameters you can change
        a_00 = 0.0
        a_01 = 0.0
        a_10 = 0.0
        a_11 = 0.0
        t_x  = 0.0
        t_y  = 0.0

        ## Dont change
        A = [
            [a_00, a_01, t_x],
            [a_10, a_11, t_y]
        ]
        trans = 'affine'
        img_new = img_trans.affine(A)
        out_path = get_output_path(output_dir, img_path, trans)
        imageio.imwrite(out_path, img_new)


        # Projective function
        '''
        User specified vector of 9 parameters for projective transformation.
        '''
        ## Parameters you can change
        h_00 = 0.0
        h_01 = 0.0
        h_02 = 0.0
        h_10 = 0.0
        h_11 = 0.0
        h_12 = 0.0
        h_20 = 0.0
        h_21 = 0.0
        h_22 = 0.0

        ## Dont change
        H = [
            [h_00, h_01, h_02],
            [h_10, h_11, h_12],
            [h_20, h_21, h_22]
        ]
        trans = 'projective'
        img_new = img_trans.projective(H)
        out_path = get_output_path(output_dir, img_path, trans)
        imageio.imwrite(out_path, img_new)


        # Brightness and Contrast Modulation Function
        '''
        Contrast and brightness modulation of the L channel.
        '''
        ## Parameters you can change
        a = 0.0
        b = 0.0

        ## Dont change
        trans = 'brightness_contrast'
        img_new = img_trans.brightness_contrast(a, b)
        out_path = get_output_path(output_dir, img_path, trans)
        imageio.imwrite(out_path, img_new)


        # Gamma Correction
        '''
        Gamma correction of the L channel
        '''
        ## Parameters you can change
        a = 0.0
        b = 0.0

        ## Dont change
        trans = 'gamme_correction'
        img_new = img_trans.gamma_correction(a, b)
        out_path = get_output_path(output_dir, img_path, trans)
        imageio.imwrite(out_path, img_new)


        # Histogram Equalization
        '''
        Histogram equalization for the L channel
        '''
        ## Parameters you can change
        a = 0.0
        b = 0.0

        ## Dont change
        trans = 'histogram_equalization'
        img_new = img_trans.histogram_equalization(a, b)
        out_path = get_output_path(output_dir, img_path, trans)
        imageio.imwrite(out_path, img_new)

        ### STUDENT SECTION END ###



    ### NORMALIZE FUNCTIONS ###
    # Setup batch images
    img_trans = transformations(None, img_path_batch_list)

    ### STUDENT SECTION START ###

    # Compute mean and SD image function
    ## Parameters you can change
    resize_w, resize_h = 300, 200 

    ## Dont change
    img_mean, img_sd = img_trans.mean_sd(resize_w, resize_h)
    out_path1 = os.path.join(output_batch_dir, 'batch-mean.png')
    out_path2 = os.path.join(output_batch_dir, 'batch-sd.png')
    imageio.imwrite(out_path1, img_mean)
    imageio.imwrite(out_path2, img_sd)


    # Batch Normalization
    print('\nBatch Normalization...')
    ## Parameters you can change
    resize_w, resize_h = 300, 200

    ## Dont change
    batch = img_trans.batch_norm(resize_w, resize_h)
    trans = 'batch_norm'
    print('\nSaving batch normalized images...')
    for i in tqdm(range(len(batch))):
        img_new = batch[i]
        img_path = img_path_batch_list[i]
        out_path = get_output_path(output_batch_dir, img_path, trans)
        imageio.imwrite(out_path, img_new)

    ### STUDENT SECTION END ###

##### MAIN FUNCTION END #####


if __name__ == '__main__':
    main()