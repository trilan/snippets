from setuptools import setup, find_packages


setup(
    name='snippets',
    version='0.0.dev',
    license='ISC',
    description='Code snippets repository generator',
    url='https://github.com/trilan/snippets',
    author='Mike Yumatov',
    author_email='mike@yumatov.org',
    packages=find_packages(),
    install_requires=[
        'Pygments',
    ],
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
