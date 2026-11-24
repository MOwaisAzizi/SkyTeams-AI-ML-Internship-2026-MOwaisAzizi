from setuptools import setup, find_packages

setup(
    name='text_analyzer',
    version='1.0.0',
    description='A package for analyzing word frequencies',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'matplotlib>=3.8.0'
    ]
)