# Portfolio Flask

This project is a Flask migration of the React portfolio from the original repository.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```

## Structure

- `app.py`: Flask application entrypoint
- `templates/`: Jinja2 HTML templates
- `static/css/style.css`: site styles
- `static/js/main.js`: frontend interactions
- `static/images/`: portfolio images
