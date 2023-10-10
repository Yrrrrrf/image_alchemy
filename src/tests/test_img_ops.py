# standard imports
import unittest

# third-party imports
import cv2 as cv

# local imports
import src.img_ops.convolution as convolution
import src.img_ops.histogram as histogram
import src.img_ops.noise as noise
import src.img_ops.pixel as pixel
import src.config.globals as Assets

# test image
readImage = cv.imread(Assets.Assets.TEST_IMAGES.value+'Lenna.png')


class TestImgOps(unittest.TestCase):
    '''
    Test the histogram module.
    '''
    def test_resources(self):
        '''
        Test the resources module. Shloud be done if all the resources are available
        '''
        # todo: implement tests
        # load_resources() ...
        pass


    def test_histogram(self):
        img = readImage
        assert histogram.equalize_img(img) is not None
        assert histogram.equalize_hist_rgb(img) is not None
        assert histogram.resize_img_scale(img, 100) is not None
        assert histogram.resize_img(img, 100, 100) is not None

    def test_pixel(self):
        '''
        Test the pixel module.
        '''
        assert pixel.vertical_flip(None) is None
        assert pixel.horizontal_flip(None) is None
        assert pixel.invert
        assert pixel.clear_zone(None, 1, 1, 1, 1) is None
        assert pixel.change_brightness(None, 1) is None
        assert pixel.change_contrast(None, 1) is None
        assert pixel.logarithmic_transform(None) is None
        assert pixel.exponential_transform(None) is None
        assert pixel.gamma_correction(None, 1) is None
        assert pixel.power_law_transform(None, 1) is None
        assert pixel.piecewise_linear_transform(None, 1, 1, 1, 1) is None


    def test_convolutions(self):
        '''
        Test the convolutions module.
        '''
        assert convolution.absurd_filter(None) is None
        assert convolution.sharpen_filter(None) is None 
        assert convolution.gaussian_filter(None, 1) is None
        assert convolution.mean_filter(None, 1) is None
        assert convolution.median_filter(None, 1) is None
        assert convolution.laplacian_filter(None, 1) is None
        assert convolution.ordered_range_filter(None, 1) is None
        assert convolution.bilateral_filter(None, 1) is None
        assert convolution.sobel_filter(None, 1) is None
        assert convolution.emboss_filter(None, 1) is None
        assert convolution.edge_filter(None, 1) is None


    def test_noise(self):
        '''
        Test the noise module.
        '''
        assert noise.gaussian_noise(None, 1) is None
        assert noise.salt_noise(None, 1) is None    
        assert noise.pepper_noise(None, 1) is None    
        assert noise.salt_pepper_noise(None, 1) is None
        assert noise.speckle_noise(None, 1) is None    
        assert noise.rayleigh_noise(None, 1) is None    
        assert noise.laplace_noise(None, 1) is None    
        assert noise.poisson_noise(None, 1) is None    
        assert noise.uniform_noise(None, 1) is None
        assert noise.exponential_noise(None, 1) is None
