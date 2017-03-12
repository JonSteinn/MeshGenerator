import math


def grid_xyz(function, val1, val2, d1, d2):
    return [
        [val1, function(val1, val2), val2],
        [val1 + d1, function(val1 + d1, val2), val2],
        [val1, function(val1, val2 + d2), val2 + d2],
        [val1 + d1, function(val1 + d1, val2 + d2), val2 + d2]
    ]


def grid_parametric(function, val1, val2, d1, d2):
    return [
        [function[0](val1, val2), function[1](val1, val2), function[2](val1, val2)],
        [function[0](val1 + d1, val2), function[1](val1 + d1, val2), function[2](val1 + d1, val2)],
        [function[0](val1, val2 + d2), function[1](val1, val2 + d2), function[2](val1, val2 + d2)],
        [function[0](val1 + d1, val2 + d2), function[1](val1 + d1, val2 + d2), function[2](val1 + d1, val2 + d2)],
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


def write_quad(quad, fd, index):
    normal = cross_product(vec_from_to(quad[0], quad[1]), vec_from_to(quad[0], quad[2]))
    fd.write('v {:.6f} {:6f} {:6f}\n'.format(quad[0][0], quad[0][1], quad[0][2]))
    fd.write('v {:.6f} {:6f} {:6f}\n'.format(quad[1][0], quad[1][1], quad[1][2]))
    fd.write('v {:.6f} {:6f} {:6f}\n'.format(quad[2][0], quad[2][1], quad[2][2]))
    fd.write('v {:.6f} {:6f} {:6f}\n'.format(quad[3][0], quad[3][1], quad[3][2]))
    fd.write('vn {:.6f} {:6f} {:6f}\n'.format(normal[0], normal[1], normal[2]))
    fd.write('f {:d} {:d} {:d}\n'.format(index + 1, index + 3, index + 4))
    fd.write('f {:d} {:d} {:d}\n'.format(index + 1, index + 4, index + 2))
    fd.write('f {:d} {:d} {:d}\n'.format(index + 1, index + 2, index + 4))
    fd.write('f {:d} {:d} {:d}\n'.format(index + 1, index + 4, index + 3))


def generate_files_xyz(f, x_min, x_max, x_grid_count, z_min, z_max, z_grid_count, fd):
    dx = (x_max - x_min) / x_grid_count
    dz = (z_max - z_min) / z_grid_count
    for x in range(0, x_grid_count):
        for z in range(0, z_grid_count):
            quad = grid_xyz(f, x_min + x * dx, z_min + z * dz, dx, dz)
            write_quad(quad, fd, z * 4 + (z_grid_count * 4 * x))


def generate_files_parametric(f, u_min, u_max, u_grid_count, v_min, v_max, v_grid_count, fd):
    du = (u_max - u_min) / u_grid_count
    dv = (v_max - v_min) / v_grid_count
    for u in range(0, u_grid_count):
        for v in range(0, v_grid_count):
            quad = grid_parametric(f, u_min + u * du, v_min + v * dv, du, dv)
            write_quad(quad, fd, v * 4 + (v_grid_count * 4 * u))