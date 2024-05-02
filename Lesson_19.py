import json
data = {
    'model': 'Malibu',
    'rang': 'qora',
    'yil': 2020,
    'narh': 40000
}
# data_json = json.dumps(data, indent=4)
# print(data_json)
with open('data1.json','w') as fJson:
    json.dump(data,fJson)

person = {'ism': 'Azamat', 'familya': 'Jumabayev','yil': 2004}
# person_json = json.dumps(person,indent=4)
# print(person_json)
with open('person.json', 'w') as fJson:
    json.dump(person, fJson)
