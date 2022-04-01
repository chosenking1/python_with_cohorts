# Author: Joshua
# Title :

import datetime
import json
import os
import random
import time


def chatbot():
    response = "yes"
    while response == "yes":

        question = input("What's that your question sef?\n").split()

        data = open("C:/Users/ADMIN/OneDrive/Documents/Various_files/chatty.json", )

        dictionary = json.load(data)
        # dictionary = {
        #     "time": ["The time is " + str(datetime.datetime.now().time()), "Go buy wristwatch"],
        #     "name": ["Siri", "Sam", "Alexa", "Ask me something else biko"],
        #     "love": ["Ja, ich liebe dich!", "Nein, ich liebe dich nicht", "Scheiße", "Love is wicked"],
        #     "eat": ["Yeah, baby!", "Nah 😢"],
        #     "single": ["I'm single as feck", "It's like I'm in one relationship like that joor"],
        #     "programs": ["I write python sometimes", "I'm learning java", "I can't kill myself on golang",
        #                  "C# is unnecessarily hard"],
        #     "emotion": ["Happy", "Grumpy", "Sad", "Terrible", "Upbeat", "Angry"],
        #     "country": ["I've been to Canada", "Maybe the UK", "Lovely Kenya", "Extremely beautiful Latvia"],
        #     "job": ["I work at Google", "I work at Facebook", "I work at Twitter", "I work at Netflix"],
        #     "sister": ["My sister is Rebecca", "My sister is Bidemi", "My sister is Maryann", "My sister is Tofunmi"],
        #     "age": ["I am " + str(random.randint(1, 100)) + " years old"],
        #     "play": ["It depends tho", "Biko leave me alone joor", "Make I daze you?!"],
        #     "sleep": ["I rarely sleep mehn", "I can't shutdown, I can only have a 10sec power nap daily"],
        #     "hibernate" : [os.system("shutdown /h")]
        # }

        reply = []

        question = [x.lower() for x in question]

        if ["exit"] == question:
            print("Existing...")
            break

        for key in question:

            if key in dictionary.keys():
                reply.append(random.choice(dictionary[key]))

                if reply:
                    print(random.choice(reply))
                else:
                    print("Ogbeni, don't stress me.... Ask better question biko!")

        time.sleep(1)
        print()

        response = input("Do you want to chat more? (yes or no)\n").lower()
        if response == 'no':
            print("Bye!")


chatbot()
