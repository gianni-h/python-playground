print('''
 ********************************************************************************
*                    /   \              /'\       _                              *
*\_..           /'.,/     \_         .,'   \     / \_                            *
*    \         /            \      _/       \_  /    \     _                     *
*     \__,.   /              \    /           \/.,   _|  _/ \                    *
*          \_/                \  /',.,''\      \_ \_/  \/    \                   *
*                           _  \/   /    ',../',.\    _/      \                  *
*             /           _/m\  \  /    |         \  /.,/'\   _\                 *
*           _/           /MMmm\  \_     |          \/      \_/  \                *
*          /      \     |MMMMmm|   \__   \          \_       \   \_              *
*                  \   /MMMMMMm|      \   \           \       \    \             *
*                   \  |MMMMMMmm\      \___            \_      \_   \            *
*                    \|MMMMMMMMmm|____.'  /\_            \       \   \_          *
*                    /'.,___________...,,'   \            \   \        \         *
*                   /       \          |      \    |__     \   \_       \        *
*                 _/        |           \      \_     \     \    \       \_      *
*                /                               \     \     \_   \        \     *
*                                                 \     \      \   \__      \    *
*                                                  \     \_     \     \      \   *
*                                                   |      \     \     \      \  *
*                                                    \ms          |            \ *
 ********************************************************************************
''')
print("Welcome to the Cave of the Dragons.")
name = input("What is your name? ")
print("\n")
print(f"Welcome, {name}. You're adventure starts at the entrance of the Cave of the Dragons.")
print("From here on, you shall descend deep into the cave to find the Golden Egg.")
print("But beware of the Dragons guarding the Egg. Some are friendly, others not so much.")
print("Good luck and safe travels, Warrior.")
print("######################################################################################")
print("\n")
position = "start"
print("You are outisde the entrance of the Cave of the Dragons. You are holding a torch.\n"
      "For some odd reason your feet only walk forward and you cannot turn back..."
'''There is a sign next to the entrance:
_______________________________________
|   This is a command based game.     |
|   You move through this game        |
|   by typing the following commands. |
| Movement:                           |
|    North (n): move north            |
|    East (e): move east              |
|    South (s): move south            |
|    West (w): move west              |
|#Travellers who entered the cave: 76 |
|#Travellers who got out: 0           |
|_____________________________________|
                //
                //
                //
                //
''')
move = input()
if move.lower() == "north" or move.lower() == "n":                                          #enters cave -> continue
    position = "entrance"
    print("You entered the Cave. There are spiders and other critters quickly crawling away.\n"
           "There are 2 tunnels. One goes North, one East. ")
    move = input()
    if move.lower() == "north" or move.lower() == "n":                                      #deathstalker scorpio -> dead
      print("You entered the Northern tunnel.")
      print("\n")
      print("\n")
      print("...")
      print("\n")
      art_deathstalker = r"""
       ___ __
     _{___{__}\
    {_}      `\)
   {_}        `            _.-''''--.._
   {_}                    //'.--.  \___`.
    { }__,_.--~~~-~~~-~~-::.---. `-.\  `.)
     `-.{_{_{_{_{_{_{_{_//  -- 8;=- `
        `-:,_.:,_:,_:,.`\\._ ..'=- ,
            // // // //`-.`\`   .-'/
           << << << <<    \ `--'  /----)
            ^  ^  ^  ^     `-.....--'''

            """
      print(art_deathstalker)
      print("You stepped on a Deathstalker Scorpio.\n")
      print("You are dead.")
      art_rip = r""" 
             
                               -|-
                                |
                            .-'~~~`-.
                          .'         `.
                          |  R  I  P  |
                          |           |
                          |           |
                        \\|           |//
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """
      print(art_rip)
      move = input()
    elif move.lower() == "east" or move.lower() == "e":                                     #long tunnel -> continue
        print("You entered the Eastern tunnel.")
        print("\n")
        print("\n")
        print("...")
        print("\n")
        print("It seems like this tunnel has no end")
        print("...")
        print("\n")
        print("Finally, you reach a room inside the cave.\n"
              "There is a door West of you and a ladder to your East.")
        move = input()
        if move.lower() == "east" or move.lower() == "e":                                    #ladder -> dead
            print("You start climbing down the ladder.")
            print("You did not check the strength of the ladder before climbing down.")
            print("The ladder breaks and you fall down.")
            print("Right before you hit the floor you see the Golden egg.")
            print("...")
            print("You are dead")
            #rip ascii
            art = r""" 
             
                               -|-
                                |
                            .-'~~~`-.
                          .'         `.
                          |  R  I  P  |
                          |           |
                          |           |
                        \\|           |//
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """
            print(art)
        elif move.lower() == "west" or move.lower() == "w":                                  #door -> continue
            print("The door is not locked. You open it and enter through.")
            print("There are stairs going down.")
            print("Lots of stair...")
            print("You reach the bottom of the stairs.")
            print("There is a tunnel West of you.\n"
                 "You see something glowing at the end of the tunnel.")
            move = input()
            if move.lower() == "west" or move.lower() == "w":                               #glow -> Victory
                #victory ascii art
                art_victory = r"""
                  __  __    ______ .___________.  ______   .______     ____    ____  __  
\   \  /   / |  |  /      ||           | /  __  \  |   _  \    \   \  /   / |  | 
 \   \/   /  |  | |  ,----'`---|  |----`|  |  |  | |  |_)  |    \   \/   /  |  | 
  \      /   |  | |  |         |  |     |  |  |  | |      /      \_    _/   |  | 
   \    /    |  | |  `----.    |  |     |  `--'  | |  |\  \----.   |  |     |__| 
    \__/     |__|  \______|    |__|      \______/  | _| `._____|   |__|     (__) 
                                                                                
                """
                print(f"Congratulations {name}, you have found the Golden egg!")
                print(art_victory)
