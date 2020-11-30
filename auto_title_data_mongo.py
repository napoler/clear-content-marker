# -*-coding:utf-8-*-
import os

import pymongo
client = pymongo.MongoClient("localhost", 27017)
DB = client.gpt2Write



items={}
for i, it in  enumerate(DB.content_pet.find({})):

    
    # kw=it['entity']+it['value']
    # if len(it['data'])>1:
    # print(it["title"])
    # if ("|" in it["title"] or "-" in it["title"] or "_" in it["title"] or "|" in it["title"] or "~" in it["title"] )and it["title"] not in items:
    if "|" in it["title"] or "-" in it["title"] or "_" in it["title"] or "|" in it["title"] or "~" in it["title"] :
        # print(it["title"])
        print(i)
        # if  it["title"] not in items:
        # items.append(it["title"])
        items[it["title"]]=0
print(len(items))
# items=list(set(items))
# print(len(items))
# 以写的方式打开文件，如果文件不存在，就会自动创建

# os.makedirs("data/t01")
dirnum=100
for i in range(dirnum):
    try:
        os.makedirs(f"data/{i}")
        pass
    except:
        pass
    

for n,item in enumerate( items.keys()):
    
    if n%10==0:
        fn=n%dirnum
        name=f"data/{fn}/title{n}.txt"
        f= open(name, 'w')
    n=n+1
    print("-"*20)
    print(item)
    f.writelines(item)
    f.writelines("\n")
    f.writelines("\n")


        
f.close()

# for i,resp in enumerate( scanResp):
#     qid = resp['_id']
#     print(resp)
# print(111)
#     print(resp['_source']['title'])
#     f.writelines(resp['_source']['title'])
#     f.writelines("\n")
#     f.writelines("\n")
#     if i%10==0 and i !=0:
#         name=f"data/title{i}.txt"
#         f= open(name, 'w')
# f.close()
