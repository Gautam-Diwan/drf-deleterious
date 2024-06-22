# setup.py

from setuptools import setup, find_packages

setup(
    name="drf-deleterious",
    version="0.1.0",
    packages=find_packages(),
    author="Gautam Diwan",
    author_email='gautamdiwan3@email.com',
    description="DRF Deleterious: A simple mixin package for Django REST Framework which adds Deleting Multiple requested entities in a single DELETE request",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
