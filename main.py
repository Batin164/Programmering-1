name = input("What is your name? ").capitalize()
print(f"Welcome to the quiz {name}")
def Quiz():
   score = 0
   print(f"Answer the questions with a yes or no, your starting score is {score}")
   answer1 = input("Is 2+2=5? ").capitalize()
   if answer1 == "No":
      score += 1  
      print(f"Wow! Suka ebana how did you do that?! You now have {score} points")   
   elif answer1 == "Yes": print("Your mader very proud of idiot she has created, wrong answer.")
   else: print("Answer with a yes or no, idiot")
   
   answer2 = input("Does my mother love me? ").capitalize()
   if answer2 == "No":
      score += 1 
      print(f"Wow! Suka ebana how did you do that?! You now have {score} points")    
   elif answer2 == "Yes": print("Your mader very proud of idiot she has created, wrong answer.")
   else: print("Answer with a yes or no, idiot")

   answer3 = input("Is Poland the best country? ").capitalize()
   if answer3 == "No":
      score += 1 
      print(f"Wow! Suka ebana how did you do that?! You now have {score} points")    
   elif answer3 == "Yes": print("Your mader very proud of idiot she has created, wrong answer.")
   else: print("Answer with a yes or no, idiot")

   answer4 = input("Is Taiwan a country? ").capitalize()
   if answer4 == "Yes":
      score += 1 
      print(f"Wow! You are not that stupid, You now have {score} points")    
   elif answer4 == "No": print("Are you chinese? wrong answer.")
   else: print("Answer with a yes or no, idiot")

   print(f"You are done with the test, you scored {score}/4")
   answer5 = input("Did you enjoy this test?").capitalize()
   if answer5 == "Yes":
      print("Did you answer this because you scored 4/4? Well done!")
   elif answer5 == "No":
      print("Ok, fuck you bitch, just because you scored <4")
   else: print("You're not special, answer with a yes or no next time.")

Quiz()
   
   




