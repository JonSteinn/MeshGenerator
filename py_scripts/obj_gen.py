import math


def grid(function, val1, val2, delta_var1, delta_var2):
    return [
        [val1, function(val1, val2), val2],
        [val1 + delta_var1, function(val1 + delta_var1, val2), val2],
        [val1, function(val1, val2 + delta_var2), val2 + delta_var2],
        [val1 + delta_var1, function(val1 + delta_var1, val2 + delta_var2), val2 + delta_var2]
    ]


def vec_from_to(p1, p2):
    return [p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]]


def vec_length(v):
    return math.sqrt(sum(map(lambda val: val**2, v)))


def normalized(v):
    l = vec_length(v)
    return list(map(lambda val: val/l, v))


def cross_product(u, v):
    return [u[1]*v[2] - u[2]*v[1], u[2]*v[0] - u[0]*v[2], u[0]*v[1] - u[1]*v[0]]


def generate_files_xyz(f, x_min, x_max, x_grid_count, z_min, z_max, z_grid_count):
    fd = open('../static/models/model.obj', 'w')
    dx = (x_max - x_min) / x_grid_count
    dz = (z_max - z_min) / z_grid_count
    for x in range(0, x_grid_count):
        for z in range(0, z_grid_count):
            quad = grid(f, x * dx, z * dz, dx, dz)
            normal = cross_product(vec_from_to(quad[0], quad[1]), vec_from_to(quad[0], quad[2]))
            print('v {:.6f} {:6f} {:6f}'.format(quad[0][0], quad[0][1], quad[0][2]), file=fd)
            print('v {:.6f} {:6f} {:6f}'.format(quad[1][0], quad[1][1], quad[1][2]), file=fd)
            print('v {:.6f} {:6f} {:6f}'.format(quad[2][0], quad[2][1], quad[2][2]), file=fd)
            print('v {:.6f} {:6f} {:6f}'.format(quad[3][0], quad[3][1], quad[3][2]), file=fd)
            print('vn {:.6f} {:6f} {:6f}'.format(normal[0], normal[1], normal[2]), file=fd)
            index = z * 4 + (z_grid_count * 4 * x)
            print('f {:d} {:d} {:d}'.format(index + 1, index + 3, index + 4), file=fd)
            print('f {:d} {:d} {:d}'.format(index + 1, index + 4, index + 2), file=fd)
            print('f {:d} {:d} {:d}'.format(index + 1, index + 2, index + 4), file=fd)
            print('f {:d} {:d} {:d}'.format(index + 1, index + 4, index + 3), file=fd)
    fd.close()