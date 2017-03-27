import math


def grid_xyz(f, x, z, dx, dz):
    return [
        [x, f(x, z), z],
        [x + dx, f(x + dx, z), z],
        [x, f(x, z + dz), z + dz],
        [x + dx, f(x + dx, z + dz), z + dz]
    ]


def grid_parametric(f, u, v, du, dv):
    return [
        [f[0](u, v), f[1](u, v), f[2](u, v)],
        [f[0](u + du, v), f[1](u + du, v), f[2](u + du, v)],
        [f[0](u, v + dv), f[1](u, v + dv), f[2](u, v + dv)],
        [f[0](u + du, v + dv), f[1](u + du, v + dv), f[2](u + du, v + dv)],
    ]


def vec_from_to(p1, p2):
    return [p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]]


def vec_length(v):
    return math.sqrt(sum(map(lambda val: val**2, v)))


def normalized(v):
    l = vec_length(v)
    if l == 0:
        return [0, 0, 0]
    return list(map(lambda val: val/l, v))


def cross_product(u, v):
    return normalized([u[1]*v[2] - u[2]*v[1], u[2]*v[0] - u[0]*v[2], u[0]*v[1] - u[1]*v[0]])


def neg_vec(v):
    return list(map(lambda x: -x, v))
