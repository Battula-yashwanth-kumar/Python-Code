# Pickling is the process of serializing an object.Serializing means storing the object in the form of binary representation so it can be saved in our main memory.
# The object could be of any type it could be a string, tuple, or any sort of object
# While writing the code for pickling , we open the file in "wb" mode (Writing binary mode).
# While unpickling we have to open the file in "rb" (read binary mode)
# Pickle.picklingError: if the pickle object doesnot support pickling then Pickle.PicklingError Exception is raised
# Pickle.unpicklingError:This exception will raise if the file contains bad or corrupted data.
# EOF Error: This exception will be raised if the end of the file is detected

import pickle
cars=["cmslc,;cl;w","qcmlskcl","wckskcl;sdc;"]
file="mycar.pkl"
fileobj=open(file,'wb')
pickle.dump(cars,fileobj)
fileobj.close()
 #unpickling

file ="mycar.pkl"
fileobj=open(file,'rb')
mycar=pickle.load(fileobj)
print(mycar)
print(type(mycar))
