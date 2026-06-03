from setuptools import find_packages, setup

setup(
    name="customer_churn_mlops",
    version="0.0.1",
    author="Pankaj",
    author_email="your_email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)