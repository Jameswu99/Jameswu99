import time
import random
loading_number_list = [0, 1]
times = ["1.0", "1.5", "2.0", "2.5", "3.0", "3.5", "4.0"]
Line_history = {"0": "Sorry the line isn't been built or the number is invalid", "1": "test test 1 2 3 "
                , "2": "test test 1 2 3", "3": "test test 1 2 3", "4": "test test 1 2 3", "5": "test test 1 2 3"
                , "6": "test test 1 2 3", "7": "test test 1 2 3", "8": "test test 1 2 3", "9": "test test 1 2 3"
                , "10": "test test 1 2 3", "11": "test test 1 2 3", "12": "test test 1 2 3", "13": "test test 1 2 3"
                , "14": "test test 1 2 3", "15": "test test 1 2 3", "16": "test test 1 2 3", "17": "test test 1 2 3"
                , "18": "test test 1 2 3", "19": "test test 1 2 3", "20": "test test 1 2 3", "21": "test test 1 2 3"
                , "22": "test test 1 2 3", "23": "test test 1 2 3", "24": "test test 1 2 3", "25": "test test 1 2 3"
                , "26": "test test 1 2 3", "27": "test test 1 2 3", "28": "test test 1 2 3", "29": "test test 1 2 3"
                , "30": "test test 1 2 3", "31": "test test 1 2 3", "32": "test test 1 2 3", "33": "test test 1 2 3"
                , "34": "test test 1 2 3", "35": "test test 1 2 3", "36": "test test 1 2 3", "37": "test test 1 2 3"
                , "38": "test test 1 2 3", "39": "test test 1 2 3", "40": "test test 1 2 3", "41": "test test 1 2 3"
                , "42": "test test 1 2 3", "43": "test test 1 2 3", "44": "test test 1 2 3", "45": "test test 1 2 3"
                , "46": "test test 1 2 3", "47": "test test 1 2 3"
                , "BA": "test test 1 2 3", "NHS": "test test 1 2 3", "HS": "test test 1 2 3"}
while True:
    Line_number = str(input("Choose a line number between 1 and 47, BA and NHS and HS:"))
    if Line_number == "BA" or Line_number == "NHS" or Line_number == "HS" or 0 < int(Line_number) < 48:
        loading_number = random.choice(loading_number_list)
        if loading_number == 0:
            print("loading .      0%")
            time.sleep(float(random.choice(times)))
            print("loading ..    25%")
            time.sleep(float(random.choice(times)))
            print("loading ...   50%")
            time.sleep(float(random.choice(times)))
            print("loading .     75%")
            time.sleep(float(random.choice(times)))
            print("loading ..    99%")
            print("loading ...  100%")
        elif loading_number == 1:
            pass
        print(Line_history[str(Line_number)])
    elif int(Line_number) <= 0 or int(Line_number) > 47:
        loading_number = random.choice(loading_number_list)
        if loading_number == 0:
            print("loading .      0%")
            time.sleep(float(random.choice(times)))
            print("loading ..    25%")
            time.sleep(float(random.choice(times)))
            print("loading ...   50%")
            time.sleep(float(random.choice(times)))
            print("loading .     75%")
            time.sleep(float(random.choice(times)))
            print("loading ..    99%")
            print("loading ...  100%")
        elif loading_number == 1:
            pass
        Line_number = 0
        print(Line_history[str(Line_number)])
    option = input("Do you want to see another line's history? (type yes or no):")
    if option.lower() == "no":
        break
