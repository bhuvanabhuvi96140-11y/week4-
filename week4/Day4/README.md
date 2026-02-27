This folder contains a simple Flask application demonstrating:
1. An HTML form (`templates/form.html`) where users can submit their name and email.
2. Backend logic (`app.py`) that receives form data and stores it in a SQLite database (`data.db`).
3. A display page (`templates/display.html`) that lists all stored submissions.
```powershell
cd c:\internship.bhoomi\internshipbhoomi\internshipbhoomi\week4\Day4
py -3 -m pip install -r requirements.txt
py -3 app.py
```
The script now runs with `debug=False` so you won't see the debugger PIN, restart messages, or other development-warning output. Change it back to `debug=True` only when actively debugging.
Then open a browser and visit `http://127.0.0.1:5000/` to use the form.  After submitting, you can view all entries at `http://127.0.0.1:5000/display`.
---
Feel free to extend the form with additional fields or change the database schema as needed.