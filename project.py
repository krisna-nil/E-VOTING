import time
import os
class node:
	def __init__(self,voterid,name,date_of_birth,father_name,mother_name):
		self.id=voterid
		self.name=name
		self.DOB=date_of_birth
		self.father_name=father_name
		self.mother_name=mother_name
		self.next=None
count1=0
count2=0
count3=0
count4=0
class onlinevotingsystem:
	
	
	def mainlog(self):  
		print("\n\n.......1.voter entry.........|||")
		time.sleep(1)
		print("\n\n.......2.admin panel.........|||")
		time.sleep(1)
		print("\n\n.......3.winner..............|||")
		time.sleep(1)
		print("\n\n.......4.exit.................|||")
		time.sleep(1)
		print("\n\n\n\n....... so please enter(1) for voting............")
		n=int(input())
		if(n==1):
			self.voter_entry()
		if(n==2):
			self.admin_panel()
		if(n==3):
			self.winner()
		if(n==4):
			self.exit()

	def admin_panel(self):		
		print("enter the password")
		n=int(input())
		if(n==1234):
			self.show()
		else:
			print("|||......wrong password.....|||")
	def exit(self):
			os.system("clear")
			print("you have given your vote sucessfully...........|||\n\n\n")
			print("~~~~~~~~~~~~~************T H A N K     Y O U**************~~~~~~~~~~~~~~~\n\n\n")	
		
	def show(self):
		os.system("clear")
		print("..........how many votes who get............\n")
		time.sleep(1)
		print("BJP got {} votes \n",format(count1))
		time.sleep(1)
		print("TC got {} votes \n",format(count2))
		time.sleep(1)
		print("congress got{} votes \n",format(count3)) 
		time.sleep(1)
		print("JDU  got {} votes \n",format(count4))
		time.sleep(1)
		print("enter the 1 for mainlog or 0  for the exit")
		n=int(input())
		if(n==1):
			self.mainlog()
		else:
			self.exit()
		
	def voting(self):
			global count1
			global count2
			global count3
			global count4
			os.system("clear")
			print("************...list of the condidate....******************\n\n")
			print("...........VOTER NAME            #symbol..............\n\n")
			time.sleep(1)
			print("...........1.BJP                 LOTUS FLOWER...........\n\n")
			time.sleep(1)
			print("...........2.TC                  FLOWER..................\n\n")
			time.sleep(1)			
			print("...........3.CONGRESS            HAND....................\n\n")
			time.sleep(1)
			print("...........4.JDU                 ARROW....................\n\n")
			time.sleep(1)

			print("...........so please enter your choice who you want to voted............")
			v=int(input())
			if(v==1):
				count1=count1+1
			if(v==2):
				count2=count2+1
			if(v==3):
				count3=count3+1
			if(v==4):
				count4=count4+1
			if(v!=1 and v!=2 and v!=3 and v!=4):
				print("your vote is  invlid ")
				mainlog()
			os.system("clear")
			print("if you want see the present winner enter one(1) or zero for the mainlog...")
			R=int(input())
			if(R==1):
				self.winner()
			if(R!=1):
				self.mainlog()
	def winner(self):
		if(count1>count2 and count1>count3 and  count1>count4):
			print("BJP  has got  {} votes ",format(count1))
		if(count2>count1 and  count2>count3 and count2>count4):
			print("TC has got  {} votes",format(count2))
		if(count3>count1 and count3>count2 and  count3>count4):
			print("CONGRESS has got {} votes",format(count3))
		if(count4>count1 and count4>count2 and count4>count3):
			print("JDU has got  {} votes ",format(count4))
		print(".........enter one(1) for mainlog and zero for exit.........")
		n=int(input())
		if(n==1):
			self.mainlog()
		else:
			self.exit()
	def Not_Again(self):
			os.System("clear")
			print(" you have given  your vote sucessfully\n\n\n")
			print("you can't give your vote more than one time \n\n\n")
			mainlog()
			
	def voter_entry(self):
		v1=0
		v2=0
		v3=0 
		v4=0
		os.system("clear")
		print("\n\n\n\n.....IF NATIONAL ID,YOUR NAME,BIRTH DATE,YOUR FATHER NAME AND MOTHER NAME MATCH YOU CAN GIVE VOTE OTHERWISE NOT......\n\n\n");
		time.sleep(1)
		print("enter the voter id no")
		n=int(input())
		print("enter the your name ")
		name=input()
		print("enter your date of birth")
		dob=input()
		print("enter your father name ")
		fname=input()
		print("enter your  mother name ")
		mname=input()
		voter=node(n,name,dob,fname,mname)
		if(voter.id==100001 and voter.name=="nilesh kumar" and voter.DOB=="4-06-1998" and voter.father_name=="dayanand brhamchari" and voter.mother_name=="sangita kumari"):
			v1=v1+1
			if(v1!=1):
				 self.Not_Again()
			else:
				self.voting()

		elif(voter.id==100002 and voter.name=='mohit singh' and voter.DOB=="1-03-1999" and voter.father_name=="mohan singh" and voter.mother_name=="lalita devi"):
			v2+=1
			if(v2!=1):
				self.Not_Again()
			else:
				self.voting()
		elif(voter.id==100003 and voter.name=="aruneema saha" and voter.DOB=="25-03-1998" and voter.father_name=="mahesh saw" and voter.mother_name=="lalmuni devi"):
			v3+=1
			if(v3!=1):
				self.Not_Again()
			else:
				self.voting()
		elif(voter.id==100004 and voter.name=="poonam kumari" and voter.DOB=="02-10-2002" and voter.father_name=="dayanand brahmchari" and voter.mother_name=="sangita kumari"):
			v4+=1
			if(v4!=1):
				self.Not_Again()
			else:
				self.voting()

		else:
			print("the voter id  is not  given voter in the  list")
	
		
		

if(__name__=="__main__"):
	print("~~~~~~~~~~~~*********** Welcome to Online Voting System ***********~~~~~~~~~~")
	print("                        *******************************                       \n\n\n\n")
	n=int(input(".............. please Enter(1) for logging in main log............\n"))
	if(n==1):
		obj=onlinevotingsystem()
		obj.mainlog()

	








	


 
