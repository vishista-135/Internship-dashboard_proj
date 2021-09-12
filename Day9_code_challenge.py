import re

fh = open("simpsons_phone_book.txt", 'r')

for x in fh:
    if (re.search(r'^J\w*\s*(Neu)', x)):
        print (x)
fh.close()

