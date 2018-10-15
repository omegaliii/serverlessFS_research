import memoryFS
import builtins

root = None
fullPath = None

def mountMemoryFS(path):
    global root
    root = memoryFS.getRoot()
    global fullPath 
    fullPath = path + "/"

    if (path[0] != "/"):
        print("path mush start with '/'")
        return
    if(path == "/"):
        return

    d = path.split("/")
    for i in range(1,len(d)):
        if (d[i] not in root.files):
            print("path incorrect: no", d[i])
            return
        root = root.files[d[i]]

def open(path, flag='rw'):
   mfsFileObject = memoryFS.openFile(fullPath + path, flag)
   return FileObjectWapper(mfsFileObject)


class FileObjectWapper:
    def __init__(self, mfsFileObject):
        self._f = mfsFileObject

    def __enter__(self):
        # support with statement
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # support with statement
        self.close()

    def read(self):
        if(self._f.isReadable):
            print(self._f.content)
        else:
            print("The file is not readable")

    def readline(self):
        if(self._f.isReadable):
            print(self._f.content.split('\n')[0])
        else:
            print("The file is not readable")

    def write(self, content):
        if(self._f.isWriteable):
            self._f.content += content
        else:
            print("The file is not writeable")

    def close(self):
        self._f.isOpen = False
        self._f.isReadable = False
        self._f.isWriteable = False


savedio_open = builtins.open
builtins.open = open