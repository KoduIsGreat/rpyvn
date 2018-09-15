# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define a = Character("Aryal")
define e = Character("Eliee")
image bg walledvalley = "images/walledvalley.png"
image bg ocean = "images/ocean.png"
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    play music "deep jam.ogg"

    # These display lines of dialogue.
    "Its a cold Autumn morning, the light breaks in and gently grazes The slumbering wolf-lady Aryal"
    a "How is it morning already... I better go find Eliee."
    menu:

        "Where would she be..."

        "She would go to the valley":
            jump valley

        "She would go to the ocean":
            jump ocean
    # This ends the game.


label valley:

    scene bg walledvalley
    a "Those are some beautiful mountains aren't they...? But i dont se Eliee anywhere.."
    jump ocean


label ocean:
    scene bg ocean

    a "Nothing like the ocean breeze at night..."
    a "Ah.. there she is fishing as always..."
    show eileen happy

    e "Oh hey Aryal"

    a "I've been wondering  where you were!"