import os

def load_files():
    working_dir=os.getcwd()
    pathFlag=True
    while pathFlag:
        response = input(f"Do yo want to work in {working_dir}? Y/N\n").lower()
        if response == 'n':
            while pathFlag:
                try:
                    path=input('Path you want to work in: ')
                    working_dir=path
                    pathFlag = False
                    break
                except FileNotFoundError:
                    print('This is not a correct path')
                except:
                    raise Exception('Unknown path error')
        if response == 'y':
            pathFlag = False
    print('Correct path, searching for files...')
    located_files=[]
    located_files_path=[]
    for filename in os.scandir(working_dir):
        if not os.path.isfile(filename):
            continue
        if filename.name.endswith('.xlsx'):
            located_files.append(filename.name)
            located_files_path.append(working_dir+'\\'+filename.name)

    nrOfFiles=len(located_files)
    print(f'Found {nrOfFiles} xlsx files')
    return located_files, located_files_path, working_dir
