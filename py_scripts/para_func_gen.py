import math
import os

from noise import snoise2, snoise3

from py_scripts import vector_math
from py_scripts.file_handler import append_file
from py_scripts.vector_math import *
from FilePaths import in_models


# This is just for exploring the object in the
# WebGL viewer for fun, going inside it and such...
# Not for exporting although possible
def write_obj_quad2(quad, v_i, fd_v, fd_t, fd_n, fd_f, u_adjustments, v_adjustments, values):
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[0][0], quad[0][1], quad[0][2]))
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[1][0], quad[1][1], quad[1][2]))
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[2][0], quad[2][1], quad[2][2]))
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[3][0], quad[3][1], quad[3][2]))

    normal1 = cross_product(vec_from_to(quad[3], quad[1]), vec_from_to(quad[3], quad[0]))
    normal2 = cross_product(vec_from_to(quad[0], quad[2]), vec_from_to(quad[0], quad[3]))
    normal3 = neg_vec(normal1)
    normal4 = neg_vec(normal2)
    fd_n.write('vn {:.6f} {:.6f} {:.6f}\n'.format(normal1[0], normal1[1], normal1[2]))
    fd_n.write('vn {:.6f} {:.6f} {:.6f}\n'.format(normal2[0], normal2[1], normal2[2]))
    fd_n.write('vn {:.6f} {:.6f} {:.6f}\n'.format(normal3[0], normal3[1], normal3[2]))
    fd_n.write('vn {:.6f} {:.6f} {:.6f}\n'.format(normal4[0], normal4[1], normal4[2]))

    textures_coordinates = [
        u_adjustments(values[0]),
        u_adjustments(values[1]),
        v_adjustments(values[2]),
        v_adjustments(values[3])
    ]

    fd_t.write('vt {:.6f} {:.6f}\n'.format(textures_coordinates[0], textures_coordinates[2]))
    fd_t.write('vt {:.6f} {:.6f}\n'.format(textures_coordinates[1], textures_coordinates[2]))
    fd_t.write('vt {:.6f} {:.6f}\n'.format(textures_coordinates[0], textures_coordinates[3]))
    fd_t.write('vt {:.6f} {:.6f}\n'.format(textures_coordinates[1], textures_coordinates[3]))

    # 3 1 0
    fd_f.write(
        'f {:d}/{:d}/{:d} {:d}/{:d}/{:d} {:d}/{:d}/{:d}\n'.format(
            v_i + 4, v_i + 4, v_i + 1, v_i + 2, v_i + 2, v_i + 1, v_i + 1, v_i + 1, v_i + 1))
    # 0 2 3
    fd_f.write(
        'f {:d}/{:d}/{:d} {:d}/{:d}/{:d} {:d}/{:d}/{:d}\n'.format(
            v_i + 1, v_i + 1, v_i + 2, v_i + 3, v_i + 3, v_i + 2, v_i + 4, v_i + 4, v_i + 2))

    # 3 0 1
    fd_f.write(
        'f {:d}/{:d}/{:d} {:d}/{:d}/{:d} {:d}/{:d}/{:d}\n'.format(
            v_i + 4, v_i + 4, v_i + 3, v_i + 1, v_i + 2, v_i + 3, v_i + 2, v_i + 1, v_i + 3))
    # 0 3 2
    fd_f.write(
        'f {:d}/{:d}/{:d} {:d}/{:d}/{:d} {:d}/{:d}/{:d}\n'.format(
            v_i + 1, v_i + 1, v_i + 4, v_i + 4, v_i + 3, v_i + 4, v_i + 3, v_i + 4, v_i + 4))


def write_obj_quad(quad, v_i, fd_v, fd_t, fd_n, fd_f, u_adjustments, v_adjustments, values):
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[0][0], quad[0][1], quad[0][2]))
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[1][0], quad[1][1], quad[1][2]))
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[2][0], quad[2][1], quad[2][2]))
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[3][0], quad[3][1], quad[3][2]))

    normal1 = cross_product(vec_from_to(quad[3], quad[1]), vec_from_to(quad[3], quad[0]))
    normal2 = cross_product(vec_from_to(quad[0], quad[2]), vec_from_to(quad[0], quad[3]))
    fd_n.write('vn {:.6f} {:.6f} {:.6f}\n'.format(normal1[0], normal1[1], normal1[2]))
    fd_n.write('vn {:.6f} {:.6f} {:.6f}\n'.format(normal2[0], normal2[1], normal2[2]))

    textures_coordinates = [
        u_adjustments(values[0]),
        u_adjustments(values[1]),
        v_adjustments(values[2]),
        v_adjustments(values[3])
    ]

    fd_t.write('vt {:.6f} {:.6f}\n'.format(textures_coordinates[0], textures_coordinates[2]))
    fd_t.write('vt {:.6f} {:.6f}\n'.format(textures_coordinates[1], textures_coordinates[2]))
    fd_t.write('vt {:.6f} {:.6f}\n'.format(textures_coordinates[0], textures_coordinates[3]))
    fd_t.write('vt {:.6f} {:.6f}\n'.format(textures_coordinates[1], textures_coordinates[3]))

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


def generate_parametric_func_file(f, u_min, u_max, u_grid_count, v_min, v_max, v_grid_count, fd_main, d_sided):
    du = (u_max - u_min) / u_grid_count
    dv = (v_max - v_min) / v_grid_count
    with open(in_models('face_temp.obj'), 'w') as face_fd:
        with open(in_models('normal_temp.obj'), 'w') as normal_fd:
            with open(in_models('texture_temp.obj'), 'w') as texture_fd:
                if d_sided:
                    for u in range(0, u_grid_count):
                        for v in range(0, v_grid_count):
                            quad = grid_parametric(f, u_min + u * du, v_min + v * dv, du, dv)
                            write_obj_quad2(quad, v * 4 + (v_grid_count * 4 * u),
                                            fd_main, texture_fd, normal_fd, face_fd,
                                            lambda _u: (_u - u_min) / (u_max - u_min),
                                            lambda _v: (_v - v_min) / (v_max - v_min),
                                            [u_min + u * du, u_min + (u + 1) * du,
                                             v_min + v * dv, v_min + (v + 1) * dv])
                else:
                    for u in range(0, u_grid_count):
                        for v in range(0, v_grid_count):
                            quad = grid_parametric(f, u_min + u * du, v_min + v * dv, du, dv)
                            write_obj_quad(quad, v * 4 + (v_grid_count * 4 * u),
                                           fd_main, texture_fd, normal_fd, face_fd,
                                           lambda _u: (_u - u_min) / (u_max - u_min),
                                           lambda _v: (_v - v_min) / (v_max - v_min),
                                           [u_min + u * du, u_min + (u + 1) * du,
                                            v_min + v * dv, v_min + (v + 1) * dv])
    append_file(fd_main, in_models('texture_temp.obj'))
    append_file(fd_main, in_models('normal_temp.obj'))
    append_file(fd_main, in_models('face_temp.obj'))






