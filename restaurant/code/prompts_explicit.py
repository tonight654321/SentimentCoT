

# sentiment是最终情感
PROMPT_standard_explicit = [
    """
    Review: we were seated at the sushi bar in front of yasuda.
    Sentiment: neutral
    """,
    """
    Review: While the smoothies are a little big for me, the fresh juices are the best I have ever had!
    Sentiment: positive
    """,
    """
    Review: I ate here a week ago and found most dishes average at best and too expensive.
    Sentiment: negative
    """,
    """
    Review: This little place is wonderfully warm welcoming.
    Sentiment: positive
    """,
    """
    Review: I've had pizza both times and the caprese salad appetizer.
    Sentiment: neutral
    """,
    """
    Review: Given the incredible architecture surrounding it, this place has no character.
    Sentiment: negative
    """,
    """
    Review: Great roofdeck, nice group of 30 somethings, but no music, kind of quiet.
    Sentiment: neutral
    """,
    """
    Review: However, if you want great food at a great price and don't mind the decor, you can't beat this place.
    Sentiment: positive
    """,
    """
    Review: It's a shame that a nice, convenient place like the Pink Pony can be so ruined by lousy service.
    Sentiment: negative
    """,
    """
    Review: The menu is limited but almost all of the dishes are excellent.
    Sentiment: positive
    """,
    """
    Review: The cafe itself was really nice with comfortable outdoor chairs and tables, but the service could have been better.
    Sentiment: neutral
    """,
    """
    Review: While we enjoyed the food, we were highly disappointed by the poor service (waiter was not quite competent and SLOW service) and lack of remorse.
    Sentiment: negative
    """,
    """
    Review: The service was mediocre, and the lack of air conditioning made for a less than comfortable meal.
    Sentiment: negative
    """,
    """
    Review: The prices are about $9 for an entree for dinner and even less for lunch.
    Sentiment: neutral
    """,
    """
    Review: You don't go to Mizu for excellent service, you go for the large amounts of food, the amiable atmosphere, and the hole-in-the-wall feeling of the place.
    Sentiment: positive
    """,
    """
    Review: The food itself was just ok - nothing spectacular - but the service was awful.
    Sentiment: negative
    """,
    """
    Review: The service was attentive without being overbearing and each dish we tried was wonderful from the spring rolls to the cod with pineapple tempura.
    Sentiment: positive
    """,
    """
    Review: Probably much busier for lunch, it's seldom crowded for dinner (too close to downtown).
    Sentiment: neutral
    """
]

PROMPT_explicit_COT_V1 = [
    """
    Review: we were seated at the sushi bar in front of yasuda.
    COT: Because the sushi bar is neutral, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: While the smoothies are a little big for me, the fresh juices are the best I have ever had!
    COT: Because the smoothies are negative, the fresh juices are positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: I ate here a week ago and found most dishes average at best and too expensive.
    COT: Because the dishes is negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: This little place is wonderfully warm welcoming.
    COT: Because the place is positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: I've had pizza both times and the caprese salad appetizer.
    COT: Because the pizza is neutral, the caprese salad appetizer is neutral, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: Given the incredible architecture surrounding it, this place has no character.
    COT: Because the architecture is positive, the place is negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: Great roofdeck, nice group of 30 somethings, but no music, kind of quiet.
    COT: Because the roofdeck is positive, the music is negative, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: However, if you want great food at a great price and don't mind the decor, you can't beat this place.
    COT: Because the food is positive, the price is positive, the decor is negative, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: It's a shame that a nice, convenient place like the Pink Pony can be so ruined by lousy service.
    COT: Because the place is positive, the service is negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: The menu is limited but almost all of the dishes are excellent.
    COT: Because the menu is negative, the dishes is positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: The cafe itself was really nice with comfortable outdoor chairs and tables, but the service could have been better.
    COT: Because the cafe is positive, the outdoor chairs are positive, the tables are positive, the service is negative, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: While we enjoyed the food, we were highly disappointed by the poor service (waiter was not quite competent and SLOW service) and lack of remorse.
    COT: Because the food is positive, the service is negative, the waiter is negative, the service is negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: The service was mediocre, and the lack of air conditioning made for a less than comfortable meal.
    COT: Because the service is neutral, the air conditioning is negative, the meal is negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: The prices are about $9 for an entree for dinner and even less for lunch.
    COT: Because the prices is positive, the entree is positive, the dinner is neutral, the lunch is positive, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: You don't go to Mizu for excellent service, you go for the large amounts of food, the amiable atmosphere, and the hole-in-the-wall feeling of the place.
    COT: Because the service is negative, the food is positive, the atmosphere is positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: The food itself was just ok - nothing spectacular - but the service was awful.
    COT: Because the food is neutral, the service is negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: The service was attentive without being overbearing and each dish we tried was wonderful from the spring rolls to the cod with pineapple tempura.
    COT: Because the service is positive, the dish is positive, the spring rolls is positive, the cod with pineapple tempura is positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: Probably much busier for lunch, it's seldom crowded for dinner (too close to downtown).
    COT: Because the lunch is neutral, the dinner is neutral, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """
]

