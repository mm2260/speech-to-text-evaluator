import json


def json_to_txt(json):
    f = open("transcript2.txt", "w")
    for result in json['results']:
        f.write(result['alternatives'][0]['transcript'] + '\n')


file = ''.join(open("json").readlines())
print(json.loads(file))
json_to_txt(json.loads(file))


