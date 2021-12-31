import random
words = ['alberta', 'britishcolumbia', 'manitoba', 'newbrunswick', 'newfoundlandandlabrdor', 'northwestterritories', 'novascotia', 'nunavut', 'ontario', 'princeedwardisland', 'quebec', 'saskatchewan', 'yukon', 'rhodeisland', 'delaware', 'connecticut', 'hawaii', 'newjersey', 'massachusetts', 'newhampshire', 'vermont', 'maryland', 'westvirginia', 'southcarolina', 'maine', 'virginia', 'kentucky', 'ohio', 'tennessee', 'louisiana', 'pennsylvania', 'mississippi', 'newyork', 'northcarolina', 'albama', 'arkansas', 'florida', 'wisconsin', 'illinois', 'iowa', 'michigan', 'georgia', 'washington', 'oklahoma', 'missouri', 'northdakota', 'southdakota', 'nebraska', 'minnesota', 'kansas', 'utah', 'idaho', 'oregon', 'wyoming', 'colorado', 'nevada', 'arizona', 'newmexico', 'montana', 'california', 'texas', 'alaska', 'taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu']
secret_word = random.choice(words)
clue = []
index = 0
while index < len(secret_word):
    clue.append('?')
    index += 1
heart_symbol = u'\u2764'
guessed_word_correctly = False
unknown_letters = len(secret_word)
def update_clue(guessed_letter, secret_word, clue, unknown_letters):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
            unknown_letters -= 1
        index += 1
    return unknown_letters
difficulty = input('選擇難度: (按 1, 2, 3 或 4):\n 1 寶寶模式\n 2 簡單模式\n 3 普通模式\n 4 困難模式\n')
difficulty = int(difficulty)
if difficulty == 1:
    lives = 27
elif difficulty == 2:
    lives = 12
elif difficulty == 3:
    lives = 9
else:
    lives = 6
print('規則: \n 1.本遊戲是用英文輸入法玩的，用中文輸入法的話程式是不會理你的。\n 2.在這個遊戲裡你要猜出謎底是甚麼\n 3.請用快樂的心情玩\n                                                       吳焌脩上')
while lives > 0:
    print(clue)
    print('剩下的性命: ' + heart_symbol * lives)
    guess = input('猜一個字母或單字: ')
    if guess == secret_word:
        guessed_word_correctly = True
        break
    if guess in secret_word:
        unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
    else:
        print('輸入錯誤，你失去了一條性命')
        lives -= 1
    if unknown_letters == 0:
        guessed_word_correctly = True
        break
if guessed_word_correctly:
    print('你贏了! 謎底是', secret_word)
else:
    print('你輸了! 謎底是', secret_word)
