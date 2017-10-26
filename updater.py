
# IMPORT STUFF
from pdb import set_trace as stop
import numpy as np
import os
# END IMPORT


if __name__ ==  '__main__':
    """ """
    
    cwd = os.path.abspath(os.path.curdir)
    
    os.chdir('docs')
    os.system('make html')
    os.chdir(cwd)
    os.system('rsync -avz html/ raf@msslus:/data2/gaia/usdownloads/EuclidCaldata/FrontEnd/')


