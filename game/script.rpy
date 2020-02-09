# The script of the game goes in this file.


#Images go here


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Robin")
define b = Character("Bea")
define j = Character("Julia")
define p = Character("Paul")
define m = Character("Mikey")
define d = Character("Doctor Love")
define lady = Character("Lady at Booth")
define m = Character("Man")
define dj = Character("The President")
define st = Character("Staff")
define u = Character("Unknown")
define n = Character("Nurse")
define m = Character("Minutus")
define pr = Character("Professor")

#Robin's gender is here.
default Her = "Her"
default her = "her"
default She = "She"
default she = "she"
default Hers = "Hers"
default hers = "hers"
default Herself = "Herself"
default herself = "herself"
default w = "woman"

#Variables that the game will use
default have_experience = False

#Stat variables are here.
default power = 50
default defense = 50
default agility = 50
default stamina = 50

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show text "Prologue" with Pause(4.5)

    scene black with dissolve

    scene Prologue

    "You're laying flat on your back in a pool of your own sweat."

    "Your face is hot and your arms wobble as your elbows give in."

    "You feel slight pressure in your chest as a metal bar pushes into your ribs."

    "You close your eyes and exhale. {i}You can do this...{/i} you think to yourself."

    "As you brace your pectorals and biceps, you push the bar in your hands upwards one last time as you finish your set."

    "You get up from the bench, wipe the sweat off your brow, and chug down a bit of your protein shake as you start stretching this workout off."

    "Weightlifting was never your strong suit,"

    "but you knew that you had to work hard if you wanted to survive the next few months of school."

    "Not long ago, you remember, with bated breath, checking the mailbox almost every hour,"

    "anticipating an acceptance letter from the college you applied to: "

    "{b}The School of Martial Arts and Combat {/b}."

    "SMAC is a college specifically designed for those wanting to perfect their combat and self-defense technique."

    menu:
        "You've never really taken martial arts in the past.":
            "And you haven't had much of an interest in martial arts, but you decided to give the school a shot."
            jump continue1

        "You took a brief taekwondo class in middle school.":
            "So you chose to attend SMAC to reignite your interest in martial arts."
            $ have_experience = True
            jump continue1

label continue1:

    "You're unsure if it was just a way of calming your nerves or just wanteing to look good on your first day,"

    "but you decided to get one last workout in before you take the short trip to campus."

    "You run up to your bedroom which is mostly empty at this point. Most of your belongings were already packed-"

    "you were so excited you had everything packed a week in advance."

    "All you need to do now is shower, get dressed, and you're on your way!"

    "You go into your bathroom and start up a steaming, post-workout shower."

    "After you get nice and clean, you hop out, wipe the fog off of your cabinet mirror and check yourself out in it."

    "\"Lookin good!\""

    "You put on some clothes and get onto the bus, optimistic about your fresh new start."

    "After an uneventful ride, you pull up to the main enterance of the campus."

    "You're guided by a line of signs reading \"New Students Entry\" and"

    "helpers with bright colored shirts donning the SMAC logo until you reach a line of other students waiting to enter."

    "You're lead over to a table where someone asks for your name and ID."

    $ p = renpy.input("Enter your name: ")

    $ p = p.strip()

    if p == "":
        $ p = "Alex"

    menu:
        "What do you identify as?"
        "Male":
            $ w = "man"
            $ Her = "Him"
            $ her = "him"
            $ Hers = "His"
            $ hers = "his"
            $ She = "He"
            $ she = "he"
            $ Herself = "Himself"
            $ herself = "himself"
        "Female":
            pass
        "Non-binary":
            $ w = "non-binary person"
            $ Her = "Them"
            $ her = "them"
            $ She = "They"
            $ she = "they"
            $ Hers = "Theirs"
            $ her = "theirs"
            $ Herself = "Themself"
            $ herself = "themself"

    lady "Nice to meet you, %(p)s!" #you can delete this whenever

    "After filling out some paperwork including your blood type, allergies, and other medical info, the helper"

    "hands you a map, your dorm room key card, and your student ID which also doubles as"

    "your meal ticket."

    "In the blink of an eye, another helper begins putting all your belongings on a cart,"

    "then wheels it away towards your dorm."

    "Before they send you off to explore, someone lets you know that there's a mandatory orientation for all new students in the Auditorium at 1."

    "With that, you are free to explore until then."

    menu:
        "Explore the campus a bit.":
            jump boxerpath #Meet Boxer path

        "Check out your dorm.":
            jump beapath #Meet Bea path

