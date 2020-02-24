# The script of the game goes in this file.


#Images go here
image robin = "../game/images/Rob.png"
image bea = "../game/images/Bee.png"
image jules = "../game/images/Jules.png"
image drlove = "../game/images/Love.png"
image paul = "../game/images/paul.png"
image mikey = "../game/images/Soap.png"

image defense = "../game/images/defense101gym.jpg"
image power = "../game/images/power101dojo.jpg"
image paulogym = "../game/images/paulogym.jpg"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Robin")
define b = Character("Bea")
define j = Character("Julia")
define p = Character("Paul")
define m = Character("Mikey")
define d = Character("Doctor Love")
define lady = Character("Lady at Booth")
define ma = Character("Man")
define dj = Character("The President")
define st = Character("Staff")
define u = Character("Unknown")
define n = Character("Nurse")
define mi = Character("Min")
define pr = Character("Professor")
define c = Character("Cafeteria Lady")
define w = Character("Willy")

#Robin's gender is here.
default Her = "Her"
default her = "her"
default She = "She"
default she = "she"
default Hers = "Hers"
default hers = "hers"
default Herself = "Herself"
default herself = "herself"
default woman = "woman"
default sister = "sister"

#Variables that the game will use
default have_experience = False
default food = "default"

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

    $ quick_menu = False

    scene black with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show text "Prologue" with Pause(3.5)

    scene black with dissolve

    scene Prologue

    $ quick_menu = True

    show power

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
            $ sister = "brother"
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
            $ sister = "sibling"

    #lady "Nice to meet you, %(p)s!" #you can delete this whenever

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

    show jules

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

    "She then rears back for a final blow and she- {b}HOOKS{/b} the dummy's head clean off into your direction, the head rolls to a stop at your feet."

    "Shocked and somewhat flustered, you begin backing out of the room, tripping on some chairs."

    "The boxer glares at you again, then the dummy head, and back at you."

    "You get the message and decide that you've done enough exploring for the day and make your way over to the auditorium."

    hide jules

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

    show bea

    b "Hi there! I'm Bea, nice to meet ya!"

    "She smiles and extends a hand."

    p "Hey, my name's  %(p)s, nice to meet you!"

    b " %(p)s, huh...I'm gonna have to remember that when I'm kicking your ass!"

    "She laughs."

    "You laugh awkwardly as well."

    b "Looks like we're gonna be neighbors."

    b "I'll try not to be too rowdy at night."

    b "See ya later!"

    hide bea

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

    show robin

    r "Hey!"

    "A young [woman] in a full karate gi yelled across the gym and called you over."

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


    hide robin

    "An extremely tall, unbelievably muscular bald man in a SMAC polo shirt taps on a mic and paces as he addresses the room."

    ma "Welcome! Class of 20XX!"

    "A roaring applause bursts as the man flexes."

    "The undersized polo shirt he is wearing almost shreads to pieces as he poses."

    dj "Hello students! I am Drew Jackson, your president and founder of the School for Martial Arts and Combat."

    "He flexes again, and you swear you see a couple of buttons fly off his shirt."

    dj "As many of you know, physical fitness and martial arts is something I hold near and dear to my heart."

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

    "Robin yelps and drops the nunchucks, blushing furiously."

    "Not too far off, you recognize Bea choking out a kid at least three times her size."

    "She gives you a friendly smile as the kid in her hold goes blue."

    "The refs whistle as the medics drag him off."

    "She then quickly gets up, double legs another opponent and begins to pin him down to the ground."

    "All of a sudden, you are pushed into the center of the ring where some students are engaged in a five-man battle, exchanging blows."

    "While you try to make your way out of the fray, you manage to block a couple of potshots the mob tries to throw at you-"

    "{b}BAM!{/b}"

    "You're stunned by a rabbit punch to the back of you head, right underneath your neck."

    "Your vision blurs as you stumble on your feet and all you see is a humanoid shape unleashing a roundhouse kick to your face."

    "You black out instantly and the last thing you remember is a pair of strong hands tugging on your shoulders gently as you are lifted onto a stretcher and wheeled away."

    $ quick_menu = False

    scene black with dissolve

    show text "End Prologue" with Pause(3.5)

    scene black with dissolve

    show text "Chapter One" with Pause(3.5)

    scene black with dissolve

    show text "Day One" with Pause (3.5)

    scene black with dissolve

    scene Day One

    $ quick_menu = True

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

    "Sitting across the room, you see Miguel, Bea, and Robin talking to each other."

    "You sheepishly walk over to the group, hopign they won't give you a hard time after you were embarassingly disqualified at Orientation."

    r "Enter the Wyvern is 100\% better than Kill Phil."

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

    mi "I graduated from here in 200X, did MMA for six years, and was a person trainer for about three."

    mi "I'm not like the other professors, I don't like to hand out a syllabus or anything like that."

    mi "Just a few simple rules: "

    mi "No. Weapons."

    mi "No. Maiming."

    mi "No. Babies."

    "He peers at the four of you, and his eyes look at Mikey."

    mi "You, with the nunchucks, come up here."

    mi "I wanna show you something."

    "You hear a few students murmur and go \"OOOOOOOOO\" as Mikey makes his way to the front of the class, glaring at Robin."

    mi "Alright calm down, calm down."

    mi "Now."

    mi "I wanna show you guys the basics of defense, and how using your opponent's weight and momentum against htem is key to winning a fight."

    mi "Alright, come at me with those nunchucks."

    m "Sir-those aren't mine-,"

    mi "I said come at me!"

    "Mikey charges Professor Min, nunchucks swining, and in a flash, he is disarmed and pinned to the ground almost immediately."

    "The Professor holds Mikey's arm in a way that looks unnatural against his crumpled body."

    mi "You see, that's how you disarm someone with a weapon."

    mi "The human body is the ONLY weapon you need."

    mi "Now if he were perhaps some VAGRANT on the street trying to get my goods, I would probably have broken their arms like THIS."

    "The class collectively gasps as the Professor gently tugs on Mikey's arm."

    mi "But, that's not what we're here to learn."

    mi "Are you in any pain right now, kid?"

    m "No, sir."

    mi "Right."

    "He lets Mikey get up. He stretches his arms and legs a bit."

    mi "Go ahead and take a seat again kid, thank you."

    "Mikey goes back to his seat and the Professor puts the nunchucks in his desk drawer."

    r "I'm sorry."

    m "I hate you."

    "Mikey sits down."

    mi "Now, as I was saying."

    mi "Since most of the fights you'll be getting into here at SMAC will be against other students, in an effort to mitigate serious injuries, we're here to learn how to defend yourself in a manner that causes minimal harm to your attacker."

    mi "That clear?"

    "The class agrees in unison, and Professor Min stands up and claps his hands together."

    mi "Alright. Let's start."

    "After a pretty intense session, the class is let out, and you meet with Bea, Robin, and Mikey again."

    m "Hey, %(p)s, wanna have lunch together?"

    menu:
        "Sit with them.":
            jump sit
        "Skip out on lunch.":
            jump skip

