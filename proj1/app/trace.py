def abc():
	dictionary={'akshat':'1','yash':'2','rahul':'3'}
	print dictionary['akshat']
	try:
		print dictionary['iot']
	except KeyError as e:
		
		raise Exception("Key Error ")
	#a=int(":")
	
def layer1():	
	abc()
def layer2():
	layer1()
try:
	layer2()
except Exception as e:
	print e

except Exception as e:
	print e

	
