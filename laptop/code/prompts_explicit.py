# sentiment是最终情感
PROMPT_standard_explicit = [
    """
    Review: I propose that they can just swap the hard drives.
    Sentiment: neutral
    """,
    """
    Review: Great laptop for school, easy to use for beginners in the household.
    Sentiment: positive
    """,
    """
    Review: I dislike the quality and the placement of the speakers.
    Sentiment: negative
    """,
    """
    Review: It has just enough RAM to run smoothly and enough memory to satisfy my needs.
    Sentiment: positive
    """,
    """
    Review: Strengths:Well-shaped Weaknesses:A bad videocard!
    Sentiment: neutral
    """,
    """
    Review: Looks nice, but has a horribly cheap feel.
    Sentiment: negative
    """,
    """
    Review: We paid for the three year warranty and the extended warranty after that one ended as well.
    Sentiment: neutral
    """,
    """
    Review: Battery life could be better but overall for the price and Toshiba's reputation for laptops it's great!
    Sentiment: positive
    """,
    """
    Review: Anyway, in early July of this year, the DVD burner stopped working, and the computer stared having issues with power supply.
    Sentiment: negative
    """,
    """
    Review: I connect a LaCie 2Big external drive via the firewire 800 interface, which is useful for Time Machine.
    Sentiment: positive
    """,
    """
    Review: air has higher resolution but the fonts are small.
    Sentiment: neutral
    """,
    """
    Review: while the keyboard itself is alright, the plate around it is cheap plastic and makes a hollow sound when using the mouse command buttons.
    Sentiment: negative
    """,
    """
    Review: Returned laptop for repair a 2nd time and it came back with obvious physical damage (keyboard bulging and speaker grill pressed in), buttons not working and USB ports inoperative.
    Sentiment: negative
    """,
    """
    Review: This newer netbook has no hard drive or network lights.
    Sentiment: neutral
    """,
    """
    Review: I upgraded the memory and replaced the base Windows 7 Starter to Win 7 Home, and it runs just fine.
    Sentiment: positive
    """,
    """
    Review: Overall I feel this netbook was poor quality, had poor performance, although it did have great battery life when it did work.
    Sentiment: negative
    """,
    """
    Review: It is easy to use, its keyboard easily accommodates large hands, and its weight is fantasic.
    Sentiment: positive
    """,
    """
    Review: There are eighteen seats in one room.
    Sentiment: neutral
    """
]

PROMPT_explicit_COT_V1 = [
    """
    Review: I propose that they can just swap the hard drives.
    COT: Because the hard drives is neutral, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: Great laptop for school, easy to use for beginners in the household.
    COT: Because the use is positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: I dislike the quality and the placement of the speakers.
    COT: Because the speakers is negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: It has just enough RAM to run smoothly and enough memory to satisfy my needs.
    COT: Because the RAM is positive, the memory is positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: Strengths:Well-shaped Weaknesses:A bad videocard!
    COT: Because the shaped is positive, the videocard is negative, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: Looks nice, but has a horribly cheap feel.
    COT: Because the feel is negative, the Looks is positive, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: We paid for the three year warranty and the extended warranty after that one ended as well.
    COT: Because the three year warranty is neutral, the extended warranty is neutral, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: Battery life could be better but overall for the price and Toshiba's reputation for laptops it's great!
    COT: Because the Battery life is negative, the price is positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: Anyway, in early July of this year, the DVD burner stopped working, and the computer stared having issues with power supply.
    COT: Because the DVD burner is negative, the power supply is negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: I connect a LaCie 2Big external drive via the firewire 800 interface, which is useful for Time Machine.
    COT: Because the LaCie 2Big external drive is neutral, the firewire 800 interface is positive, the Time Machine is neutral, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: air has higher resolution but the fonts are small.
    COT: Because the resolution is positive, the fonts is negative, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: while the keyboard itself is alright, the plate around it is cheap plastic and makes a hollow sound when using the mouse command buttons.
    COT: Because the keyboard is positive, the plate is negative, the mouse command buttons is negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: Returned laptop for repair a 2nd time and it came back with obvious physical damage (keyboard bulging and speaker grill pressed in), buttons not working and USB ports inoperative.
    COT: Because the keyboard is negative, the speaker grill is negative, the buttons are negative, the USB ports are negative, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: This newer netbook has no hard drive or network lights.
    COT: Because the hard drive is neutral, the network lights is neutral, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: I upgraded the memory and replaced the base Windows 7 Starter to Win 7 Home, and it runs just fine.
    COT: Because the memory is neutral, the Windows 7 Starter is neutral, the Win 7 Home is neutral, and the runs is positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: Overall I feel this netbook was poor quality, had poor performance, although it did have great battery life when it did work.
    COT: Because the quality is negative, the performance is negative, the battery life is positive, therefore the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: It is easy to use, its keyboard easily accommodates large hands, and its weight is fantasic.
    COT: Because the keyboard is positive, the weight is positive, the use is positive, therefore the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: There are eighteen seats in one room.
    COT: Because the seats is neutral, therefore the overall sentiment is neutral.
    Sentiment: neutral
    """
]

