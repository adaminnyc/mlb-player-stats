from setuptools import setup, find_packages

setup(
    name="mlb-player-stats",
    version="0.1.0",
    description="A web application to view MLB player statistics",
    author="Adam Mazza",
    author_email="amazza@gmail.com",
    url="https://github.com/yourusername/mlb-player-stats",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "gradio>=3.50.0",
        "pybaseball>=2.2.0",
        "pandas",
        "numpy",
        "matplotlib",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
) 
