var scene, camera, renderer;
var ambientLight, light;
var keyboard = {};
var speed = 0.2;

function init(){
	scene = new THREE.Scene();
	fillScene();
	renderer = new THREE.WebGLRenderer();
	renderer.setSize(500*1.77777778, 500);
	document.getElementById("display").appendChild(renderer.domElement);
	animate();
}

function addObject(){
	var mtlLoader = new THREE.MTLLoader();
	mtlLoader.load("", function(materials) {
		materials.preload();
		var objLoader = new THREE.OBJLoader();
		objLoader.setMaterials(materials);
		objLoader.load("/static/models/model.obj", function(mesh){
			scene.add(mesh);
			mesh.position.set(0, 0, 0);
			mesh.rotation.y = -Math.PI/4;
		});
	});
}

function addCamera(){
	camera = new THREE.PerspectiveCamera(90, 1.77777778, 0.1, 1000);
	camera.eulerOrder = "YXZ";
	camera.position.set(-10, 0, -10);
	camera.lookAt(new THREE.Vector3(0,0,0));
}

function addLights(){
	ambientLight = new THREE.AmbientLight(0xffffff, 0.2);
	scene.add(ambientLight);

	light = new THREE.PointLight(0xffffff, .9, 500);
	light.shadow.camera.near = 0.1;
	light.shadow.camera.far = 25;
	scene.add(light);
}

function fillScene(){
	addCamera();
	addLights();
	addObject();
}



function animate(){

	requestAnimationFrame(animate);

	// TODO: add const variable up top
	// E.g. const KEY_A = 87, KEY_LEFT = 37;
	// and replace numbers with constants
	if(keyboard[87]){ // W
		camera.translateZ( -speed );
	}
	if(keyboard[83]){ // S
		camera.translateZ( speed );
	}
	if(keyboard[65]){ // A
		camera.translateX( -speed );
	}
	if(keyboard[68]){ // D
		camera.translateX( speed );
	}
	if(keyboard[81]){ // Q
		camera.translateY( -speed );
	}
	if(keyboard[69]){ // E
		camera.translateY( speed );
	}
	if(keyboard[37]){ // left
		camera.rotation.y += speed * 0.25;
	}
	if(keyboard[39]){ // right
		camera.rotation.y -= speed * 0.25;
	}
	if(keyboard[38]){ // up
		camera.rotation.x += speed * 0.25;
	}
	if(keyboard[40]){ // down
		camera.rotation.x -= speed * 0.25;
	}

	light.position.set(camera.position.x, camera.position.y, camera.position.z);
	renderer.render(scene, camera);
}

function keyDown(event){
	keyboard[event.keyCode] = true;
}

function keyUp(event){
	keyboard[event.keyCode] = false;
}



window.addEventListener('keydown', keyDown);
window.addEventListener('keyup', keyUp);

window.onload = init;