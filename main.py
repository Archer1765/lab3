import yaml
'''
def diagnoz(num1, num2, data):
    svyaz = data['Objects'][num1]
    simpt = data['Connection'][:][num2]
    for i in range (len(data['Connection'])):
        if (data['Connection'][i]['type'] == svyaz):
            if (data['Connection'][i]['src'] == simpt):
                print("Результат: ",data['Connection'][i]['dst'])
                return data['Connection'][i]['dst']'''



with open('bz.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

#print(data,'\n')
#print(data['Objects'],'\n')
#print(data['Connection'],'\n')
#print("длина Objects: ", len(data['Objects']),'\n')
#print("длина Connection: ", len(data['Connection']),'\n')

#objects = data['Objects']
#print(objects)
#connection = data['Connection']
#print(connection)
#print(connection[0],'\n')

#print(data['Objects'][0])
#print(data['Connection'][0]['type'])

print("Симптомы:")
j = 0
for i in data['Objects']:
    print(j,'.',i)#data['Objects'][a]
    j += 1

simpt = str(input("Введите симптом: "))
#num1 = int(input("Введите номер объекта: "))

print("Связи:")
conn = ['симптом','док','где']#conn[i]
j = 0
for i in conn:
    print(j,'.',i)
    j += 1

svyaz = str(input("Введите связь: "))
#num2 = int(input("Введите номер связи: "))

for i in range(len(data['Connection'])):
    if (simpt == data['Connection'][i]['src']):
        if (data['Connection'][i]['type'] == svyaz and data['Connection'][i]['src'] == simpt):
            print("Результат: ", data['Connection'][i]['dst'])
    if (simpt == data['Connection'][i]['dst']):
        if (data['Connection'][i]['type'] == svyaz and data['Connection'][i]['dst'] == simpt):
            print("Результат: ", data['Connection'][i]['src'])


#rezult = diagnoz(num1, num2, data)
#print(rezult)
        
