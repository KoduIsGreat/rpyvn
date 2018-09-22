# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define a = Character("Akuno")
define o = Character("Okasuki")
define m = Character("MC")
image bg walledvalley = im.Scale("images/walledvalley.png", 1920, 1080)
image bg ocean = im.Scale("images/ocean.png", 1920, 1080)
image wolf happy = "images/wolf.png"
image adahm = "images/sadahm.png"
image bg spooky forest = im.Scale("images/spookyforest.jpg", 1920, 1080)
image bg camp1 = im.Scale("images/camp.jpg", 1920, 1080)
image bg office = im.Scale("images/office.jpg", 1920, 1080)
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg camp1
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    play music "tenpenny.ogg"

    # These display lines of dialogue.
    "What a waste of time."
    "It's the summer before my 2nd year of high school and I still get shipped off to a summer camp."
    "At least it's the last night I have to be here."
    "But they set up some stupid 'Test of Courage' in the woods for our last night here."
    "We all got to choose our partners, so of course I went with my childhood best friend, Akuno."
    show adahm
    m "I'm pretty sure everyone here thinks this is stupid and childish."
    a "They probably do, but who knows. It could be fun."
    m "I guess. Let's just get this over with..."
    hide adahm
    "We step through the gate and onto the forest path."
    stop music
    play sound "night forest.ogg"
    scene bg spooky forest
    # switch to spooky forest here
    "It twists and winds through the shadowy woods and dead leaves crunch under our feet"
    m "Holy macaroni it's dark in here."
    show adahm
    a "Really? I can see pretty well."
    "Akuno has always been able to see really well in the dark. Sometimes I'm envious of his gift. Like right now, for instance."
    m "What do you see with your Elven eyAHHHHHH"
    hide adahm
    "I slipped on a loose rock and crumpled to the ground. I was sliding, turning, twisting, falling, rolling down a slope."
    "I hit trees and underbrush as I rolled down the hill, until I finally came to a stop at the bottom."
    m "ow oof owie my bones"
    m "Ah jeepers how could this have happened how clumsy I am it's almost like this was a plot device or something."
    "Everything hurt. I rose slowly to my feet and tried to look around."
    "I saw nothing but blackness around me, and the milky midnight sky above stabbing through the forest canopy."
    "The trees rustled in the wind, and it sounded like they were whispering to one another about the newest arrival to their midst."
    "Suddenly, I heard a howl like a wolf pierce through the whispers. It rang in my ears and echoed over the landscape."
    "I am afraid."
    "I am alone."
    "and now there's a frickin wolf out there somewhere."
    menu:

        "What will I do?"

        "Try to find Akuno":
            jump AkunoForest

        "Investigate the howl":
            jump OkasukiForest

