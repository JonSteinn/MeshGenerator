var scene, camera, renderer;
var ambientLight, light;
var keyboard = {};
var speed = 0.2;

function init(){
	scene = new THREE.Scene();
	camera = new THREE.PerspectiveCamera(90, 1.77777778, 0.1, 1000);
	
	ambientLight = new THREE.AmbientLight(0xffffff, 0.2);
	scene.add(ambientLight);
	
	light = new THREE.PointLight(0xffffff, .9, 500);
	light.shadow.camera.near = 0.1;
	light.shadow.camera.far = 25;
	scene.add(light);

	// Model/material loading!
	var mtlLoader = new THREE.MTLLoader();
	mtlLoader.load("", function(materials) {
		materials.preload();
		var objLoader = new THREE.OBJLoader();
		objLoader.setMaterials(materials);		
		objLoader.load("/static/models/t1.obj", function(mesh){
			scene.add(mesh);
			mesh.position.set(0, 0, 0);
			mesh.rotation.y = -Math.PI/4;
		});
	});
	
	camera.position.set(0, 0, -100);
	camera.lookAt(new THREE.Vector3(0,0,0));
	
	renderer = new THREE.WebGLRenderer();
	renderer.setSize(500*1.77777778, 500);

	document.body.appendChild(renderer.domElement);
	
	animate();
}

function animate(){
	requestAnimationFrame(animate);

	if(keyboard[87]){
		camera.translateZ( -speed );
	}
	if(keyboard[83]){
		camera.translateZ( speed );
	}
	if(keyboard[65]){
		camera.translateX( -speed );
	}
	if(keyboard[68]){
		camera.translateX( speed );
	}
	if(keyboard[81]){
		camera.translateY( -speed );
	}
	if(keyboard[69]){
		camera.translateY( speed );
	}


	if(keyboard[37]){ // left arrow key
		camera.rotation.y -= speed * 0.25;
	}
	if(keyboard[39]){ // right arrow key
		camera.rotation.y += speed * 0.25;
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
