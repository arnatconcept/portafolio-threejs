// Selecciona el canvas
const canvas = document.querySelector('#canvas');

// Crea la escena
const scene = new THREE.Scene();

// Configura la cámara
const camera = new THREE.PerspectiveCamera(
    75, // Campo de visión
    window.innerWidth / window.innerHeight, // Relación de aspecto
    0.1, // Plano cercano
    1000 // Plano lejano
);
camera.position.z = 5;

// Crea el renderizador
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);

// Añade luces a la escena
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5); // Luz ambiental
scene.add(ambientLight);

const pointLight = new THREE.PointLight(0xffffff, 1); // Luz puntual
pointLight.position.set(10, 10, 10);
scene.add(pointLight);

// Geometría: Torus Knot
const geometry = new THREE.TorusKnotGeometry(1, 0.4, 100, 16);
const material = new THREE.MeshStandardMaterial({ color: 0x0077ff });
const torusKnot = new THREE.Mesh(geometry, material);
scene.add(torusKnot);

// Función de animación
function animate() {
    requestAnimationFrame(animate);

    // Rotación de la geometría
    torusKnot.rotation.x += 0.01;
    torusKnot.rotation.y += 0.01;

    renderer.render(scene, camera);
}

// Ajuste de tamaño en caso de cambio de ventana
window.addEventListener('resize', () => {
    // Actualiza el tamaño del renderizador y la cámara
    renderer.setSize(window.innerWidth, window.innerHeight);
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
});

// Inicia la animación
animate();
