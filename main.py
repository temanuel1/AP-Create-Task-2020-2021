import random
from sys import exit

correct = True
score = 0

#Establishes questions/answers for each genre and difficulty
sports_questions_easy = ["How many bases are there on a baseball field?", "How many players are on the field for a single soccer team at any give point during the game?", "What is it called when a baseball player hits a home-run with the bases loaded?",]
sports_questions_medium = ["Which country won the most recent World Cup in Men's Soccer?", "How many points is a perfect game in bowling?", "What sport can be played on clay, hard-surface, and grass?"]
sports_questions_hard = ["How many dimples are there on an average golf ball?", "How many gold medals does olympic swimmer Michael Phelps have?", "In what country was NBA player Kyrie Irving born in?"]

sports_answers_easy = ["4", "11", "grand slam"]
sports_answers_medium = ["france", "300", "tennis"]
sports_answers_hard = ["336", "23", "australia"]

history_questions_easy = ["What year was 9/11?", "When did the Titanic sink?", "What year did the US land on the moon?"]
history_questions_medium = ["How many US presidents have been assassinated?", "What year did the Cold War start?", "Who led the USSR during World War 2 (Full Name)?"]
history_questions_hard = ["Who painted the Sistine Chapel?", "Who founded the Mongol Empire?", "Who was America's 30th president?"]

history_answers_easy = ["2001", "1912", "1969"]
history_answers_medium = ["4", "1947", "joseph stalin"]
history_answers_hard = ["michelangelo", "genghis khan", "calvin coolidge"]

music_questions_easy = ["Who sings Gangam Style?", "Which group sings Yellow Submarine", "In what state is the US Rock and Roll Hall of Fame?"]
music_questions_medium = ["Which artist(s) has/have an album that features a prism on the cover?", "What is the most viewed song/music video on Youtube?", "Which artist wrote and performs Cheeeburger in Paradise?"]
music_questions_hard = ["What was Elvis' middle name?", "If there are 52 white keys on a piano, how many black keys does it have?", "In what year did Beethoven die?"]

music_answers_easy = ["psy", "the beatles", "ohio"]
music_answers_medium = ["pink floyd", "despacito", "jimmy buffett"]
music_answers_hard = ["aaron", "36", "1827"]


#Function that runs the game
def game_play():
  correct = True
  print ("\nThe difficulties are: easy, medium, and hard\n")
  print ("The three genres are: sports, history, and music\n")
  print("Choose a different difficulty/genre combination everytime you are asked to pick a new question (There are 9 total questions)\n")
  question_difficulty = input("What difficulty of question do you want? \n")
  if question_difficulty.lower() == "easy":
    print("")
  elif question_difficulty.lower() == "medium":
    print ("")
  elif question_difficulty.lower() == "hard":
    print("")
  else:
    print("\nInvalid difficulty selected, try again")
    game_play()
  question_genre = input("What genre of question do you want? \n")
  if question_genre.lower() == "sports":
    correct = True
    sports_question_number = random.randint (0,2)
    if question_difficulty.lower() == "easy":
      your_question = (sports_questions_easy[sports_question_number])
      answer = (input(str("\n" + your_question + "\n")))
      if answer.lower() == (sports_answers_easy[sports_question_number]):
        correct = True
      else:
        print("\nIncorrect, the answer is: " + str(sports_answers_easy[sports_question_number].upper()))
        correct = False
    elif question_difficulty.lower() == "medium":
      your_question = (sports_questions_medium[sports_question_number])
      answer = (input(str("\n" + your_question + "\n")))
      if answer.lower() == (sports_answers_medium[sports_question_number]):
        correct = True
      else:
        print("\nIncorrect, the answer is: " + str(sports_answers_medium[sports_question_number].upper()))
        correct = False
    elif question_difficulty.lower() == "hard":
      your_question = (sports_questions_hard[sports_question_number])
      answer = (input(str("\n" + your_question + "\n")))
      if answer.lower() == (sports_answers_hard[sports_question_number]):
        correct = True
      else:
        print("\nIncorrect, the answer is: " + str(sports_answers_hard[sports_question_number].upper()))
        correct = False
    else:
      print("\nInvalid difficulty selected, try again")
  elif question_genre.lower() == "history":
    correct = True
    history_question_number = random.randint (0,2)
    if question_difficulty.lower() == "easy":
      your_question = (history_questions_easy[history_question_number])
      answer = (input(str("\n" + your_question + "\n")))
      if answer.lower() == (history_answers_easy[history_question_number]):
        correct = True
      else:
        print("\nIncorrect, the answer is: " + str(history_answers_easy[history_question_number].upper()))
        correct = False
    elif question_difficulty.lower() == "medium":
      your_question = (history_questions_medium[history_question_number])
      answer = (input(str("\n" + your_question + "\n")))
      if answer.lower() == (history_answers_medium[history_question_number]):
        correct = True
      else:
        print("\nIncorrect, the answer is: " + str(history_answers_medium[history_question_number].upper()))
        correct = False
    elif question_difficulty.lower() == "hard":
      your_question = (history_questions_hard[history_question_number])
      answer = (input(str("\n" + your_question + "\n")))
      if answer.lower() == (history_answers_hard[history_question_number]):
        correct = True
      else:
        print("\nIncorrect, the answer is: " + str(history_answers_hard[history_question_number].upper()))
        correct = False
    else:
      print("\nInvalid difficulty selected, try again")
  elif question_genre.lower() == "music":
    correct = True
    music_question_number = random.randint (0,2)
    if question_difficulty.lower() == "easy":
      your_question = (music_questions_easy[music_question_number])
      answer = (input(str("\n" + your_question + "\n")))
      if answer.lower() == (music_answers_easy[music_question_number]):
        correct = True
      else:
        print("\nIncorrect, the answer is: " + str(music_answers_easy[music_question_number].upper()))
        correct = False
    elif question_difficulty.lower() == "medium":
      your_question = (music_questions_medium[music_question_number])
      answer = (input(str("\n" + your_question + "\n")))
      if answer.lower() == (music_answers_medium[music_question_number]):
        correct = True
      else:
        print("\nIncorrect, the answer is: " + str(music_answers_medium[music_question_number].upper()))
        correct = False
    elif question_difficulty.lower() == "hard":
      your_question = (music_questions_hard[music_question_number])
      answer = (input(str("\n" + your_question + "\n")))
      if answer.lower() == (music_answers_hard[music_question_number]):
        correct = True
      else:
        print("\nIncorrect, the answer is: " + str(music_answers_hard[music_question_number].upper()))
        correct = False
    else:
      print("\nInvalid difficulty selected, try again")
  else:
    print("\nInvalid genre selected, try again")
    game_play()
  game_start_end(correct)

#Function that awards a win when called
def won (win):
  if win == True:
    print ("\nCongrats, you have answered all 9 questions correctly! You Win!\n")
    exit() 

#Function that determines if the game should continue or if a win or loss should be awarded
def game_start_end(correct):
  global score
  while score < 9:
    if correct == True:      
      #print (questions_answered)
      print("\nCorrect! You have answered " + str(score) + " question(s) correctly!")
      score += 1
      game_play()
    if correct != True:
      print("\nSorry, you got a question wrong. Game Over!\n")
      exit()
  if correct == True and score == 9:
    win = True
    won(win)

game_start_end(correct)