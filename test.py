#first time commit:
# import requests
# BASE = "http://127.0.0.1:5000/"
#
# data = [{"likes": 78, "name":"Joe", "views": 100000},
#         {"likes": 1000, "name":"Cong", "views": 80000},
#         {"likes": 35, "name":"Tim", "views": 2000},]
# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data(i))
#     print(response.json())
# input()
# response = requests.get(GET + "video/2")
# print(response.json())

import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.patch(BASE + "video/2", {"views": 99})   #this update by path.
response = requests.patch(BASE + "video/2", {})
print(response.json())