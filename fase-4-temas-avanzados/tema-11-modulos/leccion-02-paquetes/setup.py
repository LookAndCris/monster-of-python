from struct import pack
from setuptools import setup

setup(
	name="Mensajes",
	version="0.1",
	description="Este es un paquete de ejemplo",
	author="LookAndCriss",
	author_email="look@gmail.com",
	url="http://lookandcriss.com",
    packages=['paquete','paquete.hola','paquete.adios'],
    scripts=['script.py']
)