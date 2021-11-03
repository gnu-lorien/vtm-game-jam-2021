
init:
    $ t = Character('Thrall')
    $ d = Character('Domitor')
    $ raver = Character('Raver')
    $ socialite = Character('Socialite')

init:
    # Hunting events
    $ event("choleric_acute", "act == 'hunt_choleric'", event.choose_one('choleric'), priority=200)
    $ event("choleric_intense", "act == 'hunt_choleric'", event.choose_one('choleric', group_count=5), priority=200)
    $ event("choleric_fleeting", "act == 'hunt_choleric'", event.choose_one('choleric', group_count=20), priority=200)
    $ event("melancholy_acute", "act == 'hunt_melancholy'", event.choose_one('melancholy'), priority=200)
    $ event("melancholy_intense", "act == 'hunt_melancholy'", event.choose_one('melancholy', group_count=5), priority=200)
    $ event("melancholy_fleeting", "act == 'hunt_melancholy'", event.choose_one('melancholy', group_count=20), priority=200)
    $ event("phlegmatic_acute", "act == 'hunt_phlegmatic'", event.choose_one('phlegmatic'), priority=200)
    $ event("phlegmatic_intense", "act == 'hunt_phlegmatic'", event.choose_one('phlegmatic', group_count=5), priority=200)
    $ event("phlegmatic_fleeting", "act == 'hunt_phlegmatic'", event.choose_one('phlegmatic', group_count=20), priority=200)
    $ event("sanguine_acute", "act == 'hunt_sanguine'", event.choose_one('sanguine'), priority=200)
    $ event("sanguine_intense", "act == 'hunt_sanguine'", event.choose_one('sanguine', group_count=5), priority=200)
    $ event("sanguine_fleeting", "act == 'hunt_sanguine'", event.choose_one('sanguine', group_count=20), priority=200)

    # Grooming Planner
    $ event("grooming_choleric", "act == 'groom_choleric'", event.solo(), priority=200)
    $ event("grooming_melancholy", "act == 'groom_melancholy'", event.solo(), priority=200)
    $ event("grooming_phlegmatic", "act == 'groom_phlegmatic'", event.solo(), priority=200)
    $ event("grooming_sanguine", "act == 'groom_sanguine'", event.solo(), priority=200)

    # Reporting Planner
    # For rumored events start with the events from Broken Social Scenes
    # Rather than just doubling the odds of Intensity just make all of the
    # available resonances intense.
    $ event("rumor_nothing", "act == 'report_rumors'", event.choose_one('base_rumors'), priority=200)
    $ event("rumor_art_gallery", "act == 'report_rumors'", event.choose_one('base_rumors'), priority=200)
    $ event("rumor_rave", "act == 'report_rumors'", event.choose_one('base_rumors'), priority=200)

    # First up, we define some simple events for the various actions, that
    # are run only if no higher-priority event is about to occur.
    
   #$ event("class", "act == 'class'", event.only(), priority=200)
   #$ event("class_bad", "act == 'class'", priority=210)
   #$ event("cut1", "act == 'cut'", event.choose_one('cut'), priority=200)
   #$ event("cut2", "act == 'cut'", event.choose_one('cut'), priority=200)
   #$ event("fly", "act == 'fly'", event.solo(), priority=200)
   #$ event("study", "act == 'study'", event.solo(), priority=200)
   #$ event("hang", "act == 'hang'", event.solo(), priority=200)
   #$ event("exercise", "act == 'exercise'", event.solo(), priority=200)    
   #$ event("play", "act == 'play'", event.solo(), priority=200)


   ## This is an introduction event, that runs once when we first go
   ## to class. 
   #$ event("introduction", "act == 'class'", event.once(), event.only())

   ## These are the events with glasses girl.
   ##
   ## The glasses girl is studying in the library, but we do not
   ## talk to her.
   #$ event("gg_studying",
   #        # This takes place when the action is 'study'.
   #        "act == 'study'",
   #        # This will only take place if no higher-priority
   #        # event will occur.
   #        event.solo(),
   #        # This takes place at least one day after seeing the
   #        # introduction event.
   #        event.depends("introduction"),
   #        # This takes priority over the study event.
   #        priority=190)

   ## She asks to borrow our pen. 
   #$ event("borrow_pen",
   #        # This takes place when we go to study, and we have an int
   #        # >= 50. 
   #        "act == 'study' and intelligence >= 50",
   #        # It runs only once.
   #        event.once(),
   #        # It requires the introduction event to have run at least
   #        # one day before.
   #        event.depends("introduction"))

   ## After the pen, she smiles when she sees us.
   #$ event("gg_smiling", "act == 'study'",
   #        event.solo(), event.depends("borrow_pen"),
   #        priority = 180)

   ## The bookslide.
   #$ event("bookslide", "act == 'study' and intelligence == 100",
   #        event.once(), event.depends("borrow_pen"))

   ## She makes us cookies.
   #$ event("cookies", "act == 'study'",
   #        event.once(), event.depends("bookslide"))

   ## Her solo ending.
   #$ event("gg_confess", "act == 'class'",
   #        event.once(), event.depends("cookies"))
   #
   ## Here are Sporty Girl's events that happen during the exercise act.
   #$ event("catchme", "act == 'exercise'",
   #        event.depends('introduction'), event.once())
   #$ event("cantcatchme", "act == 'exercise'",
   #        event.depends('catchme'), event.solo(), priority=190)
   #$ event("caughtme", "act == 'exercise' and strength >= 50",
   #        event.depends('catchme'), event.once())
   #$ event("together", "act == 'exercise' and strength >= 50",
   #        event.depends('caughtme'), event.solo(), priority=180)
   #$ event("apart", "act == 'exercise' and strength < 50",
   #        event.depends('caughtme'), event.solo(), priority=180)
   #$ event("pothole", "act == 'exercise' and strength >= 100",
   #        event.depends('caughtme'), event.once())
   #$ event("dontsee", "act == 'exercise'",
   #        event.depends('pothole'), event.solo(), priority=170)
   #$ event("sg_confess", "act == 'class'",
   #        event.depends('dontsee'), event.once())    
   #
   ## Relaxed ending with no girls happens if we max out our hidden relaxation stat.
   #$ event("relaxed_ending", "act=='hang' and relaxation >= 100", event.once())

   ## Ending with both girls only happens if we have seen both of their final events
   ## This needs to be higher-priority than either girl's ending.    
   #$ event('both_confess', 'act == "class"',
   #        event.depends("dontsee"), event.depends("cookies"),
   #        event.once(), priority = 50)

