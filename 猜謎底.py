import random

words = ['alberta', 'british columbia', 'manitoba', 'new brunswick', 'newfoundland and labrdor',
         'northwest territories', 'nova scotia', 'nunavut', 'ontario', 'prince edward island', 'quebec', 'saskatchewan',
         'yukon', 'rhode island', 'delaware', 'connecticut', 'hawaii', 'new jersey', 'massachusetts', 'new hampshire',
         'vermont', 'maryland', 'west virginia', 'south carolina', 'maine', 'virginia', 'kentucky', 'ohio', 'tennessee',
         'louisiana', 'pennsylvania', 'mississippi', 'new york', 'north carolina', 'albama', 'arkansas', 'florida',
         'wisconsin', 'illinois', 'iowa', 'michigan', 'georgia', 'washington', 'oklahoma', 'missouri', 'north dakota',
         'south dakota', 'nebraska', 'minnesota', 'kansas', 'utah', 'idaho', 'oregon', 'wyoming', 'colorado', 'nevada',
         'arizona', 'new mexico', 'montana', 'california', 'texas', 'alaska', 'nord-norge', 'midt-norge', 'vestlandet',
         'sorlandet', 'ostlandet', 'ege', 'karadeniz', 'ic anadolu', 'dogu anadolu', 'marmara region', 'akdeniz',
         'guneydogu anadolu', 'stockholm', 'vasterbotten', 'norrbotten', 'uppsala', 'sodermanland', 'ostergotland',
         'jonkoping', 'kronoberg', 'kalmar', 'gotland', 'blekinge', 'skane', 'halland', 'vastra gotaland', 'varmland',
         'orebro', 'vastmanland', 'dalarna', 'gavleborg', 'vasternorrland', 'jamtland', 'zurich', 'bern', 'lucerne',
         'uri', 'schwyz', 'obwalden', 'nidwalden', 'glarus', 'zug', 'fribourg', 'solothurn', 'basel-stadt',
         'basel-landschaft', 'schaffhausen', 'appenzell ausserrhoden', 'appenzell innerrhoden', 'st. gallen',
         'graubunden', 'aargau', 'thurgau', 'ticino', 'vaud', 'valais', 'neuchatel', 'geneva', 'jura', 'matrouh',
         'alexandria', 'beheira', 'kafr el sheikh', 'dakahlia', 'damietta', 'port said', 'north sinai', 'gharbia',
         'monufia', 'qalyubia', 'sharqia', 'ismailia', 'giza', 'faiyum', 'cairo', 'suez', 'south sinai', 'beni suef',
         'minya', 'new valley', 'asyut', 'red sea', 'sohag', 'qena', 'luxor', 'aswan', "south p'yongan",
         "north p'yongan", 'chagang', 'south hwanghae', 'north hwanghae', 'kangwon', 'south hamgyong',
         'north hamgyong', 'ryanggang', 'rason', 'seoul', 'busan', 'daegu', 'incheon', 'gwangju', 'daejeon', 'ulsan',
         'sejong', 'gyeonggi-do', 'gangwon-do', 'north chungcheong', 'south chungcheong', 'north jeolla',
         'south jeolla', 'north gyeongsang', 'south gyeongsang', 'jeju', 'hovedstaden', 'midtjylland', 'nordjylland',
         'sjaelland', 'syddanmark', 'bogota', 'amazonas', 'antioquia', 'arauca', 'atlantico', 'bolivar', 'boyaca',
         'caldas', 'caqueta', 'casanare', 'cauca', 'cesar\'s', 'choco', 'cordoba', 'cundinamarca', 'guainia',
         "guaviare's", 'huila', 'la guajira', "magdalena's", 'meta', 'narino', 'norte de santander', 'putumayo',
         'quindio', 'risaralda', 'the archipelago of san andres', 'santander', 'sucre', 'tolima', 'valle del cauca',
         'vaupes', 'vichada', 'cornwall county', 'hanover', 'st. elizabeth', 'st. james', 'trelawny', 'westmoreland',
         'middlesex county', 'clarendon', 'manchester', 'saint ann', 'st catherine', 'saint mary', 'surrey county',
         'kingston', 'portland', 'saint andrew', 'saint thomas', 'greater reykjavik', 'southern peninsula',
         'western region', 'westfjords', ' northwestern region', 'northeastern region', 'eastern region',
         'southern region', 'aleppo', 'raqqa', 'as-suwayda', 'damascus', 'daraa', 'deir ez-zor', 'hama', 'al-hasakah',
         'homs', 'idlib', 'latakia', 'quneitra', 'rif dimashq', 'tartus', 'aveiro', 'beja', 'braga', 'braganca',
         'castelo branco', 'coimbra', 'evora', 'faro', 'guarda', 'leiria', 'lisbon', 'portalegre', 'porto', 'santarem',
         'setubal', 'viana do castelo', 'vila real', 'viseu', 'the azores', 'madeira', 'adrar', 'chlef', 'laghouat',
         'oum el bouaghi', 'batna', 'bejaia', 'biskra', 'bechar', 'blida', 'bouira', 'tamanrasset', 'tebessa',
         'tlemcen', ' tiaret', 'tizi', 'algiers', 'djelfa', 'jijel', 'setif', 'saida', 'skikda', 'sidi belbsabbes',
         'annaba', 'guelma', 'constantine', 'medea', 'mostaganem', "m'sila", 'mascara', 'ouargla', 'oran', 'el bayadh',
         'illizi', 'bordj bou arreridj', 'boumerdes', 'el taref', 'tindouf', 'tissemsilt', 'el oued', 'khenchela',
         'souk ahras', 'tipaza', 'mila', 'ain defla', 'naama', 'ain temouchent', 'relizane', 'cherkasy', 'chernihiv',
         'chernivtsi', 'dnipropetrovsk', 'donetsk', 'ivano-frankivsk ', 'kharkiv', 'kherson', 'khmelnytskyi', 'kiev',
         'kirovohrad', 'luhansk', 'lviv', 'mykolaiv', 'odessa', 'poltava', 'rivne', 'sumy', 'ternopil', 'vinnytsia',
         'volyn', 'zakarpattia', 'zaporizhia', 'zhytomyr', 'crimea', 'kiev', 'flemish region', 'antwerp',
         'east flanders', 'flemish brabant', 'limburg', 'west flanders', 'walloon region', 'hainaut', 'liege',
         'luxembourg', 'namur', 'walloon brabant', 'brussels region', 'saint george', 'saint john', 'saint mary',
         'saint paul', 'saint peter', 'saint philip', 'redonda', 'attica', ' central greece', 'central macedonia',
         'crete', 'eastern macedonia and thrace', 'epirus', ' ionian islands', 'north aegean', 'peloponnese',
         'south aegean', 'thessaly', 'western greece', 'western macedonia', 'maount athos', 'barisal', 'chittagong',
         'dhaka', 'khulna', 'mymensingh', 'rajshahi', 'rangpur', 'sylhet', 'alborz', 'ardabil', 'east azerbaijan',
         'west azerbaijan', 'bushehr', 'chaharmahal and bakhtiari', 'pars', 'gilan', 'golestan', 'hamadan', 'hormozgan',
         'Ilam', 'Isfahan', 'Kerman', 'Kermanshah', 'North Khorasan', 'Razavi Khorasan', 'South Khorasan', 'Khuzestan',
         'Kohgiluyeh and Boyer-Ahmad', 'Kurdistan', 'Lorestan', 'Markazi', 'Mazandaran', 'Qazvin', 'Qom', 'Semnan',
         'Sistan and Baluchestan', 'Tehran', 'Yazd', 'Zanjan', 'Amazonas', 'Anzoategui', 'Apure', 'Aragua', 'Barinas',
         'Bolivar', 'Carabobo', 'Cojedes', 'Delta Amacuro', 'Falcon', 'Guarico', 'Lara', 'Merida', 'Miranda', 'Monagas',
         'Nueva Esparta', 'Portuguesa', 'Sucre', 'Tachira', 'Trujillo', 'Vargas', 'Yaracuy', 'Zulia',
         'taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu']
