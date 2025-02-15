from setuptools import setup, find_packages

setup(
    name="ndt_logger",  # The package name (this is what you install via pip)
    version="1.0.0",       # Version number
    packages=find_packages(),  # Automatically find and include the package
    install_requires=[],   # List dependencies here if needed (e.g., ["requests"])
    author="Derious Vaughn",
    author_email="deriousvaughn@gmail.com",
    description="A simple module for formatting log timestamps into natural language.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/theHaruspex/NaturalDatetimeLogger//",  # GitHub repo URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version requirement
)