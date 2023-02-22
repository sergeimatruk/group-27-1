import re

text = 'AV Analytics Vidhya AV'

result = re.match(r'.V', text)
print(result)

result = re.match(r'Analytics', text)
print(result)

result = re.search(r'.V', text)
print(result)

result = re.search(r'Analytics', text)
print(result)

result = re.findall(r'.V', text)
print(result)


result = re.split(r' ', text)
print(result)

result = re.sub(r' ', r':', text)
print(result)

with open('test_regs.txt', encoding='utf-8') as file:
    content = file.read()
    beeline_list = re.findall(r'\+996 (?:77\d|22[0-57])[0-9 ]{9}', content)
    print(f'{len(beeline_list)}: {beeline_list}')

    mega_list = re.findall(r'\+996 (?:55\d|755|99[7-950])[0-9 ]{9}', content)
    print(f'{len(mega_list)}: {mega_list}')

    o_list = re.findall(r'\+996 (?:70\d|50[0-27-945])[0-9 ]{9}', content)
    print(f'{len(o_list)}: {o_list}')