import base64
import hashlib
def method1():
	l= []
	f= open ('wordlist.txt', 'rU')
	for line in f:
        	for word in line.split():
                	l.append(word)
                #print (l)
                	word=base64.b64encode(word)
                	print(word)
def method2():
	alg_data=[]
	f= open ('wordlist.txt', 'rU')
	for line in f:
        	for terms in line.split():
                	alg_data.append(terms)
                	terms= hashlib.md5(terms)
                	print (terms.hexdigest())
def method3():
	Sha_list=[]
	f=open ('wordlist.txt','rU')
	for line in f:
        	for w in line.split():
                	Sha_list.append(w)
                	w= hashlib.sha1(w)
                	print (w.hexdigest())

print("""
     ****Welcome to my Script!****
       *Let's START!!!!!!!*
        Which encryption would you like?
          1....Base64?
          2....MD5?
          3....SHA1?
          4....Quit?
           """)

# ANOTHER WAY TO EXECUTE LOOP
#	variable = input('Enter a number from the menu: ')
#	if variable <= 4 and variable >= 1 :
#		if variable == 1:
#			method1()
#		elif variable == 2:
#			method2()
#		elif variable == 3:
#			method3()
#		elif variable == 4:
#			print('You entered (4) for exiting,BYE!')
#	    		exit()
#	else:
#			print('Please print 1-4')

variable = 1
while variable != 4:
	variable = input('Enter a number from the menu: ')
	if variable == 1:
		method1()
	elif variable == 2:
		method2()
	elif variable == 3:
		method3()
	elif variable == 4:
		print('You Entered 4 for exiting, BYE!')
	else:
		print('Please Enter a valid number 1-4')
