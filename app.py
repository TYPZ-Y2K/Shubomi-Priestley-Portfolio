from flask import Flask, app
from pages import pages_bp as bp
from extensions import db
import config

app = Flask(__name__)

app.config.from_pyfile("config.py")

db.init_app(app)

#--- Register Blueprints ---
app.register_blueprint(bp)

# --- config for WTForms ---
app.config['SECRET_KEY'] = config.SECRET_KEY

#--- Create database tables ---
with app.app_context():
    db.create_all()


#--- Run the app ---
if __name__ == "__main__":
    app.run(debug=False)