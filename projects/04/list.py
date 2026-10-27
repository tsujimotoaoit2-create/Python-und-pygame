list1 = list(range(5)) #create a list [0,1,2,3,4]
list2 = list(range(2,6))#create a list [2,3,4,5]
list3 = list(range(2,10,3)) #create a list [2,5,8]
print(list1,list2, list3)

x = [1,2,15,30]

list_for = [2*a for a in x] #create a list [2,4,30,60]
list_for2 = [2*a for a in x if a%2 == 0] #create a list[4,60]
print(list_for, list_for2)

score = {"Alice": 80, "Bob": 80, "Charlie": 80}
score["Alice"]#Aliceの値を取得

del score["Charlie"]#"Charlie"を削除
"Alice" in score #Aliceがscoreに含まれているかどうかを確認する
