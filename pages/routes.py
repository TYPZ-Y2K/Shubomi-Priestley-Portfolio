from . import pages_bp as bp
from .forms import ContactForm
from flask import flash, render_template, request, redirect, url_for
from models import ContactMessage
from extensions import db


project_data = [
    {
        "slug": "riget-zoo",
        "title": "Riget Zoo Adventures",
        "description": "A full-stack tourism and booking platform.",
        "features": [
            "Ticket booking",
            "Hotel reservations",
            "User authentication",
            "Admin dashboard"
        ],
        "image_1": "images/projects/RZA-home.webp",
        "image_2": "images/projects/RZA-dashboard.webp",
        "screencast": "https://www.youtube.com/embed/mKC6R2cN0rA",
        "tech": ["Python", "Flask", "JavaScript", "SQLite"]
    },
    {
        "slug": "gibjohn",
        "title": "GibJohn Tutoring Platform",
        "description": "An interactive tutoring system.",
        "features": [
            "Login/register",
            "Dashboards",
            "Quiz tracking"
        ],
        "image_1": "images/projects/GibJohn-home.webp",
        "image_2": "images/projects/GibJohn-dashboard.webp",
        "screencast": "",
        "tech": ["Python", "Flask", "JavaScript", "SQLite"]
    },
    {
        "slug": "rolsa-tech",
        "title": "Rolsa Technologies",
        "description": "Green technology platform.",
        "features": [
            "Product information",
            "Consultation booking concept",
            "Carbon footprint tools",
            "Energy usage tracking concept",
            "Accessibility-focused design"
        ],
        "image_1": "images/projects/Rolsa-home.webp",
        "image_2": "images/projects/Rolsa-dashboard.webp",
        "screencast": "https://www.youtube.com/embed/DSJ5JVAUx4o",
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
    return render_template("pages/projects.html", projects=project_data)


@bp.route("/projects/<slug>")
def project_detail(slug):
    project = next((p for p in project_data if p["slug"] == slug), None)

    if project is None:
        return "Project not found", 404

    return render_template("pages/project-details.html", project=project)


@bp.route("/contact", methods=["GET", "POST"])
def contact():   
    form = ContactForm()

    if form.validate_on_submit():
        new_message = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            message=form.message.data
        )

        db.session.add(new_message)
        db.session.commit()

        flash("Message sent successfully!", "success")
        return redirect(url_for("pages.contact"))

    return render_template("pages/contact.html", form=form)


@bp.route("/services")
def services():
    return render_template("pages/services.html")


@bp.route("/messages")
def messages():
    messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()
    return render_template("pages/messages.html", messages=messages)