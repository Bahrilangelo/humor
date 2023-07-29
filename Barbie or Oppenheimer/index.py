def movie(x):
    if x == 'Barbie':
        return 'Barbie'
    elif x == 'Oppenheimer':
        return 'Oppenheimer'
    else:
        return 'Error'

def barbie():
    print('Why you select the barbie?')
    print("Aren't you a man?")
    z = input('Now make an explanation (r: For Ryan gosling, m: For Margot robbie, o: Other): ')
    if z == 'r':
        print('Oh thats acceptable reson')
    elif z == 'm':
        print('Hmmm i dont like this reson')
    elif z == 'o':
        print('Okey you arent man')
    else:
        print('Error')

def oppenheimer():
    print('Few people laughed, few people cryed, most people in silent')
    print('BOOOOOOOOMMMMMMM *Fat boy is launched')