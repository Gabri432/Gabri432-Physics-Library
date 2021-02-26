from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9"
]

setup (
    name="gabri432physicslibrary",
    version="0.0.4",
    description="A short set of Physics formulas and constants",
    long_description=open("README.txt").read() + "\n\n" + open("CHANGELOG.txt").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Gabri432/gabri432physicslibrary",
    author="Gabriele Gatti",
    author_email="gabrielegatti432@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords="physics,library,lib",
    packages=find_packages(),
    install_requires=[""]

)