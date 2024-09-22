from setuptools import setup, find_packages

setup(
    name='nyNotTimes',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
           'nyNotTimes=nyNotTimes.nyNotTimes:main', 
        ],
    },
    author='rh4hunnid',
    author_email='rh4@keemail.me',
    description='A script to fetch and clean HTML from a given URL.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rh4hunnid/nyNotTimes',
    license='MIT',
)
