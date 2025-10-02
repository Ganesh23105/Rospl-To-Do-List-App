# 📝 Flask To-Do List App

A simple, elegant web-based to-do list application built with Python Flask. This app helps you stay organized and productive with an intuitive interface for managing your daily tasks.

![Flask](https://img.shields.io/badge/Flask-2.0+-blue.svg)
![Python](https://img.shields.io/badge/Python-3.7+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **📋 Task Management**: Create, edit, and delete tasks with ease
- **✅ Completion Tracking**: Mark tasks as complete or incomplete
- **📊 Progress Statistics**: View total, completed, and pending task counts
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices
- **⏰ Timestamps**: Track when tasks were created and last updated
- **🗑️ Bulk Actions**: Clear all completed tasks at once
- **💬 User Feedback**: Flash messages for all user actions
- **🎨 Modern UI**: Clean, intuitive interface with hover effects and animations

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project files**
   ```bash
   git clone <your-repo-url>
   cd flask-todo-app
   ```

2. **Install Dependencies**
   ```bash
   # You should first create a virtual environment (recommended)
   python -m venv venv
   source venv/bin/activate  # On Linux/macOS
   .\venv\Scripts\activate   # On Windows

   # Then install dependencies. If a requirements.txt file exists:
   pip install -r requirements.txt
   # Otherwise (for now):
   pip install flask
   ```

3. **Set up the project structure**
   ```
   flask-todo-app/
   ├── app.py
   ├── templates/
   │   ├── base.html
   │   ├── index.html
   │   ├── add_task.html
   │   └── edit_task.html
   └── README.md
   ```

4. **Check the Project Structure**
   The repository already contains the necessary template files in the `templates/` directory. No manual copying is required after cloning.

### Running the Application

1. **Start the Flask development server**
   ```bash
   python app.py
   ```

2. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Start managing your tasks!** 🎉

## 📖 Usage Guide

### Adding Tasks
1. Click the "➕ Add New Task" button on the main page
2. Enter a task title (required) and optional description
3. Click "💾 Add Task" to save

### Managing Tasks
- **Complete a task**: Click the "✅ Complete" button
- **Edit a task**: Click the "✏️ Edit" button to modify title/description
- **Delete a task**: Click the "🗑️ Delete" button (with confirmation)
- **Undo completion**: Click "↩️ Undo" on completed tasks

### Bulk Operations
- **Clear completed tasks**: Use "🗑️ Clear Completed" to remove all finished tasks

## 🏗️ Project Structure

```
flask-todo-app/
├── app.py                 # Main Flask application
├── templates/
│   ├── base.html         # Base template with common layout
│   ├── index.html        # Main task list page
│   ├── add_task.html     # Add new task form
│   └── edit_task.html    # Edit existing task form
└── README.md             # This file
```

## 🔧 Technical Details

### Core Components

- **Flask Framework**: Web application framework
- **Jinja2 Templates**: HTML templating engine
- **In-Memory Storage**: Tasks stored in Python lists (session-based)
- **CSS Styling**: Embedded modern CSS with gradients and animations
- **Responsive Design**: Mobile-friendly interface

### Key Classes and Functions

#### Task Class
```python
class Task:
    def __init__(self, id, title, description="", completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
```
### Key Imports
The application relies on `datetime` for timestamping and `os` (though currently unused for its main purpose) for checking directory existence.

#### Main Routes
- `/` - Display all tasks
- `/add` - Add new task (GET/POST)
- `/edit/<task_id>` - Edit existing task (GET/POST)
- `/complete/<task_id>` - Toggle task completion
- `/delete/<task_id>` - Delete a task
- `/clear_completed` - Remove all completed tasks

## 🎨 Screenshots

### Main Task List
- Clean, organized view of all tasks
- Color-coded completed vs pending tasks
- Quick action buttons for each task

### Add/Edit Forms
- Simple, intuitive form design
- Required field validation
- Cancel option to return without saving

## 🚀 Deployment Options

### Local Development
The app runs on Flask's development server by default:
```bash
python app.py
```

### Production Deployment
For production, consider:

1. **Use a production WSGI server** (Gunicorn, uWSGI)
   ```bash
   pip install gunicorn
   gunicorn -w 4 app:app
   ```

2. **Set up a reverse proxy** (Nginx, Apache)

3. **Use environment variables** for configuration
   ```python
   app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key')
   ```

## 🔄 Future Enhancements

### Database Integration
Replace in-memory storage with a persistent database:

```python
# Example with SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

### Additional Features
- **User Authentication**: Multiple user support with login/register
- **Categories/Tags**: Organize tasks by category
- **Due Dates**: Add deadline tracking with notifications
- **Priority Levels**: High, medium, low priority tasks
- **Search & Filter**: Find tasks by title, description, or status
- **Export/Import**: Backup tasks to JSON/CSV files
- **Dark Mode**: Toggle between light and dark themes
- **API Endpoints**: RESTful API for mobile app integration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Troubleshooting

### Common Issues

**Flask not found**
```bash
pip install flask
```

**Templates not loading**
- Ensure the `templates/` folder is in the same directory as `app.py`
- Check that all HTML files are properly saved in the templates folder

**Port already in use**
```bash
# Change the port in app.py
app.run(debug=True, port=5001)
```

**Flash messages not showing**
- Ensure you have a secret key set in the Flask app
- Check that the base template includes the flash message block

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the code comments in `app.py`
3. Ensure all dependencies are properly installed
4. Verify the project structure matches the requirements

## 🙏 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/) - The Python micro web framework
- Styled with modern CSS3 features and responsive design principles
- Icons used are Unicode emoji characters for universal compatibility

---

**Happy Task Managing! 🎯**