PROMPT_explicit_COT_V2 = [
    """
    Review: I propose that they can just swap the hard drives.
    COT: The sentiment polarity of (hard drives) goes through (neutral) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: Great laptop for school, easy to use for beginners in the household.
    COT: The sentiment polarity of (use) goes through (positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: I dislike the quality and the placement of the speakers.
    COT: The sentiment polarity of (speakers) goes through (negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: It has just enough RAM to run smoothly and enough memory to satisfy my needs.
    COT: The sentiment polarity of (RAM, memory) goes through (positive, positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: Strengths:Well-shaped Weaknesses:A bad videocard!
    COT: The sentiment polarity of (shaped, videocard) goes through (positive, negative) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: Looks nice, but has a horribly cheap feel.
    COT: The sentiment polarity of (feel, Looks) goes through (negative, positive) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: We paid for the three year warranty and the extended warranty after that one ended as well.
    COT: The sentiment polarity of (three year warranty, extended warranty) goes through (neutral, neutral) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: Battery life could be better but overall for the price and Toshiba's reputation for laptops it's great!
    COT: The sentiment polarity of (Battery life, price) goes through (negative, positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: Anyway, in early July of this year, the DVD burner stopped working, and the computer stared having issues with power supply.
    COT: The sentiment polarity of (DVD burner, power supply) goes through (negative, negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: I connect a LaCie 2Big external drive via the firewire 800 interface, which is useful for Time Machine.
    COT: The sentiment polarity of (LaCie 2Big external drive, firewire 800 interface, Time Machine) goes through (neutral, positive, neutral) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: air has higher resolution but the fonts are small.
    COT: The sentiment polarity of (resolution, fonts) goes through (positive, negative) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: while the keyboard itself is alright, the plate around it is cheap plastic and makes a hollow sound when using the mouse command buttons.
    COT: The sentiment polarity of (keyboard, plate, mouse command buttons) goes through (positive, negative, negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: Returned laptop for repair a 2nd time and it came back with obvious physical damage (keyboard bulging and speaker grill pressed in), buttons not working and USB ports inoperative.
    COT: The sentiment polarity of (keyboard, speaker grill, buttons, USB ports) goes through (negative, negative, negative, negative) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: This newer netbook has no hard drive or network lights.
    COT: The sentiment polarity of (hard drive, network lights) goes through (neutral, neutral) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: I upgraded the memory and replaced the base Windows 7 Starter to Win 7 Home, and it runs just fine.
    COT: The sentiment polarity of (memory, Windows 7 Starter, Win 7 Home, runs) goes through (neutral, neutral, neutral, positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: Overall I feel this netbook was poor quality, had poor performance, although it did have great battery life when it did work.
    COT: The sentiment polarity of (quality, performance, battery life) goes through (negative, negative, positive) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: It is easy to use, its keyboard easily accommodates large hands, and its weight is fantasic.
    COT: The sentiment polarity of (keyboard, weight, use) goes through (positive, positive, positive) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """
    Review: There are eighteen seats in one room.
    COT: The sentiment polarity of (seats) goes through (neutral) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """
]

PROMPT_explicit_COT_V3 = [
    """
    Review: I propose that they can just swap the hard drives.
    COT: neutral -> neutral
    Sentiment: neutral
    """,
    """
    Review: Great laptop for school, easy to use for beginners in the household.
    COT: positive -> positive
    Sentiment: positive
    """,
    """
    Review: I dislike the quality and the placement of the speakers.
    COT: negative -> negative
    Sentiment: negative
    """,
    """
    Review: It has just enough RAM to run smoothly and enough memory to satisfy my needs.
    COT: positive -> positive -> positive
    Sentiment: positive
    """,
    """
    Review: Strengths:Well-shaped Weaknesses:A bad videocard!
    COT: positive -> negative -> neutral
    Sentiment: neutral
    """,
    """
    Review: Looks nice, but has a horribly cheap feel.
    COT: negative -> positive -> negative
    Sentiment: negative
    """,
    """
    Review: We paid for the three year warranty and the extended warranty after that one ended as well.
    COT: neutral -> neutral -> neutral
    Sentiment: neutral
    """,
    """
    Review: Battery life could be better but overall for the price and Toshiba's reputation for laptops it's great!
    COT: negative -> positive -> positive
    Sentiment: positive
    """,
    """
    Review: Anyway, in early July of this year, the DVD burner stopped working, and the computer stared having issues with power supply.
    COT: negative -> negative -> negative
    Sentiment: negative
    """,
    """
    Review: I connect a LaCie 2Big external drive via the firewire 800 interface, which is useful for Time Machine.
    COT: neutral -> positive -> neutral -> positive
    Sentiment: positive
    """,
    """
    Review: air has higher resolution but the fonts are small.
    COT: positive -> negative -> neutral
    Sentiment: neutral
    """,
    """
    Review: while the keyboard itself is alright, the plate around it is cheap plastic and makes a hollow sound when using the mouse command buttons.
    COT: positive -> negative -> negative -> negative
    Sentiment: negative
    """,
    """
    Review: Returned laptop for repair a 2nd time and it came back with obvious physical damage (keyboard bulging and speaker grill pressed in), buttons not working and USB ports inoperative.
    COT: negative -> negative -> negative -> negative -> negative
    Sentiment: negative
    """,
    """
    Review: This newer netbook has no hard drive or network lights.
    COT: neutral -> neutral -> neutral
    Sentiment: neutral
    """,
    """
    Review: I upgraded the memory and replaced the base Windows 7 Starter to Win 7 Home, and it runs just fine.
    COT: neutral -> neutral -> neutral -> positive -> positive
    Sentiment: positive
    """,
    """
    Review: Overall I feel this netbook was poor quality, had poor performance, although it did have great battery life when it did work.
    COT: negative -> negative -> positive -> negative
    Sentiment: negative
    """,
    """
    Review: It is easy to use, its keyboard easily accommodates large hands, and its weight is fantasic.
    COT: positive -> positive -> positive -> positive
    Sentiment: positive
    """,
    """
    Review: There are eighteen seats in one room.
    COT: neutral -> neutral
    Sentiment: neutral
    """
]