label boxerpath:

    "The campus is pretty much seperated into 6 different buildings: "

    "The Core is the main building where you came in."

    "In it are most of the 1st year classes, as well as some offices,"

    "and the auditorium -- Leg Hall 1 and 2, two buildings on either side of The Core for"

    "the 1st year dorms, Arms 1 and 2, the year 2 and 3 dorms, and The Brain, which is reserved for Elite students and staff members."

    "You wander around the campus refusing any helper's guidance; you wanted to check things out for yourself."

    "The more you saw of the school, the more you begin to realize just how much the institute encouraged being physically active."

    "There was a gym in almost every building!"

    "The halls were lined with several vending machines with power bars and shakes;"

    "almost all the paths outside had benches and stretch stations; and there were several punching bags and dummies spread out all over campus."

    "Curious to see what the Elite student building looks like, you make your way through The Core and head towards The Brain."

    "You're surprised to see that the building is a lot smaller and quieter than you thought it would be - presumably because there aren't as many seniors as there are underclassmen."

    "You slowly make your way through the double doors and are greeted by a dimly lit hallway."

    "As you suspected, there aren't really any seniors milling about and you don't see a single living soul anywhere in this hall."

    "You pass by the dorm's gym to see that most of the weights and machines in there are much more advanced than any of the gyms you've seen so far."

    "As you near a corner you start to hear grunting and the umistakable sound of punches landing on hard foam."

    "You approach the source of the sound and find a door that's cracked open halfway."

    menu:
        "You look inside.":
            jump meetboxer
        "You turn back around.":
            jump turnaround

label meetboxer:

    "You slowly creep into the doorway and peer into a dark room with a boxing ring in the middle."

    "There are a few chairs surrounding the ring as well as a blackboard on wheels and other training gear."

    "On the far side of the room you see a tall, extremely ripped person with buzzed blonde hair just laying into a training dummy."

    "A jab! A hook! An uppercut!"

    "All of these blows are just as powerful as they are fast."

    "The figure attacks with precision unlike anything you've ever seen, you're sure that every hit they landed on this inanimate dummy would have been lethal to any human."

    "You find yourself so amazed by this person's technique you find yourself watching them for quite some time."

    "You watch intently as punch after punch, beads of sweat fly off their body and they let out audible puffs of air, their toned legs consstantly moving"

    "as they shift their weight around."

    "Out of nowhere, the figure turns to you and stares you dead in the eyes."

    "You now see her face, which is bruised and contorted from years of getting punched while fighting,"

    "her nose is crooked, and her cold eyes are sunken deep into her skull, but you somehow find her absolutely stunning."

    "She then rears back for a final blow and she- {b}HOOKS{/b} the dummy's head clean off into your direction, the head rolls to a stop at your feet.{/b}"

    "Shocked and somewhat flustered, you begin backing out of the room, tripping on some chairs."

    "The boxer glares at you again, then the dummy head, and back at you."

    "You get the message and decide that you've done enough exploring for the day and make your way over to the auditorium."

    jump orientation

    return

    # This ends the game.

label turnaround:

    "You decide that you've done enough exploring for the day and head over to the auditorium."

    jump orientation

    return

    # This ends the game.


