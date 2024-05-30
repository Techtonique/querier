from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '0.5.0'

with open("README.md", "r") as fh:
    long_description = fh.read()

# get the dependencies and installs
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]

setup(
    name='querier',
    version=__version__,
    description='Querying data-frames',
    long_description="A query language for data frames",
    url='https://github.com/thierrymoudiki/querier',
    download_url='https://github.com/thierrymoudiki/querier/tarball/' + __version__,
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Thierry Moudiki',
    install_requires=install_requires,
    author_email='thierry.moudiki@gmail.com'
)
