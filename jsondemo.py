'''json对象'''

import json

filepath = '/Users/pro/Desktop/fool.json'


data = {
    '1':'one',
    '2':'two',
    '3':'three'
}

json_str = json.dumps(data)
# print('原始数据{0}'.format(repr(json_str)))
# print(json_str)
#
with open(filepath,'w') as f:
    json.dump(data,f)

with open(filepath,'r') as f:
    data = json.load(f)
    print(data)
