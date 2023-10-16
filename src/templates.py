# # '''
# #     This file contains the templates for the images.
# #     The templates are used to create the image buffers.
# # '''


# from enum import Enum

# class Templates(Enum):
#     _1x1 = lambda w, h, m: [
#         [m, m, int(w - 2 * m), int(h - 2 * m)]
#     ]
#     _2c = lambda w, h, m: [
#         [m, m, int(w / 2 - 1.5 * m), int(h - 2 * m)],
#         [int((w / 2) + m / 2), m, int(w / 2 - 1.5 * m), int(h - 2 * m)],
#     ]
#     _3c = lambda w, h, m: [
#         [m, m, int((w / 3) - 1.5 * m), int(h - 2 * m)],
#         [int((w / 3) + m / 2), m, int((w / 3) - 1.5 * m), int(h - 2 * m)],
#         [int((w / 3) * 2 + m / 2), m, int((w / 3) - 1.5 * m), int(h - 2 * m)],
#     ]
#     _2r = lambda w, h, m: [
#         [m, m, int(w - 2 * m), int(h / 2 - 1.5 * m)],
#         [m, int((h / 2) + m / 2), int(w - 2 * m), int(h / 2 - 1.5 * m)],
#     ]
#     _3r = lambda w, h, m: [
#         [m, m, int(w - 2 * m), int((h / 3) - 1.5 * m)],
#         [m, int((h / 3) + m / 2), int(w - 2 * m), int((h / 3) - m)],
#         [m, int((h / 3) * 2 + m / 2), int(w - 2 * m), int((h / 3) - 1.5 * m)],
#     ]
#     _2x2 = lambda w, h, m: [
#         [m, m, int((w / 2) - 1.5 * m), int((h / 2) - 1.5 * m)],
#         [int((w / 2) + m / 2), m, int((w / 2) - 1.5 * m), int((h / 2) - 1.5 * m)],
#         [m, int((h / 2) + m / 2), int((w / 2) - 1.5 * m), int((h / 2) - 1.5 * m)],
#         [int((w / 2) + m / 2), int((h / 2) + m / 2), int((w / 2) - 1.5 * m), int((h / 2) - 1.5 * m)],
#     ]
#     r_1_2c = lambda w, h, m: [
#         [m, m, int(w - 2 * m), int(h / 2 - 1.5 * m)],
#         [m, int((h / 2) + m / 2), int(w / 2 - 1.5 * m), int(h / 2 - 1.5 * m)],
#         [int((w / 2) + m / 2), int((h / 2) + m / 2), int(w / 2 - 1.5 * m), int(h / 2 - 1.5 * m)],
#     ]
#     r_1_3c = lambda w, h, m: [
#         [m, m, int(w - 2 * m), int(h / 2 - 1.5 * m)],
#         [m, int((h / 2) + m / 2), int((w / 3) - 1.5 * m), int(h / 2 - 1.5 * m)],
#         [int((w / 3) + m / 2), int((h / 2) + m / 2), int((w / 3) - 1.5 * m), int(h / 2 - 1.5 * m)],
#         [int((w / 3) * 2 + m / 2), int((h / 2) + m / 2), int((w / 3) - 1.5 * m), int(h / 2 - 1.5 * m)],
#     ]
#     c_1_2r = lambda w, h, m: [
#         [m, m, int(w / 2 - 1.5 * m), int(h - 2 * m)],
#         [int((w / 2) + m / 2), m, int(w / 2 - 1.5 * m), int(h / 2 - 1.5 * m)],
#         [int((w / 2) + m / 2), int((h / 2) + m / 2), int(w / 2 - 1.5 * m), int(h / 2 - 1.5 * m)],
#     ]
#     c_1_3r = lambda w, h, m: [
#         [m, m, int((w / 2) - 1.5 * m), int(h - 2 * m)],
#         [int((w / 2) + m / 2), m, int((w / 2) - 1.5 * m), int((h / 3) - 1.5 * m)],
#         [int((w / 2) + m / 2), int((h / 3) + m / 2), int((w / 2) - 1.5 * m), int((h / 3) - 1.5 * m)],
#         [int((w / 2) + m / 2), int((h / 3) * 2 + m / 2), int((w / 2) - 1.5 * m), int((h / 3) - 1.5 * m)],
#     ]
#     r_2c_1 = lambda w, h, m: [
#         [m, m, int(w / 2 - 1.5 * m), int(h / 2 - 1.5 * m)],
#         [int((w / 2) + m / 2), m, int(w / 2 - 1.5 * m), int(h / 2 - 1.5 * m)],
#         [m, int((h / 2) + m / 2), int(w - 2 * m), int(h / 2 - 1.5 * m)],
#     ]
#     r_3c_1 = lambda w, h, m: [
#         [m, m, int((w / 3) - 1.5 * m), int((h / 2) - 1.5 * m)],
#         [int((w / 3) + m / 2), m, int((w / 3) - 1.5 * m), int((h / 2) - 1.5 * m)],
#         [int((w / 3) * 2 + m / 2), m, int((w / 3) - 1.5 * m), int((h / 2) - 1.5 * m)],
#         [m, int((h / 2) + m / 2), int(w - 2 * m), int((h / 2) - 1.5 * m)],
#     ]
#     c_2r_1 = lambda w, h, m: [
#         [m, m, int(w / 2 - 1.5 * m), int(h / 2 - 1.5 * m)],
#         [m, int((h / 2) + m / 2), int(w / 2 - 1.5 * m), int(h / 2 - 1.5 * m)],
#         [int((w / 2) + m / 2), m, int(w / 2 - 1.5 * m), int(h - 2 * m)],
#     ]
#     c_3r_1 = lambda w, h, m: [
#         [int((w / 2) + m / 2), m, int((w / 2) - 1.5 * m), int(h - 2 * m)],
#         [m, m, int((w / 2) - 1.5 * m), int((h / 3) - 1.5 * m)],
#         [m, int((h / 3) + m / 2), int((w / 2) - 1.5 * m), int((h / 3) - 1.5 * m)],
#         [m, int((h / 3) * 2 + m / 2), int((w / 2) - 1.5 * m), int((h / 3) - 1.5 * m)],
#     ]

