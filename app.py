from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI='postgresql://postgres:@localhost/access_mgmt',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # Initialize Plugins
    db.init_app(app)
    Migrate(app, db)

    with app.app_context():
        from access_mgmt import models
        db.create_all()

    return app
