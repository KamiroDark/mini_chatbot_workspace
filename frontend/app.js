// Estado de la aplicación
let availableComponents = [];
let selectedComponents = [];

// Elementos DOM
const componentsList = document.getElementById('components-list');
const buildBtn = document.getElementById('build-btn');
const statusMessage = document.getElementById('status-message');

// Cargar componentes al iniciar
document.addEventListener('DOMContentLoaded', () => {
    loadComponents();
});

// Función para cargar componentes desde la API
async function loadComponents() {
    try {
        const response = await fetch('http://localhost:3000/api/components');
        const data = await response.json();
        
        if (data.success) {
            availableComponents = data.components;
            renderComponents();
        }
    } catch (error) {
        console.error('Error loading components:', error);
        componentsList.innerHTML = '<p style="color: red;">Error loading components. Make sure the server is running.</p>';
    }
}

// Renderizar componentes en el DOM
function renderComponents() {
    if (availableComponents.length === 0) {
        componentsList.innerHTML = '<p>No components available</p>';
        return;
    }

    componentsList.innerHTML = availableComponents.map(comp => `
        <div class="component-card" id="card-${comp.id}">
            <label>
                <input 
                    type="checkbox" 
                    value="${comp.id}" 
                    onchange="toggleComponent(${comp.id})"
                >
                <div class="component-info">
                    <h3>${comp.name}</h3>
                    <p>${comp.description}</p>
                    <small style="color: #999;">File: ${comp.file}</small>
                </div>
            </label>
        </div>
    `).join('');
}

// Manejar selección de componentes
function toggleComponent(componentId) {
    const card = document.getElementById(`card-${componentId}`);
    
    if (selectedComponents.includes(componentId)) {
        selectedComponents = selectedComponents.filter(id => id !== componentId);
        card.classList.remove('selected');
    } else {
        selectedComponents.push(componentId);
        card.classList.add('selected');
    }
    
    // Habilitar/deshabilitar botón de build
    buildBtn.disabled = selectedComponents.length === 0;
    
    // Limpiar mensaje de estado
    statusMessage.textContent = '';
    statusMessage.className = '';
}

// Event listener para el botón Build
buildBtn.addEventListener('click', buildPackage);

// Función para construir y descargar el paquete
async function buildPackage() {
    if (selectedComponents.length === 0) {
        showStatus('Please select at least one component', 'error');
        return;
    }

    // Mostrar estado de carga
    buildBtn.disabled = true;
    buildBtn.textContent = '🔨 Building Package...';
    showStatus('Generating your chatbot package...', 'success');

    try {
        const response = await fetch('http://localhost:3000/api/build', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                components: selectedComponents
            })
        });

        if (!response.ok) {
            throw new Error('Build failed');
        }

        // Obtener el archivo como blob
        const blob = await response.blob();
        
        // Crear URL temporal para descarga
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `chatbot-package-${Date.now()}.zip`;
        document.body.appendChild(a);
        a.click();
        
        // Limpiar
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);

        showStatus('✅ Package downloaded successfully! Check your downloads folder.', 'success');
        
    } catch (error) {
        console.error('Error building package:', error);
        showStatus('❌ Error building package. Please try again.', 'error');
    } finally {
        // Restaurar botón
        buildBtn.disabled = false;
        buildBtn.textContent = 'Build & Download Package';
    }
}

// Función auxiliar para mostrar mensajes de estado
function showStatus(message, type) {
    statusMessage.textContent = message;
    statusMessage.className = type;
}