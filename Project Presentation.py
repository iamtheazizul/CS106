from time import sleep

def fanChecker():
    if trueFan == "y":
        sleep(1.5)
        print("Did you know people's trait change as they grow up? Let's check your house again")
        sleep(2)
        print("But first.. A quick recap for you")
        sleep(1.5)
        house_details()
        trueFan_initial = input("What is your Hogwarts house?: ")
    elif trueFan == "n":
        house_details()
        trueFan_initial = input("\nBased on these traits, what do you think is your Hogwarts house?: ")
    sleep(1.0)
    print("Let's start the quiz.")
    sleep(2.5)
    print("\nThe quiz begins in")
    sleep(1.5)
    print("3...")
    sleep(1.5)
    print("2.....")
    sleep(1.5)
    print("1......")
    return trueFan_initial

def house_details():
    sleep(1.5)
    print("Story time!")
    sleep(1.50)
    print("Hogwarts has 4 houses in total")
    sleep(1.50)
    print("Hufflepuff is the house of Hardworking, Diligent & Kind")
    sleep(3.50)
    print("Slytherin is the house of Smart, Driven & Ambitious")
    sleep(3.50)
    print("Gryffindor is the house of Brave, Loyal & Courageous")
    sleep(3.50)
    print("Ravenclaw is the house of Intellingent, Clever & Smart")
    sleep(3.50)

def question_one():
    print("------------------------------------*")
    print("What is your idea of a perfect vacation?")
    print("a) Taking up an interactive or skill-based course")
    print("b) Join the local charity organization")
    print("c) Watch movies and relax")
    print("d) Chilling out with friends and taking up new adventures")
    ques1 = input("Choose an option between a through d: ")

    if ques1 == "a":
        yellow_ls.append(3)
        green_ls.append(1)
        red_ls.append(2)
        blue_ls.append(4)
    elif ques1 == "b":
        yellow_ls.append(4)
        green_ls.append(1)
        red_ls.append(3)
        blue_ls.append(2)
    elif ques1 == "c":
        yellow_ls.append(2)
        green_ls.append(4)
        red_ls.append(3)
        blue_ls.append(1)
    elif ques1 == "d":
        yellow_ls.append(2)
        green_ls.append(3)
        red_ls.append(4)
        blue_ls.append(1)
    big_ls = []
    big_ls.append(yellow_ls)
    big_ls.append(green_ls)
    big_ls.append(red_ls)
    big_ls.append(blue_ls)
    return big_ls
def question_two(big_ls):
    print("--*---------------------------------*")
    print("What skill of yours are you most proud of?")
    print("a) Ability to absorb new information")
    print("b) Ability to make new friends")
    print("c) Ability to get what you want")
    print("d) Ability to keep secrets")
    ques2 = input("Choose an option between a through d: ")

    if ques2 == "a":
        yellow_ls.append(1)
        green_ls.append(2)
        red_ls.append(3)
        blue_ls.append(4)
    elif ques2 == "b":
        yellow_ls.append(3)
        green_ls.append(1)
        red_ls.append(4)
        blue_ls.append(2)
    elif ques2 == "c":
        yellow_ls.append(1)
        green_ls.append(4)
        red_ls.append(3)
        blue_ls.append(2)
    elif ques2 == "d":
        yellow_ls.append(1)
        green_ls.append(3)
        red_ls.append(4)
        blue_ls.append(2)
    return big_ls
def question_three(big_ls):
    print("-----*------------------------------*")
    print("You are trapped in a burning building and only have 10 seconds to get out. What would you do?")
    print("a) Save myself, of course")
    print("b) Run and grab my friend that is still in the building")
    print("c) It depends, if I have a way to save my friend, then yes, but if there's no way, then I'm above everybody else.")
    print("d) I will stay in the building and find a way to get rid of the fire")
    ques3 = input("Choose an option between a through d: ")

    if ques3 == "a":
        yellow_ls.append(2)
        green_ls.append(4)
        red_ls.append(1)
        blue_ls.append(3)
    elif ques3 == "b":
        yellow_ls.append(3)
        green_ls.append(1)
        red_ls.append(4)
        blue_ls.append(2)
    elif ques3 == "c":
        yellow_ls.append(3)
        green_ls.append(1)
        red_ls.append(2)
        blue_ls.append(4)
    elif ques3 == "d":
        yellow_ls.append(1)
        green_ls.append(2)
        red_ls.append(4)
        blue_ls.append(3)

    return big_ls
