
# IMPORT STUFF
from pdb import set_trace as stop
import numpy as np
import os
from optparse import OptionParser
# END IMPORT



def update(broadcast=False):
    """ """
    
    cwd = os.path.abspath(os.path.curdir)
    
    os.chdir('docs')
    os.system('make html')
    os.chdir(cwd)
    if broadcast:
        os.system('rsync -avz html/ raf@msslus:/data2/gaia/usdownloads/EuclidCaldata/FrontEnd/')

    

if __name__ ==  '__main__':
    """ """
    
    parser = OptionParser()
    parser.add_option("-B","--broadcast",dest="broadcast",\
                      action='store_true',default=False,help="")
    
    (options, args) = parser.parse_args()
    
    broadcast = bool(options.broadcast)
    
    update(broadcast)
    
    