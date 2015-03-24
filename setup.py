try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'News Bcaster',
    'author': 'Siddhant Gupta',
    'version': '0.1',
    'install_requires': ['pyaudio'],
    'packages': ['newsbcaster'],
    'scripts': [],
    'name': 'newsbcasttemplater'
}

setup(**config)