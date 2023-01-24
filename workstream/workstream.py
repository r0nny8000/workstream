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
    return