import h5py as h5
import numpy as np

# Input parameters
fileName = 'master-standard.h5'
totalNumberStates = 71

# Open file
file = h5.File(fileName,'r')

# Close file
file.close()
