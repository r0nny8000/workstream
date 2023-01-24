import os




def createWorkstreamFolder(home, name):
    workstream_folder = home  + '/' + name
    if os.path.exists(workstream_folder):
        print("Workstram folder already exists.")
    else:
        os.mkdir(workstream_folder)


def createSymLink(home, links, name):
    if os.path.islink(links + '/' + name):
        print("Link already exists.")
    else:
        os.symlink(home + '/' + name, links + '/' + name)
    