def Main():
  import re
  import random as r
  import time as t
  from datetime import datetime as d
  from datetime import timezone
  import webbrowser
  import os
  import pytz
  from PyDictionary import PyDictionary
  import csv
  from getpass import getpass as g
  dictionary = PyDictionary()
  os.environ['TZ'] = 'Asia/Kolkata'
  t.tzset()
  IST = pytz.timezone('Asia/Kolkata')
  def timothy():
    x = eval(str(d.now(timezone.utc).astimezone(IST).isoformat())[11:13])
    if x >= 0 and x < 12:
      return "Good Morning"
    elif x == 12:
      return "Good Noon "
    elif x >= 12 and x <= 16:
      return "Good Afternoon"
    elif x > 16:
      return "Good Evening"
  def tim():
    x = eval(str(d.now(timezone.utc).astimezone(IST).isoformat())[11:13])
    if x >= 20:
      return True
    else:
      return False
  def clear():
    # for windows
    if os.name == 'nt':
      _ = os.system('cls')
    # for mac and linux
    else:
      _ = os.system('clear')
  def table(Table):
    for i in range(1, 11):
      print(f"{Table} × {i}  =  {Table*i}")
  def unknown():
    response = [
      "Could you please re-phrase that? ", "...", "Sounds about right.",
      "What does that mean?", "Don't know what you say?"
    ][r.randrange(5)]
    return response
  def message_probability(user_message,
                          recognised_words,
                          s_response=False,
                          required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
      if word in recognised_words:
        message_certainty += 1
    percentage = float(message_certainty) / float(len(recognised_words))
    for word in required_words:
      if word not in user_message:
        has_required_words = False
        break
    if has_required_words or s_response:
      return int(percentage * 100)
    else:
      return 0
  def check_all_messages(message, bot, creator):
    highest_prob = {}

    def response(bot_response,
                 list_of_words,
                 s_response=False,
                 required_words=[]):
      nonlocal highest_prob, bot
      highest_prob[bot_response] = message_probability(message, list_of_words,
                                                       s_response,
                                                       required_words)

    #1
    response("I'm Sorry", ["bad", "joke"],
             s_response=False,
             required_words=['bad', 'joke'])
    #2
    response("Thank You", ["good", "joke"],
             s_response=False,
             required_words=["good", "joke"])
    #3
    response(["Ok", "Okay", "OK"][r.randrange(3)], ['yes'],
             s_response=True,
             required_words=['yes'])
    #4
    response(["Ok", "Okay", "OK"][r.randrange(3)], ['no'],
             s_response=True,
             required_words=['no'])
    #5
    response(["Ok", "Okay", "OK"][r.randrange(3)], ['ok', 'okay'],
             s_response=True,
             required_words=['ok', 'okay'])
    #6
    response([
      f'Hi, my name is {bot} obviously!',
      f'My name is {bot} can change it if you want to, just say: change your name to ....',
      f"People call me {bot} what do they call you ?"
    ][r.randrange(3)], ['what', 'is', 'your', 'name', 'what\'s'],
             s_response=False,
             required_words=['your', 'name'])
    #8
    response("Hello! I'm " + bot + " How are You?",
             ['hello', 'hi', 'hey', 'sup', 'heyo'],
             s_response=True)
    #9
    response(['See you!', 'Bye bye', 'Bye :)', 'Sayonara'][r.randrange(4)],
             ['bye', 'goodbye'],
             s_response=True)
    #10
    response([
      'I\'m doing fine, and you?', 'Just fine', 'I am fine how are you?'
    ][r.randrange(3)], ['how', 'are', 'you', 'doing'],
             required_words=['how'])
    #11
    response('You\'re welcome!', ['thank', 'thanks', 'you'], s_response=False)
    #12
    response('Yes sirrrr', ['change', 'your', 'name', 'to'],
             s_response=True,
             required_words=['change', 'your', 'name', 'to'])
    #13
    response('What is your name?', ["i", "am", "fine"],
             s_response=False,
             required_words=['i', 'am', 'fine'])
    #14
    response(
      "You know, I am just a scripted bot. You should ask this question to your mother, or maybe Google.",
      ['give', 'advice'],
      required_words=['advice'])
    #15
    response(
      ["My favorite meal is bytes of information.",
       "I eat your computer"][r.randrange(2)], ['what', 'you', 'eat', 'do'],
      required_words=['you', 'eat'])
    #16
    response([
      "My favorite meal is bytes of information.", "I eat your computer"
    ][r.randrange(2)], ['what', 'you', 'eat', 'do'],
             ['what', 'your', 'food', 'eat'],
             required_words=['food', 'what'])
    #17
    response("table", ["make", "write", "table"],
             s_response=False,
             required_words=["table"])
    #18
    response("calc", ["calculate", "solve"], s_response=True)
    #19
    response("solve", ["solve", "sums", "for", "me"],
             s_response=False,
             required_words=["solve", "sums"])
    #20
    response("search", ["search"], required_words=["search"])
    #21
    response("math", ["give", "me", "sum"],
             s_response=False,
             required_words=["give", "sum"])
    #22
    response("clear", ["clear"], s_response=True)
    #23
    response(f"I am a chatbot named {bot} designed by {creator}",
             ["who", "are", "you"],
             required_words=["who", "are", "you"])
    #24
    response(f"I am a chatbot named {bot} designed by {creator}",
             ["what", "are", "you"],
             required_words=["what", "are", "you"])
    #25
    response(str(d.now().date()), ["what", "is", "the", "date"],
             required_words=["date"])
    #26
    response(str(d.now().time()), ["what", "is", "the", "time"],
             required_words=["time"])
    #27
    response("meaning", ["what", "is", "the", "meaning", "of"],
             required_words=["meaning"])
    #28
    response("synonym", ["what", "is", "the", "synonym", "of"],
             required_words=["synonym"])
    #29
    response("antonym", ["what", "is", "the", "antonym", "of"],
             required_words=["antonym"])
    #30
    response("goodn",
             ["good", "evening", "night", "morning", "noon", "afternoon"],
             required_words=["good"])
    best_match = max(highest_prob, key=highest_prob.get)
    return unknown() if highest_prob[best_match] < 1 else best_match
  def get_response(user_input, bot, creator):
    split_message = re.split(r'\s+|[,;?!\."-]\s*', user_input.lower())
    response = check_all_messages(split_message, bot, creator)
    return response
  def filesearch(roar, f, us, u, lister):
    for row in csv.reader(f):
      if us == row[roar]:
        clear()
        us = input(f"{u.title()} already taken\nEnter a different {u}\n")
        filesearch(roar, f, us, u)
    lister += [us]
    return True
  def fileresearch(f):
    username = input("Enter your username:\n")
    passwd = g("Password:\n")
    for row in csv.reader(f):
      if username == row[0] and passwd == row[1]:
        return row[2]
    clear()
    print("Incorrect Username or Password")
    fileresearch(f)
  def Login(bot):
    entity = input(f'{bot.title()}:Do you have an account Y/N\n').upper()
    if entity == "Y":
      with open("Login.csv", 'r') as f:
        Username_ = fileresearch(f)
        return Username_
    elif entity == "N":
      with open("Login.csv", "a+") as f:
        f.seek(2)
        liste = []
        username = input("Create your username:\n")
        annexe = filesearch(0, f, username, "userme", liste)
        passwd = g("Password:\n")
        annex = filesearch(1, f, passwd, "password", liste)
        if annexe and annex:
          Username_ = input("Enter name:\n")
          liste += [Username_]
        csv.writer(f, delimiter=',').writerow(liste)
        return Username_
  def Mains():
    Creator = "Aryan"
    bot = 'Roast'
    Username_ = Login(bot)
    clear()
    print(f'{bot.title()}: {timothy()} to {Username_}')
    while True:
      try:
        l = input(Username_ + ': ')
        k = re.split(r'\s+|[,;?!\."-]\s*', l.lower())
        sett = get_response(l, bot, Creator)
        if sett == "I eat your computer":
          print(f'{bot.title()}: {sett}')
          t.sleep(1)
          print(f"{bot.title()}: JK")
        elif sett == 'Yes sir':
          print(f'{bot.title()}: {sett}')
          bot = str(l.lower().split()[-1].title())
        elif sett == "People call me " + bot + " what do they call you ?" or sett == 'What is your name?':
          print(f'{bot.title()}: {sett}')
          l = input(f'{Username_.title()}: ')
          if len(l) >= 7:
            print(f'{bot.title()}: What a big name!!')
          Username_ = l.title()
        elif sett == "table":
          print(f'{bot.title()}:')
          table(float(l.split()[-1]))
        elif sett == "calc":
          ttn = ''
          for i in l.split():
            if i.lower() == "calculate" or i.lower() == "solve":
              pass
            else:
              ttn += i
          print(f'{bot.title()}: {eval(ttn)}')
        elif sett == "solve":
          print(f'{bot.title()}: Enter your sum')
          lttt = eval(input(f'{Username_.title()}'))
          print(f'{bot.title()}: {lttt}:')
        elif sett == "math":
          v = r.randrange(1, 5)
          if v == 1:
            lnn = f'{r.randint(1,10)}{["+","-","*","/","**"][r.randrange(5)]}{r.randint(1,10)}'
          elif v == 2:
            lnn = f'{r.randint(1,10)}{["+","-","*","/","**"][r.randrange(5)]}{r.randint(1,10)}{["+","-","*","/","**"][r.randrange(5)]}{r.randint(1,10)}'
          elif v == 3:
            lnn = f'{r.randint(1,10)}{["+","-","*","/","**"][r.randrange(5)]}{r.randint(1,10)}{["+","-","*","/","**"][r.randrange(5)]}{r.randint(1,10)}{["+","-","*","/","**"][r.randrange(5)]}{r.randint(1,10)}'
          elif v == 4:
            lnn = f'{r.randint(1,10)}{["+","-","*","/","**"][r.randrange(5)]}{r.randint(1,10)}{["+","-","*","/","**"][r.randrange(5)]}{r.randint(1,10)}{["+","-","*","/","**"][r.randrange(5)]}{r.randint(1,10)}{["+","-","*","/","**"][r.randrange(5)]}{r.randint(1,10)}'
          print(f'{bot.title()}: Solve {lnn}')
          lttt = eval(input(f'{Username_}:'))
          if int(eval(lnn)) == lttt or eval(lnn) == lttt:
            print(f'{bot.title()}: You are correct')
          else:
            print(f'{bot.title()}: You are wrong, the answer is {eval(lnn)}')
        elif sett == "search":
          l = l.replace(" ", "+")
          xnt = l.lower().replace("search+", "")
          webbrowser.open(f'http://www.google.com/search?q={xnt}')
        elif sett == "clear":
          clear()
        elif sett in ['See you!', 'Bye bye', 'Bye :)', 'Sayonara']:
          if tim() == True:
            print(f'{bot.title()}: Good Night')
          else:
            print(f'{bot.title()}: {sett}')
        elif sett == "meaning":
          k = re.split(r'\s+|[,;?!\."-]\s*', l.lower())
          for i in ["what", "is", "the", "meaning", "of", "dictionary"]:
            if i in k:
              k.remove(i)
          word = ''
          for j in k:
            word += j
          print(
            f'{bot.title()}: Meaning of {word} is {dictionary.meaning(f"{word}")}'
          )
        elif sett == "synonym":
          k = re.split(r'\s+|[,;?!\."-]\s*', l.lower())
          for i in ["what", "is", "the", "synonym", "of"]:
            if i in k:
              k.remove(i)
          word = ''
          for j in k:
            word += j
          print(
            f'{bot.title()}: Synonym of {word} is {dictionary.synonym(f"{word}")}'
          )
        elif sett == "antonym":
          k = re.split(r'\s+|[,;?!\."-]\s*', l.lower())
          for i in ["what", "is", "the", "antonym", "of"]:
            if i in k:
              k.remove(i)
          word = ''
          for j in k:
            word += j
          print(
            f'{bot.title()}: Antonym of {word} is {dictionary.antonym(f"{word}")}'
          )
        elif sett == "goodn":
          ntt = ""
          for i in k:
            if i in [
                "good", "evening", "night", "morning", "noon", "afternoon"
            ]:
              ntt += f"{i.title()} "
          if timothy().lower() == ntt:
            print(f'{bot}: {timothy()}')
          else:
            print(f'You should say {timothy()} not {ntt}')
        else:
          print(f'{bot.title()}: {sett}')
      except Exception:
        print(f'{bot.title()}: {unknown()}')
  if __name__ == '__main__':
    Mains()
if __name__ == '__main__':
  Main()