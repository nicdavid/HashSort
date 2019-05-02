'''
Developer: Nick Barnette
'''
import random
import time
import string


class List():
    def __init__(self):
        self.head = ListItem(0)
        self.tail = ListItem(0)
        self.length = 0
        
    def addItem(self, v):
        li = ListItem(v)
        if self.length == 0:
            self.head = li
        elif self.length == 1:
            self.tail = li
            self.head.setNext(li)
            self.tail.setPrev(self.head)
        else:
            li.prev = self.tail
            self.tail.next = li
            self.tail = li
        self.length += 1
            
    def getItems(self):
        a = []
        if self.length == 0:
            return a
        i = self.head
        while i:
            a.append(i.value)
            if i.next:
                i = i.next
            else:
                break
        return a
    
    def getString(self):
        s = ''
        l = self.head
        while l:
            s += str(l.value) + ', '
            l = l.next
        return s[:-2]
        
        
class ListItem():
    def __init__(self, v):
        self.prev = None
        self.next = None
        self.value = v
        
    def setNext(self, i):
        self.next = i
        
    def setPrev(self, i):
        self.prev = i
        
    def __str__(self):
        return self.value
    
    
def insertionSort(a):
    print("Insertion Sorting " + str(len(a)) + " items...")
    st = time.time()
    for i, f in enumerate(a):
        if i == 0:
            continue
        n = i
        while n >= 1:
            if a[n-1] > a[n]:
                tmp = a[n]
                a[n] = a[n-1]
                a[n-1] = tmp
                n-=1
            else:
                break
    print("--- Insertion Sort: %s seconds ---" % (time.time() - st))
    return a
                
    
# Hash Table
class HashTable():
    def __init__(self, size=260, width=4):
        self.table = [None] * size
        self.length = 0
        self.width = width
        
    
    def hash(v,w):
        if type(v) == str:
            o = 0
            for i,c in enumerate(v):
                if i == w:
                    break
                o += (ord(c)-96)*pow(26,w-i-1)//(i+1)
            return o
        else:
            return v
    
    
    def append(self, i):
        v = hash(i,self.width)
        if v >= len(self.table):
            v = len(self.table)-1
        if self.table[v] == None:
            self.table[v] = List()
        self.table[v].addItem(i)
        self.length += 1
        
    def getValues(self):
        a = []
        for i in self.table:
            if i != None:
                v = i.head
                while v:
                    a.append(v.value)
                    v = v.next
        return a
        
    def __len__(self):
        return self.length
    
    def __str__(self):
        s = '['
        for i in self.table:
            if i != None:
                s += i.getString() + ', '
        s = s[:-2]
        s += ']'
        return s    

def getSize(l):
    o = 0
    for i in range(1,l):
        o += pow(26,l)
    return o
        
    
def hashSort(h,l):
    print("Hash Sorting " + str(len(h)) + " items...")
    st = time.time()
    a = HashTable(getSize(l), l)
    for i in h:
        a.append(i)
    print("--- Hash Sort: %s seconds ---" % (time.time() - st))
    return a

def verifySort(a):
    i = 0
    out = 'Values have been sorted properly!'
    num_err = 0
    while i < len(a)-1:
        if a[i] > a[i+1]:
#             print(a[i] + ' ' + a[i+1])
            out = '[ERROR] Values have not been sorted properly!'
            num_err += 1
        i+=1
    print(out + ' [' + str(num_err) + ']')


# In[47]:

# Create a random array
total = 1000000

# It appears that when sorting using anything less than 
# five, words do not always end up in sorted order. This 
# may be a bug. It seems to change depending on how many
# values are being sorted.
max_length = 4
a = []
b = []
for i in range(0,total):
    s = ''
    for j in range(0,20):
        s += random.choice(string.ascii_letters)
    a.append(s.lower())
    n = random.randint(0, total-1)
    b.append(n)
    
l = hashSort(a,max_length)
print(str(len(a)) + ' ' + str(len(l)))
print('Verifying Hash Sort (Words)...')
verifySort(l.getValues())

# print(a)
# print(l)

print('\n\n')

l = hashSort(b,max_length)
print(str(len(b)) + ' ' + str(len(l)))
print('Verifying Hash Sort (Integers)...')
verifySort(l.getValues())

# l2 = insertionSort(a)
# print('Verifying Insertion Sort...')
# verifySort(l2)



# In[ ]:




# In[ ]:



