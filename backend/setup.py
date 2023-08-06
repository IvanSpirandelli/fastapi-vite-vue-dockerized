"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
import setuptools
from os.path import basename, dirname, join, splitext, abspath
from glob import glob


requirements_path = join(dirname(abspath(__file__)), "requirements.txt")

with open(requirements_path) as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="backend",
    version="0.0.1",
    install_requires=requirements,
    # The project's main homepage. This particular fork extends the main project in terms of the needs of Berlin based
    # company DNL. To reach DNL write a message to info@dnl.de. In this setup file we reference the original author.
    author="Ivan Spirandelli",
    author_email="ivan@spirandelli.de",
    description="Main backend application for this project",
    packages=setuptools.find_packages("src"),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)