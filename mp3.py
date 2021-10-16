from pygame import mixer


def play(n):
    mixer.init()
    mixer.music.load(n)
    mixer.music.play()


def datetime():
    import datetime
    return datetime.datetime.now()


def log(string):
    time = str(datetime())
    with open("Song_log.txt", "a") as f:
        f.write(f"[{time}] : {string} \n")


def options():
    print("P-To Pause\n"
          "R-To resume\n"
          "E-To stop the current song\n")
    while True:
        query = input()
        if query == "P":
            mixer.music.pause()
        elif query == "R":
            mixer.music.unpause()
        elif query == "E":
            mixer.music.stop()
            break


print("*********************************Audio Player****************************************************\n"
      "1-Alone (Alam Walker)\n"
      "2-Believer (Imagine Dragons)\n"
      "3-Blinding Lights (The Weeknd)\n"
      "4-Capital Letters (Hailee Steinfeld)\n"
      "5-Colour (Mnek and Hailee Steinfeld)\n"
      "6-Despacito (Luis Fonsi and Daddy Yankee)\n"
      "7-Echame la Clupa (Luis Fonsi and Demi Lovato)\n"
      "8-Eenie Menie (Justin Bieber)\n"
      "9-Faded (Alan Walker)\n"
      "10-Happy\n"
      "11-Intentions (Justin Bieber)\n"
      "12-Levitating (Dua Lipa)\n"
      "13-On My Way (Alan Walker,Sabrina Carpenter and Farruko)\n"
      "14-Peaches (Justin Bieber)\n"
      "15-Roar (Katy Perry)\n"
      "16-Chantaje (Shakira)\n"
      "17-Hips Don't Lie (Shakira)\n"
      "18-Shape Of You (Ed Sheeran)\n"
      "19-South of the Border (Ed Sheeran, Camilla Cabello and Cardi B)\n"
      "20-Sunflower (Post Malone)\n"
      "21-Taki Taki (Ozuna,DJ Snake,Selena Gomez and Cardi B)\n"
      "22-Thunderclouds (Labyrinth,Sia and Diplo)\n")
program_over = False
while not program_over:
    choice = input("Enter the song you want to play : ")
    if choice == "1":
        play("Alone.mp3")
        options()
        log("1-Alone (Alam Walker)")
    elif choice == "2":
        play("Believer.mp3")
        options()
        log("2-Believer (Imagine Dragons)")
    elif choice == "3":
        play("Blinding lights.mp3")
        options()
        log("3-Blinding Lights (The Weeknd)")
    elif choice == "4":
        play("Capital Letters.mp3")
        options()
        log("4-Capital Letters (Hailee Steinfeld)")
    elif choice == "5":
        play("Colour.mp3")
        options()
        log("5-Colour (Mnek and Hailee Steinfeld)")
    elif choice == "6":
        play("Despacito.mp3")
        options()
        log("6-Despacito (Luis Fonsi and Daddy Yankee)")
    elif choice == "7":
        play("Echame la Clupa.mp3")
        options()
        log("7-Echame la Clupa (Luis Fonsi and Demi Lovato)")
    elif choice == "8":
        play("Eenie Menie.mp3")
        options()
        log("8-Eenie Menie (Justin Bieber)")
    elif choice == "9":
        play("Faded.mp3")
        options()
        log("9-Faded (Alan Walker)")
    elif choice == "10":
        play("Happy (from Despicable Me 2) G I R L - 320Kbps.mp3")
        options()
        log("10-Happy")
    if choice == "11":
        play("Intentions.mp3")
        options()
        log("11-Intentions (Justin Bieber)")
    elif choice == "12":
        play("Levitating.mp3")
        options()
        log("12-Levitating (Dua Lipa)")
    elif choice == "13":
        play("On My Way.mp3")
        options()
        log("13-On My Way (Alan Walker,Sabrina Carpenter and Farruko)")
    elif choice == "14":
        play("Peaches.mp3")
        options()
        log("14-Peaches (Justin Bieber)")
    elif choice == "15":
        play("Roar.mp3")
        options()
        log("15-Roar (Katy Perry)")
    if choice == "16":
        play("Shakira - Chantaje ft. Maluma.mp3")
        options()
        log("16-Chantaje (Shakira)")
    elif choice == "17":
        play("Shakira - Hips Don t Lie ft. Wyclef Jean.mp3")
        options()
        log("17-Hips Don't Lie (Shakira)")
    elif choice == "18":
        play("Shape_of_You .mp3")
        options()
        log("18-Shape Of You (Ed Sheeran)")
    elif choice == "19":
        play("South_of_the_Border.mp3")
        options()
        log("19-South of the Border (Ed Sheeran, Camilla Cabello and Cardi B)")
    elif choice == "20":
        play("Sunflower.mp3")
        options()
        log("20-Sunflower (Post Malone)")
    elif choice == "21":
        play("Taki Taki.mp3")
        options()
        log("21-Taki Taki (Ozuna,DJ Snake,Selena Gomez and Cardi B)")
    elif choice == "22":
        play("Thunderclouds.mp3")
        options()
        log("22-Thunderclouds (Labyrinth,Sia and Diplo)")
    print("Do you want to continue(Y/N)?")
    choice2 = input()
    if choice2 == "Y" or choice2=="y":
        continue
    elif choice2=="N" or choice2=="n":
        program_over = True
    else:
        print("Invalid Input")
        continue