label beapath:

    "The campus was pretty much seperated into 6 different buildings: The Octogon is the main building where you came in from - "

    "in it are most of the 1st year classes as well as some offices and the auditorium, Leg Hall 1 and 2, which were two buildings on either side of"

    "The Oct which are first year dorms, Arms 1 and 2 which are year 2 and 3 dorms, and Lee Hall, which is reserved for Elite students and staff members."

    "It takes you maybe fifteen minutes to find your room, but you finally make it."

    "You see other students moving into rooms next to yours, none of them really pay attention to you- they're all busy saying goodbye to their parents or lugging boxes of belongings to even make eye contact."

    "One girl, however, smiles at you as you arrive at your door."

    "She walks towards the door next to yours, rolling a pink luggage with all sorts of cartoon pins and buttons attached."

    "She is wearing an oversized Konnichiwa Cat sweater."

    "You catch yourself thinking she looks too cute for a fighting school, but you ignore the thought as she approaches you."

    b "Hi there! I'm Bea, nice to meet ya!"

    "She smiles and extends a hand."

    p "Hey, my name's  %(p)s, nice to meet you!"

    b " %(p)s, huh...I'm gonna have to remember that when I'm kicking your ass!"

    "She laughs."

    "You laugh awkwardly as well."

    b "Looks like we're gonna be neighbors."

    b "I'll try not to be too rowdy at night."

    b "See ya later!"

    "She pats you on the shoulder and walks into her room."

    p "{i}What was that? {/i}"

    "You shrug it off and proceed into your room as well."

    "You walk in to see the average college dorm setup - one big room with 2 desks, chairs, and a bed on the side of a window."

    "It looks like someone has already taken one of the sides of the room."

    "Whoever they were, it seems like this was their dream school because the entire side was covered floor to ceiling with karate gear."

    "The whole wall was plastered with classic kung-fu movie posters, tournament trophies, and a display of all their belts earned in karate encased behind the glass."

    p "I hope I won't have to fight against them..."

    "You looked over to your corner where the helpers have dropped off all your boxes and your car keys."

    "You organized your side of the room."

    "Once you finished, you checked your watch."

    p "Time for orientation."

    "You put on your SMAC t-shirt and headed out to find the auditorium."

    jump orientation



