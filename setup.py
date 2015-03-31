from distutils.core import setup

config = {
    'description': 'News Broadcasting Software for the masses',
    'author': 'Siddhant Gupta',
    'version': '0.0.1',
    'Author-email': 'ncb@ncb.com'
                    'packages': ["newsBcasterClient"],
    'install_requires': ['pyaudio'],
                        'name': 'NewsBcaster'
}

setup(**config)