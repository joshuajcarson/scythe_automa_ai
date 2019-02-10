from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='gym_scythe',
    version='0.1.0',
    description='App to build AI for Scythe',
    long_description=readme,
    author='Joshua Carson',
    author_email='joshuajcarson@gmail.com',
    url='https://github.com/joshuajcarson/gym_scythe',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)