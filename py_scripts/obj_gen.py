import math
import os

from FilePaths import in_models


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


def write_obj_quad(quad, fd1, fd2, fd3, index):
    normal = cross_product(vec_from_to(quad[0], quad[1]), vec_from_to(quad[0], quad[2]))
    fd1.write('v {:.6f} {:6f} {:6f}\n'.format(quad[0][0], quad[0][1], quad[0][2]))
    fd1.write('v {:.6f} {:6f} {:6f}\n'.format(quad[1][0], quad[1][1], quad[1][2]))
    fd1.write('v {:.6f} {:6f} {:6f}\n'.format(quad[2][0], quad[2][1], quad[2][2]))
    fd1.write('v {:.6f} {:6f} {:6f}\n'.format(quad[3][0], quad[3][1], quad[3][2]))
    fd1.write('vn {:.6f} {:6f} {:6f}\n'.format(normal[0], normal[1], normal[2]))
    fd1.write('f {:d} {:d} {:d}\n'.format(index + 1, index + 3, index + 4))
    fd1.write('f {:d} {:d} {:d}\n'.format(index + 1, index + 4, index + 2))
    fd1.write('f {:d} {:d} {:d}\n'.format(index + 1, index + 2, index + 4))
    fd1.write('f {:d} {:d} {:d}\n'.format(index + 1, index + 4, index + 3))
    xml_vertex(fd2, quad, normal)
    xml_faces(fd3, index)


def write_obj_quad_single(quad, fd1, fd2, fd3, index):
    normal = cross_product(vec_from_to(quad[0], quad[1]), vec_from_to(quad[0], quad[2]))
    fd1.write('v {:.6f} {:6f} {:6f}\n'.format(quad[0][0], quad[0][1], quad[0][2]))
    fd1.write('v {:.6f} {:6f} {:6f}\n'.format(quad[1][0], quad[1][1], quad[1][2]))
    fd1.write('v {:.6f} {:6f} {:6f}\n'.format(quad[2][0], quad[2][1], quad[2][2]))
    fd1.write('v {:.6f} {:6f} {:6f}\n'.format(quad[3][0], quad[3][1], quad[3][2]))
    fd1.write('vn {:.6f} {:6f} {:6f}\n'.format(normal[0], normal[1], normal[2]))
    fd1.write('f {:d} {:d} {:d}\n'.format(index + 1, index + 3, index + 4))
    fd1.write('f {:d} {:d} {:d}\n'.format(index + 1, index + 4, index + 2))
    xml_vertex(fd2, quad, normal)
    xml_faces(fd3, index)


def xml_header(fd, vertices):
    fd.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    fd.write('<mesh>\n')
    fd.write('\t<sharedgeometry vertexcount="{:d}">\n'.format(vertices))
    fd.write('\t\t<vertexbuffer positions="true" normals="true" colours_diffuse="False" texture_coords="0">\n')


def xml_vertex(fd, quad, normal):
    fd.write('\t\t\t<vertex>\n')
    fd.write('\t\t\t\t<position z="{:.6f}" y="{:.6f}" x="{:.6f}"/>\n'.format(quad[0][0], quad[0][1], quad[0][2]))
    fd.write('\t\t\t\t<normal z="{:.6f}" y="{:.6f}" x="{:.6f}"/>\n'.format(normal[0], normal[1], normal[2]))
    fd.write('\t\t\t</vertex>\n')
    fd.write('\t\t\t<vertex>\n')
    fd.write('\t\t\t\t<position z="{:.6f}" y="{:.6f}" x="{:.6f}"/>\n'.format(quad[1][0], quad[1][1], quad[1][2]))
    fd.write('\t\t\t\t<normal z="{:.6f}" y="{:.6f}" x="{:.6f}"/>\n'.format(normal[0], normal[1], normal[2]))
    fd.write('\t\t\t</vertex>\n')
    fd.write('\t\t\t<vertex>\n')
    fd.write('\t\t\t\t<position z="{:.6f}" y="{:.6f}" x="{:.6f}"/>\n'.format(quad[2][0], quad[2][1], quad[2][2]))
    fd.write('\t\t\t\t<normal z="{:.6f}" y="{:.6f}" x="{:.6f}"/>\n'.format(normal[0], normal[1], normal[2]))
    fd.write('\t\t\t</vertex>\n')
    fd.write('\t\t\t<vertex>\n')
    fd.write('\t\t\t\t<position z="{:.6f}" y="{:.6f}" x="{:.6f}"/>\n'.format(quad[3][0], quad[3][1], quad[3][2]))
    fd.write('\t\t\t\t<normal z="{:.6f}" y="{:.6f}" x="{:.6f}"/>\n'.format(normal[0], normal[1], normal[2]))
    fd.write('\t\t\t</vertex>\n')


