class File:

    def __init__(self):
        self.isFile = False
        self.files = {}
        self.content = ""

root = File()
def mkdir(path):
    t = root
    if (path[0] != "/"):
        print("path mush start with '/'")
        return

    d = path.split("/")
    for i in range(1,len(d)):
        if (d[i] not in t.files):
            t.files[d[i]] = File()
        t = t.files[d[i]]

def rmdir(path):
    t = root
    if (path[0] != "/"):
        print("path mush start with '/'")
        return

    if(path != "/"): 
        d = path.split("/")
        for i in range(1,len(d)-1):
            if (d[i] not in t.files):
                print("path incorrect: no", d[i])
                return
            t = t.files.get(d[i])
        
        if(t.files[d[-1]].isFile):
            print("It is not a directory.")
        else:
            del t.files[d[-1]]
            return

    print("root can't be removed")
        

def ls(path):
    t = root

    if (path[0] != "/"):
        print("path mush start with '/'")
        return

    if(path != "/"): 
        d = path.split("/")
        for i in range(1,len(d)):
            if (d[i] not in t.files):
                print("path incorrect: no", d[i])
                return
            t = t.files.get(d[i])

    for i in t.files.keys():
        print(i)

def create(path):
    if (path[0] != "/"):
        print("path mush start with '/'")
        return

    t = root
    d = path.split("/")
    for i in range(1,len(d)-1):
        if (d[i] not in t.files):
            print("path incorrect: no", d[i])
            return
        t = t.files[d[i]]

    if (d[-1] in t.files):
        print("File already exist.")
        return
    
    t.files[d[-1]] = File()
    t = t.files[d[-1]]
    t.isFile = True

def read(path):
    if (path[0] != "/"):
        print("path mush start with '/'")
        return

    t = root
    d = path.split("/")
    for i in range(1,len(d)):
        if (d[i] not in t.files):
            print("path incorrect: no", d[i])
            return
        t = t.files[d[i]]
    
    if(t.isFile):
        if(not t.content):
            return
        else:
            print(t.content)
    else:
        print("Not a file. Can't be read")

def readline(path):
    if (path[0] != "/"):
        print("path mush start with '/'")
        return

    t = root
    d = path.split("/")
    for i in range(1,len(d)):
        if (d[i] not in t.files):
            print("path incorrect: no", d[i])
            return
        t = t.files[d[i]]
    
    if(t.isFile):
        if(not t.content):
            return
        else:
            print(t.content.split('\n')[0])
    else:
        print("Not a file. Can't be read")

def write(path, content):
    if (path[0] != "/"):
        print("path mush start with '/'")
        return

    t = root
    d = path.split("/")
    for i in range(1,len(d)):
        if (d[i] not in t.files):
            print("path incorrect: no", d[i])
            return
        t = t.files[d[i]]
    
    if(t.isFile):
        t.content = t.content + content
    else:
        print("Not a file. Can't be write")

