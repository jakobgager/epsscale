EPS Scaling
===========


1) use epsscale script (PyX)
    may not work for all eps files (?)

2) use epsscale script (PS) or pstops directly
    problem with Bounding box
    eps2eps rasters the font!

Usage: epsscale [options...] input.eps input2.eps ...

~~~~~~~~~~~~~~
Possible options are:
  -s, --scalefactor      define the scalefactor
  -p, --ps               use the postscript scaling tool
                         instead of the PyX tool
  -r, --replace          replaces the input files instead of 
                         creating new ones (with _scale)
  -h, --help             print this help message
~~~~~~~~~~~~~~

Uses the PyX library as default scaling tool. This library
has to be available!
Download and add to python-path variable if necessary.

Depending on the eps files either PyX of PS might not work
due to some problems within the ps-code. Try the other one!
The eps2eps call in the PS option leads to a rasterized font 
representation.  
