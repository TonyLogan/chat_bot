# UTF-8
import random as r
from playsound import playsound
import pyttsx3
import time

def hell_heaven_game():
    hell = 0
    heaven = 0
    print("Here are some person and you need to guess wether they will go to HELL or HEAVEN.\n")
    theif = input("\nTheif (HELL or HEAVEN) : ").lower()
    maid = input("\nMaid (HELL or HEAVEN) : ").lower()
    president = input("\nPresident (HELL or HEAVEN) : ").lower()
    gangster = input("\nGangster (HELL or HEAVEN) : ").lower()
    # theif
    if theif == "heaven":
        heaven += 1
    else:
        hell += 1
    # maid
    if maid == "heaven":
        heaven += 1
    else:
        hell += 1 
    # president
    if president == "heaven":
        heaven += 1
    else:
        hell += 1
    # gangster
    if gangster == "heaven":
        heaven += 1
    else:
        hell += 1
    print(f"\nYou sent {hell} people to hell and {heaven} people to heaven.")
    print("\nThank you for playing")

def number_guessing():
    winning_number = r.randint(1, 100)            
    game_over = True
    print("Number Guessing Game".center(170))
    number = int(input("Enter a number between 1 to 100 : "))
    guess = 1
    while game_over:
        if number == winning_number:
            print(f"\nYou win, you guessed {guess} times \U0001F600")
            print("\nThank you for playing")
            game_over = False
        else:
            if number < winning_number:
                print("\nYou guessed to low! \U0001F61C")    
            else:
                print("\nYou guessed too high! \U0001F635")
            
            guess += 1
            number = int(input("\ntry again : "))

def char_count():
    user_name, character = input("Write your name and a character used in it and seperate them by a comma: ").split(",")
    print(f"\nLenght of your name is {len(user_name.strip())}")
    print(f"\ncharacter count : {user_name.lower().count(character.strip().lower())}")

def calc():
    while True:
        number_1 = int(input("Enter first number : "))
        number_2 = int(input("Enter second number : "))
        operation = input("Enter operation : ").lower()
        if operation == "multiplication" or operation == "*":
            print(f"Your answer is {number_1 * number_2}")
            break
        elif operation == "division" or operation == '/':
            print(f"Your answer is {number_1 // number_2}")
            break
        elif operation == "addition" or operation == "+":
            print(f"Your answer is {number_1 + number_2}")
            break
        elif operation == "subtraction" or operation == "-":
            print(f"Your answer is {number_1 - number_2}")
            break
        else:
            print("\nYOU DIDN't ENTER THE OPERATION !!!! try again \U0001F620")
           
def Odd_Even_printer():
    odd_even = input("\nODD or EVEN? : ").lower()
    odd_even_start = int(input("\nFrom which number you need to start? : "))
    stop_argument = int(input("\nTill what number you want? : "))
    if odd_even == "even":
        for i in range(odd_even_start, stop_argument + 1, 2):
            print(f"\n{i}")
    elif odd_even == "odd":
        for m in range(odd_even_start, stop_argument + 1, 2):
            print(f"\n{m}")
 
def odd_even():
    num = int(input("Number : "))
    if num%2 == 0:
        print("Even")
    else:
        print("Odd")

