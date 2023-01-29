import os




def createWorkstreamFolder(workstreams, name):
    if os.path.exists(workstreams  + '/' + name):
        print("Workstram folder already exists.")
    else:
        os.mkdir(workstreams  + '/' + name)


def createSymLink(workstreams, links, name):
    if os.path.islink(links + '/' + name):
        print("Link already exists.")
    else:
        os.symlink(workstreams + '/' + name, links + '/' + name)


def createReadme(workstreams, name):
    try:
        with open(workstreams + '/' + name + '/README.markdown', 'x', encoding="utf-8") as readme:
            readme.write(name)
            underline = '\n'
            for n in name:
                underline += '='
            readme.write(underline)
    except FileNotFoundError:
        print("Folder " + workstreams + '/' + name + " does not exist.")
    except FileExistsError:
        print("Readme file already exists.")
    