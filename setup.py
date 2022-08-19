from setuptools import setup

with open("READ.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

REPO_NAME = "mlflow-project-template"
AUTHOR_USER_NAME = "aibi10"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = []

setup(
    name = SRC_REPO,
    version = "0.0.1",
    author = AUTHOR_USER_NAME,
    description = "a small description for MLFlow app",
    long_description = "long_description",
    long_description_content_type = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
    author_email = "isingh.abhishek10@gmail.com",
    packages = [SRC_REPO],
    License = "MIT",
    python_requrires = ">=3.6",
    install_requires = LIST_OF_REQUIREMENTS
)