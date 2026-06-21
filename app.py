from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

NAV = [
    {"id": "home", "label": "Home"},
    {"id": "about", "label": "About"},
    {"id": "education", "label": "Education"},
    {"id": "experience", "label": "Experience"},
    {"id": "skills", "label": "Skills"},
    {"id": "projects", "label": "Projects"},
    {"id": "contact", "label": "Contact"},
]

achievements = [
    {"value": "2nd", "label": "Badminton Tournament", "icon": "trophy"},
    {"value": "8.5", "label": "Current CGPA", "icon": "graduation-cap"},
    {"value": "1", "label": "Data Analytics Internship", "icon": "briefcase"},
    {"value": "5+", "label": "Skills in Progress", "icon": "award"},
]

services = [
    {"title": "Data Analytics", "description": "Data cleaning, exploration, and turning raw numbers into business insights.", "icon": "bar-chart-3"},
    {"title": "Power BI Dashboards", "description": "Interactive dashboards, KPI tracking, and business intelligence reporting.", "icon": "trending-up"},
    {"title": "SQL Data Analysis", "description": "Query optimization, data extraction, and database-driven analysis.", "icon": "database"},
    {"title": "AI & Data Science", "description": "Basic machine-learning projects and small data-driven solutions.", "icon": "brain"},
    {"title": "Web Development", "description": "Responsive websites and approachable front-end projects.", "icon": "code-2"},
    {"title": "Continuous Collaboration", "description": "Teamwork on data and tech projects with a curious, learning-first mindset.", "icon": "sparkles"},
]

skills_groups = [
    {"category": "Programming", "icon": "code-2", "items": [["Python", 80], ["Java", 70], ["C++", 65]]},
    {"category": "Data Analytics", "icon": "bar-chart-3", "items": [["SQL", 85], ["Power BI", 82], ["Excel", 88]]},
    {"category": "Web Development", "icon": "code-2", "items": [["HTML", 85], ["CSS", 78], ["JavaScript", 60]]},
    {"category": "Artificial Intelligence", "icon": "brain", "items": [["Machine Learning", 65], ["Deep Learning", 55]]},
    {"category": "Databases & Tools", "icon": "database", "items": [["MySQL", 80], ["SAP (Learning)", 50]]},
    {"category": "Professional", "icon": "sparkles", "items": [["Problem Solving", 90], ["Analytical Thinking", 88], ["Teamwork", 92]]},
]

experience_bullets = [
    "SQL for database management & querying",
    "Power BI dashboard development",
    "Data visualization techniques",
    "Business data analysis",
    "Generating actionable business insights",
    "Building HTML & CSS foundations",
]

contact_cards = [
    {"label": "Email", "value": "nandhinih08@gmail.com", "href": "mailto:nandhinih08@gmail.com", "icon": "mail"},
    {"label": "Phone", "value": "+91 6381366517", "href": "tel:+916381366517", "icon": "phone"},
    {"label": "Location", "value": "Ranipet, Tamil Nadu, India", "href": None, "icon": "map-pin"},
    {"label": "LinkedIn", "value": "/in/hema-nandhini-87390b2ba", "href": "https://www.linkedin.com/in/hema-nandhini-87390b2ba/", "icon": "linkedin"},
    {"label": "GitHub", "value": "@Hemanandhini-28", "href": "https://github.com/Hemanandhini-28", "icon": "github"},
]

@app.route("/", methods=["GET", "POST"])
def home():
    status = None
    if request.method == "POST":
        status = "sent"
    return render_template(
        "index.html",
        nav=NAV,
        achievements=achievements,
        services=services,
        skills_groups=skills_groups,
        experience_bullets=experience_bullets,
        contact_cards=contact_cards,
        status=status,
    )

if __name__ == "__main__":
    app.run(debug=True)
