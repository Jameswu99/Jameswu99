import random

words = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick', 'Newfoundland and Labrdor',
         'Northwest Territories', 'Nova Scotia', 'Nunavut', 'ontario', 'prince edward island', 'quebec', 'saskatchewan',
         'yukon', 'rhode island', 'delaware', 'connecticut', 'hawaii', 'new jersey', 'massachusetts', 'new hampshire',
         'vermont', 'maryland', 'west virginia', 'south carolina', 'maine', 'virginia', 'kentucky', 'ohio', 'tennessee',
         'louisiana', 'pennsylvania', 'mississippi', 'new york', 'north carolina', 'Albama', 'Arkansas', 'florida',
         'wisconsin', 'illinois', 'iowa', 'michigan', 'georgia', 'washington', 'oklahoma', 'missouri', 'north dakota',
         'south dakota', 'nebraska', 'minnesota', 'kansas', 'utah', 'idaho', 'oregon', 'wyoming', 'colorado', 'nevada',
         'Arizona', 'new mexico', 'montana', 'california', 'texas', 'Alaska', 'nord-norge', 'midt-norge', 'vestlandet',
         'sorlandet', 'ostlandet', 'ege', 'karadeniz', 'ic Anadolu', 'dogu Anadolu', 'marmara region', 'Akdeniz',
         'guneydogu Anadolu', 'stockholm', 'vasterbotten', 'norrbotten', 'uppsala', 'sodermanland', 'ostergotland',
         'jonkoping', 'kronoberg', 'kalmar', 'gotland', 'Blekinge', 'skane', 'halland', 'vastra gotaland', 'varmland',
         'orebro', 'vastmanland', 'dalarna', 'gavleborg', 'vasternorrland', 'jamtland', 'zurich', 'Bern', 'lucerne',
         'uri', 'schwyz', 'obwalden', 'nidwalden', 'glarus', 'zug', 'fribourg', 'solothurn', 'Basel-stadt',
         'Basel-landschaft', 'schaffhausen', 'Appenzell Ausserrhoden', 'Appenzell innerrhoden', 'st. gallen',
         'graubunden', 'Aargau', 'thurgau', 'ticino', 'vaud', 'valais', 'neuchatel', 'geneva', 'jura', 'matrouh',
         'Alexandria', 'Beheira', 'kafr el sheikh', 'dakahlia', 'damietta', 'port said', 'north sinai', 'gharbia',
         'monufia', 'qalyubia', 'sharqia', 'ismailia', 'giza', 'faiyum', 'cairo', 'suez', 'south sinai', 'Beni suef',
         'minya', 'new valley', 'Asyut', 'red sea', 'sohag', 'qena', 'luxor', 'Aswan', "south p'yongan",
         "north p'yongan", 'chagang', 'south hwanghae', 'north hwanghae', 'kangwon', 'south hamgyong',
         'north hamgyong', 'ryanggang', 'rason', 'seoul', 'Busan', 'daegu', 'incheon', 'gwangju', 'daejeon', 'ulsan',
         'sejong', 'gyeonggi-do', 'gangwon-do', 'north chungcheong', 'south chungcheong', 'north jeolla',
         'south jeolla', 'north gyeongsang', 'south gyeongsang', 'jeju', 'hovedstaden', 'midtjylland', 'nordjylland',
         'sjaelland', 'syddanmark', 'Bogota', 'Amazonas', 'Antioquia', 'Arauca', 'Atlantico', 'Bolivar', 'Boyaca',
         'caldas', 'caqueta', 'casanare', 'cauca', "cesar's", 'choco', 'cordoba', 'cundinamarca', 'guainia',
         "guaviare's", 'huila', 'la guajira', "magdalena's", 'meta', 'narino', 'norte de santander', 'putumayo',
         'quindio', 'risaralda', 'Archipelago of san Andres', 'santander', 'sucre', 'tolima', 'valle del cauca',
         'vaupes', 'vichada', 'cornwall county', 'hanover', 'st. elizabeth', 'st. james', 'trelawny', 'westmoreland',
         'middlesex county', 'clarendon', 'manchester', 'saint Ann', 'st catherine', 'saint mary', 'surrey county',
         'kingston', 'portland', 'saint Andrew', 'saint thomas', 'greater reykjavik', 'southern peninsula',
         'western region', 'westfjords', 'northwestern region', 'northeastern region', 'eastern region',
         'southern region', 'Aleppo', 'raqqa', 'As-suwayda', 'damascus', 'daraa', 'deir ez-zor', 'hama', 'Al-hasakah',
         'homs', 'idlib', 'latakia', 'quneitra', 'rif dimashq', 'tartus', 'Aveiro', 'Beja', 'Braga', 'Braganca',
         'castelo branco', 'coimbra', 'evora', 'faro', 'guarda', 'leiria', 'lisbon', 'portalegre', 'porto', 'santarem',
         'setubal', 'viana do castelo', 'vila real', 'viseu', 'Azores', 'madeira', 'Adrar', 'chlef', 'laghouat',
         'oum el bouaghi', 'Batna', 'Bejaia', 'Biskra', 'Bechar', 'Blida', 'Bouira', 'tamanrasset', 'tebessa',
         'tlemcen', 'tiaret', 'tizi', 'Algiers', 'djelfa', 'jijel', 'setif', 'saida', 'skikda', 'sidi belbsabbes',
         'Annaba', 'guelma', 'constantine', 'medea', 'mostaganem', "m'sila", 'mascara', 'ouargla', 'oran', 'el bayadh',
         'illizi', 'Bordj bou Arreridj', 'Boumerdes', 'el taref', 'tindouf', 'tissemsilt', 'el oued', 'khenchela',
         'souk Ahras', 'tipaza', 'mila', 'Ain defla', 'naama', 'Ain temouchent', 'relizane', 'cherkasy', 'chernihiv',
         'chernivtsi', 'dnipropetrovsk', 'donetsk', 'ivano-frankivsk', 'kharkiv', 'kherson', 'khmelnytskyi', 'kiev',
         'kirovohrad', 'luhansk', 'lviv', 'mykolaiv', 'odessa', 'poltava', 'rivne', 'sumy', 'ternopil', 'vinnytsia',
         'volyn', 'zakarpattia', 'zaporizhia', 'zhytomyr', 'crimea', 'kiev', 'flemish region', 'Antwerp',
         'east flanders', 'flemish brabant', 'limburg', 'west flanders', 'walloon region', 'hainaut', 'liege',
         'luxembourg', 'namur', 'walloon brabant', 'Brussels region', 'saint george', 'saint john', 'saint mary',
         'saint paul', 'saint peter', 'saint philip', 'redonda', 'Attica', 'central greece', 'central macedonia',
         'crete', 'eastern macedonia and thrace', 'epirus', 'ionian islands', 'north Aegean', 'peloponnese',
         'south Aegean', 'thessaly', 'western greece', 'western macedonia', 'maount Athos', 'Barisal', 'chittagong',
         'dhaka', 'khulna', 'mymensingh', 'rajshahi', 'rangpur', 'sylhet', 'Alborz', 'Ardabil', 'east Azerbaijan',
         'west Azerbaijan', 'Bushehr', 'chaharmahal and bakhtiari', 'pars', 'gilan', 'golestan', 'hamadan', 'hormozgan',
         'Ilam', 'Isfahan', 'Kerman', 'Kermanshah', 'North Khorasan', 'Razavi Khorasan', 'South Khorasan', 'Khuzestan',
         'Kohgiluyeh and Boyer-Ahmad', 'Kurdistan', 'Lorestan', 'Markazi', 'Mazandaran', 'Qazvin', 'Qom', 'Semnan',
         'Sistan and Baluchestan', 'Tehran', 'Yazd', 'Zanjan', 'Amazonas', 'Anzoategui', 'Apure', 'Aragua', 'Barinas',
         'Bolivar', 'Carabobo', 'Cojedes', 'Delta Amacuro', 'Falcon', 'Guarico', 'Lara', 'Merida', 'Miranda', 'Monagas',
         'Nueva Esparta', 'Portuguesa', 'Sucre', 'Tachira', 'Trujillo', 'Vargas', 'Yaracuy', 'Zulia', 'Bumthang',
         'Chukha', 'Dagana', 'Gasa', 'Haa', 'Lhuntse', 'Mongar', 'Paro', 'Pemagatshel', 'Punakha', 'Samdrup Jongkhar',
         'Samtse', 'Sarpang', 'Thimphu', 'Trashigang', 'Trashiyangtse', 'Trongsa', 'Tsirang', 'Wangdue Phodrang',
         'Zhemgang', 'Azad Jammu and Kashmir', 'Gilgit-Baltistan', 'Balochistan', 'Khyber Pakhtunkhwa', 'Punjab',
         'Sindh', 'Islamabad', 'Al Anbar', 'Babil', 'Baghdad', 'Basra', 'Dhi Qar', 'Al-Qadisiyah', 'Diyala', 'Dohuk',
         'Erbil', 'Halabja', 'Karbala', 'Kirkuk', 'Maysan', 'Muthanna', 'Najaf', 'Nineveh', 'Salah ad Din',
         'Sulaymaniyah', 'Wasit', 'Beni', 'Chuquisaca', 'Cochabamba', 'La Paz', 'Oruro', 'Pando', 'Potosi',
         'Santa Cruz', 'Tarija', 'taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu']
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
