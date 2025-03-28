
# sentiment是最终情感
PROMPT_standard_implicit = [
    """
    Review: I should have checked this before I installed my applications.
    Sentiment: neutral
    """,
    """
    Review: My last computer, a Toshiba, cost only $400, and worked like a charm for many years.
    Sentiment: positive
    """,
    """
    Review: when i first got it i thought the size of it was a joke.
    Sentiment: negative
    """,
    """
    Review: Learning all of the keyboard shortcuts only took a few minutes to get used to as some of the shortcuts are the same on Windows machines.
    Sentiment: positive
    """,
    """
    Review: There is a small red circle next to it with a x in the middle, and when I click on it it says: " Consider replacing your battery" and it does not hold full charge.
    Sentiment: negative
    """,
    """
    Review: The laptop is outstanding in all aspects except that it has the Windows 7 starter and not the full Windows 7.
    Sentiment: neutral
    """,
    """
    Review: they improved nothing else such as Resolution, appearance, cooling system, graphics card, etc.
    Sentiment: negative
    """,
    """
    Review: I'm using this computer for word processing, web browsing, some gaming, and I'm learning programming.
    Sentiment: neutral
    """,
    """
    Review: I even got my teenage son one, because of the features that it offers, like, iChat, Photobooth, garage band and more!
    Sentiment: positive
    """,
    """
    Review: It's been time for a new laptop, and the only debate was which size of the Mac laptops, and whether to spring for the retina display.
    Sentiment: neutral
    """,
    """
    Review: The reason why I choose apple MacBook because of their design and the aluminum casing.
    Sentiment: positive
    """,
    """
    Review: Also, in using the built-in camera, my voice recording for my vlog sounds like the interplanetary transmissions in the "Star Wars" saga.
    Sentiment: negative
    """,
    """
    Review: In desparation, I called their Customer Service number and was told that my warranty had expired (2 days old) and that the priviledge of talking to a technician would cost me ("have your credit card ready").
    Sentiment: negative
    """,
    """
    Review: The speed, the simplicity, the design.. it is lightyears ahead of any PC I have ever owned.
    Sentiment: positive
    """,
    """
    Review: That's very possible, but since they don't make Windows XP drivers for the sound card in this machine, I was stuck until Windows 7 came out.
    Sentiment: neutral
    """,
    """
    Review: It gives me the power and speed that I need to run all the programs I use to edit.
    Sentiment: positive
    """,
    """
    Review: Setting would change for some reason, the screen size would change on it's own, like the pixel sizes and whatnot.
    Sentiment: negative
    """,
    """
    Review: I work in film editing and post production, so I need a laptop that not only has power, but memory and speed as well.
    Sentiment: neutral
    """,
]

