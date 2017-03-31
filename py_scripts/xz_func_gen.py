import math
import os

from py_scripts import vector_math
from py_scripts.file_handler import append_file
from py_scripts.vector_math import *
from FilePaths import in_models


def write_obj_quad_tex_len(quad, v_i, fd_v, fd_t, fd_n, fd_f, u_vals, v_vals):
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[0][0], quad[0][1], quad[0][2]))
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[1][0], quad[1][1], quad[1][2]))
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[2][0], quad[2][1], quad[2][2]))
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[3][0], quad[3][1], quad[3][2]))

    normal = cross_product(vec_from_to(quad[3], quad[1]), vec_from_to(quad[3], quad[0]))
    fd_n.write('vn {:.6f} {:.6f} {:.6f}\n'.format(normal[0], normal[1], normal[2]))
    normal = cross_product(vec_from_to(quad[0], quad[2]), vec_from_to(quad[0], quad[3]))
    fd_n.write('vn {:.6f} {:.6f} {:.6f}\n'.format(normal[0], normal[1], normal[2]))

    fd_t.write('vt {:.6f} {:.6f}\n'.format(u_vals[0], v_vals[0]))
    fd_t.write('vt {:.6f} {:.6f}\n'.format(u_vals[1], v_vals[1]))
    fd_t.write('vt {:.6f} {:.6f}\n'.format(u_vals[2], v_vals[2]))
    fd_t.write('vt {:.6f} {:.6f}\n'.format(u_vals[3], v_vals[3]))

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


def generate_xz_func_file_tex_len(f, x_min, x_max, x_grid_count, z_min, z_max, z_grid_count, fd_main):
    dx = (x_max - x_min) / x_grid_count
    dz = (z_max - z_min) / z_grid_count
    h_dict = {}
    v_dict = {}
    for z in range(0, x_grid_count+1):
        if not h_dict.__contains__(z):
            h_dict[z] = 0
        for x in range(0, z_grid_count):
            p_from = [x_min + x*dx, f(x_min + x*dx, z_min + z*dz), z_min + z*dz]
            p_to = [x_min + x*dx+dx, f(x_min + x*dx+dx, z_min + z*dz), z_min + z*dz]
            h_dict[z] += vector_math.vec_length(vector_math.vec_from_to(p_from, p_to))
    for x in range(0, z_grid_count + 1):
        if not v_dict.__contains__(x):
            v_dict[x] = 0
        for z in range(0, x_grid_count):
            p_from = [x_min + x*dx, f(x_min + x*dx, z_min + z*dz), z_min + z*dz]
            p_to = [x_min + x*dx, f(x_min + x*dx, z_min + z*dz + dz), z_min + z*dz + dz]
            v_dict[x] += vector_math.vec_length(vector_math.vec_from_to(p_from, p_to))

    u_map = {}
    v_map = {}
    for z in range(0, z_grid_count+1):
        u_map[(0,z)] = 0.0
        for x in range(1,x_grid_count + 1):
            p_to = [x_min + x*dx, f(x_min + x*dx, z_min + z*dz), z_min + z*dz]
            p_from = [x_min + x*dx-dx, f(x_min + x*dx-dx, z_min + z*dz), z_min + z*dz]
            u_map[(x,z)] = u_map[(x-1,z)] + vector_math.vec_length(vector_math.vec_from_to(p_from, p_to)) / h_dict[z]
    for x in range(0, x_grid_count+1):
        v_map[(x,0)] = 0.0
        for z in range(1, z_grid_count + 1):
            p_to = [x_min + x*dx, f(x_min + x*dx, z_min + z*dz), z_min + z*dz]
            p_from = [x_min + x*dx, f(x_min + x*dx, z_min + z*dz - dz), z_min + z*dz - dz]
            v_map[(x,z)] = v_map[(x,z-1)] + vector_math.vec_length(vector_math.vec_from_to(p_from, p_to)) / v_dict[x]

    with open(in_models('face_temp.obj'), 'w') as face_fd:
        with open(in_models('normal_temp.obj'), 'w') as normal_fd:
            with open(in_models('texture_temp.obj'), 'w') as texture_fd:
                for x in range(0, x_grid_count):
                    for z in range(0, z_grid_count):
                        u_li = []
                        v_li = []
                        u_li += [u_map[(x,z)]]
                        u_li += [u_map[(x+1,z)]]
                        u_li += [u_map[(x,z+1)]]
                        u_li += [u_map[(x+1,z+1)]]
                        v_li += [v_map[(x,z)]]
                        v_li += [v_map[(x+1,z)]]
                        v_li += [v_map[(x,z+1)]]
                        v_li += [v_map[(x+1,z+1)]]

                        quad = grid_xyz(f, x * dx, z * dz, dx, dz)
                        write_obj_quad_tex_len(quad, z * 4 + (z_grid_count * 4 * x),
                                               fd_main, texture_fd, normal_fd, face_fd,
                                               u_li, v_li)
    append_file(fd_main, in_models('texture_temp.obj'))
    append_file(fd_main, in_models('normal_temp.obj'))
    append_file(fd_main, in_models('face_temp.obj'))


def write_obj_quad(quad, v_i, fd_v, fd_t, fd_n, fd_f, u_adjustment, v_adjustment):
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[0][0], quad[0][1], quad[0][2]))
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[1][0], quad[1][1], quad[1][2]))
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[2][0], quad[2][1], quad[2][2]))
    fd_v.write('v {:.6f} {:.6f} {:.6f}\n'.format(quad[3][0], quad[3][1], quad[3][2]))

    normal = cross_product(vec_from_to(quad[3], quad[1]), vec_from_to(quad[3], quad[0]))
    fd_n.write('vn {:.6f} {:.6f} {:.6f}\n'.format(normal[0], normal[1], normal[2]))
    normal = cross_product(vec_from_to(quad[0], quad[2]), vec_from_to(quad[0], quad[3]))
    fd_n.write('vn {:.6f} {:.6f} {:.6f}\n'.format(normal[0], normal[1], normal[2]))

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


def generate_xz_func_file(f, x_min, x_max, x_grid_count, z_min, z_max, z_grid_count, fd_main):
    dx = (x_max - x_min) / x_grid_count
    dz = (z_max - z_min) / z_grid_count
    with open(in_models('face_temp.obj'), 'w') as face_fd:
        with open(in_models('normal_temp.obj'), 'w') as normal_fd:
            with open(in_models('texture_temp.obj'), 'w') as texture_fd:
                for x in range(0, x_grid_count):
                    for z in range(0, z_grid_count):
                        quad = grid_xyz(f, x_min + x * dx, z_min + z * dz, dx, dz)
                        write_obj_quad(quad, z * 4 + (z_grid_count * 4 * x),
                                       fd_main, texture_fd, normal_fd, face_fd,
                                       lambda u: (u - x_min) / (x_max - x_min),
                                       lambda v: (v - z_min) / (z_max - z_min))
    append_file(fd_main, in_models('texture_temp.obj'))
    append_file(fd_main, in_models('normal_temp.obj'))
    append_file(fd_main, in_models('face_temp.obj'))