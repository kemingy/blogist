from setuptools import setup, find_packages
from os import path
from io import open


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requires = [req.strip() for req in f if req]


setup(
    name='blogist',
    version='0.0.2',
    author='keming',
    author_email='kemingy94@gmail.com',
    description="a tool to get user's blog posts from GitHub Gist",
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/kemingy/blogist',
    packages=find_packages(exclude=['examples*', 'tests*']),
    package_data={},
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=requires,
    python_requires='>=3.7',
    extras_require={},
    entry_points={
        'console_scripts': ['blogist=blogist:main'],
    },
)