def question_four(big_ls):
    print("--------*---------------------------*")
    print("You accidentally read your roommates diary. What would you do?")
    print("a) Wave it in their face and start reading the open passage aloud")
    print("b) Put it back, but delight in knowing something more about them")
    print("c) Accidentally, I've been reading it all along to gather dirt")
    print("d) I sit down with them and talk about their problems")
    ques4 = input("Choose an option between a through d: ")

    if ques4 == "a":
        yellow_ls.append(1)
        green_ls.append(4)
        red_ls.append(3)
        blue_ls.append(2)
    elif ques4 == "b":
        yellow_ls.append(3)
        green_ls.append(1)
        red_ls.append(2)
        blue_ls.append(4)
    elif ques4 == "c":
        yellow_ls.append(1)
        green_ls.append(4)
        red_ls.append(3)
        blue_ls.append(2)
    elif ques4 == "d":
        yellow_ls.append(4)
        green_ls.append(1)
        red_ls.append(3)
        blue_ls.append(2)

    return big_ls
def question_five(big_ls):
    print("-----------*------------------------*")
    print("How do you flirt with someone you like?")
    print("a) You don't; you'll tell someone straight up if you like them")
    print("b) Try to have a real, deep conversation")
    print("c) You make witty jokes and smile coyly to charm them")
    print("d) You deliver a great, cheesy pick-up or wink at them")
    ques5 = input("Choose an option between a through d: ")

    if ques5 == "a":
        yellow_ls.append(2)
        green_ls.append(4)
        red_ls.append(3)
        blue_ls.append(1)
    elif ques5 == "b":
        yellow_ls.append(2)
        green_ls.append(1)
        red_ls.append(3)
        blue_ls.append(4)
    elif ques5 == "c":
        yellow_ls.append(1)
        green_ls.append(2)
        red_ls.append(3)
        blue_ls.append(4)
    elif ques5 == "d":
        yellow_ls.append(1)
        green_ls.append(3)
        red_ls.append(4)
        blue_ls.append(2)

    return big_ls
def question_six(big_ls):
    print("--------------*---------------------*")
    print("What do you want to achieve before you die?")
    print("a) Acquire as many skills as you can")
    print("b) Become super wealthy")
    print("c) Make as many friends as possible")
    print("d) Travel the whole world")
    ques6 = input("Choose an option between a through d: ")

    if ques6 == "a":
        yellow_ls.append(2)
        green_ls.append(1)
        red_ls.append(3)
        blue_ls.append(4)
    elif ques6 == "b":
        yellow_ls.append(3)
        green_ls.append(1)
        red_ls.append(1)
        blue_ls.append(2)
    elif ques6 == "c":
        yellow_ls.append(4)
        green_ls.append(2)
        red_ls.append(3)
        blue_ls.append(1)
    elif ques6 == "d":
        yellow_ls.append(2)
        green_ls.append(1)
        red_ls.append(4)
        blue_ls.append(3)

    return big_ls
def question_seven(big_ls):
    print("-----------------*------------------*")
    print("You are making a presentation for a class project, You..")
    print("a) Take charge, organize everyone, and end up doing almost everything")
    print("b) Do as little as you can. The perks of group projects")
    print("c) Do a little of everything")
    print("d) Do most of the research and writing, but let other people make it flashy")
    ques7 = input("Choose an option between a through d: ")

    if ques7 == "a":
        yellow_ls.append(3)
        green_ls.append(1)
        red_ls.append(4)
        blue_ls.append(2)
    elif ques7 == "b":
        yellow_ls.append(2)
        green_ls.append(4)
        red_ls.append(1)
        blue_ls.append(3)
    elif ques7 == "c":
        yellow_ls.append(3)
        green_ls.append(2)
        red_ls.append(1)
        blue_ls.append(4)
    elif ques7 == "d":
        yellow_ls.append(4)
        green_ls.append(1)
        red_ls.append(3)
        blue_ls.append(2)

    return big_ls
def question_eight(big_ls):
    print("--------------------*---------------*")
    print("What fault do you notice in people that bother you the most?")
    print("a) Stupidity")
    print("b) Dishonesty")
    print("c) Cowardice")
    print("d) Laziness")
    ques8 = input("Choose an option between a through d: ")

    if ques8 == "a":
        yellow_ls.append(1)
        green_ls.append(3)
        red_ls.append(2)
        blue_ls.append(4)
    elif ques8 == "b":
        yellow_ls.append(4)
        green_ls.append(1)
        red_ls.append(3)
        blue_ls.append(2)
    elif ques8 == "c":
        yellow_ls.append(1)
        green_ls.append(3)
        red_ls.append(4)
        blue_ls.append(2)
    elif ques8 == "d":
        yellow_ls.append(4)
        green_ls.append(1)
        red_ls.append(3)
        blue_ls.append(2)

    return big_ls
