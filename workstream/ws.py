import fire
import os

from workstream import createWorkstreamFolder
from workstream import createSymLink
from workstream import createReadme

WORKSTREAMS = os.path.expanduser('~/Documents')
LINKS = os.path.expanduser('~/Desktop')

def create(name):
    print("Prechecks...")
    if not os.path.exists(WORKSTREAMS):
        print("Folder for workstreams does not exist.")
        return

    if not os.path.exists(LINKS):
        print("Folder for symbolic links does not exist.")
        return

    print("done.")

    print("Creating a new workstream with the name " + name + "...")
    createWorkstreamFolder(WORKSTREAMS, name)
    createSymLink(WORKSTREAMS, LINKS, name)
    createReadme(WORKSTREAMS, name)
    print("done.")

def _main():
    fire.Fire()

if __name__ == '__main__':
    _main()
