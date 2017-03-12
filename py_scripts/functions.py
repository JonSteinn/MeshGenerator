import math


def parse(command):
    command = command.translate({ord(c): '' for c in " !@#$%&[]{};:,?\|`~_"})
    command = command\
        .replace('^', '**')\
        .replace('E', 'math.E')\
        .replace('PI', 'math.pi')\
        .replace('sin', 'math.sin')\
        .replace('cos', 'math.cos')\
        .replace('tan', 'math.tan')\
        .replace('atan', 'math.atan')\
        .replace('atan2', 'math.atan2')\
        .replace('acos', 'math.acos')\
        .replace('asin', 'math.asin')\
        .replace('sqrt', 'math.sqrt')\
        .replace('lg', 'math.log2')\
        .replace('log', 'math.log10')\
        .replace('ln', 'math.log')\
        .replace('ceil', 'math.ceil')\
        .replace('cosh', 'math.cosh')\
        .replace('sinh', 'math.sinh')\
        .replace('tanh', 'math.tanh')\
        .replace('acosh', 'math.acosh')\
        .replace('asinh', 'math.asinh')\
        .replace('atanh', 'math.atanh')\
        .replace('mod', '%')\
        .replace('if', ' if ')\
        .replace('else', ' else ')\
        .replace('not', ' not ')\
        .replace('and', ' and ')\
        .replace('or', ' or ')
    return command


def eval_xyz(command):
    return lambda x, z: eval(parse(command))


def eval_parametric(x_command, y_command, z_command):
    return [
        lambda u, v: eval(parse(x_command)),
        lambda u, v: eval(parse(y_command)),
        lambda u, v: eval(parse(z_command))
    ]