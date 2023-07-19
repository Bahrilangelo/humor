import time
current_year = time.localtime().tm_year
def main(birthYear):
    if current_year - birthYear >= 18:
        print('Yeah man this is a legal enjoy')
    else:
        print('oww man i called cops, can you hear the siren sound')