def rock_paper():
    engine = pyttsx3.init()
    comp = 0
    player_1_score = 0
    rounds_played = 0
    while True:
        volume = engine.getProperty("volume")
        rate = engine.getProperty("rate")
        engine.setProperty("volume", 1)
        engine.setProperty("rate", 150)
        speak = ["Oh No!", "Better Luck Next Time", "You are a loser"]
        speaking = r.choice(speak)
        speak2 = ["Winner Winner \"Chicken\" Dinner", "You Are The \"Master\"", "Amazing"]
        speaking2 = r.choice(speak2)
        speak3 = ["Winner Winner 2 Plate \"Chicken\" Dinner", "Both Are The Masters", "Luck Is Charming For Both"]
        speaking3 = r.choice(speak3)
        choices = ["rock", "paper", "scissors"]
        computer_play = r.choice(choices)
        user_play = input("\nEnter a choice (rock, paper, scissors) : ").lower()
        # play
        if user_play == computer_play:
            print(f"\nYou chose: {user_play} and computer chose: {computer_play}. TIE!")
            comp += 1
            player_1_score += 1
            rounds_played += 1
            print(f"\n***SCORE TILL NOW***\n\nYour score: {player_1_score}\nComputer Score: {comp}")
        elif user_play == "rock":
            if computer_play == "paper":
                print(f"\nYou chose: {user_play} and computer chose: {computer_play}. You Lose!")
                comp += 1
                rounds_played += 1
                print(f"\n***SCORE TILL NOW***\n\nYour score: {player_1_score}\nComputer Score: {comp}")
            else:
                print(f"\nYou chose: {user_play} and computer chose: {computer_play}. You Win!")
                player_1_score += 1
                rounds_played += 1
                print(f"\n***SCORE TILL NOW***\n\nYour score: {player_1_score}\nComputer Score: {comp}")
        elif user_play == "paper":
            if computer_play == "rock":
                print(f"\nYou chose: {user_play} and computer chose: {computer_play}. You Win!")
                player_1_score += 1
                rounds_played += 1
                print(f"\n***SCORE TILL NOW***\n\nYour score: {player_1_score}\nComputer Score: {comp}")
            else:
                print(f"\nYou chose: {user_play} and computer chose: {computer_play}. You Lose!")
                comp += 1
                rounds_played += 1
                print(f"\n***SCORE TILL NOW***\n\nYour score: {player_1_score}\nComputer Score: {comp}")
        elif user_play == "scissors":
            if computer_play == "paper":
                print(f"\nYou chose: {user_play} and computer chose: {computer_play}. You Win!")
                player_1_score += 1
                rounds_played += 1
                print(f"\n***SCORE TILL NOW***\n\nYour score: {player_1_score}\nComputer Score: {comp}")
            else:
                print(f"\nYou chose: {user_play} and computer chose: {computer_play}. You Lose!")
                comp += 1
                rounds_played += 1
                print(f"\n***SCORE TILL NOW***\n\nYour score: {player_1_score}\nComputer Score: {comp}")
        else:
            print("\nCheck your spelling!\n")
            continue
        play_again = input("\nWant to play more? : ").lower()
        if play_again[0] != "y":
            print("\nFinal Scores:")
            playsound('F:\\chat_bot\\song\\Referee Whistle.wav')
            print(f"\nComputer Scores : {comp}")
            print(f"Your Score : {player_1_score}\n")
            if comp == player_1_score:
                print("TIE!\n")
                playsound('F:\\chat_bot\\song\\TIE.wav')
                print(speaking3)
                engine.say(speaking3)
                print(f"\nYou played {rounds_played} rounds.\n")
                engine.say(f"You played {rounds_played} rounds.")
                print("\nThank you for playing!")
                engine.say("Thank you for playing!")
            elif comp > player_1_score:
                print("Computer Win!\n")
                playsound('F:\\chat_bot\\song\\Loser.wav')
                print(f"\n{speaking}")
                engine.say(speaking)
                print(f"\nYou played {rounds_played} rounds.\n")
                engine.say(f"You played {rounds_played} rounds.")
                print("\nThank you for playing!")
                engine.say("Thank you for playing!")
            else:
                print("You win!\n")
                playsound('F:\\chat_bot\\song\\Winner.wav')
                print(f"\n{speaking2}")
                engine.say(speaking2)
                print(f"\nYou played {rounds_played} rounds.\n")
                engine.say(f"You played {rounds_played} rounds.")
                print("\nThank you for playing!")
                engine.say("Thank you for playing!")
            engine.runAndWait()
            break

