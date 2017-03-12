import math


def parse(command):
    command = command.translate({ord(c): '' for c in " !@#$%&[]{};:,?\|`~_"})
    command = command\
        .replace('^', '**')\
        .replace('E', 'math.e')\
        .replace('PI', 'math.pi')\
        .replace('cosh', '!')\
        .replace('sinh', '@')\
        .replace('tanh', '#')\
        .replace('acosh', '$')\
        .replace('asinh', '%')\
        .replace('atanh', '&')\
        .replace('atan2', '[')\
        .replace('atan', ']')\
        .replace('acos', '{')\
        .replace('asin', '}')\
        .replace('sin', 'math.sin')\
        .replace('cos', 'math.cos')\
        .replace('tan', 'math.tan')\
        .replace('{', 'math.acos')\
        .replace('}', 'math.asin')\
        .replace(']', 'math.atan')\
        .replace('[', 'math.atan2')\
        .replace('!', 'math.cosh')\
        .replace('@', 'math.sinh')\
        .replace('#', 'math.tanh')\
        .replace('$', 'math.acosh')\
        .replace('%', 'math.asinh')\
        .replace('&', 'math.atanh')\
        .replace('sqrt', 'math.sqrt')\
        .replace('lg', 'math.log2')\
        .replace('log', 'math.log10')\
        .replace('ln', 'math.log')\
        .replace('ceil', 'math.ceil')\
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