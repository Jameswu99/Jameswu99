import random
fruits = ['durian', 'jackfruit', 'white pitaya', 'dragon fruit', 'cherimoya'
          , 'kiwano', 'horned melon', 'korean melon', 'passion fruit', 'feijoa'
          , 'pineapple guava', 'tamarillo', 'tree tomato', 'loquat', 'sour plum'
          , 'longan', 'physalis', 'golden berries', 'mulberries', 'jujube',
          'date', 'lime']
adjectives = ['overwrought', 'helpless', 'freezing', 'great', 'flimsy', 'hurt'
              , 'reminiscent', 'difficult', 'satisfying', 'lethal']
adverbs = ['weekly', 'generally', 'tensely', 'therefore', 'usually', 'roughly'
           , 'frankly', 'greatly', 'ultimately', 'briefly', 'finally',
           'queasily']
feeling = ['hopeful', 'interested', 'worried', 'confident', 'heartbroken',
           'excited', 'confused', 'overwhelmed', 'surprised', 'happy', 'strong'
           , 'hesitant', 'loved', 'playful', 'rejected', 'stressed']
nouns = ['rat', 'cough', 'woman', 'bed', 'oranges', 'gun', 'snail', 'voice',
        'playground', 'idea']
nounpl = ['calendars', 'rabbits', 'planes', 'fingers', 'uses', 'roads',
          'degrees','coils', 'whips', 'vests']
place_name = ['city of Oran', 'city of Chaozhou', 'city of Quito'
              , 'city of Isfahan', 'city of Qom', 'Zzyzx Raod', 'city of Ptuj'
              , 'city of Qeqertarsuatsiaat', 'village of Å', 'D river']
adj1 = random.choice(adjectives)
adj2 = random.choice(adjectives)
nounpl1 = random.choice(nounpl)
place = random.choice(place_name)
adj3 = random.choice(adjectives)
adv = random.choice(adverbs)
adj4 = random.choice(adjectives)
nounpl2 = random.choice(nounpl)
feel = random.choice(feeling)
noun = random.choice(nouns)
fruit = random.choice(fruits)
nounpl3 = random.choice(nounpl)
adj5 = random.choice(adjectives)
print('The weather on this day was ' + adj1 + ' and ' + adj2 + '.')
print('After some confusing texts, phone call and '+ nounpl1
      + ', we met at the  '+ place + ', to get our kayaks.')
print('My friend dropped his ' + adj3 + " pencil and we couldn't find it.")
print('Finally, we ' + adv + ' put our boats into the ' + adj4 + ' water.')
print('I noticed there were angry ' + nounpl2
      + ' swimming around in the water, and I started to feel ' + feel + '.')
print('My friend Bob dropped his ' + noun + ' in the water, and they ate it!')
print('I started to think about going home, but Bob said I was being a ' +
      fruit + '.')
print('Finally, we got in, and dropped ' + nounpl3
      + ' into the water to scare away the ' + nounpl2 + '.')
print('It was a ' + adj5 +' day.')

