

import json
import requests

'''stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'

jsondata = json.loads(stringOfJsonData)


file1=open('jsonfile.json','w')
json.dump(stringOfJsonData,file1)
'''
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
todostring=json.dumps(todos)

print(todos)

file1=open('jsonfile2.txt','w')
file1.write(todostring)




