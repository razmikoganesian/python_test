# The Ultimate Python Bootcamp — Progress Repository

A personal learning repository for the course **"The Ultimate Python Bootcamp: Learn by Building 50 Projects"**.

Currently completed: **~75%**  
Current progress: **Section 13 — Video 103**

---

## 📚 Course Progress

### ✅ Completed Sections

- [x] Section 1 — Introduction to Coding World with Python
- [x] Section 2 — Data types in Python
- [x] Section 3 — Conditionals in Python
- [x] Section 4 — Loops in Python | Mini Projects
- [x] Section 5 — Functions in Python
- [x] Section 6 — Comprehensions in Python
- [x] Section 7 — Generators and Decorators in Python
- [x] Section 8 — Object Oriented Programming in Python
- [x] Section 9 — File and Exception Handling in Python
- [x] Section 10 — More in Python
- [x] Section 11 — Utilities Projects
- [x] Section 12 — Data Handling Projects

---

## 🚧 Current Section

### Section 13 — Web Scraping in Python

Progress: **5 / 10 videos**

Completed:

- [x] Day 1 — Scraping Wiki Headings
- [x] Day 2 — Save Hacker News in CSV
- [x] Day 3 — Multi Page Data Scraping
- [x] Day 4 — Download Image Stream in Raw Code
- [x] Day 5 — Scrape and Download Anything with wget

Current lesson:

- ▶️ Video 103 — _Day 5 scrape and download anything with wget_

Upcoming:

- [ ] Day 6 — Generate Images with Quotes
- [ ] Day 7 — Crypto Price Tracker with Graphs
- [ ] Day 8 — Do This Task Every Hour
- [ ] Day 9 — Store and Search in SQLite DB
- [ ] Day 10 — Read PDF with PyMuPDF

---

## 🛠 Topics Covered So Far

### Python Fundamentals

- Variables and Data Types
- Conditionals
- Loops
- Functions
- Comprehensions

### Intermediate Python

- Generators
- Decorators
- OOP
- Exception Handling
- File Handling

### Practical Projects

- Utilities Automation
- CSV/Data Processing
- Web Scraping
- Image Downloading
- Working with APIs
- SQLite Basics

---

## 📁 Repository Structure

````bash
.
├── basics/
├── functions/
├── oop/
├── file_handling/
├── mini_projects/
├── utilities/
├── data_handling/
├── web_scraping/
└── README.md


# 🎯 Goal

The main goal of this repository is to complete all **50 projects** from the course:

> **The Ultimate Python Bootcamp: Learn by Building 50 Projects**

This repository documents my learning journey while building real Python projects and improving practical programming skills.

The focus is on:

- writing clean and readable Python code
- learning by building real projects
- improving problem-solving abilities
- understanding practical Python development
- gaining hands-on experience with automation, web scraping, data handling, and more

---

# 🚀 Technologies & Libraries

The following technologies and libraries are used throughout the course and projects:

## Core Language

- Python 3

---

## Libraries & Tools

### `requests`
Used for making HTTP requests and working with APIs/web pages.

### `beautifulsoup4`
Used for parsing HTML and performing web scraping tasks.

### `csv`
Built-in Python module for reading and writing CSV files.

### `sqlite3`
Built-in lightweight SQL database for storing and querying data.

### `wget`
Used for downloading files directly from the internet.

### `PyMuPDF`
Library for reading and processing PDF documents.

---

# 📌 Repository Purpose

This repository is used for:

- practicing Python consistently
- tracking course progress
- storing daily coding exercises
- building mini-projects
- experimenting with new Python concepts
- improving debugging and problem-solving skills
- documenting the learning journey

---

# 📈 Current Status

## Progress

```text
███████████████░░░░ 75%
````

### Current Position

- ✅ Sections 1–12 completed
- 🚧 Currently working on:
  - Section 13 — Web Scraping in Python
  - Video 103

---

# 🔥 Learning Journey

Every section in this repository represents practical progress in Python development.

Topics covered so far include:

- Python fundamentals
- Functions and OOP
- File handling
- Decorators and generators
- Web scraping
- Data processing
- SQLite databases
- Automation scripts
- Mini utility projects

---

# 🚀 Status

Still learning.  
Still building.  
Still improving 🚀

# ⚙️ Environment Setup

This project uses a Python virtual environment to manage dependencies and keep the development environment isolated.

---

## 📁 Create Project Folder

```bash
mkdir my_project
cd my_project
```

---

# 🐍 Create Virtual Environment

A virtual environment helps keep project dependencies separate from the global Python installation.

## Option 1 — Recommended (`.venv`)

Create virtual environment:

```bash
python3 -m venv .venv
```

Activate environment:

```bash
source .venv/bin/activate
```

---

## Option 2 — Standard (`venv`)

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
source venv/bin/activate
```

---

# 📦 Install Dependencies

Install all required packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

# 🔄 Virtual Environment Commands

## Activate Environment

If you are using `.venv`:

```bash
source .venv/bin/activate
```

If you are using `venv`:

```bash
source venv/bin/activate
```

---

## Deactivate Environment

To exit the virtual environment:

```bash
deactivate
```

---

# 📋 pip Commands

## Show Installed Packages

```bash
pip freeze
```

Displays all installed dependencies inside the current virtual environment.

---

## Save Dependencies

```bash
pip freeze > requirements.txt
```

Creates or updates the `requirements.txt` file with all installed packages.

---

# 🗂 Recommended Project Structure

```bash
project/
├── .venv/
├── src/
├── requirements.txt
└── README.md
```

---

# 💡 Notes

- Always activate the virtual environment before working on the project.
- Keep `requirements.txt` updated when installing new packages.
- Do not upload the virtual environment folder (`venv/` or `.venv/`) to GitHub.

Example `.gitignore`:

```gitignore
venv/
.venv/
__pycache__/
*.pyc
```
