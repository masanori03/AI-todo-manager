# Smart TODO CLI App

A simple command-line TODO application built with Python and Groq API.

This project allows users to create tasks and uses the Groq API to automatically assign a priority level (High, Medium, or Low) based on the task title and task description.

## Features

* Add TODO tasks from the command line
* Store tasks in json file using Python lists
* Automatic AI-based priority assignment and sorting
* Environment variable support with `.env`

## Technologies Used

* Python 3
* Groq API
* python-dotenv

## Setup & Installation

1. **Clone the repository:**

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <REPOSITORY_FOLDER>
```

2. **Install dependencies:**

```bash
pip install groq python-dotenv
``` 

3. **Configure Environment Variables:**

Create a .env file in the root directory and place your Groq API key:

```Plaintext
GROQ_API_KEY=your_actual_groq_api_key_here
```

4. **Run the application:**

```Bash
python main.py
```

## Future Improvements

* Mark tasks as completed
* Delete tasks
* Due date support
* Task filtering
* Better AI task analysis
* Build a frontend
* Connect with Database
* Deplyment
