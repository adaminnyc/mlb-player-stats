from setuptools import setup

setup(
    name="mlb-player-stats",
    version="0.1.0",
    description="A web application to view MLB player statistics",
    author="Your Name",
    install_requires=[
        "gradio>=3.50.0",
        "pybaseball>=2.2.0",
        "pandas",
        "numpy",
        "matplotlib",
    ],
    python_requires=">=3.8",
) 