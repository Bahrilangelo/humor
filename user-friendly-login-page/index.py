def login(password):
    mylist = []
    number = [0,1,2,3,4,5,6,7,8,9]
    letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    consecutive = ''
    for i in str(password):
        mylist.append(i)
    for k in range(len(str(password)) - 2):
        if mylist[k] in number and mylist[k + 1] + 1 in number and mylist[k + 2] in number:
            z = number.index(mylist[k])
            if z + 1 == number.index(mylist[k + 1]) and z + 2 == number.index(mylist[k + 2]):
                consecutive = 'False'
            else:
                consecutive = 'True'
        elif mylist[k] in letter and mylist[k + 1] in letter and mylist[k + 2] in letter:
            z = letter.index(mylist[k])
            if z + 1 == letter.index(mylist[k + 1]) and z + 2 == letter.index(mylist[k + 2]):
                consecutive = 'False'
            else:
                consecutive = 'True'
    if len(str(password)) < 8 or mylist not in letter or mylist not in number or consecutive == 'False':
        print("Your password is not strong enough. Even my grandma creates a stronger password loser.")
    else:
        print("Wow your pass is almost excellent.")
