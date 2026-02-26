from setuptools import setup, find_packages

setup(
    name="my_data_project",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "pyspark"
    ],
    entry_points={
        "console_scripts": [
            "main=src.main:main"
        ]
    }
)