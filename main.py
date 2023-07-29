import hFiles
import pandas as pd

files, paths, working = hFiles.load_files()
for sheet_nr in range(len(files)):
    df = pd.read_excel(paths[sheet_nr])
    with open(working+'\\'+files[sheet_nr][:-4]+'txt', 'w') as outfile:
        df.to_string(outfile)