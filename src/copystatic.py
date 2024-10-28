import os
import shutil

def copy_source_to_destination(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)

    entries = os.listdir(source)

    for entry in entries:
        if os.path.isfile(f'{source}/{entry}'):
            shutil.copy(f'{source}/{entry}', destination)
        else:
            copy_source_to_destination(f'{source}/{entry}', f'{destination}/{entry}')
