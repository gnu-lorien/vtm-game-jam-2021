# The Dating Sim Engine was written by PyTom, 
# with updates added by Andrea Landaker (qirien),
# and contributions by Edmund Wilfong (Pneumonica)
#
# For support, see the Lemma Soft forums thread:
# http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=31571
#
# It is released under the MIT License - see DSE-LICENSE.txt
#
#
# This is the main part of the program, where you setup your schedule and
# the options for the user. You can change the stats, periods, and choices
# here; just make sure they match up with the events setup in
# dse-events.rpy.  You can even have different time periods (months, instead
# of times of day, for example).

# Set up a default schedule.
init python:

    FLEETING_VALUE = 1
    INTENSE_VALUE = 5
    ACUTE_VALUE = 20

    # Core sheets stats for the thrall you are playing as
    register_stat("Strength", "strength", 10, 100, hidden=True)
    #register_stat("Dexterity", "dexterity", 10, 100)
    #register_stat("Stamina", "stamina", 10, 100)
    #register_stat("Charisma", "charisma", 10, 100)
    #register_stat("Manipulation", "manipulation", 10, 100)
    #register_stat("Composure", "composure", 10, 100)
    register_stat("Intelligence", "intelligence", 10, 100, hidden=True)
    #register_stat("Wits", "wits", 10, 100)
    #register_stat("Resolve", "resolve", 10, 100)
    #register_stat("Relaxation", "relaxation", hidden=True)

    register_stat("Grooming Choleric", "grooming_choleric_skill", 10, 100, hidden=True)
    register_stat("Grooming Melancholy", "grooming_melancholy_skill", 10, 100, hidden=True)
    register_stat("Grooming Phlegmatic", "grooming_phlegmatic_skill", 10, 100, hidden=True)
    register_stat("Grooming Sanguine", "grooming_sanguine_skill", 10, 100, hidden=True)

    # Circulatory System stats
    register_stat("Choleric", "choleric", 0, 100)
    register_stat("Melancholy", "melancholy", 0, 100)
    register_stat("Phlegmatic", "phlegmatic", 0, 100)
    register_stat("Sanguine", "sanguine", 0, 100)

    # Domitor's opinion of you
    register_stat("Regnant Satisfaction", "satisfaction", 10, 100, hidden=True)

    # Hunting for new Resonance sources
    dp_period("Hunting", "hunting_act")
    dp_choice("D Choleric", "hunt_choleric_debug", show="DEBUG_MODE")
    dp_choice("D Melancholy", "hunt_melancholy_debug", show="DEBUG_MODE")
    dp_choice("D Phlegmatic", "hunt_phlegmatic_debug", show="DEBUG_MODE")
    dp_choice("D Sanguine", "hunt_sanguine_debug", show="DEBUG_MODE")
    dp_choice("Wander", "hunt_wander")
    dp_choice("No Special Events", "hunt_no_special", show="next_rumor is None", enable="False")
    dp_choice("Art Gallery", "hunt_art_gallery", show="next_rumor == 'art_gallery'", enable="True")
    dp_choice("Rave", "hunt_rave", show="next_rumor == 'rave'", enable="True")

    # Improving and maintaining current resonance sources
    # Fleeting, Intense, and acute.
    dp_period("Grooming", "grooming_act")
    dp_choice("None", "groom_none")
    dp_choice("Choleric", "groom_choleric", show="choleric >= 1 and choleric <= 100")
    dp_choice("Melancholy", "groom_melancholy", show="melancholy >= 1 and melancholy <= 100")
    dp_choice("Phlegmatic", "groom_phlegmatic", show="phlegmatic >= 1 and phlegmatic <= 100")
    dp_choice("Sanguine", "groom_sanguine", show="sanguine >= 1 and sanguine <= 100")

    # Working your information sources to get intel. p 334
    dp_period("Hitting the Streets", "streets_act")
    dp_choice("None", "streets_none")
    dp_choice("Legwork", "streets_legwork")
    dp_choice("Paper Chase", "streets_paperchase")
    dp_choice("Scrounging", "streets_scrounging")

    dp_period("Midnight", "midnight_act")
    
# This is the entry point into the game.
label start:

    # Initialize the default values of some of the variables used in
    # the game.
    $ day = 0
    $ next_rumor = None
    $ current_goal = None
    $ DEBUG_MODE = True

    # Show a default background.
    scene black

    # The script here is run before any event.

    "It's not been very long since my Domitor first took me."

    "I don't know much about what's expected of me."

    "I do know that I'm supposed to find others like me and provide them."

    "I don't know what else she wants with me."

    # We jump to day to start the first day.
    jump day


# This is the label that is jumped to at the start of a day.
label day:

    # Increment the day it is.
    $ day += 1

    # We may also want to compute the name for the day here, but
    # right now we don't bother.

    "It's day %(day)d."

    # Here, we want to set up some of the default values for the
    # day planner. In a more complicated game, we would probably
    # want to add and remove choices from the dp_ variables
    # (especially dp_period_acts) to reflect the choices the
    # user has available.

    $ hunting_act = None
    $ grooming_act = None
    $ streets_act = None
    # Evolve this as your feelings towards her change?
    $ narrator("How shall I satisfy my domitor?", interact=False)
    window show
    

    # Now, we call the day planner, which may set the act variables
    # to new values. We call it with a list of periods that we want
    # to compute the values for.
    call screen day_planner(["Hitting the Streets", "Grooming", "Hunting"])
    window auto
    
    # We process each of the three periods of the day, in turn.
label hitting_the_streets:
    centered "Hitting the Streets"

    $ period = "streets"
    $ act = streets_act
    
    call events_run_period

label grooming:
    if check_skip_period():
        jump hunting

    centered "Grooming"

    $ period = "grooming"
    $ act = grooming_act

    call events_run_period

label hunting:
    if check_skip_period():
        jump midnight

    centered "Hunting"

    $ period = "hunting"
    $ act = hunting_act

    call events_run_period

label midnight:
    centered "Midnight"

    $ period = "midnight"
    $ act = None

    call events_run_period

label daybreak:

    # This is now the end of the day, and not a period in which
    # events can be run. We put some boilerplate end-of-day text
    # in here.

    centered "Daybreak"

    "My Domitor has gone to sleep for the day. Now I can rest."

    # We call events_end_day to let it know that the day is done.
    call events_end_day

    # And we jump back to day to start the next day. This goes
    # on forever, until an event ends the game.
    jump day
