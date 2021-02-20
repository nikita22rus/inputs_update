import os
import fnmatch
import pandas as pd
listOfFiles = os.listdir('.')
pattern = "future_*.zip"
date = []
inputs = pd.DataFrame()
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        date.append((entry.split('_')[-1].split('.')[0]))

inputs = pd.DataFrame({'date':date})
inputs.to_excel('inputs.xlsx')