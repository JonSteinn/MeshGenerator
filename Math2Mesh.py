from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory

from py_scripts import functions, obj_gen, file_handler


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/func3', methods=['GET', 'POST'])
def func3():
    if request.method == 'POST':
        with open('/Users/Jonni/Desktop/mesh/static/models/model.obj', 'w') as fd:  # TODO: remove hardcoded path
            obj_gen.generate_files_xyz(
                functions.eval_xyz(request.form['func']),
                float(request.form['min_x']),
                float(request.form['max_x']),
                int(request.form['grid_x']),
                float(request.form['min_z']),
                float(request.form['max_z']),
                int(request.form['grid_z']),
                fd
            )
            fd.close()
    return redirect('/')


@app.route('/funcPara', methods=['GET', 'POST'])
def func_para():
    if request.method == 'POST':
        with open('/Users/Jonni/Desktop/mesh/static/models/model.obj', 'w') as fd:  # TODO: remove hardcoded path
            obj_gen.generate_files_parametric(
                functions.eval_parametric(request.form['funcX'], request.form['funcY'], request.form['funcZ']),
                float(request.form['min_u']),
                float(request.form['max_u']),
                int(request.form['grid_u']),
                float(request.form['min_v']),
                float(request.form['max_v']),
                int(request.form['grid_v']),
                fd
            )
            fd.close()
    return redirect('/')


@app.route('/dl', methods=['GET'])
def download():
    file_handler.zip_objects()
    return send_from_directory('static', 'models/download/objects.zip')


if __name__ == '__main__':
    app.run()
