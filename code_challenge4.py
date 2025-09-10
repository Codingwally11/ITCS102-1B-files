print(" Welcome to the Manga Reader Recommender!")
print("Answer a few question.")

genre = str(input("What genre that you like? (action,comedy,sports): "))
length = str(input("How long this should manga be?(short,medium,long): "))
decade = eval(input("Which decade(2005,2020): "))
#ACTIION 1
if genre == "action":
    if length == "short":
        if decade == 2005:
            print("We Recommend: Dog's Bullets & Carnage")
        else:
            ("NOT AVAILABLE FOR NOW")

if genre == "action":
    if length == "medium":
        if decade == 2005:
            print("WE RECOMMEND: Air Gear")


if genre == "action":
    if length == "long":
        if decade == 2005:
            print("WE RECOMMEND: Bleach")


#ACTION 2
if genre == "action":
    if length == "short":
        if decade == 2020:
            print("WE RECOMMEND: Time Paradox Ghostwriter")


if genre == "action":
    if length == "medium":
        if decade == 2020:
            print("WE RECOMMEND: Akatsuki no Inu")


if genre == "action":
    if length == "long":
        if decade == 2020:
            print("WE RECOMMEND: Tokyo Duel")



#COMEDY 1
if genre == "comedy":
    if length == "short":
        if decade == 2005:
            print("We Recommend: Angel Densetsu")


if genre == "comedy":
    if length == "medium":
        if decade == 2005:
            print("We Recommend: Cromartie High School"
                            " (Sakigake!! Cromartie Koukou)")

if genre == "comedy":
    if length == "long":
        if decade == 2005:
            print("We Recommend: Gintama")


#COMEDY 2
if genre == "comedy":
    if length == "short":
        if decade == 2020:
            print("We Recommend: Itoyan Goto Naki")


if genre == "comedy":
    if length == "medium":
        if decade == 2020:
            print("We Recommend: Magu-chan: God of Destruction"
                                " (Hakaishin Magu-chan)")


if genre == "comedy":
    if length == "long":
        if decade == 2020:
            print("We Recommend: Sakamoto Days")



#SPORTS 1
if genre == "sports":
    if length == "short":
        if decade == 2005:
            print("We Recommend: Hajime no Ippo")


if genre == "sports":
    if length == "medium":
        if decade == 2005:
            print("We Recommend: Big Windup!")

if genre == "sports":
    if length == "long":
        if decade == 2005:
            print("We Recommend: Eyeshield 21")


#SPORTS 2
if genre == "sports":
    if length == "short":
        if decade == 2020:
            print("We Recommend: Blue Lock")


if genre == "sports":
    if length == "medium":
        if decade == 2020:
            print("We Recommend: Inazuma Eleven")


if genre == "sports":
    if length == "long":
        if decade == 2020:
            print("We Recommend: Ao Ashi")