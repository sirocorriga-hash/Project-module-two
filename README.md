## Splitz
Splitz is a lightweight and intuitive web application built with Python (Flask), designed to eliminate the stress of splitting group expenses during trips. Easily add participants, track your expenses, and get an automatic, transparent summary of who owes what.

Github Repository - https://github.com/sirocorriga-hash/Project-module-two
Web service - https://siro-flask-demo.onrender.com


## Key Features
Central Dashboard: Instant overview of the number of participants and total spending volume.
Dynamic Management: Quickly add new members to your travel group.
Transparent Tracking: Detailed logging of every expense, specifying who paid and who participated.
Automated Balance Calculation: The integrated engine instantly determines the net debt or credit for every participant.
Responsive Design: Clean, "mobile-first" interface based on Bootstrap 5.3.

## Project Report – Python Application “Splitz”
Introduction
This project was developed as part of a beginner-level Python programming course and consists of a web application called “Splitz”, designed to manage and split shared expenses among multiple users. The main objective of the project was to apply in a practical and realistic context the fundamental concepts learned during the course, with particular focus on Python programming basics, object-oriented programming, and web development using the Flask framework. 
Since this is my first experience working with Python code, I have consciously chosen to maintain a very elementary approach, avoiding unnecessary complications while striving for absolute precision in how the different functionalities and technologies are interconnected. Specifically, I have focused on the integration of Bootstrap, Flask, and Jinja, bridging them seamlessly with the HTML and CSS frontend components.
The application simulates a real-life scenario in which a group of people share expenses, such as during a trip or a collective activity. It provides an automated system for tracking payments and calculating balances between participants in a transparent and efficient way.


## About this project
“Splitz” is a beginner-level web application developed as part of a Python programming course. The project is inspired by real-world expense-splitting tools and simulates a simplified system for managing shared costs among multiple users.
The main goal of this project was not to create an original product, but to gain practical experience in software development by implementing the core functionalities of a web application using Python and the Flask framework.
Through this project, I focused on learning and applying key concepts such as object-oriented programming, backend logic design, and web development fundamentals. Particular attention was given to the integration between the Flask backend, Jinja2 templating engine, and a Bootstrap-based frontend.
The application allows users to be added, expenses to be recorded, and automatically calculates balances between participants, simulating a basic shared-cost settlement system.
This project represents a first step toward understanding how full-stack web applications are structured, from routing and business logic to user interface rendering.
Future improvements could include persistent database integration, user authentication, and the development of a REST API to extend the application’s functionality and scalability.

## Problem Analysis and System Objectives
The problem addressed by the application is the management of shared expenses among multiple users, where each participant may pay for common costs on behalf of the group. Without an automated system, calculating reimbursements and balances would require manual operations that are time-consuming and prone to errors.
The main objective of the system is to fully automate this process by allowing users to register, add expenses, and instantly obtain an updated overview of debts and credits among participants. The system is designed to ensure data consistency, ease of use, and clarity in the representation of financial results.
General Architecture of the Application
The application is built using Flask, a lightweight Python web framework that enables modular and flexible web development. The architecture follows a simplified Model-View-Controller (MVC)-like approach, where data logic is separated from presentation logic.
Flask routes are responsible for handling HTTP requests and connecting the user interface with the backend logic. The core business logic is centralized in a separate module that manages users and expenses.
The project is therefore structured into three main layers: backend logic implemented in Python, data management through object-oriented programming, and presentation using HTML templates with Jinja2 and Bootstrap.


## Object-Oriented Programming and Data Structure
A fundamental part of the project is implemented using object-oriented programming principles. A class was defined to represent a single expense, encapsulating the essential information required by the system: a description of the expense, the amount, and the user who paid for it. The amount is stored as a floating-point number to allow accurate mathematical operations.
In addition, a second class acts as the main application manager. This class maintains the global state of the system through two main data structures: a list of users and a list of expenses. This approach simulates an in-memory database, which is common in educational-level projects.
The manager class provides dedicated methods for adding users and expenses, offering a centralized and simple interface for data manipulation.
Balance Calculation Logic
The core functionality of the application is the calculation of balances among participants. The system distributes each expense equally among all registered users, assuming that costs must be shared fairly.
For each expense, an individual share is computed by dividing the total amount by the number of participants. The system then updates each user’s balance: the person who paid receives a credit equal to the total amount minus their own share, while the other participants accumulate a debt equal to their share.
This mechanism provides an automatic settlement system that accurately reflects the financial situation of the group, clearly indicating who owes money and who should be reimbursed.


## Request Handling and Backend Functionality
The application uses Flask routing to manage different functionalities. Each route corresponds to a specific page or action within the system. HTTP requests are handled by distinguishing between GET and POST methods: GET requests are used to display pages, while POST requests are used to process data submitted through forms.
The process of adding users and expenses follows a standard web flow: data is collected through HTML forms, sent to the server, processed by Python logic, and then the user is redirected to an updated page. This mechanism prevents duplicate submissions and ensures a consistent user experience.
User Interface and Frontend Design
The graphical interface is built using HTML, Bootstrap, and Jinja2. Bootstrap ensures a modern, responsive, and visually consistent layout without requiring complex custom CSS.
Templates are organized using a base layout that is extended by all pages. This modular approach reduces code duplication and improves maintainability.
The application pages are designed to guide the user intuitively. The homepage introduces the system, the expenses page displays all recorded transactions, the add-expense page allows new entries, and the summary page presents final balances clearly, using visual indicators to distinguish credits and debts.



## Tech Stack
Backend: Python 3, Flask
Frontend: HTML5, CSS3, Bootstrap 5.3
Template Engine: Jinja2
Architecture: Simplified MVC pattern (Model-Controller-View)

## flowchart TD 

A[User opens the application] --> B[Flask Homepage] B --> C{User selects action}

C --> D[Add Person]
C --> E[Add Expense]
C --> F[View Expenses]
C --> G[View Summary]

D --> D1[Add Person Form]
D1 --> D2[POST /addperson]
D2 --> D3[manager.add_person]
D3 --> B

E --> E1[Add Expense Form]
E1 --> E2[POST /add]
E2 --> E3[manager.add_expense]
E3 --> B

F --> F1[GET /expenses]
F1 --> F2[Render expenses list]
F2 --> B

G --> G1[GET /summary]
G1 --> G2[manager.calculate_balances]
G2 --> G3[Render Summary Table]
G3 --> B


## The app will be accessible at http://127.0.0.1:5000 and on https://siro-flask-demo.onrender.com/

## Project Structure
app.py: Main controller handling Flask routes and interaction logic.
models.py: Contains the ExpenseManager class and the balance calculation logic.
/templates/: HTML files that compose the application views.
/static/: CSS files (style.css) and static assets.

## Contributing
This project is open to contributions. If you have ideas to improve the balance algorithm or want to implement persistent database support, feel free to open an Issue or submit a Pull Request.

## Quick Start Guide

Clone the repository:
g
it clone [https://github.com/your-username/splitz.git](https://github.com/your-username/splitz.git)

cd splitz


## **Set up a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

Install dependencies:
pip install flask
Run the application:
python app.py