label choleric_acute:
    "Found choleric acute"
    $ choleric += ACUTE_VALUE
    return

label choleric_intense:
    "Found intense"
    $ choleric += INTENSE_VALUE
    return

label choleric_fleeting:
    "Found choleric fleeting"
    $ choleric += FLEETING_VALUE
    return

label melancholy_acute:
    "Found melancholy acute"
    $ melancholy += ACUTE_VALUE
    return

label melancholy_intense:
    "Found intense"
    $ melancholy += INTENSE_VALUE
    return

label melancholy_fleeting:
    "Found melancholy fleeting"
    $ melancholy += FLEETING_VALUE
    return

label phlegmatic_acute:
    "Found phlegmatic acute"
    $ phlegmatic += ACUTE_VALUE
    return

label phlegmatic_intense:
    "Found intense"
    $ phlegmatic += INTENSE_VALUE
    return

label phlegmatic_fleeting:
    "Found phlegmatic fleeting"
    $ phlegmatic += FLEETING_VALUE
    return

label sanguine_acute:
    "Found sanguine acute"
    $ sanguine += ACUTE_VALUE
    return

label sanguine_intense:
    "Found intense"
    $ sanguine += INTENSE_VALUE
    return

label sanguine_fleeting:
    "Found sanguine fleeting"
    $ sanguine += FLEETING_VALUE
    return

label grooming_choleric:
    "I identify and groom the choleric people"
    $ choleric += grooming_choleric_skill
    return

label grooming_melancholy:
    "I identify and groom the melancholy people"
    $ melancholy += grooming_melancholy_skill
    return

label grooming_phlegmatic:
    "I identify and groom the phlegmatic people"
    $ phlegmatic += grooming_phlegmatic_skill
    return

label grooming_sanguine:
    "I identify and groom the sanguine people"
    $ sanguine += grooming_sanguine_skill
    return

label rumor_nothing:
    "I listen for the whispers of the night and hear nothing in return."
    $ next_rumor = None
    return

label rumor_art_gallery:
    "I seek out an artiste who knows the scene."
    socialite "A new gallery is coming through town."
    t "Why don't you get me in and we can meet up after?"
    socialite "I'll get you in, but I've got better plans for my night."
    $ next_rumor = 'art_gallery'
    return

label rumor_rave:
    "I come across a raver dressed to party."
    raver "Just one more night and we get to disappear into the sound."
    t "Is it worth it for me to show up?"
    raver "Not if you want to miss the best party this town's seen in a decade."
    $ next_rumor = 'rave'
    return
