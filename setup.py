try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import defpackage

setup(
    name='defpackage', # Name of the package ./defpackage
    version=defpackage.__version__,
    packages=['defpackage'],
    url='https://github.com/defpackage',
    author=defpackage.__author__,
    author_email='gelbander@gmail.com',
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
    description='A Sample package',
)
