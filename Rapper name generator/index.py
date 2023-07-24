import random
def nameGenerator(name):
    names = 'lil-'
    names += random.choice(name.lower())
    names += random.choice(name.lower())
    names += random.choice(name.lower())

    return names

print(nameGenerator('Bahri'))