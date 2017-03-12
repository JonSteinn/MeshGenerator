/**
 * Created by Jonni on 3/12/2017.
 */

function func3Validate(){

    var func = document.getElementById('func3d').value;
    if (func == "") {
        toast("Function can't be empty!")
        return false;
    }

    var min_x = document.getElementById('minx').value;
    if (min_x == "") {
        toast("Min x can't be empty!");
        return false;
    }
    if (isNaN(min_x)) {
        toast("Min x must be numeric!");
        return false;
    }

    var max_x = document.getElementById('maxx').value;
    if (max_x == "") {
        toast("Max x can't be empty!");
        return false;
    }
    if (isNaN(max_x)) {
        toast('Max x must be numeric!');
        return false;
    }
    if (parseFloat(min_x) >= parseFloat(max_x)) {
        toast('Min x must be less than max x');
        return false;
    }

    var grid_x = document.getElementById('gridx').value;
    if (!isInt(grid_x)) {
        toast('Grid count x must be an integer!');
        return false;
    }

    var min_z = document.getElementById('minz').value;
    if (min_z == "") {
        toast("Min z can't be empty!");
        return false;
    }
    if (isNaN(min_z)) {
        toast("Min z must be numeric!");
        return false;
    }

    var max_z = document.getElementById('maxz').value;
    if (max_z == "") {
        toast("Max z can't be empty!");
        return false;
    }
    if (isNaN(max_z)) {
        toast('Max z must be numeric!');
        return false;
    }
    if (parseFloat(min_z) >= parseFloat(max_z)) {
        toast('Min z must be less than max x');
        return false;
    }

    var grid_z = document.getElementById('gridz').value;
    if (!isInt(grid_z)) {
        toast('Grid count z must be an integer!');
        return false;
    }

    return true;
}

function funcPValidate() {



    return true;
}


function toast(msg) {
    var x = document.getElementById("toast3")
    x.innerHTML = msg;
    x.className = "show";
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
}

function isInt(value) {
  var x;
  return isNaN(value) ? !1 : (x = parseFloat(value), (0 | x) === x);
}