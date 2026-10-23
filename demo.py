#My book
library=[]
book1=input("Enter name of a book you own: ")
book2=input("enter the name of another book you own (or press 'enter'to skip) ")
library.append(book1)
library.append(book2)
print(f"Your library: {library}")

#My Wishlist
wishlist=[]
bok1=input("Enter the name of book you wish to have in the future: ")
bok2=input("Enter the name of another book you wish (or press 'enter'to skip) ")
wishlist.append(bok1)
wishlist.append(bok2)
print(f"your wishlist{wishlist}")

book3=input ("enter the name of a book from your wish list that you've a quired (or press'enter'to skip)")
if book3 in wishlist:
    wishlist.remove(book3)
    library.append(book3)
    print(f"Updated Library:{library}" )
    print(f"Updated wishlist{wishlist}")
else:
    print(f"wishlist{wishlist}\nlibrary {library}")
book4=input("Enter the name of a book from your library you wish to don ate (or press enter to skip):" )


if book4 in library:
    library.remove(book4)
    print(f"final library after Donations:{library}")
else:
    print(f"final library after Donations:{library}")
