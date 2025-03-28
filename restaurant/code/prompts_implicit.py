
# sentiment是最终情感
PROMPT_standard_implicit = [
    """
    Review: last Tuesday for a late lunch with a friend.
    Sentiment: neutral
    """,
    """
    Review: their brunch menu had something for everyone.
    Sentiment: positive
    """,
    """
    Review: You have to increase the service a lot.
    Sentiment: negative
    """,
    """
    Review: The first time I went, and was completely taken by the live jazz band and atmosphere, I ordered the Lobster Cobb Salad.
    Sentiment: positive
    """,
    """
    Review: The waitress came by to pick up the soy sauce WHILE we were eating our lunch!!!!!
    Sentiment: negative
    """,
    """
    Review: The bill is approximately $25 for 2 at lunch without drinks.
    Sentiment: neutral
    """,
    """
    Review: To my right, the hostess stood over a busboy and hissed rapido, rapido as he tried to clear and re-set a table for six.
    Sentiment: negative
    """,
    """
    Review: Entrees include classics like lasagna, fettuccine Alfredo and chicken parmigiana.
    Sentiment: neutral
    """,
    """
    Review: From the erbazzone emiliana to the mostarda on the cheese plate, the dishes at this restaurant are all handled with delicate care.
    Sentiment: positive
    """,
    """
    Review: I had roast chicken and a salad.
    Sentiment: neutral
    """,
    """
    Review: the real kicker of the menu, however, is the beef cubes or the chicken with chili and lemon grass.
    Sentiment: positive
    """,
    """
    Review: All the money went into the interior decoration, none of it went to the chefs.
    Sentiment: negative
    """,
    """
    Review: Would you ever believe that when you complain about over an hour wait, when they tell you it will be 20-30 minutes, the manager tells the bartender to spill the drinks you just paid for?
    Sentiment: negative
    """,
    """
    Review: If anyones has doubt of not knowing enough about wines,please check their wine list.
    Sentiment: positive
    """,
    """
    Review: We started with the scallops and asparagus and also had the soft shell crab as well as the cheese plate.
    Sentiment: neutral
    """,
    """
    Review: It doesn't look like much on the outside, but the minute you walk inside, it's a whole other atmosphere.
    Sentiment: positive
    """,
    """
    Review: For the price you pay for the food here, you'd expect it to be at least on par with other Japanese restaurants.
    Sentiment: negative
    """,
    """
    Review: It's about $7 for lunch and they have take-out or dine-in.
    Sentiment: neutral
    """,
]

