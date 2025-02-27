# coding=utf-8
import os
import sys

try:
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements

from setuptools import find_packages, setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)

BUILD = 0
VERSION = "0.3.17"
RELEASE = VERSION


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


install_reqs = parse_requirements('req.txt', session='hack')
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='oms-cms',
    version=VERSION,
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON),
    url='https://djangochannel.com',
    author='DJWOMS - Omelchenko Michael',
    author_email='djwoms@gmail.com',
    description=('A high-level Python Web CMS'),
    long_description=read('README.md'),
    license='BSD',
    packages=['oms_cms'],
    include_package_data=True,
    install_requires=reqs,
    entry_points={'console_scripts': [
        'oms-start = oms_cms.scripts.create_project:cli_create',
    ]},
    # extras_require={
    #     "bcrypt": ["bcrypt"],
    #     "argon2": ["argon2-cffi >= 16.1.0"],
    # },
    zip_safe=False,
    classifiers=[
        'Development Status :: 0.15 - Beta',
        'Environment :: Web Environment',
        'CMS :: Moses-CMS',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
        # 'Documentation': 'https://',
        'Source': 'https://github.com/DJWOMS/oms_cms',
    },
)
