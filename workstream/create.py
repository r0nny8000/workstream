import os




def createWorkstreamFolder(workstreams, name):
    try:
        os.mkdir(workstreams  + '/' + name)
    except FileExistsError:
        print("Workstram folder exists.")


def createSymLink(workstreams, links, name):
    try:
        os.symlink(workstreams + '/' + name, links + '/' + name)
    except FileExistsError:
        print("Link exists.")


def createReadme(workstreams, name):
    try:
        with open(workstreams + '/' + name + '/README.md', 'x', encoding="utf-8") as readme:
            readme.write(name)
            underline = '\n'
            for n in name:
                underline += '='
            readme.write(underline)
    except FileNotFoundError:
        print("Folder " + workstreams + '/' + name + " does not exist.")
    except FileExistsError:
        print("Readme file exists.")
    