PROMPT_implicit_COT_V1 = [
    """
    Review: last Tuesday for a late lunch with a friend.
    COT: Because the late lunch is neutral, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: their brunch menu had something for everyone.
    COT: Because the brunch menu is positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: You have to increase the service a lot.
    COT: Because the service is negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: The first time I went, and was completely taken by the live jazz band and atmosphere, I ordered the Lobster Cobb Salad.
    COT: Because the live jazz band is positive, the atmosphere is positive, the Lobster Cobb Salad is neutral, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: The waitress came by to pick up the soy sauce WHILE we were eating our lunch!!!!!
    COT: Because the waitress is negative, the soy sauce is neutral, the lunch is neutral, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: The bill is approximately $25 for 2 at lunch without drinks.
    COT: Because the bill is neutral, the lunch is neutral, the drinks are neutral, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: To my right, the hostess stood over a busboy and hissed rapido, rapido as he tried to clear and re-set a table for six.
    COT: Because the hostess is negative, the busboy is neutral, the table is neutral, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: Entrees include classics like lasagna, fettuccine Alfredo and chicken parmigiana.
    COT: Because the Entrees is neutral, the lasagna is neutral, the fettuccine Alfredo is neutral, the chicken parmigiana is neutral, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: From the erbazzone emiliana to the mostarda on the cheese plate, the dishes at this restaurant are all handled with delicate care.
    COT: Because the erbazzone emiliana is positive, the mostarda on the cheese plate is positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: I had roast chicken and a salad.
    COT: Because the roast chicken is neutral, the salad is neutral, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: the real kicker of the menu, however, is the beef cubes or the chicken with chili and lemon grass.
    COT: Because the menu is neutral, the beef cubes is positive, the chicken with chili and lemon grass is positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: All the money went into the interior decoration, none of it went to the chefs.
    COT: Because the interior decoration is positive, the chefs are negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: Would you ever believe that when you complain about over an hour wait, when they tell you it will be 20-30 minutes, the manager tells the bartender to spill the drinks you just paid for?
    COT: Because the wait is negative, the manager is negative, the bartender is neutral, the drinks are neutral, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: If anyones has doubt of not knowing enough about wines,please check their wine list.
    COT: Because the wines is neutral, the wine list is positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: We started with the scallops and asparagus and also had the soft shell crab as well as the cheese plate.
    COT: Because the scallops is neutral, the asparagus is neutral, the soft shell crab is neutral, the cheese plate is neutral, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: It doesn't look like much on the outside, but the minute you walk inside, it's a whole other atmosphere.
    COT: Because the outside is negative, the atmosphere is positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: For the price you pay for the food here, you'd expect it to be at least on par with other Japanese restaurants.
    COT: Because the price is negative, the food is negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: It's about $7 for lunch and they have take-out or dine-in.
    COT: Because the lunch is neutral, the take-out is neutral, the dine-in is neutral, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
]

PROMPT_implicit_COT_V2 = [
    """
    Review: last Tuesday for a late lunch with a friend.
    COT: The sentiment polarity of (late lunch) goes through (neutral) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: their brunch menu had something for everyone.
    COT: The sentiment polarity of (brunch menu) goes through (positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: You have to increase the service a lot.
    COT: The sentiment polarity of (service) goes through (negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: The first time I went, and was completely taken by the live jazz band and atmosphere, I ordered the Lobster Cobb Salad.
    COT: The sentiment polarity of (live jazz band, atmosphere, Lobster Cobb Salad) goes through (positive, positive, neutral) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: The waitress came by to pick up the soy sauce WHILE we were eating our lunch!!!!!
    COT: The sentiment polarity of (waitress, soy sauce, lunch) goes through (negative, neutral, neutral) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: The bill is approximately $25 for 2 at lunch without drinks.
    COT: The sentiment polarity of (bill, lunch, drinks) goes through (neutral, neutral, neutral) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: To my right, the hostess stood over a busboy and hissed rapido, rapido as he tried to clear and re-set a table for six.
    COT: The sentiment polarity of (hostess, busboy, table) goes through (negative, neutral, neutral) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: Entrees include classics like lasagna, fettuccine Alfredo and chicken parmigiana.
    COT: The sentiment polarity of (Entrees,lasagna, fettuccine Alfredo, chicken parmigiana) goes through (neutral, neutral, neutral, neutral) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: From the erbazzone emiliana to the mostarda on the cheese plate, the dishes at this restaurant are all handled with delicate care.
    COT: The sentiment polarity of (erbazzone emiliana, mostarda on the cheese plate) goes through (positive, positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: I had roast chicken and a salad.
    COT: The sentiment polarity of (roast chicken, salad) goes through (neutral, neutral) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: the real kicker of the menu, however, is the beef cubes or the chicken with chili and lemon grass.
    COT: The sentiment polarity of (menu, beef cubes, chicken with chili and lemon grass) goes through (neutral, positive, positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: All the money went into the interior decoration, none of it went to the chefs.
    COT: The sentiment polarity of (interior decoration, chefs) goes through (positive, negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: Would you ever believe that when you complain about over an hour wait, when they tell you it will be 20-30 minutes, the manager tells the bartender to spill the drinks you just paid for?
    COT: The sentiment polarity of (wait, manager, bartender, drinks) goes through (negative, negative, neutral,neutral) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: If anyones has doubt of not knowing enough about wines,please check their wine list.
    COT: The sentiment polarity of (wines, wine list) goes through (neutral, positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: We started with the scallops and asparagus and also had the soft shell crab as well as the cheese plate.
    COT: The sentiment polarity of (scallops, asparagus, soft shell crab, cheese plate) goes through (neutral, neutral, neutral, neutral) in sequence. Andthe overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: It doesn't look like much on the outside, but the minute you walk inside, it's a whole other atmosphere.
    COT: The sentiment polarity of (outside, atmosphere) goes through (negative, positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: For the price you pay for the food here, you'd expect it to be at least on par with other Japanese restaurants.
    COT: The sentiment polarity of (price, food) goes through (negative, negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: It's about $7 for lunch and they have take-out or dine-in.
    COT: The sentiment polarity of (lunch, take-out, dine-in) goes through (neutral, neutral, neutral) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
]

PROMPT_implicit_COT_V3 = [ 
    """
    Review: last Tuesday for a late lunch with a friend.
    COT: neutral -> neutral
    Sentiment: neutral
    """,
    """
    Review: their brunch menu had something for everyone.
    COT: positive -> positive
    Sentiment: positive
    """,
    """
    Review: You have to increase the service a lot.
    COT: negative -> negative
    Sentiment: negative
    """,
    """
    Review: The first time I went, and was completely taken by the live jazz band and atmosphere, I ordered the Lobster Cobb Salad.
    COT: positive -> positive -> neutral -> positive
    Sentiment: positive
    """,
    """
    Review: The waitress came by to pick up the soy sauce WHILE we were eating our lunch!!!!!
    COT: negative -> neutral -> neutral -> negative
    Sentiment: negative
    """,
    """
    Review: The bill is approximately $25 for 2 at lunch without drinks.
    COT: neutral -> neutral -> neutral -> neutral
    Sentiment: neutral
    """,
    """
    Review: To my right, the hostess stood over a busboy and hissed rapido, rapido as he tried to clear and re-set a table for six.
    COT: negative -> neutral -> neutral -> negative
    Sentiment: negative
    """,
    """
    Review: Entrees include classics like lasagna, fettuccine Alfredo and chicken parmigiana.
    COT: neutral -> neutral -> neutral -> neutral -> neutral
    Sentiment: neutral
    """,
    """
    Review: From the erbazzone emiliana to the mostarda on the cheese plate, the dishes at this restaurant are all handled with delicate care.
    COT: positive -> positive -> positive
    Sentiment: positive
    """,
    """
    Review: I had roast chicken and a salad.
    COT: neutral -> neutral -> neutral
    Sentiment: neutral
    """,
    """
    Review: the real kicker of the menu, however, is the beef cubes or the chicken with chili and lemon grass.
    COT: neutral -> positive -> positive -> positive
    Sentiment: positive
    """,
    """
    Review: All the money went into the interior decoration, none of it went to the chefs.
    COT: positive -> negative -> negative
    Sentiment: negative
    """,
    """
    Review: Would you ever believe that when you complain about over an hour wait, when they tell you it will be 20-30 minutes, the manager tells the bartender to spill the drinks you just paid for?
    COT: negative -> negative -> neutral -> neutral -> negative
    Sentiment: negative

    """,
    """
    Review: If anyones has doubt of not knowing enough about wines,please check their wine list.
    COT: neutral -> positive -> positive.
    Sentiment: positive
    """,
    """
    Review: We started with the scallops and asparagus and also had the soft shell crab as well as the cheese plate.
    COT: neutral -> neutral -> neutral -> neutral -> neutral
    Sentiment: neutral
    """,
    """
    Review: It doesn't look like much on the outside, but the minute you walk inside, it's a whole other atmosphere.
    COT: negative -> positive -> positive
    Sentiment: positive
    """,
    """
    Review: For the price you pay for the food here, you'd expect it to be at least on par with other Japanese restaurants.
    COT: negative -> negative -> negative
    Sentiment: negative
    """,
    """
    Review: It's about $7 for lunch and they have take-out or dine-in.
    COT: neutral -> neutral -> neutral -> neutral
    Sentiment: neutral
    """,
]