label orientation:

    "You walked to the Octogon and saw a crowd of helpers and students walking into the auditorium."

    "You made your way through the double doors."

    "Instead of the traditional school assembly arrangement, the Octogon had no chairs, no stage, and no podium."

    "It was just a large gymnasium styled room with a fighting ring in the middle."

    "On either side of the ring bleachers lined the walls, filled with noisy students."

    "You looked around for a space to sit when someone in the crowd waved in your direction."

    r "Hey!"

    "A young [w] in a full karate gi yelled across the gym and called you over."

    r "Hey, %(p)s, it's been so long!"

    if have_experience == False:
            r "We had 7th grade PE together! You don't remember me?"

            "{i}That was at least 10 years ago, how's anyone suposed to remember anything from middle school? {/i}"

            p "I'm sorry...I don't remember. My memory's pretty bad..."

            "[She] frowned a bit, but smiled and slapped you on the back."

            r "No worries, that was forever ago."

            r "My name's Robin, and don't you forget it!"

            p "Nice to meet you too."

            "You shake [her] hand as the squeal of a microphone's feedback cuts through the chatter."


    else:

            r "We took taekwondo together back in middle school."

            "You vaguely remembered sparring with them but you didn't stay in the class for too long."

            p "Master Kim's right?"

            "Back then, the studio was a front for Master Kim's underground MMA fights."

            r "Yeah!"

            r "He was a great Sa Bum, but he was a bit wild."

            r "Wanna sit together?"

            p "Sure!"

            "You sit with Robin as the squeal of a microphone cuts through the chatter."


    "An extremely tall, unbelievably muscular bald man in a SMAC polo shirt taps on a mic and paces as he addresses the room."

    m "Welcome! Class of 20XX!"

    "A roaring applause bursts as the man flexes."

    "The undersized polo shirt he is wearing almost shreads to pieces as he poses."

    dj "Hello students! I am Drew Jackson, your president and founder of the School for Martial Arts and Combat."

    "He flexes again, and you swear you see a couple of buttons fly off his shirt."

    fd "As many of you know, physical fitness and martial arts is something I hold near and dear to my heart."

    dj "As I had somewhat of a turbulent upbringing, I always found comfort and joy in what I was most passionate about: wrestling."

    dj "No matter what I was going through, being in the ring always gave me the motivation to work hard and improve myself physically and mentally."

    dj "And that's why it is with great honor that I can pass on that passion and the drive to want to be the best onto all of you in this room."

    "The room breaks into an uproar again, and Robin hollers along with the crowd."

    dj "You have survived the audition process and, hopefully, you have been conditioning your bodies for the upcoming semester."

    dj "Now we will test if you have what it takes to continue your education!"

    dj "We will now seperate you all into groups of twenty, which will be a fight to the death, Bloodsport style!"

    "The silence is deafening."

    "You immediately swall an avacado sized gulp."

    dj "Just kidding, of course!"

    dj "You will be sparring amonst your peers as a way to assess your skills and help plan your coursework accordingly."

    dj "Some will do better than others, and there have been extreme injuries in the past - so please be wary."

    dj "In any case - the first group will be: "

    dj "Miguel Santos."

    dj "Robin De Santa."

    dj "Beatrix Washington."

    dj "and %(p)s."

    "You, Robin, and a few other students begin making their way to the center ring as some helpers hand you some gear."

    "The President beigns explaning the rules but the sound of your heartbeat drowns out all the noise."

    dj "With that being said, best of luck to you all, and let the Class of 20XX Royale begin!"

    "Your fight or flight instincts kick in and you immediately begin bouncing around on your feet and blockign your face."

    "It's absolute insanity in the ring; most of your oppenents battle in the center of the stage in a sort of mosh pit - you decide to stray far away from them."

    "On the other side of the ring you recognize Miguel as he lassos one opponent running at him and suplexes another."

    "You hear two bells ding as the two students are dragged off the mat towards the hospital wing."

    "You make your way to the opposite side of the ring."

    "Over here, you see Robin blocking and parryign attacks from five different opponents."

    "They pull a pair of nunchucks and start beating several people over their heads."

    "They go flying out of the ring like a kung fu movie."

    "Five more dings go off."

    st "No weapons!"

    "Robin yelsps and drops the nunchucks, blushing furiously."

    "Not too far off, you recognize Bea chocking out a kid at least three times her size."

    "She gives you a friendly smile as the kid in her hold goes blue."

    "The refs whistle as the medics drag him off."

    "She then quickly gets up, double legs another opponent and begins to pin him down to the ground."

    "All of a sudden, you are pushed into the center of the ring where some students are engaged in a five-man battle, exchanging blows."

    "While you try to make your way out of the fray, you manage to blocka couple of potshots the mob tries to throw at you-"

    "{b}BAM!{/b}"

    "You're stunned by a rabbit punch to the back of you head, right underneath your neck."

    "Your vision blurs as you stumble on your feet and all you see is a humanoid shape unleasing a roundhouse kick to your face."

    "You black out instantly and the last thing you remember is a pair of strong hands tugging on your shoulders gently as you are lifted onto a stretcher and wheeled away."

    scene black with dissolve

    show text "End Prologue" with Pause(4.5)

    scene black with dissolve

    show text "Chapter One" with Pause(4.5)

    scene black with dissolve

    show text "Day One" with Pause (4.5)

    scene black with dissolve

    scene Day One

    "You wake up in a cold room."

    "You are covered in fluffy, yet scratchy blankets in a hospital cot."

    p "W-where am I?"

    n "You got wrecked pretty hard."

    "An older student with green eyes stands over you to make sure you've come to."

    "He has a clipboard and pen in hand."

    "He checks something off as he examines you for a minute."

    "He clicks the pen closed and places it in his long brown hair tucked into a loose bun."

    n "It wasn't that bad was it?"

    "Your cheeks go red from embarrassment."

    p "Not really, but it was pretty pathetic."

    "He gives a teasing, toothy smile."

    n "Don't take it personally though Champ, I've seen worse."

    "He points to several other people in the cots next to you."

    "Some of them have black eyes and chipped teeth."

    n "You didn't even injure your head that bad. No concussion or anything, but we kept you overnight just to be sure. We take head injuries seriously here."

    p "Overnight? What time is it? I'm late for class!"

    "You begin to get up but the nurse pushes you back down."

    n "Relaaaax. It's only 8:25."

    "He presses a couple of buttons on a screen."

    n "See, your first class doesn't start until 9."

    "You sink back into the bed a bit."

    n "Let me just finish up your record and I'll wheel you over in no time!"

    p "Wheel me over? I feel fine. I can just walk, it's no biggie."

    "You object, not wanting to inconvience him further."

    n "No can do Champ, it's hospital policy."

    n "Anyone who comes in through those doors, can only leave at the price of their legs!"

    n "Just kidding...It's just so that we'ere not resposible if one of you dumbasses slips and falls on the way out of here."

    n "Besides, your class is right around the corner."

    n "I'll be right back with a chair, your stuff is on the table next to you."

    "The nurse comes back with the wheelchair the color of his scrubs."

    n "All aboard....{b}THE LOVE TRAIN!{b}"

    p "The...'Love Train'?"

    "Your face flushes again."

    "The nurse's face also turns red."

    n "I uh...sorry. It's uh, Love, Doctor Love."

    p "So you're a nurse named...Doctor?"

    d "Yea I get that a lot...My parents were kinda weird like that."

    d "Would you believe me if I told you my brother's name is Lawyer?"

    p "Is he...a lawyer?"

    d "Uh...no. He's a garbage man. Hope on!"

    "You take a seat on the wheelchair, and Doctor Love rolls you out the double doors past a few rows of battle scarred students."

    "After a few twists and turns down some hallways, you make it to your classroom in no time."

    d "Alright, here we are, Defense 101."

    "Dr. Love opens the door for you."

    p "Thanks."

    d "No problem."

    "He pulls you aside a bit."

    d "If you ever need anything, feel free to stop by The Heart anytime. Hopefully under less...critical circumstances."

    "He winks and waves at you as you walk into class."

    "You see several students already standing around and chatting idly."

    "The professor stands a ta desk just off the side of the ring, typing away on a laptop, ignoring the chatter."

    "SItting across the room, you see Miguel, Bea, and Robin talking to each other."

    "You sheepishly walk over to the group, hopign they won't give you a hard time after you were embarassingly disqualified at Orientation."

    r "Enter the Wyvern is 100% better than Kill Phil."

    m "Are you seriously comparing those two movies? You're comparing apples to, like, gummy bears. They're totally different genres."

    r "Both are fighting movies. Ruth Lee's form and technique is SO much better than Irma Theremin's."

    m "Dude, what are you even arguing? Kill Phil is practically a comedy."

    r "Either way I'm right."

    b "You're BOTH wrong, My Ninja High School is WAY better than either of those."

    r "Yea that's true."

    m "For sure."

    r "Hey, %(p)s! Are you alright?"

    p "Yep, all good. It really wasn't that bad..."

    if have_experience == False:

        r "Yea...you were four spots ahead of last place. Pretty bad, but I'm sure there's room for improvement, right?"

        "You sigh."

    else:

        r "Hey, at least you made it right? Top 10. Not bad."

    r "Oh, this is Bea and Mikey, if you didn't know already."

    p "Yea, we met...Kinda. What place did you guys get?"

    m "Fourth!"

    r "Second."

    "Bea smiles and holds up her index finger."

    r "Argh! I would have taken the gold if they didn't disqualify me for using my nunchucks!"

    b "It's a martial arts fight, weapons are il-le-gal."

    r "But nunchucks are martial weapons, mar-tial!"

    b "Whatever, I still woulda beat your ass."

    "Robin pulls out [her] nunchucks and starts running towards Bea."

    "Mikey stops them and takes the nunchucks away just as the professor finally looks up from his laptop."

    pr "Alright guys...Listen up...Listen up, listen up."

    pr "First day of class."

    pr "Just want to lay out the groundwork."

    pr "My name is Professor Minutus, just call me Min."

    m "I graduated from ehere in 200X, did MMA for six years, and was a person trainer for abotu three."

    m "I'm not like other professors, I don't like to hand out a syllabus or anything like that."

    m "Just a few simple rules: "

    m "No. Weapons."

    m "No. Maiming."

    m "No. Babies."

    "He peers at the four of you, and his eyes look at Mikey."

    m "You, with the nunchucks, come up here."

    m "I wanna show you something."

















    # This ends the game.
    r "The game is over."

    return
