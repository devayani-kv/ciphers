import string 
dict1 = {}
dict2 = {}

def assign():
    str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cnt = 0
    for i in str:
        dict1[cnt] = i
        dict2[i] = cnt
        cnt = cnt+1

def encrypt(keyword):
    n = len(keyword)
    str1 = ''
    file1 = open('input.txt', 'r')  
    file2 = open('encrypted.txt', 'w')
    while 1:
        i = file1.read(1) 
        #print('i = ', i)
        if (not i) or (i.isspace()== True):
            #print('str1 = ', str1) 
            l = len(str1)
            key = keyword
            pos=0
            while (len(key) < l):
                key = key + keyword[pos] 
                pos = (pos+1)%n 
            j =  0
            #print('key = ', key)
            while (j<l):
                #print('entered')
                #print(dict2[str1[j]])
                #print(dict2[key[j]])
                if (str1[j].isalpha() == False or key[j].isalpha()==False):
                    file2.write(str1[j]) 
                    j = j+1
                    continue 
                c = (dict2[str1[j]] + dict2[key[j]])%26 
                file2.write(dict1[c]) 
                j = j+1
            if (i.isspace() == True):
                file2.write(" ")
            elif not i:
                break
            str1 = ''
        else:
            str1 = str1 + i.upper() 
            #print('str1 ==== ', str1)
    file2.close() 
    file2 = open('encrypted.txt', 'r')
    print('encrypted text') 
    print(file2.read()) 

def decrypt(keyword):
    n = len(keyword)
    str1 = ''  
    file2 = open('encrypted.txt', 'r')
    file3 = open('decrypted.txt', 'w')
    while 1:
        i = file2.read(1) 
        #print('i = ', i)
        if (not i) or (i.isspace()== True):
            #print('str1 = ', str1) 
            l = len(str1)
            key = keyword
            pos=0
            while (len(key) < l):
                key = key + keyword[pos] 
                pos = (pos+1)%n 
            j =  0
            #print('key = ', key)
            while (j<l):
                #print('entered')
                #print(dict2[str1[j]])
                #print(dict2[key[j]])
                if (str1[j].isalpha() == False or key[j].isalpha()==False):
                    file3.write(str1[j]) 
                    j = j+1
                    continue   
                c = (dict2[str1[j]] - dict2[key[j]] + 26)%26 
                file3.write(dict1[c]) 
                j = j+1
            if (i.isspace() == True):
                file3.write(" ")
            elif not i:
                break
            str1 = ''
        else:
            str1 = str1 + i.upper() 
            #print('str1 ==== ', str1)
    file3.close() 
    file3 = open('decrypted.txt', 'r')
    print('decrypted text')
    print(file3.read()) 


assign()
