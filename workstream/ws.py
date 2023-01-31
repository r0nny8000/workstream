import fire
import os

from workstream import create as c

WORKSTREAMS = os.path.expanduser(os.getenv('WORKSTREAMS','~/Documents'))
LINKS = os.path.expanduser(os.getenv('LINKS','~/Desktop'))

def env():
    '''Shows the current environment variables used by this program.'''
    print("WORKSTREAMS: " + WORKSTREAMS)
    print("LINKS: " + LINKS)

def create(name):
    '''Creates a new Workstream.'''
    print("Prechecks...")
    if not os.path.exists(WORKSTREAMS):
        print("Folder for workstreams does not exist.")
        return

    if not os.path.exists(LINKS):
        print("Folder for symbolic links does not exist.")
        return

    print("done.")

    print("Creating a new workstream with the name " + name + "...")
    c.createWorkstreamFolder(WORKSTREAMS, name)
    c.createSymLink(WORKSTREAMS, LINKS, name)
    c.createReadme(WORKSTREAMS, name)
    print("done.")

def _main():
    fire.Fire()

if __name__ == '__main__':
    _main()