label sit:

    p "Sure!"

    "You all walk towards the cafeteria."

    "It is around 11:30 now and both students and professors are flooding the dining courtyard."

    "There are seats all over a circular pavilion with a huge awning shielding everyone from the August sun."

    "Rows of benches are filled with people chatting and eating."

    "You make out a group of students half dressed in wrestlign gear armwrestling each other."

    "All over the perimeter of the courtyard you can see several booths."

    "There is a salad bar stacked with different greens, toppings, and other veggies on one end of the courtyard, a cereal bar, a sandwich making station, a dessert table, a fruit stand, and a couple of booths where they serve hot foods."

    "You all decide to walk towards one of the hot food booths, grab trays, and line up behind a couple of students."

    r "Man I'm starving!"

    r "Professor Min really didn't pull any punches for our first lesson, huh?"

    "Robin bounces as you all take a couple of steps forward in line."

    m "Yeah, no kidding."

    "Robin chuckles and scratches the back of Mikey's head."

    r "Heh, sorry Mike. I didn't think he'd end up bringing you in front of the whole class like that."

    r "That musta been hella embarrassing."

    r "I'm really sorry about that."

    r "I can get you some extra pizza to make up for it."

    "Mikey pats Robin on the shoulder."

    m "Eh, don't worry about it bud."

    m "Besides, it was kinda funn.y"

    m "I'm gonna take you up on that pizza though, I could eat a whole pie right about now!"

    b "Awww, ain't y'all a pair?"

    b "Hey, %(p)s, what do you think you'll have?"

    menu:
        "Pizza":
            $ food = "pizza"
        "Steak":
            $ food = "steak"
        "Tofu Stir Fry":
            $ food = "tofu stir fry"
        "Grilled Salmon":
            $ food = "grilled salmon"

    p "Uh, I think I'll have some %(food)s."

    r "Yeah! Mee too. Aw man, I can hardly wait!"

    "Robin jumps as you all approach the muscular looking cafeteria lady."

    c "Hi babies, what can I get you?"

    r "Hi lady! Can I get two- no - three steaks, and a salad?"

    "Robin points at each item through the sneeze guard."

    "Mikey clears his throat."

    r "Oh, and two slices of pizza for my friend here."

    c "Here you go baby. Next?"

    m "Just some tofu for me ma'am."

    # c "Good. You look like you could lose some weight."

    c "Alrighty. Whatchu want baby?"

    b "I'll have the salmon miss, thank you."

    c "And you, baby?"

    p "Some %(food)s please."

    "You hand the lunch lady your tray as she gives you a decent sized portion."

    c "Salad and fruits are over there babies. See you later."

    "The lunch lady waves you off as more students line up in front of her."

    "You all walk around the courtyard grabbing just a bit of everything from each station."

    "Robin loads [her] tray with tons of proteins and veggies, Mikey raids the vegetarian items, and Bea gets a healthy mix of everything."

    "Once everyone's made their rounds, you guys find an empty bench and dig in."

    b "Ugh...I shouldn'ta had that second ice cream sandwich."

    r "Yeah, I think I'm gonna- I think I might start mooing if I have another bite of this steak..."

    "Robin unravels [her] black belt a bit."

    m "It's almost 1 o'clock. What class you guys got next?"

    "You pull out and scan your class schedule."

    p "Power and How to Control Your Inner Deamon...?"

    b "Oh, me too!"

    r "Yeah, same."

    m "Really? I guess that makes all of us. Lets head on over."

    "Mikey gets up and grabs everyone's trays and throws them out for you."

    "After Mikey catches up with you, you all walk back into the freshman building towards your next class."

    jump power