# # # Example usage:
# # w, h, m = 100, 100, 5
# # template = Templates._2c
# # result = template.value(w, h, m)
# # print(result)




templates = {
    # w -> width,   h -> height,   m -> margin
        '1x1': lambda w, h, m: [[m, m, int(w-m*2), int(h-m*2)]],
         '2c': lambda w, h, m: [[m, m, int(w/2-m*1.5), int(h-m*2)],
                                [int((w/2)+m/2), m, int(w/2-m*1.5), int(h-m*2)]],
         '3c': lambda w, h, m: [[m, m, int((w/3)-m*1.5), int(h-m*2)],
                                [int((w/3)+m/2), m, int((w/3)-m*1.5), int(h-m*2)],
                                [int((w/3)*2+m/2), m, int((w/3)-m*1.5), int(h-m*2)]],
         '2r': lambda w, h, m: [[m, m, int(w-m*2), int(h/2-m*1.5)],
                                [m, int((h/2)+m/2), int(w-m*2), int(h/2-m*1.5)]],
         '3r': lambda w, h, m: [[m, m, int(w-m*2), int((h/3)-m*1.5)],
                                [m, int((h/3)+m/2), int(w-m*2), int((h/3)-m)],
                                [m, int((h/3)*2+m/2), int(w-m*2), int((h/3)-m*1.5)]],
        '2x2': lambda w, h, m: [[m, m, int((w/2)-m*1.5), int((h/2)-m*1.5)],
                                [int((w/2)+m/2), m, int((w/2)-m*1.5), int((h/2)-m*1.5)],
                                [m, int((h/2)+m/2), int((w/2)-m*1.5), int((h/2)-m*1.5)],
                                [int((w/2)+m/2), int((h/2)+m/2), int((w/2)-m*1.5), int((h/2)-m*1.5)]],
    'r(1 2c)': lambda w, h, m: [[m, m, int(w-m*2), int(h/2-m*1.5)],
                                [m, int((h/2)+m/2), int(w/2-m*1.5), int(h/2-m*1.5)],
                                [int((w/2)+m/2), int((h/2)+m/2), int(w/2-m*1.5), int(h/2-m*1.5)]],
    'r(1 3c)': lambda w, h, m: [[m, m, int(w-m*2), int((h/2)-m*1.5)],
                                [m, int((h/2)+m/2), int((w/3)-m*1.5), int((h/2)-m*1.5)],
                                [int((w/3)+m/2), int((h/2)+m/2), int((w/3)-m*1.5), int((h/2)-m*1.5)],
                                [int((w/3)*2+m/2), int((h/2)+m/2), int((w/3)-m*1.5), int((h/2)-m*1.5)]],
    'c(1 2r)': lambda w, h, m: [[m, m, int(w/2-m*1.5), int(h-m*2)],
                                [int((w/2)+m/2), m, int(w/2-m*1.5), int(h/2-m*1.5)],
                                [int((w/2)+m/2), int((h/2)+m/2), int(w/2-m*1.5), int(h/2-m*1.5)]],
    'c(1 3r)': lambda w, h, m: [[m, m, int((w/2)-m*1.5), int(h-m*2)],
                                [int((w/2)+m/2), m, int((w/2)-m*1.5), int((h/3)-m*1.5)],
                                [int((w/2)+m/2), int((h/3)+m/2), int((w/2)-m*1.5), int((h/3)-m*1.5)],
                                [int((w/2)+m/2), int((h/3)*2+m/2), int((w/2)-m*1.5), int((h/3)-m*1.5)]],
    'r(2c 1)': lambda w, h, m: [[m, m, int(w/2-m*1.5), int(h/2-m*1.5)],
                                [int((w/2)+m/2), m, int(w/2-m*1.5), int(h/2-m*1.5)],
                                [m, int((h/2)+m/2), int(w-m*2), int(h/2-m*1.5)]],
    'r(3c 1)': lambda w, h, m: [[m, m, int((w/3)-m*1.5), int((h/2)-m*1.5)],
                                [int((w/3)+m/2), m, int((w/3)-m*1.5), int((h/2)-m*1.5)],
                                [int((w/3)*2+m/2), m, int((w/3)-m*1.5), int((h/2)-m*1.5)],
                                [m, int((h/2)+m/2), int(w-m*2), int((h/2)-m*1.5)]],
    'c(2r 1)': lambda w, h, m: [[m, m, int(w/2-m*1.5), int(h/2-m*1.5)],
                                [m, int((h/2)+m/2), int(w/2-m*1.5), int(h/2-m*1.5)],
                                [int((w/2)+m/2), m, int(w/2-m*1.5), int(h-m*2)]],
    'c(3r 1)': lambda w, h, m: [[int((w/2)+m/2), m, int((w/2)-m*1.5), int(h-m*2)],
                                [m, m, int((w/2)-m*1.5), int((h/3)-m*1.5)],
                                [m, int((h/3)+m/2), int((w/2)-m*1.5), int((h/3)-m*1.5)],
                                [m, int((h/3)*2+m/2), int((w/2)-m*1.5), int((h/3)-m*1.5)]],
}

