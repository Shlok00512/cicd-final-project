from setuptools import setup, find_packages

setup(
    name="accounts",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Flask==2.1.2",
        "Flask-SQLAlchemy==2.5.1",
        "gunicorn==20.1.0",
    ],
)
