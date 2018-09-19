import logging

"""
Open the file by path name and logging the operation
Param:
    pathName[String]: path of the file
    mode[String]: default is 'r'(read only).
                  some common modes: 'w'(write only), 'r+' (read and write only)
                                     'a'(append)
Return:
    [File Object]
"""
def openFile(pathName, mode='r'):
    # Setting up the logger
    logging.basicConfig(filename='os.log',level=logging.INFO)
    logging.info('Trying to OPEN file: ' + pathName)

    try:
        # Open the file by path name, default mode("r") is read only
        # More modes info: https://docs.python.org/3/library/functions.html#open
        fileObject = open(pathName, mode)
        logging.info('Open file ' + pathName + ' successfully.')
        return fileObject
    except Exception as err:
        logging.error("Can't open file " + pathName + " : " + str(err))
        print(err)


"""
Close the file and logging the operation
Param:
    fileObject[File Object]: which is return by openFile()
"""
def closeFile(fileObject):
    # Setting up the logger
    logging.basicConfig(filename='os.log',level=logging.INFO)
    logging.info('Trying to CLOSE file: ' + fileObject.name)

    try:
        fileObject.close()
        logging.info('Close file ' + fileObject.name + ' successfully.')
    except Exception as err:
        logging.error("Can't close file " + fileObject.name + " : " + str(err))
        print(err)

"""
Read the file from the given File OBject and logging the operation
Param:
    fileObject[File Object]: which is return by openFile()
Return:
    [String]: the context of the file
"""
def readFile(fileObject):
    # Setting up the logger
    logging.basicConfig(filename='os.log',level=logging.INFO)
    logging.info('Tring to READ file: ' + fileObject.name)

    try:
        context = fileObject.read()
        logging.info('Read file ' + fileObject.name + ' successfully.')
        return context
    except Exception as err:
        logging.error("Can't close file " + fileObject.name + " : " + str(err))
        print(err)


"""
Write the file by given the File Object and logging the operation
Param:
    fileObject[File Object]: which is return by openFile()
"""
def writeFile(fileObject, content):
    # Setting up the logger
    logging.basicConfig(filename='os.log',level=logging.INFO)
    logging.info('Trying to WIRTE file:' + fileObject.name)

    try:
        fileObject.write(content)
        logging.info('Wirte file: ' + fileObject.name + ' successfully.')
    except Exception as err:
        logging.error("Can't write file " + fileObject.name + " : " + str(err))
        print(err)

