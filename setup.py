import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="console_widgets",
    version="0.0.565",
    author="Borna GOjšić",
    author_email="bornagojsic@gmail.com",
    description="A simple Python package for terminal based widgets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bornagojsic/console-widgets",
    project_urls={
        "Bug Tracker": "https://github.com/bornagojsic/console-widgets/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #package_dir={"": "src"},
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)