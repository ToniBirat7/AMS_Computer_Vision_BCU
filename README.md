<div align="center">
  <img src="static/images/logo.png" alt="AMS Logo" width="200"/>
  <h1>🎓 Attendance Management System</h1>
  <p>A modern, responsive web application for managing student attendance and performance</p>

  <div class="badges">
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python"/>
    <img src="https://img.shields.io/badge/Django-4.2-green?style=for-the-badge&logo=django"/>
    <img src="https://img.shields.io/badge/JavaScript-ES6-yellow?style=for-the-badge&logo=javascript"/>
    <img src="https://img.shields.io/badge/CSS3-Flexbox-orange?style=for-the-badge&logo=css3"/>
    <img src="https://img.shields.io/badge/Responsive-Design-blue?style=for-the-badge&logo=responsive"/>
  </div>
</div>

## 📑 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Color Theme & Design](#-color-theme--design)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Performance Notes](#-performance-notes)
- [Contributing](#-contributing)

## ✨ Features

### Authentication & Authorization
- 🔐 Secure login system with remember me functionality
- 👥 Role-based access control (Admin, Teachers)
- 🚪 Protected routes and API endpoints

### Admin Dashboard
- 📊 Interactive dashboard with real-time statistics
- 👨‍🏫 Teacher management (Add, Edit, Delete)
- 👨‍🎓 Student management (Add, Edit, Delete)
- 📚 Course management
- 📋 Class allocation

### Student Management
- 📝 Comprehensive student profiles
- 📊 Attendance tracking and reporting
- 📈 Performance analytics
- 🤖 AI-powered grade prediction
- 📥 Downloadable reports

### Attendance System
- ✅ Mark attendance by course
- 📅 Date-wise attendance records
- 📊 Statistical analysis
- 📈 Trend visualization

### Reports & Analytics
- 📊 Interactive charts and graphs
- 📈 Attendance trends
- 🎯 Performance predictions
- 📱 Responsive data visualization

### Prediction API
```python
GET /predict-performance/<student_id>/
- Returns:
  - predicted_grade: string
  - confidence: number
  - attendance_rate: number
  - chart_image: base64
```

## 🛠 Tech Stack

### Backend
- **Framework**: Django 4.2
- **Database**: SQLite3
- **Authentication**: Django Auth System
- **API**: Django REST Framework
- **ML Libraries**: 
  - NumPy
  - Matplotlib
  - Scikit-learn

### Frontend
- **JavaScript**: ES6+
- **CSS**: Custom CSS3 with Flexbox/Grid
- **Charts**: Chart.js
- **Icons**: Boxicons
- **HTTP Client**: Fetch API

### Development Tools
- **Version Control**: Git
- **IDE**: VS Code
- **API Testing**: Postman
- **Browser Tools**: Chrome DevTools

## 🎨 Color Theme & Design

### Color Palette
```css
:root {
  /* Primary Colors */
  --primary: #003b5c;    /* Deep Blue */
  --secondary: #00a4bd;  /* Turquoise */
  --accent: #e31837;     /* Red */
  
  /* Background Colors */
  --background: #f5f7fa;  /* Light Gray */
  --white: #ffffff;
  
  /* Text Colors */
  --text-primary: #2d3748;
  --text-secondary: #4a5568;
  
  /* Status Colors */
  --error: #e53e3e;
  --success: #38a169;
}
```

### Design Philosophy
- **Modern & Clean**: Minimalist design with clear hierarchy
- **Responsive First**: Mobile-friendly layouts using CSS Grid/Flexbox
- **Consistent Spacing**: Using a 4-point grid system (0.25rem units)
- **Interactive Elements**: Smooth transitions and hover effects
- **Accessibility**: High contrast ratios and clear focus states

### Components
- **Cards**: Elevated surfaces for content grouping
- **Buttons**: Clear action hierarchy with visual feedback
- **Forms**: Clean layouts with inline validation
- **Charts**: Interactive data visualization
- **Modals**: Focused task completion
- **Tables**: Responsive data presentation

## 📁 Project Structure

```bash
attendance_system/
├── auth_app/
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── static/
│   │   ├── admin/
│   │   │   ├── admin.css
│   │   │   ├── admin.js
│   │   │   ├── student_report.css
│   │   │   ├── student_report.js
│   │   │   └── teacher_list.js
│   │   ├── css/
│   │   └── js/
│   │   └── profile_pics/
│   ├── templates/
│   │   ├── auth/
│   │   │   ├── admin.html
│   │   │   ├── login.html
│   │   │   └── student_report.html
│   │   └── base.html
│   ├── manage.py
│   └── requirements.txt
```

### Key Directories
- **auth_app/**: Core application logic and models
- **static/**: CSS, JavaScript, and other static assets
- **templates/**: HTML templates with Django template language
- **media/**: User-uploaded content
- **migrations/**: Database schema changes

### Key Files
- **models.py**: Database schema definitions
- **views.py**: Request handling and business logic
- **urls.py**: URL routing configuration
- **admin.js**: Dashboard functionality
- **student_report.js**: Student analytics features

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git
- Node.js (for frontend development)

### Setup Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/attendance_system.git
   cd attendance_system
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file in the root directory:
   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

## 💻 Usage Guide

### Admin Interface

1. **Dashboard Overview**
   - Real-time statistics
   - Quick action buttons
   - Recent activity logs

2. **Teacher Management**
   ```javascript
   // Example of teacher addition
   async function addTeacher(data) {
     const response = await fetch('/add-teacher/', {
       method: 'POST',
       body: JSON.stringify(data)
     });
     return response.json();
   }
   ```

3. **Student Management**
   - Bulk student import/export
   - Course assignment
   - Performance tracking

### Student Reports

1. **Attendance Analytics**
   - Course-wise breakdown
   - Monthly trends
   - Comparative analysis

2. **Performance Prediction**
   ```python
   # Example prediction model
   def predict_performance(attendance_data, exam_scores):
       features = prepare_features(attendance_data, exam_scores)
       return model.predict(features)
   ```

## 📈 Performance Optimization Guide

### Frontend Performance

1. **JavaScript Optimization**
   ```javascript
   // Efficient DOM manipulation
   const fragment = document.createDocumentFragment();
   students.forEach(student => {
     const element = createStudentElement(student);
     fragment.appendChild(element);
   });
   container.appendChild(fragment);
   ```

2. **CSS Best Practices**
   ```css
   /* Efficient animations */
   .card {
     transform: translateZ(0);
     will-change: transform;
     transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
   }
   ```

3. **Asset Optimization**
   - Image compression
   - CSS/JS minification
   - Lazy loading
   ```html
   <img loading="lazy" src="large-image.jpg" alt="Lazy loaded image">
   ```

### Backend Performance

1. **Database Optimization**
   ```python
   # Efficient queries
   from django.db.models import Prefetch
   
   students = Student.objects.prefetch_related(
       Prefetch('attendance_set', queryset=Attendance.objects.select_related('course'))
   ).select_related('class')
   ```

2. **Caching Implementation**
   ```python
   from django.core.cache import cache
   
   def get_student_stats(student_id):
       cache_key = f'student_stats_{student_id}'
       stats = cache.get(cache_key)
       if stats is None:
           stats = calculate_student_stats(student_id)
           cache.set(cache_key, stats, timeout=3600)
       return stats
   ```

3. **Asynchronous Processing**
   ```python
   from asgiref.sync import async_to_sync
   
   @async_to_sync
   async def generate_report(student_id):
       data = await fetch_student_data(student_id)
       report = await process_report(data)
       return report
   ```

### Security Measures

1. **API Security**
   ```python
   from django.views.decorators.http import require_http_methods
   
   @require_http_methods(["POST"])
   @csrf_protect
   def update_student(request):
       # Validation and processing
   ```

2. **Rate Limiting**
   ```python
   from django.core.cache import cache
   
   def rate_limit(request, key_prefix, limit=100, period=3600):
       cache_key = f'{key_prefix}_{request.user.id}'
       count = cache.get(cache_key, 0)
       if count >= limit:
           return True
       cache.set(cache_key, count + 1, period)
       return False
   ```

## 🔧 Maintenance & Troubleshooting

### Common Issues
1. **Database Connections**
   - Connection pool exhaustion
   - Timeout handling
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
           'CONN_MAX_AGE': 60,
           'OPTIONS': {
               'timeout': 20,
           }
       }
   }
   ```

2. **Memory Management**
   - Cache eviction policies
   - Large query pagination
   ```python
   from django.core.paginator import Paginator
   
   def get_large_dataset():
       queryset = LargeModel.objects.all()
       paginator = Paginator(queryset, 100)
       for page in paginator:
           process_batch(page.object_list)
   ```

## 📚 Contributing Guidelines

1. **Code Style**
   - Follow PEP 8 for Python
   - ESLint for JavaScript
   - Prettier for formatting

2. **Pull Request Process**
   - Create feature branch
   - Write tests
   - Update documentation
   - Submit PR with description

3. **Development Workflow**
   ```bash
   # Setup development environment
   make setup-dev
   
   # Run tests
   make test
   
   # Check code style
   make lint
   ```

## 📝 License
MIT License - see LICENSE.md
