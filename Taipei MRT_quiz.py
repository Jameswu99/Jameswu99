def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct answer!')
            score = score + 3 - attempt
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry, wrong answer. Try again. ')
            attempt += 1
    if attempt == 3:
        print('The correct answer is:', answer)


score = 0
print('Guess the correct answer!')
guess0 = input('May I ask which administrative district has the \nmost MRT stations in all the administrative \n'
               'districts of Taipei City and New Taipei City \nthat the Taipei MRT passes through?(As of May 2020)\n A)'
               ' Banqiao District\n B) Tamshui District\n C) Da\'an District\n D) Zhongshan District\nType A, B, C or '
               'D:')
check_guess(guess0, 'C')
print('Your score is', str(score))
