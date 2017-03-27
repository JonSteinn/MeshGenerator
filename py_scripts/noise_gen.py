import math
import os

from py_scripts.file_handler import append_file
from py_scripts.vector_math import *
from noise import pnoise2
from FilePaths import in_models


def write_obj_quad(quad, v_i, fd_v, fd_t, fd_n, fd_f, u_adjustment, v_adjustment):
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[0][0], quad[0][1], quad[0][2]))
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[1][0], quad[1][1], quad[1][2]))
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[2][0], quad[2][1], quad[2][2]))
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[3][0], quad[3][1], quad[3][2]))

    normal1 = cross_product(vec_from_to(quad[3], quad[1]), vec_from_to(quad[3], quad[0]))
    normal2 = cross_product(vec_from_to(quad[0], quad[2]), vec_from_to(quad[0], quad[3]))
    fd_n.write('vn {:.6f} {:.6f} {:.6f}\n'.format(normal1[0], normal1[1], normal1[2]))
    fd_n.write('vn {:.6f} {:.6f} {:.6f}\n'.format(normal2[0], normal2[1], normal2[2]))

    fd_t.write('vt {:.6f} {:.6f}\n'.format(u_adjustment(quad[0][0]), v_adjustment(quad[0][2])))
    fd_t.write('vt {:.6f} {:.6f}\n'.format(u_adjustment(quad[1][0]), v_adjustment(quad[1][2])))
    fd_t.write('vt {:.6f} {:.6f}\n'.format(u_adjustment(quad[2][0]), v_adjustment(quad[2][2])))
    fd_t.write('vt {:.6f} {:.6f}\n'.format(u_adjustment(quad[3][0]), v_adjustment(quad[3][2])))

    f_i = v_i // 2 + 1
    # 3 1 0
    fd_f.write(
        'f {:d}/{:d}/{:d} {:d}/{:d}/{:d} {:d}/{:d}/{:d}\n'.format(
            v_i + 4, v_i + 4, f_i, v_i + 2, v_i + 2, f_i, v_i + 1, v_i + 1, f_i))
    f_i += 1
    # 0 2 3
    fd_f.write(
        'f {:d}/{:d}/{:d} {:d}/{:d}/{:d} {:d}/{:d}/{:d}\n'.format(
            v_i + 1, v_i + 1, f_i, v_i + 3, v_i + 3, f_i, v_i + 4, v_i + 4, f_i))


def generate_noise_file(f, x_max, x_grid_count, z_max, z_grid_count, fd_main):
    dx = x_max / x_grid_count
    dz = z_max / z_grid_count
    with open(in_models('face_temp.obj'), 'w') as face_fd:
        with open(in_models('normal_temp.obj'), 'w') as normal_fd:
            with open(in_models('texture_temp.obj'), 'w') as texture_fd:
                for x in range(0, x_grid_count):
                    for z in range(0, z_grid_count):
                        quad = grid_xyz(f, x * dx, z * dz, dx, dz)
                        write_obj_quad(quad, z * 4 + (z_grid_count * 4 * x),
                                       fd_main, texture_fd, normal_fd, face_fd,
                                       lambda u: u / x_max,
                                       lambda v: v / z_max)
    append_file(fd_main, in_models('texture_temp.obj'))
    append_file(fd_main, in_models('normal_temp.obj'))
    append_file(fd_main, in_models('face_temp.obj'))
