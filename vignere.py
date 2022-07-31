import functions_vignere

print('enter input')
inp = input()
file1 = open('input.txt', 'w')
for i in inp:
    file1.write(i) 
file1.close()
print('enter keyword')
keyword = input()

functions_vignere.encrypt(keyword)
functions_vignere.decrypt(keyword)