import memoryFS as mfs
import sfs
import pandas as pd
from io import StringIO

print('===============================')
print('Initializing the in memoryFS......')
mfs.mkdir("/dir1")
mfs.mkdir("/dir2")
mfs.create("/dir1/test.txt")
mfs.openFile("/dir1/test.txt")
mfs.write("/dir1/test.txt", "hello\nworld")
sfs.replace_builtin_open()
print('===============================')

print('Testing sfs open and read:')
sfs.mountMemoryFS("/dir1")
with open('test.txt') as f:
    print(f.read())
print('===============================')


print('Testing sfs write:')
with open('test.txt') as f:
    f.write('\ntoday is monday')
    print(f.read())
print('===============================')

print('Testing JSON dump and load:')

import json
inputdata = {"name":"omega", "age":66}
with open("data.json", "w") as write_file:
    json.dump(inputdata, write_file)

with open("data.json", "r") as read_file:
    outputdata = json.load(read_file)

print("Output Data: ", outputdata)
print('===============================')

print('Testing numpy save and load:')

import numpy as np
inputArray = np.array([1,2,3])
print("Input Array: ", inputArray)
with open("numpyData.npy", "wb") as np_write_file:
    np.save(np_write_file, inputArray)

with open("numpyData.npy", "rb") as np_load_file:
    outputArray = np.load(np_load_file)  

print("Output Array: ", outputArray)
print('===============================')

print('Testing panda save and load:')

input_df = pd.DataFrame({"name":['foo','bar'],"id":[1,2]})
print("Input DataFrame: ")
print(input_df)
with open("pandaDF.csv", "w") as pd_write_file:
    input_df.to_csv(pd_write_file)

with open("pandaDF.csv", "r") as pd_load_file:
    h = StringIO(pd_load_file.read())
    outputdf = pd.read_csv(h, sep=',')

print("Output DataFrame: ")
print(outputdf)
print('===============================')
