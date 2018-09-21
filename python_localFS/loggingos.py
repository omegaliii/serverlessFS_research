import logging
import builtins

"""
Open the file by path and logging the operation
Param:
    pathName[String]: path of the file
    mode[String]: default is 'r'(read only).
                  some common modes: 'w'(write only), 'r+' (read and write only)
                                     'a'(append)
Return:
    [File Object]
"""
def open(path, mode='r'):
    # Setting up the logger
    logging.basicConfig(filename='os.log',level=logging.INFO)
    logging.info('Trying to OPEN file: ' + path)

    try:
        # Open the file by path name, default mode("r") is read only
        # More modes info: https://docs.python.org/3/library/functions.html#open
        fileObject = builtins.open(path, mode)
        logging.info('Open file ' + path + ' successfully.')
        return LoggingosFile(fileObject)
    except Exception as err:
        logging.error("Can't open file " + path + " : " + str(err))
        print(err)

class LoggingosFile:
    def __init__(self, fileObject):
        self._f = fileObject

    """
    Close the file and logging the operation
    Param:
        fileObject[File Object]: which is return by openFile()
    """
    def close(self):
        # Setting up the logger
        logging.basicConfig(filename='os.log',level=logging.INFO)
        logging.info('Trying to CLOSE file: ' + self._f.name)

        try:
            self._f.close()
            logging.info('Close file ' + self._f.name + ' successfully.')
        except Exception as err:
            logging.error("Can't close file " + self._f.name + " : " + str(err))
            print(err)

    """
    Read the file from the given File OBject and logging the operation
    Param:
        fileObject[File Object]: which is return by openFile()
    Return:
        [String]: the context of the file
    """
    def read(self):
        # Setting up the logger
        logging.basicConfig(filename='os.log',level=logging.INFO)
        logging.info('Tring to READ file: ' + self._f.name)

        try:
            context = self._f.read()
            logging.info('Read file ' + self._f.name + ' successfully.')
            return context
        except Exception as err:
            logging.error("Can't close file " + self._f.name + " : " + str(err))
            print(err)


    """
    Write the file by given the File Object and logging the operation
    Param:
        fileObject[File Object]: which is return by openFile()
    """
    def write(self, content):
        # Setting up the logger
        logging.basicConfig(filename='os.log',level=logging.INFO)
        logging.info('Trying to WIRTE file:' + self._f.name)

        try:
            self._f.write(content)
            logging.info('Wirte file: ' + self._f.name + ' successfully.')
        except Exception as err:
            logging.error("Can't write file " + self._f.name + " : " + str(err))
            print(err)

