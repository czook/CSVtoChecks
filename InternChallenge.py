import csv
import config
import requests

url = "https://demo.checkbook.io/v3/check/digital"
data = []
#takes file and turns it into a list
with open('cb_checks.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter =',', quotechar='|')
    for raw in reader:
        print(raw)

# payload = "{\"recipient\": \"data[2][0]+" "+data[2][1]\",\"name\":\"Widgets Inc.\",\"amount\":5,\"description\":\"Test Check\"}"
# headers = {
#     'accept': "application/json",
#     'content-type': "application/json",
#     'authorization': "d6aa2703655f4ba2af2a56202961ca86:dXbCgzYBMibj8ZwuQMd2NXr6rtvjZ8"
#     }
# response = requests.request("POST", url, data=payload, headers=headers)
# print(response.text)
# print(response.status_code)
    