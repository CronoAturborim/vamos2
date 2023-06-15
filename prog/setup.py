from setuptools import setup

readme = open("./README.md","r")
setup(

name='uispodemos',

packages=['nelsonpackage'], # this must be the same as the name above

version='0.1',

description='Esta es la descripcion de mi paquete', 
long_description=readme.read(),

long_description_content_type='text/markdown', author='Nelson Hernandez',

author_email='nelsonher019@gmail.com', 
# use the URL to the github repo

url='https://github.com/nelsonher019/nelsonpackage',

download_url='https://github.com/nelsonher019/nelson aludo/tarball/0.7',
keywords=['testing', 'logging', 'example'],

classifiers=[],

license='MIT',

include_package_data=True
)