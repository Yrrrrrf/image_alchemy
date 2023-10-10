from img_operations.convolution import *
from img_operations.histogram import *
from img_operations.noise import *
from img_operations.pixel import *


operation_types_dict = {
    'pixel': [ 
        {
            'name': 'vertical flip',
            'function': vertical_flip,
        },
        {
            'name': 'rgb to gray',
            'function': rgb_to_gray,
        },
        {
            'name': 'horizontal flip',
            'function': horizontal_flip,
        },
        {
            'name': 'invert colors',
            'function': invert,
        },
        {
            'name': 'clear zone',
            'function': clear_zone,
        },
        {
            'name': 'brightness',
            'function': change_brightness,
        },
        {
            'name': 'contrast',
            'function': change_contrast,
        },
        {
            'name': 'logarithmic transform',
            'function': logarithmic_transform,
        },
        {
            'name': 'power transformation',
            'function': power_transformation,
        },
        {
            'name': 'exponential transform',
            'function': exponential_transform,
        },
        {
            'name': 'gamma correction',
            'function': gamma_correction,
        },
        {
            'name': 'power law transform',
            'function': power_law_transform,
        },
        {
            'name': 'piecewise linear transform',
            'function': piecewise_linear_transform,
        },
    ],
    'convolution': [
        {
            'name': 'absurd filter',
            'function': absurd_filter,
        },
        {
            'name': 'sharpen filter',
            'function': sharpen_filter,
        },
        {
            'name': 'gaussian filter',
            'function': gaussian_filter,
        },
        {
            'name': 'mean filter',
            'function': mean_filter,
        },
        {
            'name': 'median filter',
            'function': median_filter,
        },
        {
            'name': 'laplacian filter',
            'function': laplacian_filter,
        },
        {
            'name': 'ordered range filter',
            'function': ordered_range_filter,
        },
        {
            'name': 'bilateral filter',
            'function': bilateral_filter,
        },
        {
            'name': 'sobel filter',
            'function': sobel_filter,
        },
        {
            'name': 'emboss filter',
            'function': emboss_filter,
        },
        {
            'name': 'edge filter',
            'function': edge_filter,
        },
    ],
    'histogram': [
        {
            'name': 'equalize image',
            'function': equalize_img,
        },
        {
            'name': 'equalize histogram rgb',
            'function': equalize_hist_rgb,
        },
        {
            'name': 'resize image scale',
            'function': resize_img_scale,
        },
        {
            'name': 'resize image',
            'function': resize_img,
        },
    ],
    'noise': [
        {
            'name': 'gaussian noise',
            'function': gaussian_noise,
        },
        {
            'name': 'salt noise',
            'function': salt_noise,
        },
        {
            'name': 'pepper noise',
            'function': pepper_noise,
        },
        {
            'name': 'salt pepper noise',
            'function': salt_pepper_noise,
        },
        {
            'name': 'speckle noise',
            'function': speckle_noise,
        },
        {
            'name': 'rayleigh noise',
            'function': rayleigh_noise,
        },
        {
            'name': 'laplace noise',
            'function': laplace_noise,
        },
        {
            'name': 'poisson noise',
            'function': poisson_noise,
        },
        {
            'name': 'uniform noise',
            'function': uniform_noise,
        },
        {
            'name': 'exponential noise',
            'function': exponential_noise,
        },
    ],
    'brush': [
        {
            'name': 'set text',
            'function': lambda: print('set text'),
        },
        {
            'name': 'draw',
            'function': lambda: print('draw'),
        },
        {
            'name': 'blur',
            'function': lambda: print('blur'),
        },
        {
            'name': 'something else...',
            'function': lambda: print('something else...'),
        },
        {
            'name': 'something else...',
            'function': lambda: print('something else...'),
        },
    ],
    'cube': [
        {
            'name': 'cube_1',
            'function': None,
        },
        {
            'name': 'cube_2',
            'function': None,
        },
        {
            'name': 'cube_3',
            'function': None,
        },
        {
            'name': 'cube_4',
            'function': None,
        },
    ],
    'graph': [
        {
            'name': 'graph_1',
            'function': None,
        },
        {
            'name': 'graph_2',
            'function': None,
        },
        {
            'name': 'graph_3',
            'function': None,
        },
        {
            'name': 'graph_4',
            'function': None,
        },
    ],
    'log': [
        {
            'name': 'log_1',
            'function': None,
        },
        {
            'name': 'log_2',
            'function': None,
        },
        {
            'name': 'log_3',
            'function': None,
        },
        {
            'name': 'log_4',
            'function': None,
        },
    ],
    'nucleus': [
        {
            'name': 'nucleus_1',
            'function': None,
        },
        {
            'name': 'nucleus_2',
            'function': None,
        },
        {
            'name': 'nucleus_3',
            'function': None,
        },
        {
            'name': 'nucleus_4',
            'function': None,
        },
    ],
    'cells': [
        {
            'name': 'cells_1',
            'function': None,
        },
        {
            'name': 'cells_2',
            'function': None,
        },
        {
            'name': 'cells_3',
            'function': None,
        },
        {
            'name': 'cells_4',
            'function': None,
        },
    ],
}

