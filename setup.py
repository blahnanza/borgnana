#! /usr/bin/env python

from setuptools import setup
setup(name="pyborg",
      version="1.2.0b2",
      packages=["pyborg"],
      scripts=['pyborg-reddit.py',
               'pyborg-filein.py',
               'pyborg-telnet.py',
               'pyborg-linein.py',
               'pyborg-irc.py',
               'pyborg-bigfilein.py',
               'pyborg_irc2.py',
               'pyborg_tumblr.py'],
      author="Jack Laxson",
      author_email="jackjrabbit@gmail.com",
      description="Markov chain bot for irc which generates replies to messages",
      license="GPL v2 or later",
      install_requires=["irc==14.2", "toml", "baker==1.3",
                        "arrow==0.7.0", "PyTumblr==0.0.6", "requests"],
      url="https://github.com/jrabbit/pyborg-1up/",
      classifiers=["License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
                   "Topic :: Communications :: Chat :: Internet Relay Chat",
                   "Topic :: Games/Entertainment"])
