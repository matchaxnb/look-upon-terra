from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Implements parse_requirements as standalone functionality
with open("requirements.txt") as f:
    reqs = [l.strip('\n') for l in f if l.strip('\n') and not l.startswith('#')]

setup(
    name='lookuponterra',
    version='0.1.25',
    python_requires='>=3.10.0',
    description='Interactive Terraform graph visualizations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Matcha',
    author_email='matchalunatic@gmail.com',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    scripts=['bin/look-upon-terra'],
    install_requires=reqs,
    include_package_data=True
)
