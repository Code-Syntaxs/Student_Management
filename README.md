# Django Student Management System (Beta)
Welcome to the **Django Student Management System**! 🎓✨

This is a simple, yet powerful student management system developed using **Python (Django)** for educational purposes. Feel free to customize it according to your requirements.

⭐️ If you like this project, consider giving it a **STAR**! Your support is appreciated! ⭐️

---

## 🚀 Features

### 🛠️ Admin Users Can:
1. **Dashboard Overview**: View summary charts for student performance, staff performance, courses, subjects, leave applications, and more.
2. **Staff Management**: Add, update, and delete staff records.
3. **Student Management**: Add, update, and delete student records.
4. **Course Management**: Add, update, and delete courses.
5. **Subject Management**: Add, update, and delete subjects.
6. **Session Management**: Add, update, and delete academic sessions.
7. **Attendance**: View detailed attendance records for students.
8. **Feedback**: Review and reply to feedback from students and staff.
9. **Leave Applications**: Approve or reject leave requests from students and staff.

### 📚 Staff/Teachers Can:
1. **Dashboard Overview**: View summary charts for their subjects, students, and leave status.
2. **Attendance Management**: Mark and update student attendance.
3. **Results Management**: Add and update student results.
4. **Leave Applications**: Apply for leave.
5. **Feedback**: Send feedback directly to the HOD.

### 🎓 Students Can:
1. **Dashboard Overview**: View charts related to their attendance, subjects, and leave status.
2. **Attendance Records**: Check their attendance details.
3. **Results**: View their academic results.
4. **Leave Applications**: Apply for leave.
5. **Feedback**: Send feedback to the HOD.

---

## 🛠️ Installation Guide

Follow these simple steps to get started with the project:

### Step 1: Create a Project Folder
Create a folder to store the project files.

### Step 2: Set Up a Virtual Environment
Install and activate a virtual environment:

#### Install Virtual Environment
```bash
pip install virtualenv
```

#### Create Virtual Environment
- **For Windows:**
  ```bash
  python -m venv venv
  ```
- **For Mac:**
  ```bash
  python3 -m venv venv
  ```

#### Activate Virtual Environment
- **For Windows:**
  ```bash
  source venv/scripts/activate
  ```
- **For Mac:**
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies
Install the required packages using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### Step 4: Update Allowed Hosts
- Open the `settings.py` file.
- Add the following to `ALLOWED_HOSTS`:
  ```python
  ALLOWED_HOSTS = ['*']
  ```

### Step 5: Run the Server
Run the development server:
- **For Windows:**
  ```bash
  python manage.py runserver
  ```
- **For Mac:**
  ```bash
  python3 manage.py runserver
  ```

### Step 6: Create Superuser (HOD)
Create an admin account:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up the email, username, and password.

Alternatively, you can use the default credentials provided below.

---

## 🔑 Default Login Credentials

### Super Admin (HOD)
- **Email:** admin@gmail.com
- **Password:** admin

### Staff
- **Email:** staff@gmail.com
- **Password:** staff

### Student
- **Email:** student@gmail.com
- **Password:** student

---

## 📚 About the Project
This project was created while learning Django by following a tutorial series from **SuperCoders**. It is designed to help beginners understand Django's core concepts through practical implementation.

Feel free to modify and enhance the project to suit your needs. Happy coding! 😃
#   S t u d e n t _ M a n a g e m e n t  
 #   S t u d e n t _ M a n a g e m e n t  
 #   S t u d e n t _ M a n a g e m e n t  
 #   S t u d e n t _ M a n a g e m e n t  
 