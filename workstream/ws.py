import fire
from workstream import createFolder

def create(name):
    print("creating a new workstream with the name " + name + "...")
    createFolder(name)
    print("done.")

def _main():
    fire.Fire()

if __name__ == '__main__':
    _main()
