# #KAUN BANEGA CROREPATI 

question= [
	"How many continents are there in India?",  
	"What is the capital of India?",
	"What is the course being taught in navgurukul?"
]

option= [
	["Four", "Nine", "Seven", "Eight", "50:50"], 
	["Chandigarh", "Bhopal", "Chennai", "Delhi", "50:50"],
	["Software Engineering", "Counseling", "Tourism", "Agriculture", "50:50"]
]
solution = [3, 4, 1]
sol=[ [2, 3], [1, 4], [2, 1]]
n=0
k=1
d=0
for i in question:
	print("Your Question is : ")
	print(i)
	print("Your options are : ")
	for i in option[n]:
		if k==6:
			k=1
		print(k, i)
		k+=1
		
	inp=int(input())
	if inp==solution[n]:
		print("Congratualtions!")
	elif inp==5:
		if d==1:
			print("You aleady chose this option :) ")
			
		else:
			
			for i in range(1):
				print("option number", sol[n])
			inp=int(input())
			if inp==solution[n]:
				print("Congratualtions!")
				d+=1
		
	else:
		print("Sorry! Wrong answer!")
		print("Alas! You loosed the game, better luck next time :)")
		break
		
	n+=1