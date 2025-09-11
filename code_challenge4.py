print(" Welcome to the Manga Reader Recommender!")
print("Answer a few question.")

genre = str(input("What genre that you like? (action,comedy,sports): "))
length = str(input("How long this should manga be?(short,medium,long): "))
decade = eval(input("Which decade(2005,2020): "))

#ACTIION 
if genre.lower() == "action": 
    if length.lower() == "short":
        if decade == 2005:
            print("We Recommend: Dog's Bullets & Carnage")
        elif decade == 2020:
            print("We Recommend: Time Paradox Ghostwriter")



if genre.lower() == "action":
    if length.lower() == "medium":
        if decade == 2005:
            print("WE RECOMMEND: Air Gear")
        elif decade == 2020:
            print("WE RECOMMEND: Akatsuki no Inu")



if genre.lower() == "action":
    if length.lower() == "long":
        if decade == 2005:
            print("WE RECOMMEND: Bleach")
        elif decade == 2020:
            print("WE RECOMMEND: Tokyo Duel")






#COMEDY 
if genre.lower() == "comedy":
    if length.lower() == "short":
        if decade == 2005:
            print("We Recommend: Angel Densetsu")
        elif decade == 2020:
            print("We Recommend: My Senpai is Annoying"
                            " (Senpai ga Uzai Kouhai no Hanashi)")



if genre.lower() == "comedy":
    if length.lower() == "medium":
        if decade == 2005:
            print("We Recommend: Cromartie High School"
                            " (Sakigake!! Cromartie Koukou)")
        elif decade == 2020:
            print("We Recommend: Don't Toy with Me, Miss Nagatoro"
                            " (Ijiranaide, Nagatoro-san)")


if genre.lower() == "comedy":
    if length.lower() == "long":
        if decade == 2005:
            print("We Recommend: Gintama")
        elif decade == 2020:
            print("We Recommend: Kaguya-sama: Love is War"
                            " (Kaguya-sama wa Kokurasetai: Tensai-tachi no Renai Zunousen")






#SPORTS 
if genre.lower() == "sports":
    if length.lower() == "short":
        if decade == 2005:
            print("We Recommend: Hajime no Ippo")
        elif decade == 2020:
            print("We Recommend: Run with the Wind"
                            " (Kaze ga Tsuyoku Fuiteiru)")



if genre.lower() == "sports":
    if length.lower() == "medium":
        if decade == 2005:
            print("We Recommend: Big Windup!")
        elif decade == 2020:
            print("We Recommend: Sk8 the Infinity")


if genre.lower() == "sports":
    if length.lower() == "long":
        if decade == 2005:
            print("We Recommend: Eyeshield 21")
        elif decade == 2020:
            print("We Recommend: Haikyuu!!")

if decade != 2005 and decade != 2020:
     print("Sorry, we don't have any recommendations for that decade.")
if genre.lower() != "action" and genre.lower() != "comedy" and genre.lower() != "sports":
        print("Sorry, we don't have any recommendations for that genre.")
if length.lower() != "short" and length.lower() != "medium" and length.lower() != "long":
        print("Sorry, we don't have any recommendations for that length.")