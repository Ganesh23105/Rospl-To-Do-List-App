from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'HarshPadyal'  # Change this in production

# In-memory storage for tasks (use database in production)
tasks = []
task_counter = 1

class Task:
    def __init__(self, id, title, description="", completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

@app.route('/')
def index():
    """Display all tasks"""
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    """Add a new task"""
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        
        if title:
            global task_counter
            new_task = Task(task_counter, title, description)
            tasks.append(new_task)
            task_counter += 1
            flash('Task added successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Task title is required!', 'error')
    
    return render_template('add_task.html')

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    """Edit an existing task"""
    task = next((t for t in tasks if t.id == task_id), None)
    
    if not task:
        flash('Task not found!', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        
        if title:
            task.title = title
            task.description = description
            task.updated_at = datetime.now()
            flash('Task updated successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Task title is required!', 'error')
    
    return render_template('edit_task.html', task=task)

@app.route('/complete/<int:task_id>')
def toggle_complete(task_id):
    """Toggle task completion status"""
    task = next((t for t in tasks if t.id == task_id), None)
    
    if task:
        task.completed = not task.completed
        task.updated_at = datetime.now()
        status = 'completed' if task.completed else 'marked as incomplete'
        flash(f'Task {status}!', 'success')
    else:
        flash('Task not found!', 'error')
    
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Delete a task"""
    global tasks
    task = next((t for t in tasks if t.id == task_id), None)
    
    if task:
        tasks = [t for t in tasks if t.id != task_id]
        flash('Task deleted successfully!', 'success')
    else:
        flash('Task not found!', 'error')
    
    return redirect(url_for('index'))

@app.route('/clear_completed')
def clear_completed():
    """Delete all completed tasks"""
    global tasks
    completed_count = len([t for t in tasks if t.completed])
    tasks = [t for t in tasks if not t.completed]
    
    if completed_count > 0:
        flash(f'{completed_count} completed task(s) deleted!', 'success')
    else:
        flash('No completed tasks to delete!', 'info')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
        
    # Add some sample tasks for demonstration
    tasks.extend([
        Task(1, "Learn Flask", "Build a todo app with Flask framework", False),
        Task(2, "Buy groceries", "Milk, eggs, bread, and fruits", False),
        Task(3, "Exercise", "30 minutes of cardio", True)
    ])
    task_counter = 4
    
    app.run(debug=True)