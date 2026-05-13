from . import pages_bp as bp
from .forms import ContactForm
from flask import flash, render_template, request
from models import ContactMessage
from extensions import db


project_data = [
    {
        "slug": "Riget-Zoo",
        "title": "Riget Zoo Adventures",
        "description": "A full-stack tourism and booking platform.",
        "features": [
            "Ticket booking",
            "Hotel reservations",
            "User authentication",
            "Admin dashboard"
        ],
        "tech": ["Python", "Flask", "JavaScript", "SQLite"]
    },
    {
        "slug": "GibJohn",
        "title": "GibJohn Tutoring Platform",
        "description": "An interactive tutoring system.",
        "features": [
            "Login/register",
            "Dashboards",
            "Quiz tracking"
        ],
        "tech": ["Python", "Flask", "JavaScript", "SQLite"]
    },
    {
        "slug": "Rolsa-Tech",
        "title": "Rolsa Technologies",
        "description": "Green technology platform.",
        "features": [
            "Product information",
            "Consultation booking concept",
            "Carbon footprint tools",
            "Energy usage tracking concept",
            "Accessibility-focused design"
        ],
        "tech": ["Python", "Flask", "JavaScript", "SQLite"]
    },
    {
        "slug": "GLH",
        "title": "Greenfield Local Hub",
        "description": "Community marketplace platform.",
        "features": [
            "Farmers market",
            "Checkout system",
            "Customer dashboard",
            "Admin product management",
            "Stock updates",
            "Order tracking"
        ],
        "tech": ["Python", "Flask", "JavaScript", "SQLite"]
    }
]

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")

@bp.route("/projects")
def projects():
    return render_template("pages/projects.html")

@bp.route("/projects/<slug>")
def project_detail(slug):
    project = next((p for p in project_data if p["slug"] == slug), None)

    if project is None:
        return "Project not found", 404

    return render_template("pages/project-details.html", project=project)

@bp.route("/contact", methods=["GET", "POST"])
def contact():   
    form = ContactForm()

    if request.method == "POST":
        name = form.name.data
        email = form.email.data
        message = form.message.data

        if form.validate_on_submit():
            new_message = ContactMessage(
                name=name,
                email=email,
                message=message
            )

        db.session.add(new_message)
        db.session.commit()

        flash("Message sent successfully!", "success")
    return render_template("pages/contact.html", form=form)

@bp.route("/services")
def services():
    return render_template("pages/services.html") 