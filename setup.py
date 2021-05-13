from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='CombineMols',

version='1.0.0.2',

description='Easy to combine two molecules',

long_description=long_description,
long_description_content_type="text/markdown",

author='Hyunseung Kong',

author_email='antibody91@naver.com',

url='https://github.com/gumgo91',

license='MIT',

py_modules=['CombineMols'],

python_requires='>=3',

install_requires=['mendeleev'],

packages=find_packages(exclude = []),

classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

)