label skip:

    p "Nah, I'm not really hungry."

    p "I'll catch up with you guys later."

    "Mikey, Robin, and Bea all walk towards the cafeteria, while you decide to explore around campus some more."

    "Maybe it's the leftover adrenaline from your previous class's drills, but something draws you towards one of the gyms near the freshman dorms."

    "You walk into the gym to see that it's completely empty."

    "You're astonished by just how well equipped the gym is."

    "It has weight lifting machines and other training equipment."

    "You know that there are around 5 gyms around campus, not counting the ones in classrooms, and wonder if those are as stacked as this one."

    "You look around at the couple rows of treadmills, exercise bikes, and free weights."

    p "I guess THIS is where my tuition's going."

    "You analyze which machine you'll use."

    menu:
        "Go for a run":
            jump treadmill
        "Pump some iron":
            jump weights
        "Work on your downward dog":
            jump yoga

label treadmill:

    "You hop onto one of the treadmills just to get your blood pumping a bit."

    "You put the settings to Quick Start and begin jogging at a light pace."

    "You've done a lot of jogging over the summer in preparation for this semester, so you're able to pace yourself quite well."

    "Just as you begin working up a bit of a sweat, some guy walks in and locks eyes with you."

    "You quickly turn your head and continue running."

    "The treadmill picks up speed a little bit and you're now running at a moderate pace as the guy walks behind you and gets on the treadmill."

    "RIGHT. NEXT. TO. YOU."

    "You decide you won't let this guy ruin your workout and let it slide."

    "You continue running, trying to ignore hims tretchign and groaning excessively loud in the corner of your vision."

    "You hear the guy press a couple of buttons on his machine and begin jogging."

    "You're finally able to get a good look at him now that he's no longer behind you and you see his golden-brown locks bouncing up and down off his strong shoulers with every stride."

    "His face peeks in and out from beneath his hair and from what you can see, he's not bad looking."

    "As he picks up speed and begins to sweat, he undoes a couple of buttons on his white button down shirt revealing his well defined chest."

    "You're not sure if you should feel aroused or threatened by his presence, but you're considering the latter because of how he's dressed."

    "Only psychopaths wear slacks and boat shoes while running."

    "As you look back up to his face, he is staring DIRECTLY at you."

    "At first you were a little paranoid about him deciding to run right next to you, but now you know this guy is a freak."

    "You try your very best to finish up your workout, but after a few minutes of running, he taps you on the shoulder."

    if w == "man" and w == "non-binary":

        u "Your muscles, they excite me."

        u "Would you like me to feel them?"

    else:

        u "I like a woman with nice curves."

    "He says this with a disgusting smile on his face."

    "Visibly creeped out, you smile awkwardly at the douchebag."

    "You pressed the stop button intensely and leave the gym."

    jump weird

