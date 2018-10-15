import memoryFS as mfs
import sfs

print('===============================')
print('Initializing the in memoryFS......')
mfs.mkdir("/dir1")
mfs.mkdir("/dir2")
mfs.create("/dir1/test.txt")
mfs.openFile("/dir1/test.txt", 'rw')
mfs.write("/dir1/test.txt", "hello\nworld")
print('===============================')

print('Testing sfs open and read')
sfs.mountMemoryFS("/dir1")
with open('test.txt') as f:
    f.read()
print('===============================')


print('Testing sfs write')
with open('test.txt') as f:
    f.write('\ntoday is monday')
    f.read()
print('===============================')
