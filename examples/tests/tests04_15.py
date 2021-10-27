# tests04_15.py
#
# David Lampert (djlampert@gmail.com)
#
# runs the TEST04.UCI through TEST15.UCI simulations

# Import the hspf library et al.

from pyhspf import hspf

import os

if os.path.isdir('data'):

    os.chdir('data')

else:
    print('you appear to be missing the data files in the "data"')
    print('directory that are needed for this simulation')
    raise

# this is the path to the message file in PyHSPF (hspfmsg.wdm)

pyhspfdirectory = os.path.dirname(hspf.__file__)
messagepath = 'hspfmsg.wdm'

# there is really nothing to do but just run these--but if you feel creative
# and wish to contribute it would be nice if someone would pull out the results
# of these and make plots to illustrate what the simulations do.

print('')

for i in range(4, 16):

    p = 'test{:02d}.uci'.format(i)
    if os.path.isfile(p): 
        print('performing HSPF simulation {}'.format(p))
        hspf.hsppy(p, messagepath)
        print('successfully completed simulation\n')
    else:
        print('unable to locate {}, terminating'.format(p))
        raise