label weights:

    "You decide to grab a couple of dumbbells and just do some bicep curls."

    "You look at the mirror and flex."

    "Just as you start your first set, a guy wearing a button down shirt, slacks, and boat shoes walks in, winks at you, and makes his way towards a squat rack."

    "Suddenly, the guy takes off his shirt, revealing his stunning torso."

    "You continue lifting weights, trying not to stare at his abs. After watching him stretch a bit, you see him start undoing his pants."

    "{i}Oh god, what the-{/i}"

    "It turns out the guy wears gym shorts under his dress pants. You're relived at this sight."

    "Finally, the guy sets his weights and squats."

    "You're thoroughly impressed that his physique isn't just for show - he starts squatting around 200 pounds almost effortlessly."

    "Realizing you've been distracted for too long, you return to your lifting."

    "As you're finishing up your set, you look back up at the guy and see him looking right in the eyes as he squats."

    "Each lift, his grunts keep getting louder and louder, his shoulders now glistening with sweat, and his gaze never leaving you."

    u "You like what you see?"

    "He flexes his thigh muscles, making them dance in a grotesque way."

    u "You want to get like me?"

    "Disgusted, you throw your weights to the ground and stomp angrily out of the gym."

    jump weird

label yoga:

    "You decide that after an eventful morning, you need to clear your mind a bit and grab a yoga mat."

    "You roll the mat out onto the ground and begin going through some poses."

    "You slowly bring yourself to the ground, legs and arms out, and your head under your shoulders in the child's pose."

    "You then stretch yourself out and bring your body up to a plank, and slowly drop and bend forward in a cobra - carefully breathing in and out with each calculated movement."

    "From the cobra, you stretch your arms out and bend backwards into the downward dog."

    "As you bring your feet forward and stretch your body into a standing position, you notice someone has been standing at the gym door staring at you the entire time."

    "You sit down quickly, thinking he might have stared at your posterior."

    u "Don't mind me."

    "He grabs a yoga mat and rolls it out across the room."

    "He then takes off his shoes and eases into a headstand."

    "You look him up and down and see that he's dressed like some sort of Spanish soap opera heartthrob with a silk button down shirt."

    "He's clearly not dressed for a workout, but he seems to know what he's doing, so you let it slide."

    "You repeat your sun salutation again, working your way back into a plank."

    "You keep breathing in and out as you feel your muscles releasing the tension in your body."

    "As you bend down into a cobra, you see the guy doing a bent-down version of the Tree Pose, his hands folded as if in prayer while standing on his right foot."

    "He breathes loudly as he bends even further, pushing his behind even further up."

    "Creeped out, you get up and start walking out of the gym without rolling your mat back up."

    jump weird

