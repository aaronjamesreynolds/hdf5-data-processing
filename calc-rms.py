import h5py as h5
import numpy as np

# Input parameters
fileName = 'master-standard.h5'
totalNumberStates = 72

# Open file
file = h5.File(fileName,'r')

# Calculate RMS power at each state
for x in range(0, totalNumberStates):
  
  # Formulate state name
  if x < 10:    
    stateName = 'STATE_000' + str(x)
  else:
    stateName = 'STATE_00' + str(x)
  print(stateName)  

# Close file
file.close()
