import random 
random.seed(100)
lst = [random.randint(1,100) for x in range(100)]
new_lst = []
while lst:
    lst1 = lst[0]
    for i in lst:
        if i < lst1:
            lst1 = i
    new_lst.append(lst1)
    lst.remove(lst1)

print new_lst

word = "word"
wlst = list(word)
print [ord(x) for x in wlst]
