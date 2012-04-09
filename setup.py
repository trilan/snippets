import os
import sys
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


requirements = ['Pygments', 'Jinja2']
if sys.version_info < (2, 7):
    requirements.append('argparse')


setup(
    name='snippets',
    version='0.0.dev',
    license='ISC',
    description='Code snippets repository generator',
    long_description=read('README.rst'),
    url='https://github.com/trilan/snippets',
    author='Mike Yumatov',
    author_email='mike@yumatov.org',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'snippets = snippets.__main__:run',
        ],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