PROMPT_implicit_COT_V1 = [
    """
    Review: I should have checked this before I installed my applications.
    COT: Because the applications is neutral, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: My last computer, a Toshiba, cost only $400, and worked like a charm for many years.
    COT: Because the cost is positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: when i first got it i thought the size of it was a joke.
    COT: Because the size is negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: Learning all of the keyboard shortcuts only took a few minutes to get used to as some of the shortcuts are the same on Windows machines.
    COT: Because the keyboard shortcuts are positive, the shortcuts are neutral, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: There is a small red circle next to it with a x in the middle, and when I click on it it says: " Consider replacing your battery" and it does not hold full charge.
    COT: Because the battery is neutral, the charge is negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: The laptop is outstanding in all aspects except that it has the Windows 7 starter and not the full Windows 7.
    COT: Because the Windows 7 starter is negative, the Windows 7 is positive, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: they improved nothing else such as Resolution, appearance, cooling system, graphics card, etc.
    COT: Because the Resolution is negative, the appearance is negative, the cooling system is negative, the graphics card is negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: I'm using this computer for word processing, web browsing, some gaming, and I'm learning programming.
    COT: Because the word processing is neutral, the web browsing is neutral, the gaming is neutral, the programming is neutral, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: I even got my teenage son one, because of the features that it offers, like, iChat, Photobooth, garage band and more!
    COT: Because the features are positive, iChat is positive, Photobooth is positive, garage band is positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: It's been time for a new laptop, and the only debate was which size of the Mac laptops, and whether to spring for the retina display.
    COT: Because the size is neutral, the retina display is neutral, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: The reason why I choose apple MacBook because of their design and the aluminum casing.
    COT: Because the design is positive, the aluminum casing is positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: Also, in using the built-in camera, my voice recording for my vlog sounds like the interplanetary transmissions in the "Star Wars" saga.
    COT: Because the built-in camera is neutral, the voice recording is negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: In desparation, I called their Customer Service number and was told that my warranty had expired (2 days old) and that the priviledge of talking to a technician would cost me ("have your credit card ready").
    COT: Because the Customer Service number is neutral, the warranty is negative, the talking to a technician is negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: The speed, the simplicity, the design.. it is lightyears ahead of any PC I have ever owned.
    COT: Because the speed is positive, the simplicity is positive, the design is positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: That's very possible, but since they don't make Windows XP drivers for the sound card in this machine, I was stuck until Windows 7 came out.
    COT: Because the Windows XP drivers are negative, the sound card is negative, the Windows 7 is positive, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: It gives me the power and speed that I need to run all the programs I use to edit.
    COT: Because the power is positive, the speed is positive, the programs are neutral, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: Setting would change for some reason, the screen size would change on it's own, like the pixel sizes and whatnot.
    COT: Because the Setting is negative, the screen size is negative, the pixel sizes are negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: I work in film editing and post production, so I need a laptop that not only has power, but memory and speed as well.
    COT: Because the power is neutral, the memory is neutral, the speed is neutral, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
]

PROMPT_implicit_COT_V2 = [
    """
    Review: I should have checked this before I installed my applications.
    COT: The sentiment polarity of (application) goes through (neutral) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: My last computer, a Toshiba, cost only $400, and worked like a charm for many years.
    COT: The sentiment polarity of (cost) goes through (positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: when i first got it i thought the size of it was a joke.
    COT: The sentiment polarity of (size) goes through (negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: Learning all of the keyboard shortcuts only took a few minutes to get used to as some of the shortcuts are the same on Windows machines.
    COT: The sentiment polarity of (keyboard shortcuts, shortcuts) goes through (positive, neutral) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: There is a small red circle next to it with a x in the middle, and when I click on it it says: " Consider replacing your battery" and it does not hold full charge.
    COT: The sentiment polarity of (battery, charge) goes through (neutral, negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: The laptop is outstanding in all aspects except that it has the Windows 7 starter and not the full Windows 7.
    COT: The sentiment polarity of (Windows 7 starter, Windows 7) goes through (negative, positive) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: they improved nothing else such as Resolution, appearance, cooling system, graphics card, etc.
    COT: The sentiment polarity of (Resolution, appearance, cooling system, graphics card) goes through (negative, negative, negative, negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: I'm using this computer for word processing, web browsing, some gaming, and I'm learning programming.
    COT: The sentiment polarity of (word processing, web browsing, gaming, programming) goes through (neutral, neutral, neutral, neutral) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: I even got my teenage son one, because of the features that it offers, like, iChat, Photobooth, garage band and more!
    COT: The sentiment polarity of (features, iChat, Photobooth, garage band) goes through (positive, positive, positive, positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: It's been time for a new laptop, and the only debate was which size of the Mac laptops, and whether to spring for the retina display.
    COT: The sentiment polarity of (size, retina display) goes through (neutral, neutral) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: The reason why I choose apple MacBook because of their design and the aluminum casing.
    COT: The sentiment polarity of (design, aluminum casing) goes through (positive, positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: Also, in using the built-in camera, my voice recording for my vlog sounds like the interplanetary transmissions in the "Star Wars" saga.
    COT: The sentiment polarity of (built-in camera, voice recording) goes through (neutral, negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: In desparation, I called their Customer Service number and was told that my warranty had expired (2 days old) and that the priviledge of talking to a technician would cost me ("have your credit card ready").
    COT: The sentiment polarity of (Customer Service number, warranty, talking to a technician) goes through (neutral, negative, negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: The speed, the simplicity, the design.. it is lightyears ahead of any PC I have ever owned.
    COT: The sentiment polarity of (speed, simplicity, design) goes through (positive, positive, positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: That's very possible, but since they don't make Windows XP drivers for the sound card in this machine, I was stuck until Windows 7 came out.
    COT: The sentiment polarity of (Windows XP drivers, sound card, Windows 7) goes through (negative, negative, positive) in sequence. Andthe overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: It gives me the power and speed that I need to run all the programs I use to edit.
    COT: The sentiment polarity of (power, speed, programs) goes through (positive, positive, neutral) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: Setting would change for some reason, the screen size would change on it's own, like the pixel sizes and whatnot.
    COT: The sentiment polarity of (Setting, screen size, pixel sizes) goes through (negative, negative, negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: I work in film editing and post production, so I need a laptop that not only has power, but memory and speed as well.
    COT: The sentiment polarity of (power, memory, speed) goes through (neutral, neutral, neutral) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
]

PROMPT_implicit_COT_V3 = [
    """
    Review: I should have checked this before I installed my applications.
    COT: neutral -> neutral
    Sentiment: neutral
    """,
    """
    Review: My last computer, a Toshiba, cost only $400, and worked like a charm for many years.
    COT: positive -> positive
    Sentiment: positive
    """,
    """
    Review: when i first got it i thought the size of it was a joke.
    COT: negative -> negative
    Sentiment: negative
    """,
    """
    Review: Learning all of the keyboard shortcuts only took a few minutes to get used to as some of the shortcuts are the same on Windows machines.
    COT: positive -> neutral -> positive
    Sentiment: positive
    """,
    """
    Review: There is a small red circle next to it with a x in the middle, and when I click on it it says: " Consider replacing your battery" and it does not hold full charge.
    COT: neutral -> negative -> negative
    Sentiment: negative
    """,
    """
    Review: The laptop is outstanding in all aspects except that it has the Windows 7 starter and not the full Windows 7.
    COT: negative -> positive -> neutral
    Sentiment: neutral
    """,
    """
    Review: they improved nothing else such as Resolution, appearance, cooling system, graphics card, etc.
    COT: negative -> negative -> negative -> negative -> negative
    Sentiment: negative
    """,
    """
    Review: I'm using this computer for word processing, web browsing, some gaming, and I'm learning programming.
    COT: neutral -> neutral -> neutral -> neutral -> neutral
    Sentiment: neutral
    """,
    """
    Review: I even got my teenage son one, because of the features that it offers, like, iChat, Photobooth, garage band and more!
    COT: positive -> positive -> positive -> positive -> positive
    Sentiment: positive
    """,
    """
    Review: It's been time for a new laptop, and the only debate was which size of the Mac laptops, and whether to spring for the retina display.
    COT: neutral -> neutral -> neutral
    Sentiment: neutral
    """,
    """
    Review: The reason why I choose apple MacBook because of their design and the aluminum casing.
    COT: positive -> positive -> positive
    Sentiment: positive
    """,
    """
    Review: Also, in using the built-in camera, my voice recording for my vlog sounds like the interplanetary transmissions in the "Star Wars" saga.
    COT: neutral -> negative -> negative
    Sentiment: negative
    """,
    """
    Review: In desparation, I called their Customer Service number and was told that my warranty had expired (2 days old) and that the priviledge of talking to a technician would cost me ("have your credit card ready").
    COT: neutral -> negative -> negative -> negative
    Sentiment: negative
    """,
    """
    Review: The speed, the simplicity, the design.. it is lightyears ahead of any PC I have ever owned.
    COT: positive -> positive -> positive -> positive
    Sentiment: positive
    """,
    """
    Review: That's very possible, but since they don't make Windows XP drivers for the sound card in this machine, I was stuck until Windows 7 came out.
    COT: negative -> negative -> positive -> neutral
    Sentiment: neutral
    """,
    """
    Review: It gives me the power and speed that I need to run all the programs I use to edit.
    COT: positive -> positive -> neutral -> positive
    Sentiment: positive
    """,
    """
    Review: Setting would change for some reason, the screen size would change on it's own, like the pixel sizes and whatnot.
    COT: negative -> negative -> negative -> negative
    Sentiment: negative
    """,
    """
    Review: I work in film editing and post production, so I need a laptop that not only has power, but memory and speed as well.
    COT: neutral -> neutral -> neutral -> neutral
    Sentiment: neutral
    """,
]

