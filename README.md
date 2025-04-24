# Password Strength Checker

## Description

This is a simple web application that checks the strength of a password based on the following criteria:

* Length: At least 16 characters
* Complexity: Mix of uppercase and lowercase letters, numbers, and symbols
* Uniqueness: (The application reminds the user to use unique passwords)

The application is built using Streamlit, a Python framework for creating interactive web applications.

## Features

* Password input field
* Real-time feedback on password strength
* Clear indication of whether a password is weak, medium, or strong
* User-friendly interface with descriptive messages

## How to Run the App

1.  **Prerequisites:**
    * Python 3.6 or higher
    * Streamlit (install using `pip install streamlit`)

2.  **Installation:**
    * Clone this repository (or download the code as a ZIP file).
    * Navigate to the project directory in your terminal.
    * (If you haven't already installed Streamlit) Install the required packages:
        ```bash
        pip install -r requirements.txt
        ```

3.  **Run the App:**
    * Run the following command in your terminal:
        ```bash
        streamlit run password_checker.py
        ```
        (Replace `password_checker.py` with the actual name of your Python script if it's different).

4.  **Usage:**
    * Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).
    * Enter a password in the input field.
    * The app will display the password strength and provide feedback on how to improve it.

##  Password Strength Criteria

The app uses the following criteria to evaluate password strength:

* **Strong:**
    * At least 16 characters long
    * Contains uppercase and lowercase letters
    * Contains numbers
    * Contains symbols
    * (The user is reminded to use a unique password for each account)
* **Medium:**
    * Meets some, but not all, of the strong password criteria.
* **Weak:**
    * Does not meet the minimum requirements for a strong password.

##  Disclaimer

This application is intended for educational and informational purposes only.  It is not a substitute for professional security advice.  Always use strong, unique passwords and a password manager to protect your accounts.
