# The script of the game goes in this file.


#Images go here


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Robin")
define b = Character("Bea")
define j = Character("Julia")
define p = Character("Paul")
define m = Character("Mikey")
define d = Character("Dr. Love")
define lady = Character("Lady at Booth")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show text "Prologue" with Pause(1.5)

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

    "She then rears back for a final blow and she- {b}HOOKS the dummy's head clean off into your direction, the head rolls to a stop at your feet.{/b}"

    "Shocked and somewhat flustered, you begin backing out of the room, tripping on some chairs."

    "The boxer glares at you again, then the dummy head, and back at you."

    "You get the message and decide that you've done enough exploring for the day and make your way over to the auditorium."

    r "The game is over."

    return

    # This ends the game.

label turnaround:

    "You decide that you've done enough exploring for the day and head over to the auditorium."


    r "The game is over."

    return

    # This ends the game.


label beapath:

    r "The game is over."

    # This ends the game.

    return
