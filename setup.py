from setuptools import setup, find_packages

setup(
    name="mappls-django",
    version="0.1.0",
    description="Mappls Map Widget for Django",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Soumay Gupta",
    author_email="pmrs9673@gmail.com",
    url="https://github.com/soumayg9673/mappls-django",
    license="MIT",
    packages=find_packages(include=["mappls_map_widget", "mappls_map_widget.*"]),
    include_package_data=True,
    install_requires=[
        "Django>=3.2",
    ],
    python_requires=">=3.7",
)