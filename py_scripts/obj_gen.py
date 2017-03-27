# Not really using this anymore, but leaving this code here.
# This is some of the methods for generating OgreXML
# But I might as well open the obj in Blender and convert it there
# which I am already doing to get Unity assets.
# Was starting to get slow with all this file writing..


def ogre_position(x, y, z):
    return '\t\t\t\t<position z="{:.6f}" x="{:.6f}" y="{:.6f}"/>\n'.format(z, x, y)


def ogre_normal(x, y, z):
    return '\t\t\t\t<normal z="{:.6f}" x="{:.6f}" y="{:.6f}"/>\n'.format(z, x, y)


def ogre_texture(u, v):
    return '\t\t\t\t<texcoord u="{:.6f}" v="{:.6f}"/>\n'.format(u, v)


def ogre_vertex(p_x, p_y, p_z, n_x, n_y, n_z, u, v):
    return '\t\t\t<vertex>\n{:s}{:s}{:s}\t\t\t</vertex>\n'.format(
        ogre_position(p_x, p_y, p_z), ogre_normal(n_x, n_y, n_z), ogre_texture(u, v))


def ogre_face(v1, v2, v3):
    return '\t\t\t\t<face v1="{:d}" v2="{:d}" v3="{:d}"/>\n'.format(v1, v2, v3)


def ogre_start(vertex_count, fd):
    fd.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    fd.write('<mesh>\n')
    fd.write('\t<sharedgeometry vertexcount="{:d}">\n'.format(vertex_count))
    fd.write('\t\t<vertexbuffer normals="true" positions="true" colours_diffuse="False" texture_coords="1">\n')


def ogre_mid(faces_count, fd):
    fd.write('\t\t</vertexbuffer>\n')
    fd.write('\t</sharedgeometry>\n')
    fd.write('\t<submeshes>\n')
    fd.write('\t\t<submesh operationtype="triangle_list" use32bitindexes="False" usesharedvertices="true">\n')
    fd.write('\t\t\t<faces count="{:d}">\n'.format(faces_count))


def ogre_end(fd):
    fd.write('\t\t\t</faces>\n')
    fd.write('\t\t</submesh>\n')
    fd.write('\t</submeshes>\n')
    fd.write('</mesh>\n')


# o_v_fd.write(ogre_vertex(quad[3][0], quad[3][1], quad[3][2], normal1[0], normal1[1], normal1[2], u_adjustment(quad[3][0]), v_adjustment(quad[3][2])))
# o_v_fd.write(ogre_vertex(quad[1][0], quad[1][1], quad[1][2], normal1[0], normal1[1], normal1[2], u_adjustment(quad[1][0]), v_adjustment(quad[1][2])))
# o_v_fd.write(ogre_vertex(quad[0][0], quad[0][1], quad[0][2],normal1[0], normal1[1], normal1[2], u_adjustment(quad[0][0]),v_adjustment(quad[0][2])))
# o_v_fd.write(ogre_vertex(quad[0][0], quad[0][1], quad[0][2],normal2[0], normal2[1], normal2[2],u_adjustment(quad[0][0]),v_adjustment(quad[0][2])))
# o_v_fd.write(ogre_vertex(quad[2][0], quad[2][1], quad[2][2],normal2[0], normal2[1], normal2[2],u_adjustment(quad[2][0]),v_adjustment(quad[2][2])))
# o_v_fd.write(ogre_vertex(quad[3][0], quad[3][1], quad[3][2],normal2[0], normal2[1], normal2[2],u_adjustment(quad[3][0]),v_adjustment(quad[3][2])))
# o_i = (v_i // 4) * 6
# o_f_fd.write(ogre_face(o_i, o_i + 1, o_i + 2))
# o_f_fd.write(ogre_face(o_i + 3, o_i + 4, o_i + 5))


def generate_files_parametric(f, u_min, u_max, u_grid_count, v_min, v_max, v_grid_count, fd1, fd2, d_sided):
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