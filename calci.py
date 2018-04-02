import sys
class Test(object):
	def add(self,b,c):
		self.a=b	
		self.b=c
		print(self.a+self.b)
	def sub(self,b,c):
		self.a=b	
		self.b=c
		print(self.a-self.b)
	def mul(self,b,c):
		self.a=b	
		self.b=c
		print(self.a*self.b)
	def div(self,b,c):
		self.a=b	
		self.b=c
		if(self.a==0 or self.b==0):
			print("Value should not be Zero\n") 
			Test.d(self,b,c)
		print(self.a/self.b)
	def d(self,b,c):
		b=int(input("Enter the first number"))
		c=int(input("Enter the second number"))
		if(b==0 or c==0):
			print("Value should not be Zero in fun\n") 
			Test.d(self,b,c)
		else:
			Test.div(self,b,c)		
	
class menu(Test):
	while(1):
		print("\t\tSimple calci application\n")
		a=int(input("Enter the mode of operation\n 1)Addition 2)Subtraction 3)Multiplication 4)Division"))
		b=int(input("Enter the first number"))
		c=int(input("Enter the second number"))
		ar=Test()
		if a==1:
			
			ar.add(b,c)	
		if a==2:
			ar.sub(b,c)
		if a==3:
			ar.mul(b,c)
		if a==4:
			ar.div(b,c)
		if a>4:
			print("Wrong choice")
		ch=int(input("Do you want to continue 1.Yes 0.No"))
		if ch!=1:
			print("Wrong choice")
			exit(0)	
