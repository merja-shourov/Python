"""
    myDict.items()  > association
    myDict.keys()   > return all key
    myDict.values() > return all value

    myDict.get('key')   > return value
    myDict['key']       > return value ( if key don't find in dict then return error )

    myDict['key'] = 'value' > assign value

    # Delete key's val
    myDict.pop('key')   > value
    myDict.popitem()    > (key, val)
    del myDict['key']   > Delete key's val

    # dict copy
    newDict = myDict.copy()
    newDict = dict(myDict)

    
"""

info = {"name": "Shourov", "age": 23, "lan": "python", "sub_marks":{"cse": 80, "eee": 43, "mat": 89}}

student_list = ['akib', 'sakib', 'sifat']

std_tuple = (82, 89, 91, 133, 161)

product = {
    "Onion" : 120,
    "nut"   : 800,
    "sola"  : 80,
}