def question_nine(big_ls):
    print("-----------------------*------------*")
    print("Some fourth years are picking on a first year. What would you do?")
    print("a) Stand up to them")
    print("b) None of my business. I shouldn't get involved")
    print("c) I would talk later with them and ask if they're okay")
    print("d) I feel bad, but I can't do anything. They might start picking on me")
    ques9 = input("Choose an option between a through d: ")

    if ques9 == "a":
        yellow_ls.append(3)
        green_ls.append(1)
        red_ls.append(4)
        blue_ls.append(2)
    elif ques9 == "b":
        yellow_ls.append(2)
        green_ls.append(4)
        red_ls.append(1)
        blue_ls.append(3)
    elif ques9 == "c":
        yellow_ls.append(4)
        green_ls.append(1)
        red_ls.append(3)
        blue_ls.append(2)
    elif ques9 == "d":
        yellow_ls.append(4)
        green_ls.append(2)
        red_ls.append(1)
        blue_ls.append(3)

    return big_ls
def question_ten(big_ls):
    print("--------------------------*---------*")
    print("During the end-of-year exams, you notice that one of your classmates were using an enchanted quill. You come top of the class anyway, but they are second. What do you do?")
    print("a) Tell the professor immediately - cheating is wrong - no matter what")
    print("b) Nothing, but if I hadn't come top of the class, I'd definitely tell the professor")
    print("c) Encourage them to admit what they'd done to the professor")
    print("d) Give them a high five for managing to sneak the quill into the exam")
    ques10 = input("Choose an option between a through d: ")

    if ques10 == "a":
        yellow_ls.append(4)
        green_ls.append(1)
        red_ls.append(2)
        blue_ls.append(3)
    elif ques10 == "b":
        yellow_ls.append(1)
        green_ls.append(3)
        red_ls.append(2)
        blue_ls.append(4)
    elif ques10 == "c":
        yellow_ls.append(4)
        green_ls.append(1)
        red_ls.append(2)
        blue_ls.append(3)
    elif ques10 == "d":
        yellow_ls.append(1)
        green_ls.append(4)
        red_ls.append(3)
        blue_ls.append(2)

    return big_ls
def question_eleven(big_ls):
    print("-----------------------------*------*")
    print("How organized are you in studies?")
    print("a) I am the most organized person ever")
    print("b) Ehhh.. Who studies at all?")
    print("c) I am pretty good, but there's still scope for improvement")
    print("d) Only that much which is necessary")
    ques11 = input("Choose an option between a through d: ")

    if ques11 == "a":
        yellow_ls.append(3)
        green_ls.append(1)
        red_ls.append(2)
        blue_ls.append(4)
    elif ques11 == "b":
        yellow_ls.append(2)
        green_ls.append(4)
        red_ls.append(3)
        blue_ls.append(1)
    elif ques11 == "c":
        yellow_ls.append(4)
        green_ls.append(1)
        red_ls.append(3)
        blue_ls.append(2)
    elif ques11 == "d":
        yellow_ls.append(1)
        green_ls.append(4)
        red_ls.append(2)
        blue_ls.append(3)

    return big_ls
def question_twelve(big_ls):
    print("-----------------------------------**")
    print("The first Quidditch match of the season is approaching. What role are you playing?")
    print("a) Seeker. You want the glory!")
    print("b) Chaser. You like to be involved and work as part of the team")
    print("c) Beater. You like having all that power")
    print("d) You'll be in the crowd, making sure supporter morale is high")
    ques12 = input("Choose an option between a through d: ")

    if ques12 == "a":
        yellow_ls.append(1)
        green_ls.append(3)
        red_ls.append(4)
        blue_ls.append(2)
    elif ques12 == "b":
        yellow_ls.append(4)
        green_ls.append(1)
        red_ls.append(2)
        blue_ls.append(3)
    elif ques12 == "c":
        yellow_ls.append(1)
        green_ls.append(4)
        red_ls.append(3)
        blue_ls.append(2)
    elif ques12 == "d":
        yellow_ls.append(4)
        green_ls.append(1)
        red_ls.append(2)
        blue_ls.append(3)

    return big_ls


#Introduction Part
print("Warning: This program is case-sensitive.")
sleep(3.5)
print("\nWelcome to Hogwarts! Take this quiz to get sorted into your magical house!")
sleep(2.5)
print("≈ ≈ ≈ ≈ ≈ ≈ ≈ ≈ ≈ ≈ ≈ ")
trueFan = input("\nAre you already a Potterhead? (y/n): ")
trueFan_initial = fanChecker()

#Algorithm for the program

yellow_ls = []
green_ls = []
red_ls = []
blue_ls = []

#Calling question functions
big_ls = question_one()
question_two(big_ls)
question_three(big_ls)
question_four(big_ls)
question_five(big_ls)
question_six(big_ls)
question_seven(big_ls)
question_eight(big_ls)
question_nine(big_ls)
question_ten(big_ls)
question_eleven(big_ls)
question_twelve(big_ls)


