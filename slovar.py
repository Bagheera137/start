

chel={"name":"Максим","age":23,"password":"dfghj"}
b=[chel]
chel={"name":"Дима","age":41,"password":"rtyu"}
b.append(chel)
chel={"name":"Влад","age":17,"password":"cvbn"}
chel["diskwal"]=True
b.append(chel)
for i in b:
    i["age"]+=1
for i in b:
    print(i["name"],i["age"])

