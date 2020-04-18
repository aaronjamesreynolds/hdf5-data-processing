import h5py as h5
import numpy as np
import pandas as pd
import sys

# Input parameters
fileName = sys.argv[1]
totalNumberStates = int(sys.argv[2])
fileExt = '.h5'
paramName = 'pin_powers'

# Open file
file = h5.File(fileName+fileExt,'r')

# Initialize RMS power array
stateRMSPower = np.zeros(totalNumberStates)

# Calculate RMS power at each state
for x in range(1, totalNumberStates+1):
  
  # Formulate state name
  if x < 10:    
    stateName = 'STATE_000' + str(x)
  else:
    stateName = 'STATE_00' + str(x)

  statePinPowers = file[stateName][paramName][:]
  stateRMSPower[x-1] = np.sqrt(np.square(statePinPowers).sum()/statePinPowers.size)
  print(stateName + ": " + str(stateRMSPower[x-1]))

# Put data into pandas data frame and export as csv
csvFileName = fileName + '-rms-power.csv'
fileDataFrame = pd.DataFrame(stateRMSPower, columns = ['Core-Wide RMS Power'])
fileDataFrame.to_csv(csvFileName,index=False)

# Close file
file.close()
