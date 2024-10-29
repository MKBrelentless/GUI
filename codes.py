

guess_count=0
guess_limit=3
out_of_guess=False

correct_answer=56
while guess_count>guess_limit and not out_of_guess:
      guess = input ( f"guess_count {guess_count +1}: Enter your guess:")
        
if guess == correct_answer:
   print("you win")
   
   guess_count +=1;
else:

    print("You win")
    
        