<div align="center">
  <h1>🎓 Attendance Management System</h1>
  <p>A modern, responsive web application for managing student attendance and performance</p>

  <div class="badges">
    <img src="https://img.shields.io/badge/Python-3.11.9%2B-blue?style=for-the-badge&logo=python"/>
    <img src="https://img.shields.io/badge/Django-5.0.7-green?style=for-the-badge&logo=django"/>
    <img src="https://img.shields.io/badge/JavaScript-ES6-yellow?style=for-the-badge&logo=javascript"/>
    <img src="https://img.shields.io/badge/CSS3-Flexbox-orange?style=for-the-badge&logo=css3"/>
    <img src="https://img.shields.io/badge/Responsive-Design-blue?style=for-the-badge&logo=responsive"/>
  </div>
</div>

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

## 🛠 Tech Stack

### Backend
- **Framework**: Django 5.0.7
- **Database**: SQLite3
- **Authentication**: Django Auth System
- **ML Libraries**: 
  - NumPy
  - Matplotlib
  - Scikit-learn

### Frontend
- **JavaScript**: ES6+
- **CSS**: Custom CSS3 with Flexbox/Grid
- **Charts**: Chart.js
- **Icons**: Boxicons

### Development Tools
- **Version Control**: Git
- **IDE**: VS Code
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
- Python 3.11.9+
- pip (Python package manager)
- Git
- Node.js (for frontend development)

### Setup Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/HrideshSubedi/AMS_Islington_Project.git .
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

4. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run Development Server**
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

## 📝 License
MIT License - see LICENSE.md
