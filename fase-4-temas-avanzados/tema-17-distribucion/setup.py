from setuptools import setup, find_packages

setup(
    name='Messages',
    version='2.0',
    description='A simple message printer',
    author='LookAndCris',
    author_email='LookAndCris@email.com',
    url='https://LookAndCris.com',
    packages=find_packages(),
    scripts=['test.py'],
    test_suite='tests',
    #install_requires=['numpy>=1.11.1', 'matplotlib>=1.5.1'] # This is for dependencies or requirements of the project
    install_requires=[paquete.strip() for paquete in open('requirements.txt').readlines()]
)
