import math

from noise import pnoise2

from py_scripts import vector_math

x_max = 15
z_max = 15
x_grid_count = 200
z_grid_count = 200


dx = x_max / x_grid_count
dz = z_max / z_grid_count

f = lambda x, z: pnoise2(x,z)

h_dict = {}
v_dict = {}
for z in range(0, x_grid_count + 1):
    if not h_dict.__contains__(z):
        h_dict[z] = 0
    for x in range(0, z_grid_count):
        p_from = [x * dx, f(x * dx, z * dz), z * dz]
        p_to = [x * dx + dx, f(x * dx + dx, z * dz), z * dz]
        h_dict[z] += vector_math.vec_length(vector_math.vec_from_to(p_from, p_to))
for x in range(0, z_grid_count + 1):
    if not v_dict.__contains__(x):
        v_dict[x] = 0
    for z in range(0, x_grid_count):
        p_from = [x * dx, f(x * dx, z * dz), z * dz]
        p_to = [x * dx, f(x * dx, z * dz + dz), z * dz + dz]
        v_dict[x] += vector_math.vec_length(vector_math.vec_from_to(p_from, p_to))

u_map = {}
v_map = {}
for z in range(0, z_grid_count + 1):
    u_map[(0, z)] = 0.0
    for x in range(1, x_grid_count + 1):
        p_to = [x * dx, f(x * dx, z * dz), z * dz]
        p_from = [x * dx - dx, f(x * dx - dx, z * dz), z * dz]
        u_map[(x, z)] = u_map[(x - 1, z)] + vector_math.vec_length(vector_math.vec_from_to(p_from, p_to)) / h_dict[z]
        if (z == 50):
            print("{:.6f}".format(u_map[(x,z)]))
for x in range(0, x_grid_count + 1):
    v_map[(x, 0)] = 0.0
    for z in range(1, z_grid_count + 1):
        p_to = [x * dx, f(x * dx, z * dz), z * dz]
        p_from = [x * dx, f(x * dx, z * dz - dz), z * dz - dz]
        v_map[(x, z)] = v_map[(x, z - 1)] + vector_math.vec_length(vector_math.vec_from_to(p_from, p_to)) / v_dict[x]