elif move.lower() == "east" or move.lower() == "e":                                         #sleeping dragon -> dead
    #dragon ascii
    print('''
                                          ___
                                                  .~))>>
                                                 .~)>>
                                               .~))))>>>
                                             .~))>>             ___
                                           .~))>>)))>>      .-~))>>
                                         .~)))))>>       .-~))>>)>
                                       .~)))>>))))>>  .-~)>>)>
                   )                 .~))>>))))>>  .-~)))))>>)>
                ( )@@*)             //)>))))))  .-~))))>>)>
              ).@(@@               //))>>))) .-~))>>)))))>>)>
            (( @.@).              //))))) .-~)>>)))))>>)>
          ))  )@@*.@@ )          //)>))) //))))))>>))))>>)>
       ((  ((@@@.@@             |/))))) //)))))>>)))>>)>
      )) @@*. )@@ )   (\_(\-\ b  |))>)) //)))>>)))))))>>)>
    (( @@@(.@(@ .    _/`-`  ~| b |>))) //)>>)))))))>>)>
     )* @@@ )@*     (@) (@)  /\ b|))) //))))))>>))))>>
   (( @. )@( @ .   _/       /  \ b)) //))>>)))))>>>_._
    )@@ (@@*)@@.  (6,   6) / ^  \ b)//))))))>>)))>>   ~~-.
 ( @jgs@@. @@@.*@_ ~^~^~, /\  ^  \ b/)>>))))>>      _.     `,
  ((@@ @@@*.(@@ .   \^^^/' (  ^   \ b)))>>        .'         `,
   ((@@).*@@ )@ )    `-'   ((   ^  ~)_          /             `,
     (@@. (@@ ).           (((   ^    `\        |               `.
       (*.@*              / ((((        \        \      .         `.
                         /   (((((  \    \    _.-~\     Y,         ;
                        /   / (((((( \    \.-~   _.`" _.-~`,       ;
                       /   /   `(((((()    )    (((((~      `,     ;
                     _/  _/      `"""/   /'                  ;     ;
                 _.-~_.-~           /  /'                _.-~   _.'
               ((((~~              / /'              _.-~ __.--~
                                  ((((          __.-~ _.-~
                                              .'   .~~
                                              :    ,'
                                              ~~~~~
''')
    print("There's a dragon sleeping.\n"
          "Your steps woke him up.\n"
          "He's hungry\n"
          "You have been eaten by the dragon.\n"
          "\n"
          "You are dead.")
    #rip ascii
    art = r"""
             
                               -|-
                                |
                            .-'~~~`-.
                          .'         `.
                          |  R  I  P  |
                          |           |
                          |           |
                        \\|           |//
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """
    print(art)
    move = input()
elif move.lower() == "west" or move.lower() == "w":                                         #mama dragon -> dead
    #eggs ascii
    print(''' 
                       .-~-.
                     .'     '.
                    /         \.
            .-~-.  :           ;
          .'     '.|           |
         /         \           :
        :           ; .-~""~-,/
        |           /`        `'.
        :          |             \.
         \         |             /
          `.     .' \          .'
            `~~~`    '-.____.-'
''')
    print("There's eggs lying on the floor.\n"
          "It looks like the Golden Egg\n"
          "You pick it up. You were wrong.\n"
          "It was the sun's reflectin that made it look like the Golden Egg\n"
          "Mama Dragon is angry\n"
          "\n"
          "You are dead.")
    #rip ascii
    art = r""" 
             
                               -|-
                                |
                            .-'~~~`-.
                          .'         `.
                          |  R  I  P  |
                          |           |
                          |           |
                        \\|           |//
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """
    print(art)
    move = input()
elif move.lower() == "south" or move.lower() == "s":                                        #cliff -> dead
    print("You are standing at the edge of a cliff.")
    #cliff ASCII
    print(''' 
    __.-'```"""``"-.__,
    /"`                '.
    `':.,_               "._
         \`'-._             `'-._
          \    `:._              `'-._          _
          |      \ `:_                `"--"--"``
          |       \   `:_
          |      :|    \ '.
          |       |     |  `:_
          |       |:    |     `:_
          |:      |     |
          |       |
          |
          |
''')
    position = "cliff"
    move = input()
    if move.lower() == "south" or "s":
        print("You tried jumping of the cliff.\n"
               "In the midst of your fall you are caught by a blue dragon.\n"
               "You think you are saved.\n"
               "Unfortunately, he tosses you up in the air and takes a bite of your body.\n"
               "\n"
               "You are dead.")
        #rip ASCII
        art = r""" 
             
                               -|-
                                |
                            .-'~~~`-.
                          .'         `.
                          |  R  I  P  |
                          |           |
                          |           |
                        \\|           |//
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """
        print(art)
        move = input()
else: #wrong command
    print("I don't understand this.")
    move = input()