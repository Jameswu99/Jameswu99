import random

attitude = input('Do you want to type yourself or auto type?("y" for "type yourself" and "a" for "auto type"):')
mans_name = ['Camden', 'Elliot', 'Jay', 'Dillon', 'Kenyon', 'Kellen', 'Axel', 'Brady', 'Alfred', 'Muhammad',
             'Hope', 'Lucinda', 'Ann', 'Lee', 'Oliver', 'Karilyn', 'Ocean', 'Adele', 'Cody', 'Cash', 'Bullock',
             'Vargas', 'James', 'Daniel', 'Doyle', 'Sharp', 'Velez', 'Madden', 'Parsons', 'Griffith', 'Richard']
occupation_name = ['Radiologic Technologist', 'Janitor', 'Physician', 'College Professor', 'Dentist',
                   'Professional athlete', 'Personal Care Aide', 'Recreation & Fitness Worker', 'Desktop publisher',
                   'Truck Driver']
noun = ['act', 'nut', 'string', 'harbor', 'coast', 'celery', 'basket', 'action', 'market', 'cherry', 'flowers', 'loaf',
        'stove', 'support', 'burst', 'birds', 'ear', 'desire', 'toothpaste', 'sign', 'acoustics', 'quilt',
        'plantation', 'quince', 'cake', 'cable', 'example', 'lamp', 'north', 'veil', 'talk', 'number', 'advertisement',
        'adjustment', 'wood', 'bedroom', 'fire', 'star', 'pin', 'hammer', 'way', 'bikes', 'grip', 'quiet', 'marble',
        'mice', 'value', 'bells', 'vessel', 'reason', 'part', 'dime', 'book', 'guide', 'interest', 'sock', 'waves',
        'destruction', 'growth', 'shirt', 'road', 'silk', 'slave', 'self', 'powder', 'stop', 'camera', 'plot', 'dolls',
        'geese', 'tree', 'dirt', 'fuel', 'vase', 'governor', 'competition', 'women', 'pleasure', 'club', 'theory',
        'care', 'mist', 'yard', 'need', 'knot', 'cup', 'match', 'flower', 'shake', 'dad', 'poison', 'rule', 'swing',
        'frogs', 'flight', 'fly', 'key', 'cent', 'drain', 'button']
shape_name = ['irregular octagon', 'decagon', 'square-based pyramid', 'rhombus', 'hexagonal pyramid', 'cylinder',
              'nonagon', 'ellipsoid', 'octahedron', 'triangular prism', 'tetrahedron', 'dodecahedron',
              'triangular-based pyramid', 'trapezium', 'kite', 'trapezoid', 'hexahectaenneacontakaiheptagon',
              'nonanonacontanonactanonaliagon']
verb = ['extend', 'water', 'bruise', 'place', 'exist', 'shave', 'impress', 'slow', 'intend', 'stitch', 'expand',
        'borrow', 'save', 'smell', 'pretend', 'flap', 'reject', 'ignore', 'start', 'confess', 'obey', 'fail', 'crush',
        'gaze', 'clip', 'fry', 'call', 'carry', 'request', 'type', 'produce', 'trick', 'attract', 'box', 'spell',
        'twist', 'fit', 'report', 'apologise', 'arrive', 'surprise', 'breathe', 'discover', 'afford', 'repair',
        'vanish', 'soak', 'fix', 'time', 'bolt']
verbing = ['extracting', 'educating', 'organising', 'liking', 'translating', 'responding', 'facilitating', 'listening',
           'slowing', 'drawing']
womans_name = ['Charlee Abraham Daugerty', 'Mariyah Dash Stokes', 'Emerson Marcella Ritter', 'Joanna Haiden Bruce',
               'Litzy Reagan Nash', 'Reese Dustin Holmes', 'Madyson Caprice Price', 'Alyvia Louisa Shaw',
               'Jamie Gregory Bush', 'Adalynn Sean Kidd']
body_parts = ['nose', 'nostril', 'eyebrow', 'buttocks', 'calf', 'mouth', 'thumb', 'chin', 'toe', 'waist']
restaurant_names = ['Gourmand Pubhouse', 'Little Stallion Tavern', 'Rare Blossom Place', 'Blue Anchor Cucina',
                    'Artisan Honeybee Roadhouse', 'Rosy Clover Bar and Grille', 'Singing Tiger Eats',
                    'Mystic Crown Bar and Grille', 'Saffron Goblet Pub', 'Dashing Wave Pub']