def xml_faces(fd, index):
    fd.write('\t\t\t\t<face v1="{:d}" v2="{:d}" v3="{:d}"/>\n'.format(index + 1, index + 3, index + 4))
    fd.write('\t\t\t\t<face v1="{:d}" v2="{:d}" v3="{:d}"/>\n'.format(index + 1, index + 4, index + 2))
    fd.write('\t\t\t\t<face v1="{:d}" v2="{:d}" v3="{:d}"/>\n'.format(index + 1, index + 2, index + 4))
    fd.write('\t\t\t\t<face v1="{:d}" v2="{:d}" v3="{:d}"/>\n'.format(index + 1, index + 4, index + 3))


def xml_face_header(fd, faces):
    fd.write('\t\t</vertexbuffer>\n')
    fd.write('\t</sharedgeometry>\n')
    fd.write('\t<submeshes>\n')
    fd.write('\t\t<submesh use32bitindexes="False" operationtype="triangle_list" material="_missing_material_" usesharedvertices="true">\n')
    fd.write('\t\t\t<faces count="{:d}">\n'.format(faces))


def xml_end(fd):
    fd.write('\t\t\t</faces>\n')
    fd.write('\t\t</submesh>\n')
    fd.write('\t</submeshes>\n')
    fd.write('\t<submeshnames>\n')
    fd.write('\t\t<submesh name="_missing_material_" index="0">\n')
    fd.write('\t\t</submesh>\n')
    fd.write('\t</submeshnames>\n')
    fd.write('</mesh>\n')


def append_file(fd, file_path):
    with open(file_path, 'r') as fd2:
        for line in fd2:
            fd.write(line)
    os.remove(file_path)


def generate_files_xyz(f, x_min, x_max, x_grid_count, z_min, z_max, z_grid_count, fd1, fd2, d_sided):
    #  TODO FIX XML GEN
    if d_sided:
        xml_header(fd2, x_grid_count * z_grid_count * 4)
        with open(in_models('face_temp.txt'), 'w') as fd3:
            dx = (x_max - x_min) / x_grid_count
            dz = (z_max - z_min) / z_grid_count
            for x in range(0, x_grid_count):
                for z in range(0, z_grid_count):
                    quad = grid_xyz(f, x_min + x * dx, z_min + z * dz, dx, dz)
                    write_obj_quad(quad, fd1, fd2, fd3, z * 4 + (z_grid_count * 4 * x))
        xml_face_header(fd2, x_grid_count * z_grid_count * 4)
        append_file(fd2, in_models('face_temp.txt'))
        xml_end(fd2)
    else:
        #  TODO MAKE SINGLE FOR XML!
        xml_header(fd2, x_grid_count * z_grid_count * 4)
        with open(in_models('face_temp.txt'), 'w') as fd3:
            dx = (x_max - x_min) / x_grid_count
            dz = (z_max - z_min) / z_grid_count
            for x in range(0, x_grid_count):
                for z in range(0, z_grid_count):
                    quad = grid_xyz(f, x_min + x * dx, z_min + z * dz, dx, dz)
                    write_obj_quad_single(quad, fd1, fd2, fd3, z * 4 + (z_grid_count * 4 * x))
        xml_face_header(fd2, x_grid_count * z_grid_count * 4)
        append_file(fd2, in_models('face_temp.txt'))
        xml_end(fd2)


def generate_files_parametric(f, u_min, u_max, u_grid_count, v_min, v_max, v_grid_count, fd1, fd2, d_sided):
    #  TODO FIX XML GEN
    if d_sided:
        xml_header(fd2, u_grid_count * v_grid_count * 4)
        with open(in_models('face_temp.txt'), 'w') as fd3:
            du = (u_max - u_min) / u_grid_count
            dv = (v_max - v_min) / v_grid_count
            for u in range(0, u_grid_count):
                for v in range(0, v_grid_count):
                    quad = grid_parametric(f, u_min + u * du, v_min + v * dv, du, dv)
                    write_obj_quad(quad, fd1, fd2, fd3, v * 4 + (v_grid_count * 4 * u))
        xml_face_header(fd2, u_grid_count * v_grid_count * 4)
        append_file(fd2, in_models('face_temp.txt'))
        xml_end(fd2)
    else:
        #  TODO MAKE SINGLE FOR XML!
        xml_header(fd2, u_grid_count * v_grid_count * 4)
        with open(in_models('face_temp.txt'), 'w') as fd3:
            du = (u_max - u_min) / u_grid_count
            dv = (v_max - v_min) / v_grid_count
            for u in range(0, u_grid_count):
                for v in range(0, v_grid_count):
                    quad = grid_parametric(f, u_min + u * du, v_min + v * dv, du, dv)
                    write_obj_quad_single(quad, fd1, fd2, fd3, v * 4 + (v_grid_count * 4 * u))
        xml_face_header(fd2, u_grid_count * v_grid_count * 4)
        append_file(fd2, in_models('face_temp.txt'))
        xml_end(fd2)