#making the percentage probability for houses
totalPoint = []
for i in big_ls:
    totalPoint.extend(i)
wholeSum = sum(totalPoint)

huff_perc = (sum(big_ls[0])/wholeSum)*100
slyt_perc = (sum(big_ls[1])/wholeSum)*100
gryf_perc = (sum(big_ls[2])/wholeSum)*100
rave_perc = (sum(big_ls[3])/wholeSum)*100

house_perc = [huff_perc]+[slyt_perc]+[gryf_perc]+[rave_perc]
house_name = ["Hufflepuff","Slytherin","Gryffindor","Ravenclaw"]

for n, elem in enumerate(house_perc):
    if elem == max(house_perc):
        trueFan_final = house_name[n]

#printing the results
print("\n.....")
sleep(3)
print("The Quiz is done!")
sleep(1.5)
print("The sorting Hat chose your house")
sleep(1.0)
print("And you are in...")
sleep(3.0)
print(f"{trueFan_final}!!!")
if trueFan_final == "Gryffindor":
    sleep(1.0)
    print("\nGryffindor, where dwell the brave at heart, their daring, nerve and chivalry set Gryffindors apart.")
    sleep(1.0)
    print("\nGryffindors value courage, bravery, daring, and chivalry. Their house mascot is the lion, and their colors are scarlet and gold. They are generally regarded as brave, though sometimes to the point of recklessness. Gryffindors have a strong code of honor, which includes valor and nobility. They are not afraid to speak their mind or fight for what they know is right. Many are endowed with leadership qualities and emerge as the head of the pack when it comes to doing something that takes courage. They want to succeed and come out ahead, and many like the acknowledgement that comes with being seen as a hero. But at the end of the day, their hearts are noble and their motivations pure.")
if trueFan_final == "Slytherin":
    sleep(1.0)
    print("\nIn Slytherin, you'll make your real friends, those cunning folk use any means to achieve their ends.")
    sleep(1.0)
    print("\nSlytherins value ambition, cunning, leadership, and resourcefulness. Their house mascot is the serpent, and their colors are silver and green. Slytherins tend to be ambitious, shrewd, achievement-oriented, and conscious of social status. They also have a highly developed sense of self-preservation. This means that Slytherins tend to hesitate before acting, so as to weigh all possible outcomes before deciding exactly what should be done. The qualities valued by a Slytherin are cleverness, resourcefulness, and a certain disregard for the rules. Slytherins tend to be self-assured and confident in their own abilities. They like to take charge and often possess strong leadership skills.")
if trueFan_final == "Hufflepuff":
    sleep(1.0)
    print("\nHufflepuff, where they are just and loyal, those patient Hufflepuffs are true and unafraid of toil.")
    sleep(1.0)
    print("\nHufflepuffs value dedication, patience, justice, and loyalty. Their house mascot is the badger, and their colors are yellow and black. They tend to be inclusive and tolerant, valuing fair play, good spirits and enthusiasm rather than a particular aptitude in themselves or their friends. They have a strong sense of right and wrong and strive to be friendly and honest. Because of their modesty and gentle nature, Hufflepuffs may sometimes be underestimated or seen as less competitive than others. Modest about their accomplishments and with a dislike of social rivalry, Hufflepuffs are usually accepted by everyone.")

if trueFan_final == "Ravenclaw":
    sleep(1.0)
    print("\nWise old Ravenclaw, if you've a ready mind, where those of wit and learning will always find their kind.")
    sleep(1.0)
    print("\nRavenclaws value intelligence, creativity, learning, and wit. Their house mascot is the eagle, and their colors are blue and bronze. They tend to be rational, logical and curious about academic learning. They pride themselves on the originality of their ideas, as well as their vast array of book knowledge. As is sometimes the case with intellectuals, some Ravenclaws are known to be inclined to dismiss social conventions for the sake of satisfying their own intellectual curiosity. For this reason, they are sometimes thought eccentric or odd, but may end up celebrated or renowned when they manage to come up with new and valuable ideas.")

print("\n")

if trueFan_final.lower() == trueFan_initial.lower():
    sleep(3.0)
    print(f"Your prediction was right from the beginning. You are a {trueFan_final}!")
    stats = input("Do you want to see your chances of being on other houses? (y/n): ")
    if stats == "y":
        print(f"You are {huff_perc:.0f}% Hufflepuff, {slyt_perc:.0f}% Slytherin, {gryf_perc:.0f}% Gryffindor, {rave_perc:.0f}% Ravenclaw")
        print("\nThanks for playing.")
        print("The END.")
    else:
        print("We hope you will enjoy your new house!")
        print("\nThanks for playing.")
        print("The END.")
else:
    print("\nThanks for playing.")
    print("\nThe END.")
