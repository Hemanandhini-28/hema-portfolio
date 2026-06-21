from flask import Flask, render_template

app = Flask(__name__)

portfolio_items = [
    {
        "title": "Personal Portfolio Website",
        "description": "A modern responsive portfolio site built with Flask, HTML, CSS and JavaScript.",
        "link": "#portfolio"
    },
    {
        "title": "Web App Design",
        "description": "A clean interface for showcasing projects, skills, and contact details.",
        "link": "#portfolio"
    },
    {
        "title": "Interactive UI Components",
        "description": "Responsive navigation, smooth scrolling, and a mobile-friendly layout.",
        "link": "#portfolio"
    }
]

@app.route("/")
def home():
    return render_template("index.html", portfolio_items=portfolio_items)

if __name__ == "__main__":
    app.run(debug=True)