def future():
    while True:
        months_list = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
        month = input("\nBirth Month : ").lower()
        if month not in months_list:
            print("\nYour spelling of the month is wrong")
            continue
        
        if month == "january":
            print("\nYou are a hard-working, outspoken person, and you hold fast to your underlying beliefs.\nThis means you're unlikely to be swayed once you decide to manifest something.\nHowever, it also means you might have to work harder than most to defeat limiting beliefs from the past.\nYou're also a natural leader and teacher, which means you will excel at spreading the positive message of the Law of Attraction (in turn attracting more goodness into your own life).")
            break
        elif month == "february":
            print("\nYou likely have a strong creative streak, so you'll be very good at all the imaginative activities associated with manifestation (such as visualization and dream boarding).\nHowever, your innate love of adventure means you might focus on the big picture at the expense of the little details that will get you to your destination; try to remember that making a step-by-step manifestation plan is crucial.")
            break
        elif month == "march":
            print("\nYou are probably quite an introspective person. In addition, your ability to build dazzling pictures in your own mind will help you get to the root of what you really want from life.\nOn the other hand, be aware that others may sometimes take advantage of your gentleness and kindness. Consequently, think about regularly performing an inventory of your relationships to see if any might be holding you back from using the Law of Attraction to its full potential.")
            break
        elif month == "april": 
            print("\nYou are likely to thrive on attention and enjoy time in the spotlight, so keep this in mind if you're still trying to work out your life purpose.\nYour frankness and honesty will serve you well when you strive to boost self-knowledge. Plus, you're willing to take worthwhile risks.\nThat being said, remember to think your manifestation plan through before just jumping right in; excitement can get the best of you sometimes!")
            break
        elif month == "may":
            print("\nYou may struggle to pin down one thing you consistently want to attract; this lack of focus reduces the chances of success.\nNevertheless, you are a magnetic person who makes other people feel at ease.\nTherefore, you're adept at raising your own vibration and pulling more positivity into your life.\nFurther, your love of intellectual stimulation puts you in a great position to understand the theoretical groundings of the Law of Attraction.")
            break
        elif month == "june":
            print("\nYou have deep compassion and empathy, which means you'll typically do well when manifesting anything related to interpersonal goals (whether they're related to love or friendship).\nHowever, you may sometimes hesitate to express your true self to others.\nIt is only by living an authentic life that you'll reliably send your message to the universe and be able to attract what you truly need.")
            break
        elif month == "july":
            print("\nYou have an infectious kind of energy that draws other people to you.\nTherefore, you have something of a head start when trying to manifest a relationship or a business.\nYou're also talented at adopting a positive demeanor, though you may hide many of your more difficult emotions from others.\nBe sure not to ignore these feelings! Instead, properly process them so you can work against hidden negativity and remove barriers to manifesting your intentions.")
            break
        elif month == "august":
            print("\nYou're not afraid to defend your opinions, so any dissenting voices are unlikely to sway you from your goals.\nOne of your major challenges will be to resist the urge to over-think.\nConsequently, this can block access to highly valuable intuitions that can guide you towards your goal.\nTrust your heart, not just your head, when using the Law of Attraction.")
            break
        elif month == "september":
            print("\nYou hold others to high standards, so you won't settle for anything less than the friendships and relationships you deserve.\nThis trait encourages self-valuing beliefs that will help you attract goodness into your life.\nThe more difficult flip side to your high standards is that your tendency towards perfectionism can stop you from seeing just how close to your potential you really are.")
            break
        elif month == "october":
            print("\nYou're very attracted to balance and stability, so you'll understand the importance of self-care as well as the value of hard work when using the Law of Attraction.\nHowever, you may also be pulled toward excessive independence.\nIn this way, you will not always recognize when you would benefit from asking others for help or support.\nTry to work on reaching out more often, and accepting the resources others offer to you.")
            break
        elif month == "november":
            print("\nIt's typically hard for you to share your deepest feelings with others, as you value privacy.\nWhile this guards you against a certain degree of hurt, it can also reduce the depth of human connections you form, which is especially important if you're trying to manifest love.\nYou'll be better able to realize your intentions if you begin to disclose more of your identity to those who want to know you.")
            break
        elif month == "december":
            print("\nYou're a generous, adventurous person who enjoys new experiences and has a free spirit.\nYour Achilles heel is perhaps your pride.\nHowever, which may lead you to abandon goals or relationships at the first hurdle.\nRemember that every setback has something valuable to teach you! Everything will ultimately bring you closer to manifesting your dreams.")
            break
        else:
            pass

