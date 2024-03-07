# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")

#Introduce the game in the script area.

# The game starts here.

label start:

 scene scene_black

 #script de escolha de nome:

 $ povname = renpy.input("Choose your name:", length = 12)
 $ povname = povname.strip()

 if not povname:
    $ povname =  "Sam"

 #o script acaba aqui....

 scene scene_1
 with dissolve
 

 mc "Another day of work has ended. Finally, some rest..."
 mc "At least until the next project…"

 hide scene_1

 show scene_black

 mci "I contact the client to show them the finished project..."
 mci "5 pages of a website for an Animal shelter..."
 mci "All designed very diligently by me..."
 mci "......"
 mci "I glance at the window as I wait for the clients response."
 mci "Time really flies, I mean, It was late this morning when I sat here to work..."
 mci "I didn't even notice I skipped lunch."
 mci "*groans*"
 mc "...."
 mc "Well, now I noticed..."
 mci "My stomach groans..."
 mci "Suddenly I feel like I haven't eaten in days..."
 mci "I didn't think I'd be that hungry, but then again, I did have a simple breakfast and then skipped lunch."
 mci "Maybe I could have a little snack at the convenience store."
 mci "There's a good one around here, although I usually go there to do groceries, I know they have some pretty nice snacks."
 mci "Maybe I could so both this time."
 mci "Two birds, one stone."

 show scene_2
 with dissolve

 mci "I leave the house and make my way through the neighborhood, heading to the store..."
 mci "There isn't much to see around here except for the occasional friendly smile from the few neighbors I have."
 mci "But, then again, the number of people moving away from here was the soul reason why I can afford to live here, so I should be grateful about it."

 hide scene_2
 with dissolve

 show scene_5
 with dissolve

 mci "I get to the store rather quickly, time always flies when I'm lost in my thoughts, maybe that applies to distances too."
 mci "The store is almost completely deserted. It's only me, the cashier in the front and the one at the cafe..."
 mci "*groan*"
 mci "..."
 mci "I better get that snack already."
 mci "I walk towards the small cafe area in the back of the store, taking a mental note of all the things I have to restock on when I'm finished eating..."

 hide scene_5
 with dissolve

 show scene_4
 with dissolve

 show scene_3
 with dissolve
 
 mci "Once I reach the counter I'm greeted with a familiar smile."

 show AP1
 with dissolve

 ap "[povname]! Long time, no see, huh?"
 mci "It's Apollo..."
 mci "An old friend. He used to be my classmate in middle school..."
 mci "He has always been there for me ever since we first met. Somehow, we never really grew apart. In fact, I would have never heard of this place if it weren't for him."
 mc "Apollo! Great to see you! I didn't know you'd be here."
 ap "uh… why not? I work here."
 mci "He chuckles playfully..."
 mc "Yeah, well, now I know that."
 mci "I laugh and he smiles at me confused."
 ap "Only now? I told you that, when you moved here..."
 mc "huh…?"
 mci "This is awkward..."
 mci "Did he tell me?"
 mci "I glance at him..."
 mci "The confident  smug look fades into incertanty."
 ap "I mean…" 
 ap "I meant to tell you…" 
 ap "I guess..."
 mci "I'm sure he meant to..."
 mci "I chuckle..."
 mci "*Groan*"
 mci "Is it just me, or is my stomach getting louder each time..."
 mci "Apollo stares at me for a moment before letting out a soft titter..."
 ap "well, I do work here." 
 ap "So How can I help you, ma'am?"
 mci "His lips form an ironic smile when he says the last word..."

 #Primeira escolha.

 menu:
   "You're so dumb”":
      jump dumb
   "The costumer service here is awesome, good sir":
      jump drama

label continuing:
   
 show scene_4
 show scene_3
 show AP1
 with dissolve

 ap "Anyway, What will it be for today?"
 mc "Definitely, something big."
 mc "I'm super hungry!!!" 
 mc "Any recommendations?"
 ap "well…let's see."
 mci "He pauses for a moment and looks around."
 ap "The hotdogs are fresh…as in, the package was delivered today."
 ap "It will take a while to heat it on the oven, though..."
 mc "Can't you just microwave it?"
 ap "If you want raw hotdog…"
 mci "He smirks as he places a hotdog in the oven and turns it on..."
 mc "oh…no."
 ap "look, why don't you do a lap around the store? It will probably be ready when you're finished restocking."
 mci "I sigh and look around..." 
 mci "As much as I want to procrastinate, I do need to get the groceries done."
 mc "I don't think there's another route…"
 ap "Nope..."
 mci "Before I can turn around, I see Apollo's playful expression morph into a worried one..."
 
 hide AP1
 with dissolve

 show AP3
 with dissolve
 
 mci "I follow his gaze and see someone else at the store..."
 mci "When did he get here? I didn't see or hear anybody else here."
 ap "This guy…"
 mci "Apollo muttered something else, but I wasn't able to hear."
 mc "You know him?"
 mci "Apollo stared at me for a moment, before answering..." 
 mci "He didn't seem very pleased with this guy's presence."
 ap "No."
 mci "Awkward..."
 mci "Very awkward..."
 mci "I turn around to leave, sensing this weird tension grow..."
 mci "All of a sudden, Apollo pulls me back by my shoulder, making me face him..."
 ap "Just...beware, okay?"
 mci "Our playful mood is completely gone now..."
 mci "I glance to the guy in question, then back to apollo and nod..."
 mci "I didn't see any problem with this man, initially."
 mci "Sure he isn't someone I'd be begging to talk to, but now I'm quite curious…"
 mci "Do they have beef of something?"
 mci "Anyway, I must get some things done here, no time to waste."
 mci "If it's important, I'll most likely find out."

 hide AP3
 with dissolve

 show scene_5
 with dissolve

 mci "*Sigh*"

 #Time Skip:

 #teste
 jump endgame

label endgame:

 window hide dissolve

 pause 1.0

 show scene_credits

 $ renpy.pause(4.0)

return