while True:
    clue = []
    index = 0
    secret_word = random.choice(words)
    secret_word = secret_word.lower()
    while index < len(secret_word):
        clue.append("?")
        index += 1
    heart_symbol = u'\u2764'
    guessed_word_correctly = False
    unknown_letters = len(secret_word)


    def update_clue(guessed_letter, the_secret_word, thread, unknown_letter):
        exponent = 0
        while exponent < len(the_secret_word):
            if guessed_letter == the_secret_word[exponent]:
                thread[exponent] = guessed_letter
                unknown_letter -= 1
            exponent += 1
        return unknown_letter


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
    print(
        '規則: \n 1.本遊戲是用英文輸入法玩的，用中文輸入法的話程式是不會理你的。\n 2.在這個遊戲裡你要猜出謎底是甚麼\n 3.請用快樂的心情玩\n 4.本遊戲有時會出現 \' . - 和\' \'\n '
        '5.本遊戲在測試階段，有錯誤敬請見諒\n                                                       吳焌脩上')
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
    count = {x: sum([1 for char in ip_str if char == x]) for x in "abcdefghijklmnopqrstuvwxyz.'- "}
    print(count)
    response = input('你想在玩一遍嗎? 輸入 要 或 不要: ')
    if response == '不要':
        break
    elif response == '':
        break