PROMPT_explicit_COT_V2 = [
    """
    Review: we were seated at the sushi bar in front of yasuda.
    COT: The sentiment polarity of (sushi bar) goes through (neutral) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: While the smoothies are a little big for me, the fresh juices are the best I have ever had!
    COT: The sentiment polarity of (smoothies, fresh juices) goes through (negative, positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: I ate here a week ago and found most dishes average at best and too expensive.
    COT: The sentiment polarity of (dishes) goes through (negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: This little place is wonderfully warm welcoming.
    COT: The sentiment polarity of (place) goes through (positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: I've had pizza both times and the caprese salad appetizer.
    COT: The sentiment polarity of (pizza, caprese salad appetizer) goes through (neutral, neutral) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: Given the incredible architecture surrounding it, this place has no character.
    COT: The sentiment polarity of (architecture, place) goes through (positive, negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: Great roofdeck, nice group of 30 somethings, but no music, kind of quiet.
    COT: The sentiment polarity of (roofdeck, music) goes through (positive, negative) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: However, if you want great food at a great price and don't mind the decor, you can't beat this place.
    COT: The sentiment polarity of (food, price, decor) goes through (positive, positive, negative) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: It's a shame that a nice, convenient place like the Pink Pony can be so ruined by lousy service.
    COT: The sentiment polarity of (place, service) goes through (positive, negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: The menu is limited but almost all of the dishes are excellent.
    COT: The sentiment polarity of (menu, dishes) goes through (negative, positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: The cafe itself was really nice with comfortable outdoor chairs and tables, but the service could have been better.
    COT: The sentiment polarity of (cafe, outdoor chairs, tables, service) goes through (positive, positive, positive, negative) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: While we enjoyed the food, we were highly disappointed by the poor service (waiter was not quite competent and SLOW service) and lack of remorse.
    COT: The sentiment polarity of (food, service, waiter, service) goes through (positive, negative, negative, negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: The service was mediocre, and the lack of air conditioning made for a less than comfortable meal.
    COT: The sentiment polarity of (service, air conditioning, meal) goes through (neutral, negative, negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: The prices are about $9 for an entree for dinner and even less for lunch.
    COT: The sentiment polarity of (prices, entree, dinner) goes through (positive, positive, neutral) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: You don't go to Mizu for excellent service, you go for the large amounts of food, the amiable atmosphere, and the hole-in-the-wall feeling of the place.
    COT: The sentiment polarity of (service, food, atmosphere) goes through (negative, positive, positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: The food itself was just ok - nothing spectacular - but the service was awful.
    COT: The sentiment polarity of (food, service) goes through (neutral, negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: The service was attentive without being overbearing and each dish we tried was wonderful from the spring rolls to the cod with pineapple tempura.
    COT: The sentiment polarity of (service, dish, spring rolls, cod with pineapple tempura) goes through (positive, positive, positive, positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: Probably much busier for lunch, it's seldom crowded for dinner (too close to downtown).
    COT: The sentiment polarity of (lunch, dinner) goes through (neutral, neutral) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """
]

PROMPT_explicit_COT_V3 = [
    """
    Review: we were seated at the sushi bar in front of yasuda.
    COT: neutral -> neutral
    Sentiment: neutral
    """,
    """
    Review: While the smoothies are a little big for me, the fresh juices are the best I have ever had!
    COT: negative -> positive -> positive.
    Sentiment: positive
    """,
    """
    Review: I ate here a week ago and found most dishes average at best and too expensive.
    COT: negative -> negative
    Sentiment: negative
    """,
    """
    Review: This little place is wonderfully warm welcoming.
    COT: positive -> positive
    Sentiment: positive
    """,
    """
    Review: I've had pizza both times and the caprese salad appetizer.
    COT: neutral -> neutral -> neutral
    Sentiment: neutral
    """,
    """
    Review: Given the incredible architecture surrounding it, this place has no character.
    COT: positive -> negative -> negative
    Sentiment: negative
    """,
    """
    Review: Great roofdeck, nice group of 30 somethings, but no music, kind of quiet.
    COT: positive -> negative -> neutral
    Sentiment: neutral
    """,
    """
    Review: However, if you want great food at a great price and don't mind the decor, you can't beat this place.
    COT: positive -> positive -> negative -> positive
    Sentiment: positive
    """,
    """
    Review: It's a shame that a nice, convenient place like the Pink Pony can be so ruined by lousy service.
    COT: positive -> negative -> negative
    Sentiment: negative
    """,
    """
    Review: The menu is limited but almost all of the dishes are excellent.
    COT: negative -> positive -> positive
    Sentiment: positive
    """,
    """
    Review: The cafe itself was really nice with comfortable outdoor chairs and tables, but the service could have been better.
    COT: positive -> positive -> positive -> negative -> neutral
    Sentiment: neutral
    """,
    """
    Review: While we enjoyed the food, we were highly disappointed by the poor service (waiter was not quite competent and SLOW service) and lack of remorse.
    COT: positive -> negative -> negative -> negative -> negative
    Sentiment: negative
    """,
    """
    Review: The service was mediocre, and the lack of air conditioning made for a less than comfortable meal.
    COT: neutral -> negative -> negative -> negative
    Sentiment: negative
    """,
    """
    Review: The prices are about $9 for an entree for dinner and even less for lunch.
    COT: positive -> positive -> neutral -> neutral
    Sentiment: neutral
    """,
    """
    Review: You don't go to Mizu for excellent service, you go for the large amounts of food, the amiable atmosphere, and the hole-in-the-wall feeling of the place.
    COT: negative -> positive -> positive -> positive
    Sentiment: positive
    """,
    """
    Review: The food itself was just ok - nothing spectacular - but the service was awful.
    COT: neutral -> negative -> negative
    Sentiment: negative
    """,
    """
    Review: The service was attentive without being overbearing and each dish we tried was wonderful from the spring rolls to the cod with pineapple tempura.
    COT: positive -> positive -> positive -> positive -> positive
    Sentiment: positive
    """,
    """
    Review: Probably much busier for lunch, it's seldom crowded for dinner (too close to downtown).
    COT: neutral -> neutral -> neutral
    Sentiment: neutral
    """
]
