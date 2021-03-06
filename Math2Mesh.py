import os
import shutil
import sys
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from noise import pnoise2
from FilePaths import in_models
from py_scripts import functions, file_handler, noise_gen, xz_func_gen, para_func_gen


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/func3', methods=['GET', 'POST'])
def func3():
    if request.method == 'POST':
        try:
            with open(in_models('model.obj'), 'w') as fd1:
                if bool(request.form.getlist('t3d3')):
                    xz_func_gen.generate_xz_func_file_tex_len(
                        functions.eval_xyz(request.form['func']),
                        float(request.form['min_x']),
                        float(request.form['max_x']),
                        int(request.form['grid_x']),
                        float(request.form['min_z']),
                        float(request.form['max_z']),
                        int(request.form['grid_z']),
                        fd1
                    )
                else:
                    xz_func_gen.generate_xz_func_file(
                        functions.eval_xyz(request.form['func']),
                        float(request.form['min_x']),
                        float(request.form['max_x']),
                        int(request.form['grid_x']),
                        float(request.form['min_z']),
                        float(request.form['max_z']),
                        int(request.form['grid_z']),
                        fd1
                    )
        except (NameError, ValueError, ZeroDivisionError, TypeError, ArithmeticError, FloatingPointError):
            shutil.copy(in_models('error.obj'), in_models('model.obj'))
            file_handler.remove_temps()
            print(sys.exc_info()[0])
        except:  # TODO: remove
            print(sys.exc_info()[0])
    return redirect('/')


@app.route('/funcPara', methods=['GET', 'POST'])
def func_para():
    if request.method == 'POST':
        try:
            with open(in_models('model.obj'), 'w') as fd1:
                para_func_gen.generate_parametric_func_file(
                    functions.eval_parametric(request.form['funcX'], request.form['funcY'], request.form['funcZ']),
                    float(request.form['min_u']),
                    float(request.form['max_u']),
                    int(request.form['grid_u']),
                    float(request.form['min_v']),
                    float(request.form['max_v']),
                    int(request.form['grid_v']),
                    fd1,
                    bool(request.form.getlist('double_sided'))
                )
        except (NameError, ValueError, ZeroDivisionError, TypeError, ArithmeticError, FloatingPointError):
            shutil.copy(in_models('error.obj'), in_models('model.obj'))
            file_handler.remove_temps()
            print(sys.exc_info()[0])
        except:  # TODO: remove
            print(sys.exc_info()[0])
    return redirect('/')


@app.route('/funcNoise', methods=['POST'])
def func_noise():
    if request.method == 'POST':
        try:
            with open(in_models('model.obj'), 'w') as fd1:
                if bool(request.form.getlist('t3d')):
                    noise_gen.generate_noise_file_tex_len(
                        lambda x, z: float(request.form['amplitude']) * pnoise2(
                            x, z, octaves=int(request.form['octaves']),
                            persistence=float(request.form['persistence']),
                            lacunarity=float(request.form['lacunarity'])),
                        float(request.form['gridWidth']),
                        int(request.form['gridCountX']),
                        float(request.form['gridLength']),
                        int(request.form['gridCountZ']),
                        fd1
                    )
                else:
                    noise_gen.generate_noise_file(
                        lambda x, z: float(request.form['amplitude']) * pnoise2(
                            x, z, octaves=int(request.form['octaves']),
                            persistence=float(request.form['persistence']),
                            lacunarity=float(request.form['lacunarity'])),
                        float(request.form['gridWidth']),
                        int(request.form['gridCountX']),
                        float(request.form['gridLength']),
                        int(request.form['gridCountZ']),
                        fd1
                    )
        except (NameError, ValueError, ZeroDivisionError, TypeError, ArithmeticError, FloatingPointError):
            shutil.copy(in_models('error.obj'), in_models('model.obj'))
            file_handler.remove_temps()
            print(sys.exc_info()[0])
        except:  # TODO: remove
            print(sys.exc_info())
    return redirect('/')


@app.route('/dl', methods=['GET'])
def download():
    try:
        file_handler.zip_objects()
    except:  #TODO: remove
        print(sys.exc_info()[0])
    return send_from_directory('static', 'models/download/objects.zip')


if __name__ == '__main__':
    app.run()
