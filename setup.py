from setuptools import setup, find_packages

setup(
    name="tmdb-cli",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "typer==0.16.0",
        "requests",
        "python-dotenv",
        # add others here
    ],
    entry_points={
        "console_scripts": [
            "tmdb = main:app",
        ],
    },
)