label weird:

    "You rack your brain wondering what the hell happened in the guym as you storm out of the double doors."

    "You turn a corner and run into Bea, Mikey, and Robin."

    r "Oh hey dude. Why do you look so spooked?"

    p "Oh, I just ran into some pervert at the gym."

    "You think about the encounter and shudder."

    m "Whoa, really? Should we report them?"

    p "No, no, it's no big deal. He was just some weirdo, I think I'll be fine."

    b "You sure? You can't be too careful."

    p "I'm fine, really."

    p "So, uh...what's you guy's next class?"

    b "All three of us are heading to the Power class. You're headed there too?"

    p "Yeah."

    r "Cool, let's sit together again."

    "Robin fist bumps you and you all walk to class."

    jump power

label power:

    "All four of you walk into a dojo-style classroom complete with multi colored padded floors."

    "Robin's eyes light up."

    "At the front of the class with a few students is the sensei, a tall, tan, big, bald man, already showing off some basic karate forms."

    "As you all file in front of him on your own mats, he begins addressing you all."

    pr "Good morning class. This is the Freshman Power 101 course."

    pr "I will be your sensei for this term."

    pr "My name is Dr. William Blanks. But you can call me Willy."

    w "I already see that some of you may have already taken karate classes in the past, but I will let you know that in this class, you will work harder than you ever have before."

    w "Before we get started, I just want to show you some of my work, so that you get an idea of where I'm coming from."

    "Willy goes into a closet, wheels out an old TV, and pops in a VHS tape."

    "The video is a montage of mashed up backyard home video footage of a younger, hairer Willy performing all sorts of karate stunts, some shots from some professional tournaments he took place in and some shots of him training some younger fighters,"

    "all set to 80s music."

    "You feel like maybe it went on for a bit too long, but Robin seems to be enjoying [herself] quite a bit."

    "The tape ends and Billy turns the light back on."

    w "Alright, any questions? Let's begin."

    "A couple of students raise their hands, but Willy puts them into groups as the lesson begins."

    "As the session dies down and you all start to head out, Robin approaches you."

    r "Hey, I'm gonna stick around here a bit to talk to the professor."

    r "I'll catch up with you guys."

    "Robin runs over to Willy."

    m "Man, I'm gonna have to do some major stretching after that or else I'm gonna be hella sore tomorrow."

    "Mikey twists his back a bit."

    b "Wasn't that bad. I'm pretty hype to see what we do next."

    "Bea pulls out her cellphone and sighs."

    b "My parents want me over for dinner in a bit. Sorry, I'll see you guys tomorrow."

    m "See ya, Bea."

    m "Let's start walking I guess, Robin might be there for a while."

    "You and Mikey start walking towards your dorms."

    m "I can't believe you had no idea who our Principal was!"

    m "He was this super famous wrestler back in the 90s."

    p "I thought he looked familiar. Is he really THE Drew \"The Boulder\" Jackson?"

    m "Yea, he like, kinda disappeared from Pro Wrestling for a bit."

    m "I guess he was getting SMAC established."

    m "Pretty cool though, that someone that famous decided to just open up a school for people like us."

    m "Anyway, my room's that way."

    "Mikey stretches and yawns."

    m "I'm pretty beat, I'll probably just stay in for the rest of the night. See you tomorrow?"

    p "Yeah, see ya."

    "You wave at Mikey as he turns a corner."

    "You walk towards your room."

    "Feeling pretty drained, you begin heading over to your dorm as Robin catches up with you."

    r "Hey! Heading home?"

    p "Yup. Pretty tired."

    r "Looks like we're headed the same way. Might be neighbors!"

    "Robin starts walking beside you."

    "You arrive at your door."

    p "This is me-" (multiple=2)

    r "This is me-" (multiple=2)

    r "Roomies! This is gonna be great!"

    menu:
        "It's been a while since you've had a roommate.":
            p "I used to split rent with some people a while back. It was kinda...eh."

            p "Lots of passive-aggressiveness and post-it-notes."

            r "Don't worry, I'll try not to be an asshole, hah."

            r "I promise I won't eat your leftovers and stuff."

            p "Thanks."

            jump yourroom

        "You and your sibling haven't shared a room since you were kids.":

            p "My [sister] and I used to share a room as kids."

            p "It's been a while since then, but it could be nice to have a roommate again."

            r "I think it'll be fun."

            r "We'll get to see each other more often at least, get to know each other a bit more."

            r "I'm pretty excited about it."

            "Robin hops onto [her] bed."

            jump yourroom

        "You've lived alone for most of your life.":

            p "I haven't really shared a room with anyone before."

            p "Just kinda had my own space for the most part."

            "You trail off."

            r "Don't worry, I'll try to give you as much space as you need."

            p "No worries, I think it'll be fun. It can kind of be lonely sometimes, so I've been looking forward to rooming with someone actually!"

            r "I'm sure we'll get along fine then."

            jump yourroom

