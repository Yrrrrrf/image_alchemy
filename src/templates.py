'''
    This file contains the templates for the images.
    The templates are used to create the image buffers.
'''


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

# Key Notation:
# r -> rows
# c -> columns
# r() -> multirow span
# c() -> multicolumn span

# More complex notation
# c(2r 1 2r)
# c(r(2c 1 1) 2r 1)
# Starred numbers label a specific area;
# e.g. the *1 designates an area spawning across rows and columns
# c(2r *1 *1)
# c(r(*1 *1 *2) r(*1 *1 *2) r(1 *3 *3))

