try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'News Broadcast Templater',
    'author': 'Siddhant',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'newsbcasttemplater'
}

setup(**config)