label yourroom:

    "As you both finish unpacking things and organizing your respective sides, Robin springs out of [her] bed and starts putting on [her] shoes."

    r "Wanna go grab some dinner?"

    "[She] helps you put up your mirror."

    p "I could eat."

    r "Cool. I texted Mikey to see if he wanted to join, but he didn't respond."

    "Robin taps on [her] phone, frowning."

    p "Yeah, I think he's asleep. Bea's with her parents."

    r "Ah, I guess it's just the two of us then."

    "Robin holds open the door for you."

    r "Lead the way."

    "You turn off the lights and begin walking towards the cafeteria."

    "The cold night breeze cools your face as you and Robin have dinner."

    "The dining pavillion isn't nearly as active as it was during lunch time, so you're able to have a nice conversation with [her]."

    "After dinner, you return back to your room."

    "You brush your teeth and get ready for bed."

    "Robin comes out of the shower and begins doing crunches."

    r "Just because we're roommates doesn't mean that I won't put the hurt on you."

    "Robin finishes [her] crunches and starts doing pushups."

    p "Huh?"

    if(have_experience == True):

        r "We might be best friends, but we're still competing against each other."

        r "That goes for everyone else here too."

        p "Where did this come from?"

        "You chuckle."

    else:

        r "I've just been thinking. You seem like you could be a good friend, but you could also be a formidable opponent."

    r "I don't want to let my feelings get in the way of my success."

    p "Your feelings?"

    r "I mean, our relationship."

    "Robin stops mid push up."

    r "As roommates!"

    "[She] resumes."

    p "Right."

    r "So. We can still be friendly with each other. But just don't lose sight of what we're here for."

    r "So consider us...rivals."

    p "Heh."

    "Your competitive spirit sparks a bit. You make a little promise to yourself that you'll begin working a bit harder, and try to compete with Robin."

    p "Alright. This is gonna be interesting."

    "Robin wraps up [her] workout and begins to stretch, before [she] puts in [her] retainer and hops onto bed."

    r "The sunrise brings with it another battle. Rest up."

    "[She] shuts [her] lamp off."

    p "Night, Robin. See you tomorrow."

    "For the first time since you've got here, you felt a twinge of warmth in your heart."

    "It felt nice to be sharing a room with someone who sees you as an equal."

    "You think about the semester you have ahead of you and the other people you will meet as you drift into sleep."

    $ quick_menu = False

    scene black with dissolve

    show text "End of Demo" with Pause(3.5)

    scene black with dissolve

    $ quick_menu = True

    return
