'''from __future__ import print_function'''
"""for i in range(4):
    print("printing")
    if i==2:
        continue
    print(i)"""

"""l=[1,4,7]
for item in l:
    pass"""


"""def greet(name):
      greet= "hello"+ " "+name
      return greet
a=greet('Aamir')
print(a)"""

'''def factorial(n):
    for i in range(10):
      """if i == 5 or i == 6:
        return 1
      else:
        return n * factorial(n-1)"""

    print(factorial(8))'''



'''class sample:
  a="Aamir"

obj=sample()
obj.a="noor"
print(sample.a)
print(obj.a)'''
 

 
'''n = int(input()) 
i=1 
while i<=n: 
  print(i,end="") 
i+=1'''
 
'''n=int(input())
for i in range(n):
     print(i+1, end ='')'''

'''n= int(input("enter a number"))
for i in range (n):
  print(i+1,end="")'''

'''for i in range(10):
    print (i,end="")'''


'''def addition(n):
    return n + n'''
    
  
# We double all numbers using map()
'''numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))'''
 

# Double all numbers using map and lambda
  
'''numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))'''


# Add two lists using map and lambda
  
'''numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))'''

# List of strings
'''l = ['sat', 'bat', 'cat', 'mat']'''
  
# map() can listify the list of strings individually
'''test = list(map(list, l))
print(test)
Output :

[['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]'''



## Hackerrank list comprehension...Question--


'''dn,arr=(input() for _ in range(2))
nums = map(int, arr.split())
a=sorted(list(set(nums)))
if(len(a)==1):
    print(a[0])
else:
    print(a[-2])'''


'''for i in range(2,len(list1)): 
    if list1[i]>max: 
        secondmax=max
        max=list1[i] 
    else: 
        if list1[i]>secondmax: 
            secondmax=list1[i] 

print(secondmax) '''

##End


 
 # nested lists question

'''d={} #1
for _ in range(int(raw_input())): #2
    Name=raw_input() #3
    Grade=float(raw_input()) #4
    d[Name]=Grade #5
v=d.values()#6
second=sorted(list(set(v)))[1] #7
second_lowest=[] #8
for key,value in d.items():  #9
    if value==second: #10
        second_lowest.append(key) #11
second_lowest.sort() #12
for name in second_lowest: #13
    print name #14'''
    


'''if __name__ == '__main__':
    a= []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([score, name])

    a.sort()
    b = [i for i in a if i[0] != a[0][0]]
    c = [j for j in b if j[0] == b[0][0]]
    
    c.sort(key=lambda x: x[1])
    for i in range(len(c)):
        print(c[i][1])'''


 
'''score_list = []
for _ in range(int(input())):
name = input()
score = float(input())
score_list.append([name, score])
second_highest = sorted(set([score for name, score in score_list]))[1]
print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))'''



## good way of it

'''l = []
second_lowest_names = []
scores = set()

for _ in range(int(input())):
    name = input()
    score = float(input())
    l.append([name, score])
    scores.add(score)
        
second_lowest = sorted(scores)[1]

for name, score in l:
    if score == second_lowest:
        second_lowest_names.append(name)

for name in sorted(second_lowest_names):
    print(name, end='\n')'''


    ## end

## Percentage  discussion question


'''print( format(sum(student_marks[query_name])/len(student_marks[query_name]), ".2f") )'''
# OTHER WAY


'''if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    
    for key, value in student_marks.items():
        if query_name == key:
            sum = 0
            count = 0
            for i in value:
                sum += i
                count += 1
            average = sum/count
            print("{:.2f}".format(average))'''


            ## OTHER WAY


'''print(format((reduce(lambda x,y:x+y,student_marks[query_name]))/len(student_marks[query_name]),'.2f'))'''


### List discussion Question


'''if __name__ == '__main__':
    N = int(input())
    result = []
    for n in range(N):
        x = input().split(" ")
        command = x[0]
        if command == 'append':
            result.append(int(x[1]))
        if command == 'print':
            print(result)
        if command == 'insert':
            result.insert(int(x[1]), int(x[2]))
        if command == 'reverse':
            result == result[::-1]
        if command == 'pop':
            result.pop()
        if command == 'sort':
            result == sorted(result)
        if command == 'remove':
            result.remove(int(x[1]))
        print(result)'''


## other

'''if __name__ == '__main__':
    N = int(input())
    
    list=[]
    for i in range(N):
        a=input().split()
        for i in range(1,len(a)):
            a[i]=int(a[i])
        if a[0]=="insert":
            list.insert(a[1],a[2])
        elif a[0]=="print":
            print(list)
        elif a[0]=="remove":
            list.remove(a[1])
        elif a[0]=="append":
            list.append(a[1])
        elif a[0]=="sort":
            list.sort()
        elif a[0]=="pop":
            list.pop()
                       
            
        elif a[0]=="reverse":
            list.reverse()'''
        
            
                       
            
     
        
        

    
    

    
    

