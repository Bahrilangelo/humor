# H huh what is the n word..?
# Dude if you say this word by the black people proably you will die :D
# Man i'll write a code for a censor the n letter. 
# Wow interesting solution but it seems work :D

def censor(sentence):
    ans = ""
    for i in sentence:
        if i == "n":
            ans += "*"
        else:
            ans += i
    return ans 

print(censor('Hello new world!'))