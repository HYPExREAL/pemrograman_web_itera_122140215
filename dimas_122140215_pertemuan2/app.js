const taskForm = document.getElementById('taskForm');
const taskName = document.getElementById('taskName');
const taskDescription = document.getElementById('taskDescription');
const taskPriority = document.getElementById('taskPriority');
const taskList = document.getElementById('taskList');

let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

// Render tasks to the UI
const renderTasks = () => {
    taskList.innerHTML = '';
    tasks.forEach((task, index) => {
        taskList.innerHTML += `
            <div class="task ${task.priority}">
                <div>
                    <strong>${task.name}</strong>
                    <p>${task.description}</p>
                </div>
                <div>
                    <button onclick="editTask(${index})">Edit</button>
                    <button onclick="deleteTask(${index})">Hapus</button>
                </div>
            </div>
        `;
    });
};

// Add a new task
const addTask = (task) => {
    tasks.push(task);
    localStorage.setItem('tasks', JSON.stringify(tasks));
    renderTasks();
    alert('Tugas berhasil ditambahkan!');
};

// Delete a task
const deleteTask = (index) => {
    tasks.splice(index, 1);
    localStorage.setItem('tasks', JSON.stringify(tasks));
    renderTasks();
    alert('Tugas berhasil dihapus!');
};

// Edit a task (placeholder for edit functionality)
const editTask = (index) => {
    const task = tasks[index];
    taskName.value = task.name;
    taskDescription.value = task.description;
    taskPriority.value = task.priority;

// Remove the task temporarily for editing
    deleteTask(index);
    alert('Silakan edit tugas di formulir.');
};

// Handle form submission
taskForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = taskName.value.trim();
    const description = taskDescription.value.trim();
    const priority = taskPriority.value;

    if (name && description && priority) {
        const newTask = { name, description, priority };
        addTask(newTask);
        taskName.value = '';
        taskDescription.value = '';
        taskPriority.value = 'low';
    } else {
        alert('Harap lengkapi semua field.');
    }
});

// Initial render
renderTasks();