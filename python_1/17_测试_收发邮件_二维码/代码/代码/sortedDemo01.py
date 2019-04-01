#1.普通排序
#默认为升序排序，得到了的一个新的列表
list1 = [4,5,23,3,5,7]
result1 = sorted(list1)
print(list1)
print(result1)  #r[3, 4, 5, 5, 7, 23]

#2.按照绝对值进行排序
#默认为升序排序，排序的依据是所有元素的绝对值的大小
list2 = [4,5,-23,3,-5,7]
result2 = sorted(list2,key=abs)
print(result2)  #[3, 4, 5, -5, 7, -23]

#3.降序升序
list3 = [4,5,23,3,5,7]
result3 = sorted(list3,reverse=True)
print(result3)

#4.字符也可以实现排序
list4 = ["f","a","k","z"]
result4 = sorted(list4)
print(result4)

#5.自定义排序规则
#默认为升序排序
def myFunc(str):
    return len(str)
list5 = ["gsg","a","34535","efgg","562875678257fhjawhgj"]
result5 = sorted(list5,key=myFunc)
print(result5)






