from textnode import *
import os
import shutil

def main():
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    copy_source_to_destination('static', 'public')

def copy_source_to_destination(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)

    entries = os.listdir(source)

    for entry in entries:
        if os.path.isfile(f'{source}/{entry}'):
            shutil.copy(f'{source}/{entry}', destination)
        else:
            copy_source_to_destination(f'{source}/{entry}', f'{destination}/{entry}')

if __name__ == '__main__':
    main()
