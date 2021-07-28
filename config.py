import os
import click


class Config:
    ENV = os.environ["ENV"] if "ENV" in os.environ else "DEVELOPMENT"
    CSRF_ENABLED = True
    SECRET_KEY = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql-pymysql://" + os.environ["DB_USERNAME"] + ":" \
                              + os.environ["DB_PASSWORD"] + "@" \
                              + os.environ["DB_HOST"] + ":" \
                              + os.environ["DB_PORT"] + "/" \
                              + os.environ["DB_DATABASE"]

    click.echo(SQLALCHEMY_DATABASE_URI)
