#!/usr/bin/env python
#
# PyBorg ascii file input module
#
# Copyright (c) 2000, 2006, 2010 Tom Morton, Sebastien Dailly, Jrabbit
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
import sys
import urllib2
import pyborg

from pyborg import pyborg

class ModFileIn(object):
    """
    Module for file input. Learning from ASCII text files.
    """

    # Command list for this module
    commandlist = "FileIn Module Commands:\nNone"
    commanddict = {}

    def __init__(self, Borg, args):
        print "I knew "+`Borg.settings.num_words`+" words ("+`len(Borg.lines)`+" lines) before reading "+sys.argv[1]

        counter = 0

        data = urllib2.urlopen(args[1]).read()
        data.replace("\n", ' ')
        sentences = data.split('. ')

        for sentence in sentences:
            sentence += '.'
            buff = pyborg.filter_message(sentence, Borg)
            counter = counter + 1
            try:
                Borg.learn(buff)
            except Exception:
                pass
#                # Close database cleanly
                print "Premature termination :-("
            if counter == 1000:
                my_pyborg.save_all()
                counter = 0



        # Learn from input
        print "I know "+`Borg.settings.num_words`+" words ("+`len(Borg.lines)`+" lines) now."

    def shutdown(self):
        pass

    def start(self):
        sys.exit()

    def output(self, message, args):
        pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Specify a URL."
        sys.exit()
    # start the pyborg
    my_pyborg = pyborg.pyborg()
    ModFileIn(my_pyborg, sys.argv)
    my_pyborg.save_all()
    del my_pyborg
    print "Exiting..."