label AkunoForest:

    scene bg spooky forest

    "A wolf. Howling. You really think I'm gonna go running off to my death to see what that's about?"
    "Fuck that noise."
    "I start to try to claw my way back up the slope but it's too steep."
    "I try to go around to my right to find a less steep location."
    "I trudge through the darkness. It is not easy going."
    "For one thing it's dark af out here and there's trees and roots and thorn vines and frickin SPIDER WEBS UGH"
    "Anyway, I keep moving and I eventually find a place where the slope eases off and I can climb it a little."
    "I get about halfway up the hill and onto a flat section where I pause for a second."
    "The darkness is pressing in on me from all directions. The howls continue, but they are more distant."
    "I turn to keep moving and end up plunging face-first into a tangle of thorn vines."
    "The thorns tear at me visciously. I recoil in pain and yelp."
    m "stupid plants IT'S NOT LIKE I'M TRYING TO EAT YOU OR ANYTHING JUST TRYING TO GET BY, DAMN."
    "The plants don't say anything in response."
    "I can feel blood trickling down my skin."
    a "MC? Is that you?"
    "Akuno's voice sounds suddenly from behind me. I nearly jump out of my skin, it startles me so badly."
    show adahm
    a "You really scared me there. You should watch out for cliffs in the future."
    m "Now is not the time to be snide but I appreciate the insult"
    "Another howl rings through the night."
    m "Do you have any clue what that is??"
    a "Sounds like a wolf."
    m "Eat a dick."
    "Another howl."
    a "Let's go take a look."
    m "No."
    a "Okay, I guess if you're scared..."
    m "Okay, fine."
    hide adahm
    "We start walking toward the howls, which I think is frankly a bad idea."
    "Akuno is able to move much faster than I can, and he has to stop and wait for me frequently."
    "The howls get closer and closer until we step into a small clearing."
    "In the moonlight I can see a massive black shape, hunched over in the center of the clearing."
    "It is moving slightly, and I can see it taking large shuddering breaths."
    show wolf happy
    "It starts to whine as we get closer. If it wasn't so damn huge I would've felt bad for it, whatever it is."
    "We were almost standing on top of it when I notice the spike gruesomely sticking through its leg."
    "It lay perfectly still, taking weak, raspy breaths. It seemed to be waiting for us to do something."
    show adahm
    "Akuno made a disappointed sound of indifference as he looked down on the creature, before carelessly grasping the spike and tearing it free from its leg in one fluid motion."
    "It rises up from the dirt then takes off toward the edge of the clearing without making a sound. It halts for a moment."
    "It looks back at us and I could swear I heard it say 'thank you' in a faint, feminine whisper before disappearing into the darkness."
    hide wolf happy
    "A few seconds pass as I stare dumbstruck at Akuno."
    m "whatthefuckwasthatAkuno?????????"
    a "Some kind of wolf, I guess. Who cares. It's gone now. Let's head back to camp."
    hide adahm
    "He turns and starts walking and I have no choice but to follow, my mind racing."
    "I try to question Akuno further but he doesn't say another word until we get back to the camp."
    jump camp2


label OkasukiForest:
    scene bg spooky forest

    m "I'm already in this deep I might as well go see something neat before I die."
    "I start walking in the direction from which the howl came from. It is not easy going."
    "For one thing it's dark af out here and there's trees and roots and thorn vines and frickin SPIDER WEBS UGH"
    "Anyway, I keep moving and I hear the howls getting closer and closer until I step into a small clearing."
    "In the moonlight I can see a massive black shape, hunched over in the center of the clearing."
    "It is moving slightly, and I can see it taking large shuddering breaths."
    "It starts to whine as I get closer. If it wasn't so damn huge I would've felt bad for it, whatever it is."
    "I am almost standing on top of it when I notice the spike gruesomely sticking through its leg."
    "It lay perfectly still, taking weak, raspy breaths. It seemed to be waiting for me to do something."
    "Its eyes met mine in the moonlight. I could see a sort of... understanding in them."
    "I had to do it. I had to pull the spike out."
    "I grab hold of the spike with one hand and support the creature's leg with the other."
    "I pull as hard as I can in one motion and the spike comes free."
    "The creature howls again, nearly rupturing my ear drums."
    "I notice the wound heals almost immediately after the spike is removed."
    "It shudders slightly then rises to its feet, standing on its hind legs. It towers over me by a full two head-lengths."
    "The creature and I stare at one another for a moment in the sudden silence."
    "and then..."
    "it speaks?"
    "in a human female voice it says:"
    show wolf happy
    o "Thank you."
    o "I could not remove it myself."
    "In obvious shock I said nothing."
    "She snorted in what seemed like laughter."
    o "you are from the camp?"
    "All I could do was nod stupidly"
    o "you are lost?"
    "I would say I nodded again but I never really stopped in the first place."
    "My head wagged back and forth like a bobblehead."
    o "you will want to head that way."
    "she pointed over my shoulder behind me."
    "Y'know I wish I could have said something witty or smart but really I was still just nodding like an idiot."
    "She waited another moment then put her massive hand... paw... on top of my head to stop my nodding."
    o "be careful on your way back. the scent of evil is on the wind."
    hide wolf happy
    "With that, she dropped to all fours and took off into the darkness."
    "I didn't hear a single sound from her movement, surprising given her size."
    "I stood for a moment, dumbstruck, in the clearing."
    "Finally, I started walking in the direction that she indicated, and before I knew it, I had arrived back at the camp."
    jump camp2

label camp2:

    scene camp1
    stop sound
    "this is as far as i've gotten"
