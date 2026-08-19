# My Python Learning Projects

A collection of Python projects I built while learning programming and improving my practical development skills.

I am currently learning Python through small projects and gradually working with topics such as object-oriented programming, databases, APIs, file handling, input validation and Git.

## Featured Projects

### Finance Manager

A command-line application for managing personal income and expenses.

**Technologies:** Python, SQLite

**Features:**

* Add income and expense transactions
* View saved transactions
* Edit existing transactions
* Delete transactions
* Store data in an SQLite database
* Calculate the current balance
* View monthly income and expenses
* Show monthly net balance
* Find the highest expense category
* Validate transaction amounts
* Validate dates using the `DD.MM.YYYY` format
* Check transaction IDs before editing or deleting

**What I learned:**

* Working with SQLite databases in Python
* Using SQL commands such as `SELECT`, `INSERT`, `UPDATE` and `DELETE`
* Using parameterized SQL queries
* Building CRUD functionality
* Handling invalid user input with `try` / `except`
* Working with classes and methods
* Organizing program execution with a `main()` function

File: [`finance_manager.py`](finance_manager.py)

### Exam Tracker

A command-line application for organizing and tracking school exams.

**Technologies:** Python, SQLite

**Features:**

* Add exams with subject and date
* View all saved exams
* Edit existing exams
* Delete exams
* Mark exams as done or not done
* Store exam data in an SQLite database
* Validate exam IDs before editing, deleting or changing status
* Validate dates using the `DD.MM.YYYY` format
* Prevent empty subjects

**What I learned:**

* Working with SQLite databases
* Building CRUD functionality
* Using parameterized SQL queries
* Validating user input
* Handling errors with `try` / `except`
* Working with classes and methods
* Managing application state
* Organizing program execution with a `main()` function

File: [`exam_tracker_sql.py`](exam_tracker_sql.py)

### Weather App

A command-line weather application written in Python that retrieves current weather data for a city using the OpenWeather API.

File: [`weather_app.py`](weather_app.py)

### Features

* Search for current weather by city name
* Display the city and country
* Show the local date and time for the selected city
* Display the current temperature and "feels like" temperature
* Show current weather conditions
* Display humidity and wind speed
* Search for multiple cities without restarting the program
* Validate empty user input
* Handle invalid city names
* Handle invalid API keys
* Handle connection errors and request timeouts

### Technologies

* Python
* Requests
* OpenWeather API
* JSON
* Datetime

### What I Learned

While building this project, I practiced:

* sending HTTP GET requests to an external API
* passing parameters with API requests
* working with JSON responses
* reading and using HTTP status codes
* handling exceptions with `try` and `except`
* validating user input
* working with Unix timestamps and time zones
* formatting dates, times, and numbers
* organizing a Python program into separate functions
* keeping an API key outside the main source code

### Setup

1. Make sure Python is installed.

2. Install the Requests library:

```bash
pip install requests
```

3. Copy `config.example.py` and rename the copy to `config.py`.

4. Add your OpenWeather API key to `config.py`:

```python
weather_api_key = "YOUR_API_KEY"
```

5. Run the application:

```bash
python weather_app.py
```

### Example

```text
==============================
         WEATHER APP
==============================

Enter city: Mannheim

Weather in Mannheim, DE
Date (DD-MM-YYYY): 19-08-2026
Time (HH:MM): 14:30
Temperature: 24.3 °C
Feels like: 24.6 °C
Weather: Clear sky
Humidity: 55 %
Wind speed: 3.2 m/s

Search another city? (y/n):
```

### API Key

The OpenWeather API key is stored locally in `config.py`.

The real `config.py` file is excluded from Git using `.gitignore`, so the API key is not uploaded to the repository.

A safe example configuration is provided in [`config.example.py`](config.example.py).

## Other Projects

### Contact Manager

An object-oriented contact manager with file storage.

### Password Manager

Stores account information using SQLite and encryption.

### API Practice Projects

Small projects created to practice working with APIs and JSON:

* Currency Converter
* Flight Tracker
* IP Geolocation
* NASA Photo
* News Aggregator
* Translator
* Wikipedia API

### Python Practice Projects

Projects created while learning Python fundamentals:

* Number Guessing Game
* Shopping List
* Calculator
* Bank Account

### Other Experiments

* OCR text extraction from images

## Skills Practiced

* Python fundamentals
* Variables and data types
* Conditions and loops
* Functions
* Lists and dictionaries
* Object-oriented programming
* File I/O
* SQLite
* SQL basics
* Working with APIs and JSON
* Error handling and input validation
* Image processing and OCR
* Git and GitHub

## About This Repository

This repository documents my progress while learning software development.
The projects range from small exercises to larger applications as I continue improving my Python and programming skills.