import fire
import os

from workstream import createWorkstreamFolder
from workstream import createSymLink

HOME = os.path.expanduser('~/Documents')
LINKS = os.path.expanduser('~/Desktop')

def create(name):
    print("Prechecks...")
    if not os.path.exists(HOME):
        print("Folder for workstreams does not exist.")
        return

    if not os.path.exists(LINKS):
        print("Folder for symbolic links does not exist.")
        return

    print("done.")

    print("Creating a new workstream with the name " + name + "...")
    createWorkstreamFolder(HOME, name)
    createSymLink(HOME, LINKS, name)
    print("done.")

def _main():
    fire.Fire()

if __name__ == '__main__':
    _main()
