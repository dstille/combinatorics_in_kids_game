name =  'Jude'


for i in range(name[0:2]):   # name[0:2] = 'Ju', range function needs an integer
    if i < 3:
        print(name[i])   # every time print function executes, it will set the next print statement
                         # on the next line:
                         # e.g.  J
                         #       u
                         #       d
                         # you can keep the print function from advancing to a new line by doing this:
                         # print(name[i], end = '')
        break            # break statement terminates the loop; this loop would run only one time
    else:                # unnecessary else statement
        counter = counter + 1