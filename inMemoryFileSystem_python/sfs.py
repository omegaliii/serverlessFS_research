import memoryFS
import builtins


fullPath = None

def mountMemoryFS(path):
    global fullPath 
    fullPath = path + "/"

def open(path, flag='rw'):
    try:
        mfsFileObject = memoryFS.openFile(fullPath + path, flag)
    except memoryFS.PathIncorrectException:
        memoryFS.create(fullPath + path)
        mfsFileObject = memoryFS.openFile(fullPath + path, flag)
    
    flagList = list(flag)
    if('b' in flagList):
        return ByteFileObjectWapper(mfsFileObject)
    return FileObjectWapper(mfsFileObject)

savedio_open = builtins.open

def replace_builtin_open():
    builtins.open = open

def reset_builtin_open():
    builtins.open = savedio_open


class FileObjectWapper:
    def __init__(self, mfsFileObject):
        self._f = mfsFileObject
        self._currentPos = 0

    def __enter__(self):
        # support with statement
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # support with statement
        self.close()

    def __iter__(self):
        pass

    def read(self, size=None):
        if(self._f.isReadable):
            if(size != None):
                endIndex = min(self._currentPos + size, len(self._f.content)) 
                chunk = self._f.content[self._currentPos : endIndex]
                self._currentPos = self._currentPos + size
                return chunk

            return self._f.content
        else:
            raise Exception("The file is not readable")

    def readline(self):
        if(self._f.isReadable):
            print(self._f.content.split('\n')[0])
        else:
            raise Exception("The file is not readable")

    def write(self, content):
        if(self._f.isWriteable):
            self._f.content += content
        else:
            raise Exception("The file is not writeable")

    def close(self):
        self._f.isOpen = False
        self._f.isReadable = False
        self._f.isWriteable = False

    def seek(self,pos,whence=0):
        if(whence==1):
            self._currentPos += pos
        if(whence==0):
            self._currentPos = pos

class ByteFileObjectWapper:
    def __init__(self, mfsFileObject):
        self._f = mfsFileObject
        if(not isinstance(self._f.content,bytearray)):
            self._f.content = bytearray()
        self._currentPos = 0

    def __enter__(self):
        # support with statement
        return self
    
    def __iter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # support with statement
        self.close()

    def read(self, size=None):
        if(self._f.isReadable):
            if(size != None):
                endIndex = min(self._currentPos + size, len(self._f.content))                    
                chunk = bytes(self._f.content)[self._currentPos : endIndex]
                self._currentPos = self._currentPos + size
                return chunk

            return bytes(self._f.content)
        else:
            raise Exception("The file is not readable")

    def write(self, content):
        if(self._f.isWriteable):
            if(not isinstance(content, bytes)):
                raise Exception("Content is not binary.")
            self._f.content.extend(content)
        else:
            raise Exception("The file is not writeable")

    def close(self):
        self._f.isOpen = False
        self._f.isReadable = False
        self._f.isWriteable = False

    def seek(self,pos,whence=0):
        if(whence==1):
            self._currentPos += pos
        if(whence==0):
            self._currentPos = pos


