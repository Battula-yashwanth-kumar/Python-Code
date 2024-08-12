# JSON Standards for Javascript object Notation
# Json is a data-interchange format derived from javascript
# It is commonly used for  storing or transferingdata.
# if we convert the json string to python the resultant will be a dictionary
# The conversion is aslo known as parsing and that is the keyword we use professionally for the conversion.
# We can convert  from json to python or pyhton to json by using json.loads() or json.dumps() method
# load() --> The method is used to load data from a json file into a python dictionary
#loads() -->The method is used to load data from a json variables into a python dictionary
#dump() --> The method is used to load data from  the python dictionary to the json file
#dump() --> This method is used to load the data from  the python varibales to josn varibales

import json
data='{"var1":"amksacl","ajalcalsc":"mac,cma,cmal","cascmsa,c":"amscnacacaca"}'
print(data)
parsed=json.loads(data)
print(type(parsed))
data2={
    ",cdckdlc;d":"cnlascmlsacl;",
    "cascmmsakcsa;":["qjfklqkq","qwjdskqlqkq"],
    "cjacpcpqlscq":"acscsm;cmq''q;w"
}
jscomp=json.dumps(data2)
print(type(jscomp))
print(jscomp)