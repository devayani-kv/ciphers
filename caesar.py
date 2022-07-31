import functions_caesar
print ('enter input')
inp = input()
file1 = open('input.txt', 'w') 
for i in inp:
    file1.write(i) 
file1.close()
print('enter the shift value')
shift = int(input()) 

functions_caesar.encrypt(shift)
functions_caesar.decrypt(shift) 
