# LibNova-LMS
Library Management System using Django

LibNova-LMS is a web-based Library Management System developed as a final year BCA group project. It allows administrators to manage books and students while allowing students to view issued books and fines.

--------------------------------------------------

## Features

### Admin Module
• Admin login  
• Add new books  
• View available books  
• Issue books to students  
• View issued books with issue date and expiry date  
• Calculate fine (₹10 per day after expiry)  
• View registered students  

### Student Module
• Student signup and login  
• View issued books  
• View expiry date  
• View fine (if applicable)  

--------------------------------------------------

## Technologies Used

### Backend
• Python  
• Django Framework  

### Frontend
• HTML  
• CSS  
• Bootstrap  

### Database
• SQLite (default Django database)

### Tools Used
• VS Code  
• Git  
• GitHub  

--------------------------------------------------

## How to Run the Project

### Step 1 – Install requirements

Open terminal and run:

python -m pip install -r requirements.txt

### Step 2 – Run migrations

python manage.py makemigrations

python manage.py migrate

### Step 3 – Run server

python manage.py runserver

### Step 4 – Open browser

http://127.0.0.1:8000/

--------------------------------------------------

## Project Structure

library → Main app (models, views, forms)

librarymanagement → Project settings

templates → HTML frontend

static → Images and CSS

db.sqlite3 → Database

manage.py → Django runner

--------------------------------------------------

## Future Improvements

• Email notifications  
• Book return system  
• Search books feature  
• Password reset  
• Dashboard analytics  
• Deployment to cloud  

--------------------------------------------------

## Project Status

Completed basic LMS functionality. Further improvements planned.

--------------------------------------------------

## Developed By

Noorain Fathima  
BCA Final Year Project

--------------------------------------------------

## License

This project is for educational purposes.