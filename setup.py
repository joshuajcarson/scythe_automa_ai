import setuptools

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    name='scythe_automa_ai',
    version='0.1.0',
    description='Scythe Automa Environment for AI Development',
    long_description=readme,
    author='Joshua Carson',
    author_email='joshuajcarson@gmail.com',
    url='https://github.com/joshuajcarson/scythe_automa_ai',
    license=license,
    packages=setuptools.find_packages(exclude=('tests', 'docs')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
