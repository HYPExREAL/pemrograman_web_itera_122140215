document.addEventListener('DOMContentLoaded', () => {
    const taskInput = document.getElementById('taskInput');
    const addTaskButton = document.getElementById('addTaskButton');
    const taskList = document.getElementById('taskList');

    // Load tasks from localStorage
    loadTasks();

    // Add task event
    addTaskButton.addEventListener('click', () => {
        const taskText = taskInput.value.trim();
        if (taskText) {
            addTask(taskText);
            taskInput.value = ''; // Clear input
        }
    });

    // Function to add a task
    function addTask(taskText) {
        const li = document.createElement('li');
        li.textContent = taskText;

        // Create a checkbox to mark as done
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.addEventListener('change', () => {
            li.classList.toggle('completed');
            saveTasks();
        });

        // Create a delete button
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Hapus';
        deleteButton.addEventListener('click', () => {
            li.remove();
            saveTasks();
        });

        li.appendChild(checkbox);
        li.appendChild(deleteButton);
        taskList.appendChild(li);

        saveTasks(); // Save tasks to localStorage
    }

    // Function to save tasks to localStorage
    function saveTasks() {
        const tasks = [];
        taskList.querySelectorAll('li').forEach(li => {
            tasks.push({
                text: li.firstChild.textContent,
                completed: li.classList.contains('completed')
            });
        });
        localStorage.setItem('tasks', JSON.stringify(tasks));
    }

    // Function to load tasks from localStorage
    function loadTasks() {
        const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
        tasks.forEach(task => {
            const li = document.createElement('li');
            li.textContent = task.text;
            if (task.completed) {
                li.classList.add('completed');
            }

            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.checked = task.completed;
            checkbox.addEventListener('change', () => {
                li.classList.toggle('completed');
                saveTasks();
            });

            const deleteButton = document.createElement('button');
            deleteButton.textContent = 'Hapus';
            deleteButton.addEventListener('click', () => {
                li.remove();
                saveTasks();
            });

            li.appendChild(checkbox);
            li.appendChild(deleteButton);
            taskList.appendChild(li);
        });
    }
});