import os

files = os.listdir()
# exclude .git and .gitignore and 0
files.pop(0)
files.pop(0)
files.pop(0)
ind = 1
for file in files:
    # print(f'{ind}_{file}')
    os.system(f'cp {file} 0/{ind}_{file}')
    ind+=1