historic_monument_name = ['Terracotta Army', 'Machu Picchu', 'Angkor Wat', 'Ziggurat of Ur', 'Colosseum', 'Petra',
                          'Pyramids of Meroe', "Hadrian's Wall", 'Ciudad Perdida', 'Masada']
emotion_name = ['surprise', 'melancholy', 'pain', 'longing', 'pride', 'satisfaction', 'despair', 'rage', 'gratitude',
                'sorrow']
adjective = ['invincible', 'giddy', 'perpetual', 'irritating', 'oval', 'learned', 'testy', 'delightful', 'flaky',
             'successful', 'normal', 'same', 'oafish', 'torpid', 'feeble', 'silly', 'enchanted', 'vacuous',
             'well-to-do', 'macho']
while True:
    if attitude == 'a':
        man_name = random.choice(mans_name)
        occupation = random.choice(occupation_name)
        noun1 = random.choice(noun)
        noun2 = random.choice(noun)
        noun3 = random.choice(noun)
        shape = random.choice(shape_name)
        verb1 = random.choice(verb)
        woman_name = random.choice(womans_name)
        body_part = random.choice(body_parts)
        verb2 = random.choice(verb)
        noun4 = random.choice(noun)
        noun5 = random.choice(noun)
        restaurant_name = random.choice(restaurant_names)
        historic_monument = random.choice(historic_monument_name)
        verb3 = random.choice(verb)
        noun6 = random.choice(noun)
        noun7 = random.choice(noun)
        verb4 = random.choice(verb)
        noun8 = random.choice(noun)
        adjective1 = random.choice(adjective)
        adjective2 = random.choice(adjective)
        emotion = random.choice(emotion_name)
        ving = random.choice(verbing)
        noun9 = random.choice(noun)
        noun10 = random.choice(noun)
        verb5 = random.choice(verb)
    elif attitude == 'y':
        man_name = input("Name a man's name: ")
        occupation = input("Choose a occupation: ")
        noun1 = input("Choose a noun: ")
        noun2 = input("Choose a noun: ")
        noun3 = input("Choose a noun: ")
        shape = input("Choose a shape: ")
        verb1 = input("Choose a verb: ")
        woman_name = input("Choose a woman's name: ")
        body_part = input("Choose a body part: ")
        verb2 = input("Choose a verb: ")
        noun4 = input("Choose a noun: ")
        noun5 = input("Choose a noun: ")
        restaurant_name = input("Choose a restaurant's name: ")
        historic_monument = input("Choose a historic monument: ")
        verb3 = input("Choose a verb: ")
        noun6 = input("Choose a noun: ")
        noun7 = input("Choose a noun: ")
        verb4 = input("Choose a verb: ")
        noun8 = input("Choose a noun: ")
        adjective1 = input("Choose an adjective (Describing word): ")
        adjective2 = input("Choose an adjective (Describing word): ")
        emotion = input("Choose an emotion: ")
        ving = input("Choose a present tense verb: ")
        noun9 = input("Choose a noun: ")
        noun10 = input("Choose a noun: ")
        verb5 = input("Choose a verb: ")
    print("------------------------------------------")
    print(man_name, "is a normal", occupation + ".")
    print("Then one day, a", noun1, "explodes, causing a", noun2, "to blow up, and a nearby", noun3,
          "erupts into a",
          shape, "of flames.")
    print(man_name, "realizes that he's being chased by the government, who's trying to", verb1, "him.")
    print("While on the run , he teams up with an incredibly attractive woman named", woman_name,
          ", who has an incredible", body_part, ".")
    print("She may be from the streets, but she can", verb2, "like nobody's business.")
    print("The duo decide to turn the tables on their pursuers by blowing up a", noun4,
          ", which triggers a chain reaction, causing the local " + noun5 + ", " + restaurant_name, ", and the",
          historic_monument, "to explode.")
    print("Then, the bad guys' helicopter gets", verb3, "by a piece of", noun6, "from when the", noun5,
          "exploded, and the helicopter explodes and falls onto a", noun7 + ", causing it to",
          verb4 + ", which shoots a fireball straight into the heart of", noun8, "and destroys the bad guy leader.")
    print("Everything is", adjective1, "and the two decide that such a", adjective2,
          "ordeal has caused them to fall in", emotion, "with each other.")
    print("They decide to celebrate by", ving, "on the", noun9 + " and they even managed to use a", noun10,
          "from the beginning of the movie, to", verb5, "the whole story together.")
    print("------------------------------------------")
    attitude2 = input('Do you want to do it again(y for yes and n for no):')
    if attitude2.lower() == 'n':
        print('Thank you for using the mad libs generator.')
        break
