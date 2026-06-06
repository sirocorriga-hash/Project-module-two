#  Splitz

**Splitz** is a lightweight and intuitive web application built with **Python (Flask)**, designed to eliminate the stress of splitting group expenses during trips. Easily add participants, track your expenses, and get an automatic, transparent summary of who owes what.

## Key Features
* **Central Dashboard:** Instant overview of the number of participants and total spending volume.
* **Dynamic Management:** Quickly add new members to your travel group.
* **Transparent Tracking:** Detailed logging of every expense, specifying who paid and who participated.
* **Automated Balance Calculation:** The integrated engine instantly determines the net debt or credit for every participant.
* **Responsive Design:** Clean, "mobile-first" interface based on **Bootstrap 5.3**.

##  Tech Stack
* **Backend:** Python 3, Flask
* **Frontend:** HTML5, CSS3, Bootstrap 5.3
* **Template Engine:** Jinja2
* **Architecture:** Simplified MVC pattern (Model-Controller-View)

##flowchart TD
    A[User opens the application] --> B[Flask Homepage]
    B --> C{User selects action}

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

  


##  Quick Start Guide

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/splitz.git](https://github.com/your-username/splitz.git)
   cd splitz

```

2. **Set up a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

```


3. **Install dependencies:**
```bash
pip install flask

```


4. **Run the application:**
```bash
python app.py

```

The app will be accessible at `http://127.0.0.1:5000` and on https://siro-flask-demo.onrender.com/

##  Project Structure

* `app.py`: Main controller handling Flask routes and interaction logic.
* `models.py`: Contains the `ExpenseManager` class and the balance calculation logic.
* `/templates/`: HTML files that compose the application views.
* `/static/`: CSS files (`style.css`) and static assets.

##  Contributing

This project is open to contributions. If you have ideas to improve the balance algorithm or want to implement persistent database support, feel free to open an *Issue* or submit a *Pull Request*.

