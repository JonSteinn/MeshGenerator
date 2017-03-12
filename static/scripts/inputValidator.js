/**
 * Created by Jonni on 3/12/2017.
 */

function func3Validate(){

    var func = document.getElementById('func3d').value;
    if (func == "") {
        toast("Function can't be empty!", 'toast3')
        return false;
    }

    var min_x = document.getElementById('minx').value;
    if (min_x == "") {
        toast("Min x can't be empty!", 'toast3');
        return false;
    }
    if (isNaN(min_x)) {
        toast("Min x must be numeric!", 'toast3');
        return false;
    }
    if (parseFloat(min_x) < -99999) {
        toast("Min x is too small!", 'toast3');
        return false;
    }

    var max_x = document.getElementById('maxx').value;
    if (max_x == "") {
        toast("Max x can't be empty!", 'toast3');
        return false;
    }
    if (isNaN(max_x)) {
        toast('Max x must be numeric!', 'toast3');
        return false;
    }
    if (parseFloat(max_x) > 99999) {
        toast('Max x is too large!', 'toast3');
        return false;
    }
    if (parseFloat(min_x) >= parseFloat(max_x)) {
        toast('Min x must be less than max x', 'toast3');
        return false;
    }

    var grid_x = document.getElementById('gridx').value;
    if (grid_x == "") {
        toast("Grid count x can't be empty!", 'toast3');
        return false;
    }
    if (!isInt(grid_x)) {
        toast('Grid count x must be an integer!', 'toast3');
        return false;
    }

    var min_z = document.getElementById('minz').value;
    if (min_z == "") {
        toast("Min z can't be empty!", 'toast3');
        return false;
    }
    if (isNaN(min_z)) {
        toast("Min z must be numeric!", 'toast3');
        return false;
    }
    if (parseFloat(min_z) < -99999) {
        toast("Min z is too small!", 'toast3');
        return false;
    }

    var max_z = document.getElementById('maxz').value;
    if (max_z == "") {
        toast("Max z can't be empty!", 'toast3');
        return false;
    }
    if (isNaN(max_z)) {
        toast('Max z must be numeric!', 'toast3');
        return false;
    }
    if (parseFloat(max_z) > 99999) {
        toast('Max z is too large!', 'toast3');
        return false;
    }
    if (parseFloat(min_z) >= parseFloat(max_z)) {
        toast('Min z must be less than max x', 'toast3');
        return false;
    }

    var grid_z = document.getElementById('gridz').value;
    if (grid_z == "") {
        toast("Grid count z can't be empty!", 'toast3');
        return false;
    }
    if (!isInt(grid_z)) {
        toast('Grid count z must be an integer!', 'toast3');
        return false;
    }
    if (parseInt(grid_x) * parseInt(grid_z) > 250000) {
        toast("Total grid (x * z) can't exceed 25000!", 'toast3');
        return false;
    }

    return true;
}

function funcPValidate() {

    var funcX = document.getElementById('funcX').value;
    if (funcX == "") {
        toast("X function can't be empty!", 'toastP');
        return false;
    }

    var funcY = document.getElementById('funcY').value;
    if (funcY == "") {
        toast("Y function can't be empty!", 'toastP');
        return false;
    }

    var funcZ = document.getElementById('funcZ').value;
    if (funcZ == "") {
        toast("Z function can't be empty!", 'toastP');
        return false;
    }

    var min_u = document.getElementById('minu').value;
    if (min_u == "") {
        toast("Min u can't be empty!", 'toastP');
        return false;
    }
    if (isNaN(min_u)) {
        toast("Min u must be numeric!", 'toastP');
        return false;
    }
    if (parseFloat(min_u) < -99999) {
        toast('Min u is too small!', 'toastP');
        return false;
    }

    var max_u = document.getElementById('maxu').value;
    if (max_u == "") {
        toast("Max u can't be empty!", 'toastP');
        return false;
    }
    if (isNaN(max_u)) {
        toast('Max u must be numeric!', 'toastP');
        return false;
    }
    if (parseFloat(max_u) > 99999) {
        toast('Max u is too large!', 'toastP');
        return false;
    }
    if (parseFloat(min_u) >= parseFloat(max_u)) {
        toast('Min u must be less than max u', 'toastP');
        return false;
    }

    var grid_u = document.getElementById('gridu').value;
    if (grid_u == "") {
        toast("Grid count u can't be empty!", 'toastP');
        return false;
    }
    if (!isInt(grid_u)) {
        toast('Grid count u must be an integer!', 'toastP');
        return false;
    }

    var min_v = document.getElementById('minv').value;
    if (min_v == "") {
        toast("Min v can't be empty!", 'toastP');
        return false;
    }
    if (isNaN(min_v)) {
        toast("Min v must be numeric!", 'toastP');
        return false;
    }
    if (parseFloat(min_v) < -99999) {
        toast('Min v is too small!', 'toastP');
        return false;
    }

    var max_v = document.getElementById('maxv').value;
    if (max_v == "") {
        toast("Max v can't be empty!", 'toastP');
        return false;
    }
    if (isNaN(max_v)) {
        toast('Max v must be numeric!', 'toastP');
        return false;
    }
    if (parseFloat(max_v) > 99999) {
        toast('Max v is too large!', 'toastP');
        return false;
    }
    if (parseFloat(min_v) >= parseFloat(max_v)) {
        toast('Min v must be less than max v', 'toastP');
        return false;
    }

    var grid_v = document.getElementById('gridv').value;
    if (grid_v == "") {
        toast("Grid count v can't be empty!", 'toastP');
        return false;
    }
    if (!isInt(grid_v)) {
        toast('Grid count v must be an integer!', 'toastP');
        return false;
    }
    if (parseInt(grid_u) * parseInt(grid_v) > 250000) {
        toast("Total grid (u * v) can't exceed 25000!", 'toastP');
        return false;
    }

    return true;
}


function toast(msg, id) {
    var x = document.getElementById(id)
    x.innerHTML = msg;
    x.className = "show";
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}

function isInt(value) {
  var x;
  return isNaN(value) ? !1 : (x = parseFloat(value), (0 | x) === x);
}