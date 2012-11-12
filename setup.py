#!/usr/bin/env python2
from distutils.core import setup

setup(
    name='colorgpgletter',
    version='0.1',
    author='the_metalgamer',
    author_email='the_metalgamer@hackerspace.lu',
    packages=['colorgpgletter'],
    description='Encrypting letters',
    scripts=['bin/color-gpg-letter'],
    requires=['PIL'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Education',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'Topic :: Utilities'
    ],
    url="https://themetalgamer.dyndns.org/gitweb/cgi-bin/gitweb.cgi?p=color_gpg_letter.git;a=summary"
)
