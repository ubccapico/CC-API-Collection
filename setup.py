# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:55:07 2018

@author: jeremyh2
"""

from setuptools import setup

try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except:
    long_description = 'Canvas API helper functions for the CAPICO group.'

setup(
  name = 'CC_API_jh2',         # How you named your package folder (MyLib)
  packages = ['CC_API_jh2'],   # Chose the same as "name"
  version = '0.11.50',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Canvas API helper functions for the CAPICO group.',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type= 'text/markdown',
  include_package_data=True,
  author = 'Jeremy H.',                   # Type in your name
  author_email = 'jeremyh2@mail.ubc.ca',      # Type in your E-Mail
  url = 'https://github.com/JeremyH011/CAPICO-Library',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/JeremyH011/CAPICO-Library/archive/v0.1.tar.gz',    # I explain this later on
  keywords = ['CAPICO', 'Canvas'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
