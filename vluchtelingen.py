import os

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]

def start():
	os.system("cls")
	print("Its 1995 and you live in China but suddenly u hear a loud BOOM noise")
	print("what will you do?")
	print("a: LEAVE IMMDEDIATELY!")
	print("b: Stay where u are")
	choice = input()
	if choice in answer_A:
		os.system("cls")
		option_leave()
	elif choice in answer_B:
		os.system("cls")
		print("U stayed where u were and soon the military of a unknown country stormed in your place")
		print("They shot u with their LOADED weapons. . ")
		print("YOU HAVE DIED")
		quit()
	else:
		os.system("cls")
		start()

def netherlands():
	os.system("cls")
	print("You arrived at the netherlands with the boat!!!")
	print("What will you do first?")
	print("a: Go to the government")
	print("b: Illegally stay and live there")
	choice = input()
	if choice in answer_A:
		os.system("cls")
		print("You went to the government but as u saw it didnt matter because in their eyes you're not even considered a human")
		print("YOU HAVE DIED")
		quit()
	elif choice in answer_B:
		os.system("cls")
		print("You have succesfully stayed in the netherlands for a month but did you really think they wont notice you?")
		print("YOU HAVE DIED")
		quit()
	else:
		netherlands()

def stay_in_the_helicopter():
	os.system("cls")
	print("You were too scared to those soldiers and decided to stay behind")
	print("Another troop has arrived on the scene, but it was a different kind of soldier")
	print("they were very hostile and pointed their guns at you in that exact moment you regretted not going with the previous soldiers")
	print("YOU HAVE DIED")
	quit()

def go_with_them():
	os.system("cls")
	print("As you follow them you saw a lot of other injured peopele, it was like a rescue place")
	print("As you wandered around you asked the people that were already there for more information, and as you suspected it was a safe place")
	print("The soldiers assembled everyone and asked them to get on the helicopter as u walked in you suddenly felt very sleepy from all the stress and anxiety")
	print("YOU ARRIVED IN THE NETHERLANDS, what will you do now?")
	print("a: Start to live there")
	print("b: Move to another state")
	choice = input()
	if choice in answer_A:
		start_to_live_there()
	elif choice in answer_B:
		move_to_another_state()
	else:
		go_with_them()

def start_to_live_there():
	os.system("cls")
	print("You have decided to live in the Netherlands and its amazing, you have learned a lot of the new cultures")
	print("Its not been a month and everyone has been friendly enough to help you")
	print("You thought to yourself: I have made it finally..")
	quit()

def move_to_another_state():
	os.system("cls")
	print("You have moved to the new state called the hague, it seemed like a nice city")
	print("But the youth from now are so rude, you simply gave up and moved to yet another place and ")
	quit()

def fly():
	os.system("cls")
	print("You started the engine of the plane")
	print("But to your suprise it didnt start up")
	print("A few soldies from an unknown country stormed in the helicopter")
	print("They didnt speak your language but it looked like u could follow them if u wish")
	print("a: Go with them")
	print("b: stay in the helicopter")
	choice = input()
	if choice in answer_A:
		fly()
	elif choice in answer_B:
		stay_in_the_helicopter()
	else:
		fly()

def waiting():
	os.system("cls")
	print("You waited and waited till someone actually stepped up and started the helicopter engine")
	print("Soon you were already so high up the sky")
	print("but u noticed that the helicopter driver was having some problems")
	print("The helicopter was falling down because of the decline in the engine")            
	print("YOU HAVE DIED")
	quit()

def illegal():
	os.system("cls")
	print("You stayed in america and started your NEW life there")
	print("Congratulations on your long trip, wasnt the long journey, just so worth it")
	quit()

def government():
	os.system("cls")
	print("You have succesfully stayed in America and decided to moved to the netherlands to start your NEW life here!!!")
	print("Congratulations on your long trip, wasnt the long journey, just so worth it")
	quit()

def America():
	os.system("cls")
	print("You arrived in America")
	print("What will you do first?")
	print("a: Go to the government")
	print("b: Illegaly stay here")
	choice = input()
	if choice in answer_A:
		government()
	elif choice in answer_B:
		illegal()
	else:
		os.system("cls")
		America()

def columbia():
	os.system("cls")
	print("You arrived in Columbia")
	print("They dont like refugees and therfore they have shot you along with the others")
	print("YOU HAVE DIED")
	quit()

def walking():
	os.system("cls")
	print("You walked to another town, but u saw a lot of other people")
	print("a: talk to them")
	print("b: walk faster")
	choice = input()
	if choice in answer_A:
		talk_to_them()
	elif choice in answer_B:
		walk_faster()
	else:
		walking()

def talk_to_them():
	os.system("cls")
	print("You tried to talk to them but as soon as you talked to them")
	print("You got punched, kicked and even cursed on")
	print("You looked at the sky as they left your soulless body")
	print("YOU HAVE DIED")
	quit()

def walk_faster():
	print("You reached a safe point at a nearby town")
	print("After years you decided to move to the Netherlands to start your NEW life there")


def helicopter():
	os.system("cls")
	print("You ran in the helicopter hoping there would still be some space left, as u hoped there was lots of space left")
	print("but as u look to the side none was sitting at the drivers seat")
	print("a: You wait till someone arrives with some flight experience")
	print("b: You take it on yourself and try to manage it by yourself")
	choice = input()
	if choice in answer_A:
		waiting()
	elif choice in answer_B:
		fly()
	else:
		os.system("cls")
		helicopter()

def boat():
	os.system("cls")
	print("You and the other people hurried to get on the boat but as u take quick notice that there isnt a lot of space left so u had to leave a few people behind")
	print("You think to yourself: Im glad that it wasnt me")
	print("U had to go somewhere but where do u row?")
	print("a: You row straight")
	print("b: You row left")
	print("c: You row right")
	choice = input()
	if choice in answer_A:
		netherlands()
	elif choice in answer_B:
		columbia()
	elif choice in answer_C:
		America()
	else:
		os.system("cls")
		boat()


def option_leave():
	print("As u ran u saw a lot of people struggling to even get by, kids were crying and yet you had to turn away and ran EVEN further if that means you'll survive")
	print("You arrived at a safe place with other people they suggest to flee but with which transport?")
	print("a: A boat")
	print("b: A helicopter")
	print("c: JUST walking")
	choice = input()
	if choice in answer_A:
		boat()
	elif choice in answer_B:
		helicopter()
	elif choice in answer_C:
		walking()
	else:
		option_leave()

start()
