# test02.py
#
# David Lampert (djlampert@gmail.com)
#
# runs the TEST02.UCI

# Import the hspf library and WDM utility modules

from pyhspf import hspf, WDMUtil

import os

if os.path.isdir('data'):

    os.chdir('data')

else:
    print('you appear to be missing the data files in the "data"')
    print('directory that are needed for this simulation')
    raise

if not os.path.isfile('test.wdm'):
    print('warning, this simulation assumes the test.wdm file from test01')
    print('and exists; please run this example first')
    raise

# this is the path to the message file in PyHSPF (hspfmsg.wdm)

pyhspfdirectory = os.path.dirname(hspf.__file__)
messagepath = 'hspfmsg.wdm'

# the 2nd simulation adds more data to "test.wdm," so we need to create the
# datasets as before.

wdm = WDMUtil(verbose = True, messagepath = messagepath)

wdm.open('test.wdm', 'rw')

attributes = {'TCODE ': 3,      # hourly units 
              'TSSTEP': 1,      # one unit (hourly) time step
              'TSTYPE': 'PREC', # precipitation type
              'TSFORM': 2       # precip is a total amount across the step
              }

wdm.create_dataset('test.wdm',  39, attributes)
wdm.create_dataset('test.wdm', 131, attributes)
wdm.create_dataset('test.wdm', 132, attributes)

# solar radiation -- the file aggregates the hourly to bi-hourly so TSSTEP = 2

attributes['TSTYPE'] = 'SOLR'
attributes['TSSTEP'] = 2

wdm.create_dataset('test.wdm', 46, attributes)

# air temperature -- the file aggregates the hourly to bi-hourly so TSSTEP = 2
# also the from is point-values so TSFORM = 1

attributes['TSTYPE'] = 'ATMP'
attributes['TSFORM'] = 1      

wdm.create_dataset('test.wdm', 121, attributes)
wdm.create_dataset('test.wdm', 122, attributes)
wdm.create_dataset('test.wdm', 123, attributes)

wdm.close('test.wdm')

# run it

hspf.hsppy('test02.uci', messagepath)