def anything():
    name = input("Enter your name : ")
    stars = input('\nHow much to add on each side : ')
    star_convert = int(stars)*2
    thing = input("\nWhat you want to add : ")
    print(f"\nYour name : {name.center(len(name)+star_convert, thing)}")

timing_stop = r.randint(1, 3) 
print("Chat Bot".center(180))

name = input("Enter your name : ")

print(f"\nHello {name},\n")
print("\nThings that I can Do:")
print("1. Mini Games")
print("2. Character count in a word")
print("3. Calculator")
print("4. Print Odd Even between a number")
print("5. Check whether odd or even")
print("6. Know your future by month")
print("7. Add anything on both sides of your name")
print("8. Listen Jokes")
while True:
    user_to_chat = input("\nWhat you want to do (write index number or name of the command) : ").lower()
    print("")
    if user_to_chat == "1" or user_to_chat == "mini games":
        print("Games List : ")
        print("1. Hell and heaven game")
        print("2. Number guessing game")
        print("3. Rock paper scissors game")
        print("")
        game_to_play = input("Which game you want to play : ").lower()
        print("")
        if game_to_play == "1" or game_to_play == "hell and heaven game":
            print("Loading...\n")
            time.sleep(timing_stop)
            hell_heaven_game()
        elif game_to_play == "2" or game_to_play == "number guessing":
            print("Loading...")
            time.sleep(timing_stop)
            number_guessing()
        elif game_to_play == "3" or game_to_play == "rock paper scissors game":
            print("Loading...")
            time.sleep(timing_stop)
            rock_paper()
        else:
            print("Wrong spelling")
            continue
    elif user_to_chat == "2" or user_to_chat == "character count in a word":
        print("Loading...\n")
        time.sleep(timing_stop)
        char_count()
    elif user_to_chat == "3" or user_to_chat == "calculator":
        print("Loading...\n")
        time.sleep(timing_stop)
        calc()
    elif user_to_chat == "4" or user_to_chat == "odd even printer":
        print("Loading...\n")
        time.sleep(timing_stop)
        Odd_Even_printer()
    elif user_to_chat == "5" or user_to_chat == "check whether odd or even":
        print("Loading...\n")
        time.sleep(timing_stop)
        odd_even()
    elif user_to_chat == "6" or user_to_chat == "know your future by month":
        print("Loading...\n")
        time.sleep(timing_stop)
        future()
    elif user_to_chat == "7" or user_to_chat == "add anything on both sides of your name":
        print("Loading...\n")
        time.sleep(timing_stop)
        anything()
    elif user_to_chat == "8" or user_to_chat == "listen jokes":
        print("Loading...\n")
        time.sleep(timing_stop)
        english_jokes = ["Q: How is an English teacher like a judge?\nA: They both give out sentences.", "Q: Why did the teacher wear sunglasses?\nA: Because his class was so bright!", "Q: Teacher: If I had 6 oranges in one hand and 7 apples in the other, what would I have?\nA: Student: Big hands!"]
        eng_print = r.choice(english_jokes)
        print(eng_print)
    else:
        print("")
        print("Wrong Command")
        continue
    print("")
    again = input("Want to do anything else : ")
    print("")
    if again[0] != "y":
        print("Rewiew:\n")
        rewiew = input("Please write rewiew a report a bug to improve the chat bot : ")
        print("\nThank You")
        break
