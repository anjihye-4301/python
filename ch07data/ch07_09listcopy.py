oldList=['짜장면','탕수육','짬뽕']
newList=oldList
print("oldList : ", oldList)
print("newList : ", newList)
oldList.append('깐풍기')
print("oldList : ", oldList)
print("newList : ", newList)

#별개의 새로운 리스트를 만든다.
newList = oldList.copy()
print("oldList : ", oldList)
print("newList : ", newList)
oldList.append('유산슬')
print("oldList : ", oldList)
print("newList : ", newList)

#별개로 동적 데이터 복사
newList = oldList[:]

print("oldList : ", oldList)
print("newList : ", newList)
oldList.append('유린기')
print("oldList : ", oldList)
print("newList : ", newList)


#별개로 동젝 데이터 복사
newList = []
for data in oldList:
    newList.append(data)

print("oldList : ", oldList)
print("newList : ", newList)
newList.remove('유린기')
print("oldList : ", oldList)
print("newList : ", newList)
