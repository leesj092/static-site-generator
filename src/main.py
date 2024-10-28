import os
import shutil

from copystatic import copy_source_to_destination
from gencontent import generate_pages_recursive

def main():
    print("Deleting public directory...")

    if os.path.exists('public'):
        shutil.rmtree('public')

    print("Copying static files to public directory...")
    copy_source_to_destination('static', 'public')

    print("Generating content...")
    generate_pages_recursive('content', 'template.html', 'public')

if __name__ == '__main__':
    main()
