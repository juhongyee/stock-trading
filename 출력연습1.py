#format 연습
a = 100

practice = "{}%".format(a)
print(practice)

#unpacking
a = ["unpacking",1,23,45]

a1,a2,a3,a4 = a
print(a1)
print(a2)
print(a3)
print(a4)

#dictionary
s_price_dict = {'시가': 40000,'종가': 40100,'고가':40500,'저가':39000,'거래량':1000000}

print(s_price_dict['거래량'])
print(s_price_dict)

practice_dict = {'list' : [1,2,3,4],'bool' : True}

if(practice_dict['bool']):
    print("Hi")

practice_dict['list'] = [1,2,3]
print(practice_dict['list'])
print('이주홍' in practice_dict)
print(practice_dict.keys())
print(practice_dict.values())
keys = list(practice_dict.keys())
print(keys[1][0])
