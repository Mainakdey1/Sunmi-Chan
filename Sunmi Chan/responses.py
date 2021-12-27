from datetime import datetime
#this block contains all the responses that the bot has
#simply changing the user_message constants will add or modify the bot responses

def s_responses(input_text):
    user_message=str(input_text).lower()
    if user_message in ("hello","hi","sup","whats up","hey"):

        return "hey,how's it going?"
    if user_message in ("who are you", " what's your name","who you","what is your name","tell me about yourself"):
        return " I'm Sunmi chan, and i manage telegram and trello functions. Tell me something about you "
    if user_message in ("why do you exist?","what is your purpose"):
        return ("i exist to learn from others, and help others accomplish their goals")    
    if user_message in ("fine", "good"):
        return " That's great to hear "
    return  "nahane jao nahane"
      
