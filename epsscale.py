#! /usr/bin/env python

import sys, os
import getopt

#default scaling tool PyX
ps = False

try:
    from pyx import *
except:
    print 'PyX Package not found, set PS tool as default.'
    ps = True


usetext="""
Usage: epsscale [options...] input.eps input2.eps ...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Possible options are:
  -s, --scalefactor      define the scalefactor
  -p, --ps               use the postscript scaling tool
                         instead of the PyX tool
  -r, --replace          replaces the input files instead of 
                         creating new ones (with _scale)
  -h, --help             print this help message

Uses the PyX library as default scaling tool. This library
has to be available (no default library of the ILSB)!
Download and add to python-path variable if necessary.

Depending on the eps files either PyX of PS might not work
due to some problems within the ps-code. Try the other one!
The eps2eps call in the PS option leads to a rasterized font 
representation.  """

############################################################
# Method definitions
############################################################

def usage():
    print usetext

def scale(file, sf, r):
    """Uses PyX functionality but may not work with all
    eps files."""

    c = canvas.canvas()
    c.insert(epsfile.epsfile(0, 0, file, scale=sf))
    c.writeEPSfile(file[:-4] + '_scaled.eps')
    if r == True:
        os.system('mv ' + file[:-4] + '_scaled.eps '+ file)

def scaleps(file, sf, r):
    """Uses the pstops scale option and a subsequent eps2eps call
    for the bounding box recomputation"""

    os.system("pstops '0@" + str(sf) + "' " + file + ' tempfile_0q03.eps')
    if r == True:
        os.system("eps2eps tempfile_0q03.eps " + file)
    else:
        os.system('eps2eps tempfile_0q03.eps ' + file[:-4] + '_scaled.eps')
    os.system('rm tempfile_0q03.eps')

############################################################
# Main program
############################################################

try:                                
    opts, args = getopt.getopt(sys.argv[1:], "hs:rp", ["help", "scalefactor=", 
        "replace", "ps"]) 
except getopt.GetoptError, err:           
    print str(err)
    usage()                          
    sys.exit(2)                     

#default scalefactor, replaceflag
sf = 1
repl = False

# use arguments
for o, a  in opts:
    # set replace flag 
    if o in ('-r','--replace'): repl = True
    # check and set scalefactor
    elif o in ('-s','--scalefactor'): 
        if a.replace('.','',1).isdigit():
            sf = float(a)
        else:
            print 'Scalefactor has to be a number!'
            usage()
            sys.exit(2)
    # help
    elif o in ('-h','--help'): 
        usage()
        sys.exit(2)
    # postscript option
    elif o in ('-p','--ps'):
        ps = True

# check arguments
if len(args)==0: 
    print "arguments not defined"
    usage()
    sys.exit(2)

# apply scaling
if ps == False:
    for arg in args:
        scale(arg, sf, repl)
else:
    for arg in args:
        scaleps(arg, sf, repl)
