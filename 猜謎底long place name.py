import random
words = ['Taumatawhakatangihangakoauauotamateapokaiwhenuakitanatahu',
         'Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch',
         'Chargoggagoggmanchauggagoggchaubunagungamaugg',
         'Tweebuffelsmeteenskootmorsdoodgeskietfontein',
         'Azpilicuetagaraycosaroyarenberecolarrea',
         'Ateritsiputeritsipuolilautatsijanka', 
         'Pekwachnamaykoskwaskwaypinwanik', 
         'Venkatanarasimharajuvaripeta',
         'Bovenendvankeelafsnysleegte',
         'Mamungkukumpurangkuntjunya',
         'Schmedeswurtherwesterdeich', 
         'Bullaunancheathrairaluinn',
         'Gasselterboerveenschemond',
         'Verkhnenovokutlumbetyevo',
         'Staronizhestebliyevskaya',
         'Svalbarosstrandarhreppur',
         'Onafhankelijkheidsplein',
         'Kvernbergsundsodegarden',
         'Nunathloogagamiutbingoi',
         'Nizhnenovokutlumbetyevo']
clue = []
index = 0
while True:
    secret_word = random.choice(words)
    secret_word = secret_word.lower()
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
    print('規則: \n 1.本遊戲是用英文輸入法玩的，用中文輸入法的話程式是不會理你的。\n 2.在這個遊戲裡你要猜出謎底是甚麼\n 3.請用快樂的心情玩\n 4.本遊戲有時會出現 \' . - 和\' \'\n 5.本遊戲在測試階段，有錯誤敬請見諒\n                                                       吳焌脩上')
    while lives > 0:
        print(clue)
        print('剩下的性命: ' + heart_symbol * lives)
        guess = input('猜一個字母、單字、.、\'、-或\' \': ')
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
    print('       版本  1.0.0')
    ip_str = ''.join(words)
    ip_str = ip_str.lower()
    count = {x: sum([1 for char in ip_str if char == x]) for x in "abcdefghijklmnopqrstuvwxyz"}
    print(count)
    response = input('你想在玩一遍嗎? 輸入 要 或 不要: ')
    if response == '不要':
        break
    elif response == '':
        break
