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

def encrypt(shift):
    file1 = open('input.txt', 'r')  
    file2 = open('encrypted.txt', 'w') 
    while 1:
        i = file1.read(1) 
        if not i:
            break
        if (i.isalpha() ==  False):
            file2.write(i)
        else:
            a = i.upper()
            b = dict2[a]
            b = (b+shift)%26
            #print('b = ', b)
            c = dict1[b]
            file2.write(c)
    file2.close()
    print('encrypted text is')
    file2 = open('encrypted.txt', 'r')
    print(file2.read())
    file2.close()

def decrypt(shift): 
    file2 = open('encrypted.txt', 'r')
    file3 = open('decrypted.txt', 'w') 
    while 1:
        i = file2.read(1)
        if not i:
            break
        if (i.isalpha() == False):
            file3.write(i)
        else:
            a = i.upper()
            b = dict2[a]
            b = (b-shift)%26
            #print('b = ', b)
            c = dict1[b]
            file3.write(c)
    print('decrypted text is')
    file3 = open('decrypted.txt', 'r')
    print(file3.read())
    file3.close()



assign()

