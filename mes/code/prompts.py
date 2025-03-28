
# sentiment是最终情感
PROMPT_standard_implicit = [
    """
    Review: Why has the price of badminton rackets increased so quickly; my friends who play are already becoming fewer and fewer; I'm afraid it will be hard to find someone to play with in the future.
    Sentiment: negative
    """,
    """
    Review: Near the end of the workday, my boss assigned me an important task; seeing my colleagues leaving one by one, I wanted to leave too; but I was worried I wouldn't finish it by tomorrow.
    Sentiment: negative
    """,
    """
    Review: The weather finally cleared up; but I have to study for my midterm exam in the library; looking at the pile of materials, I can't help but worry about tomorrow's test.
    Sentiment: negative
    """,
    """
    Review: Yesterday, during the exam, the person in front of me reeked of body odor as soon as they sat down; after three hours, I couldn't focus at all; when I left the exam room, I realized I had made some silly mistakes; but I'm glad I probably won't have to interact with that person again.
    Sentiment: negative
    """,
    """
    Review: When Tom first started studying abroad, he was in a foreign land with no one to help him; he made many jokes due to the language barrier; but eventually, through his own efforts, he adapted to the local environment and made many friends.
    Sentiment: positive
    """,
    """
    Review: I looked at the crowd at the subway entrance, wondering if I could squeeze onto the next train; the music in my headphones temporarily calmed me; suddenly, someone tapped me on the back; it turned out they were reminding me that my backpack zipper wasn't closed properly.
    Sentiment: neutral
    """,
    """
    Review: I usually love making crafts; my parents think it's a waste of time; I have to secretly work on them to avoid their disapproval; but every time I see my work praised by people online, I feel motivated again.
    Sentiment: positive
    """,
    """
    Review: Just when I was feeling stuck with work; a cheerful song suddenly inspired me; it's a pity there's no one to share this joy with.
    Sentiment: negative
    """,
    """
    Review: Suddenly, someone called out my childhood nickname in a public place; my face instantly turned red, worried that others would hear; I turned around and saw it was an old friend I hadn't seen in ages.
    Sentiment: neutral
    """,
    """
    Review: Busy with work and life, I hadn't contacted my friends for a long time; today, I suddenly received a call from a good old friend wanting to visit; although my heart raced a bit during the call, once we met, we chatted just as easily as we used to.
    Sentiment: positive
    """,
    """
    Review: Tom won a set of kitchen knives in a points lottery; when he got home and opened the package, he found the blades were dull and a bit rusty; thinking they might be low-quality recycled products with safety hazards, he threw them away.
    Sentiment: neutral
    """,
    """
    Review: Tom accidentally scratched a car parked downstairs and hurried home to hide; but the more he thought about it, the more guilty he felt; so he decided to muster the courage to apologize to the car owner; the owner graciously accepted his apology.
    Sentiment: positive
    """,
    """
    Review: The noisy renovations next door finally stopped; but now the lawn mower from the downstairs property management is buzzing nonstop; I just hope it doesn't wake up my baby, who I just got to sleep.
    Sentiment: neutral
    """,
    """
    Review: Tom and his friends went hiking; as they climbed, the mountain path became increasingly steep; lacking protective gear, they slowed down; but they ultimately reached the summit before sunrise.
    Sentiment: neutral
    """,
    """
    Review: I dreamt of drowning and suddenly woke up in a panic; remembering that it's the weekend and I don't have to work tomorrow, I went back to sleep peacefully; the next morning, my husband told me I was shouting for help all night.
    Sentiment: neutral
    """,
    """
    Review: As a substitute player on the team, Tom rarely gets a chance to show his skills; he can only watch as the main players shine in the games; even though it's a team, he always feels a bit abandoned.
    Sentiment: negative
    """,
    """
    Review: There are quite a few discounted vegetables at the supermarket today; but last time, I bought too much just because it was cheap and couldn't finish it, and my family scolded me; but if I miss this sale, there might not be another chance.
    Sentiment: negative
    """,
    """
    Review: As graduation approaches, I realize I haven't made any close friends; soon, I'll have to face the unknown world outside; seeing my classmates with great plans and directions, I can't help but feel uncertain about my future.
    Sentiment: negative
    """,
]


PROMPT_implicit_COT_V1 = [
    """
    Determine the emontion of each sentence in the review, selecting option from the following: anxiety, shame, loneliness, fear, jealousy, happiness
    
    Review: Why has the price of badminton rackets increased so quickly; my friends who play are already becoming fewer and fewer; I'm afraid it will be hard to find someone to play with in the future.
    COT: The first sentence conveys anxiety, the second sentence conveys loneliness, and the third sentence conveys fear.
    Sentiment: negative
    """,
    """ 
    Review: Near the end of the workday, my boss assigned me an important task; seeing my colleagues leaving one by one, I wanted to leave too; but I was worried I wouldn't finish it by tomorrow.
    COT: The first sentence conveys anxiety, the second sentence conveys jealousy, and the third sentence conveys fear.
    Sentiment: negative
    """,
    """
    Review: The weather finally cleared up; but I have to study for my midterm exam in the library; looking at the pile of materials, I can't help but worry about tomorrow's test.
    COT: The first sentence conveys happiness, the second sentence conveys anxiety, and the third sentence conveys fear.
    Sentiment: negative
    """,
    """ 
    Review: Yesterday, during the exam, the person in front of me reeked of body odor as soon as they sat down; after three hours, I couldn't focus at all; when I left the exam room, I realized I had made some silly mistakes; but I'm glad I probably won't have to interact with that person again.
    COT: The first sentence conveys anxiety, the second sentence conveys anxiety, the third sentence conveys shame, and the fourth sentence conveys happiness.
    Sentiment: negative
    """,
    """ 
    Review: When Tom first started studying abroad, he was in a foreign land with no one to help him; he made many jokes due to the language barrier; but eventually, through his own efforts, he adapted to the local environment and made many friends.
    COT: The first sentence conveys loneliness, the second sentence conveys shame, and the third sentence conveys happiness.
    Sentiment: positive
    """,
    """ 
    Review: I looked at the crowd at the subway entrance, wondering if I could squeeze onto the next train; the music in my headphones temporarily calmed me; suddenly, someone tapped me on the back; it turned out they were reminding me that my backpack zipper wasn't closed properly.
    COT: The first sentence conveys anxiety, the second sentence conveys happiness, the third sentence conveys fear, and the fourth sentence conveys shame.
    Sentiment: neutral
    """,
    """ 
    Review: I usually love making crafts; my parents think it's a waste of time; I have to secretly work on them to avoid their disapproval; but every time I see my work praised by people online, I feel motivated again.
    COT: The first sentence conveys happiness, the second sentence conveys shame, the third sentence conveys fear, and the fourth sentence conveys happiness.
    Sentiment: positive
    """,
    """ 
    Review: Just when I was feeling stuck with work; a cheerful song suddenly inspired me; it's a pity there's no one to share this joy with.
    COT: The first sentence conveys anxiety, the second sentence conveys happiness, and the third sentence conveys loneliness.
    Sentiment: negative
    """,
    """ 
    Review: Suddenly, someone called out my childhood nickname in a public place; my face instantly turned red, worried that others would hear; I turned around and saw it was an old friend I hadn't seen in ages.
    COT: The first sentence conveys shame, the second sentence conveys fear, and the third sentence conveys happiness.
    Sentiment: neutral
    """,
    """ 
    Review: Busy with work and life, I hadn't contacted my friends for a long time; today, I suddenly received a call from a good old friend wanting to visit; although my heart raced a bit during the call, once we met, we chatted just as easily as we used to.
    COT: The first sentence conveys loneliness, the second sentence conveys happiness, the third sentence conveys anxiety, and the fourth sentence conveys happiness.
    Sentiment: positive
    """,
    """ 
    Review: Tom won a set of kitchen knives in a points lottery; when he got home and opened the package, he found the blades were dull and a bit rusty; thinking they might be low-quality recycled products with safety hazards, he threw them away.
    COT: The first sentence conveys happiness, the second sentence conveys anxiety, and the third sentence conveys fear.
    Sentiment: neutral
    """,
    """ 
    Review: Tom accidentally scratched a car parked downstairs and hurried home to hide; but the more he thought about it, the more guilty he felt; so he decided to muster the courage to apologize to the car owner; the owner graciously accepted his apology.
    COT: The first sentence conveys fear, the second sentence conveys shame, the third sentence conveys anxiety, and the fourth sentence conveys happiness.
    Sentiment: positive
    """,
    """ 
    Review: The noisy renovations next door finally stopped; but now the lawn mower from the downstairs property management is buzzing nonstop; I just hope it doesn't wake up my baby, who I just got to sleep.
    COT: The first sentence conveys happiness, the second sentence conveys anxiety, and the third sentence conveys fear.
    Sentiment: neutral
    """,
    """
    Review: Tom and his friends went hiking; as they climbed, the mountain path became increasingly steep; lacking protective gear, they slowed down; but they ultimately reached the summit before sunrise.
    COT: The first sentence conveys happiness, the second sentence conveys anxiety, the third sentence conveys fear, and the fourth sentence conveys happiness.
    Sentiment: neutral
    """,
    """
    Review: I dreamt of drowning and suddenly woke up in a panic; remembering that it's the weekend and I don't have to work tomorrow, I went back to sleep peacefully; the next morning, my husband told me I was shouting for help all night.
    COT: The first sentence conveys fear, the second sentence conveys happiness, and the third sentence conveys shame.
    Sentiment: neutral
    """,
    """
    Review: As a substitute player on the team, Tom rarely gets a chance to show his skills; he can only watch as the main players shine in the games; even though it's a team, he always feels a bit abandoned.
    COT: The first sentence conveys anxiety, the second sentence conveys jealousy, and the third sentence conveys loneliness.
    Sentiment: negative
    """,
    """
    Review: There are quite a few discounted vegetables at the supermarket today; but last time, I bought too much just because it was cheap and couldn't finish it, and my family scolded me; but if I miss this sale, there might not be another chance.
    COT: The first sentence conveys happiness, the second sentence conveys shame, and the third sentence conveys anxiety.
    Sentiment: negative
    """,
    """ 
    Review: As graduation approaches, I realize I haven't made any close friends; soon, I'll have to face the unknown world outside; seeing my classmates with great plans and directions, I can't help but feel uncertain about my future.
    COT: The first sentence conveys loneliness, the second sentence conveys fear, and the third sentence conveys jealousy, the fourth sentence conveys anxiety.
    Sentiment: negative
    """,
]

PROMPT_implicit_COT_V2 = [
    """
    Determine the emotion of each sentence in the review, selecting option from the following: anxiety, shame, loneliness, fear, jealousy, happiness

    Review: Why has the price of badminton rackets increased so quickly; my friends who play are already becoming fewer and fewer; I'm afraid it will be hard to find someone to play with in the future.
    COT: The emotion goes though (anxiety, loneliness, fear) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """ 
    Review: Near the end of the workday, my boss assigned me an important task; seeing my colleagues leaving one by one, I wanted to leave too; but I was worried I wouldn't finish it by tomorrow.
    COT: The emotion goes though (anxiety, jealousy, fear). And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: The weather finally cleared up; but I have to study for my midterm exam in the library; looking at the pile of materials, I can't help but worry about tomorrow's test.
    COT: The emotion goes though (happiness, anxiety, fear) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """ 
    Review: Yesterday, during the exam, the person in front of me reeked of body odor as soon as they sat down; after three hours, I couldn't focus at all; when I left the exam room, I realized I had made some silly mistakes; but I'm glad I probably won't have to interact with that person again.
    COT: The emotion goes though (anxiety, anxiety, shame, happiness) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """ 
    Review: When Tom first started studying abroad, he was in a foreign land with no one to help him; he made many jokes due to the language barrier; but eventually, through his own efforts, he adapted to the local environment and made many friends.
    COT: The emotion goes though (loneliness, shame, happiness) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """ 
    Review: I looked at the crowd at the subway entrance, wondering if I could squeeze onto the next train; the music in my headphones temporarily calmed me; suddenly, someone tapped me on the back; it turned out they were reminding me that my backpack zipper wasn't closed properly.
    COT: The emotion goes though (anxiety, happiness, fear, shame) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """ 
    Review: I usually love making crafts; my parents think it's a waste of time; I have to secretly work on them to avoid their disapproval; but every time I see my work praised by people online, I feel motivated again.
    COT: The emotion goes though (happiness, shame, fear, happiness) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """ 
    Review: Just when I was feeling stuck with work; a cheerful song suddenly inspired me; it's a pity there's no one to share this joy with.
    COT: The emotion goes though (anxiety, happiness, loneliness) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """ 
    Review: Suddenly, someone called out my childhood nickname in a public place; my face instantly turned red, worried that others would hear; I turned around and saw it was an old friend I hadn't seen in ages.
    COT: The emotion goes though (shame, fear, happiness) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """ 
    Review: Busy with work and life, I hadn't contacted my friends for a long time; today, I suddenly received a call from a good old friend wanting to visit; although my heart raced a bit during the call, once we met, we chatted just as easily as we used to.
    COT: The emotion goes though (loneliness, happiness, anxiety, happiness) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """ 
    Review: Tom won a set of kitchen knives in a points lottery; when he got home and opened the package, he found the blades were dull and a bit rusty; thinking they might be low-quality recycled products with safety hazards, he threw them away.
    COT: The emotion goes though (happiness, anxiety, fear) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """ 
    Review: Tom accidentally scratched a car parked downstairs and hurried home to hide; but the more he thought about it, the more guilty he felt; so he decided to muster the courage to apologize to the car owner; the owner graciously accepted his apology.
    COT: The emotion goes though (fear, shame, anxiety, happiness) in sequence. And the overall sentiment is positive.
    Sentiment: positive
    """,
    """ 
    Review: The noisy renovations next door finally stopped; but now the lawn mower from the downstairs property management is buzzing nonstop; I just hope it doesn't wake up my baby, who I just got to sleep.
    COT: The emotion goes though (happiness, anxiety, fear) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: Tom and his friends went hiking; as they climbed, the mountain path became increasingly steep; lacking protective gear, they slowed down; but they ultimately reached the summit before sunrise.
    COT: The emotion goes though (happiness, anxiety, fear, happiness) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: I dreamt of drowning and suddenly woke up in a panic; remembering that it's the weekend and I don't have to work tomorrow, I went back to sleep peacefully; the next morning, my husband told me I was shouting for help all night.
    COT: The emotion goes though (fear, happiness, shame) in sequence. And the overall sentiment is neutral.
    Sentiment: neutral
    """,
    """
    Review: As a substitute player on the team, Tom rarely gets a chance to show his skills; he can only watch as the main players shine in the games; even though it's a team, he always feels a bit abandoned.
    COT: The emotion goes though (anxiety, jealousy, loneliness) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """
    Review: There are quite a few discounted vegetables at the supermarket today; but last time, I bought too much just because it was cheap and couldn't finish it, and my family scolded me; but if I miss this sale, there might not be another chance.
    COT: The emotion goes though (happiness, shame, anxiety) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
    """ 
    Review: As graduation approaches, I realize I haven't made any close friends; soon, I'll have to face the unknown world outside; seeing my classmates with great plans and directions, I can't help but feel uncertain about my future.
    COT: The emotion goes though (loneliness, fear, jealousy, anxiety) in sequence. And the overall sentiment is negative.
    Sentiment: negative
    """,
]

PROMPT_implicit_COT_V3 = [
    """
    Determine the emotion of each sentence in the review, selecting option from the following: anxiety, shame, loneliness, fear, jealousy, happiness

    Review: Why has the price of badminton rackets increased so quickly; my friends who play are already becoming fewer and fewer; I'm afraid it will be hard to find someone to play with in the future.
    COT: anxiety -> loneliness -> fear -> negative.
    Sentiment: negative
    """,
    """ 
    Review: Near the end of the workday, my boss assigned me an important task; seeing my colleagues leaving one by one, I wanted to leave too; but I was worried I wouldn't finish it by tomorrow.
    COT: anxiety -> jealousy -> fear -> negative
    Sentiment: negative
    """,
    """
    Review: The weather finally cleared up; but I have to study for my midterm exam in the library; looking at the pile of materials, I can't help but worry about tomorrow's test.
    COT: happiness -> anxiety -> fear -> negative
    Sentiment: negative
    """,
    """ 
    Review: Yesterday, during the exam, the person in front of me reeked of body odor as soon as they sat down; after three hours, I couldn't focus at all; when I left the exam room, I realized I had made some silly mistakes; but I'm glad I probably won't have to interact with that person again.
    COT: anxiety -> anxiety -> shame -> happiness -> negative
    Sentiment: negative
    """,
    """ 
    Review: When Tom first started studying abroad, he was in a foreign land with no one to help him; he made many jokes due to the language barrier; but eventually, through his own efforts, he adapted to the local environment and made many friends.
    COT: loneliness -> shame -> happiness -> positive
    Sentiment: positive
    """,
    """ 
    Review: I looked at the crowd at the subway entrance, wondering if I could squeeze onto the next train; the music in my headphones temporarily calmed me; suddenly, someone tapped me on the back; it turned out they were reminding me that my backpack zipper wasn't closed properly.
    COT: anxiety -> happiness -> fear -> shame -> neutral
    Sentiment: neutral
    """,
    """ 
    Review: I usually love making crafts; my parents think it's a waste of time; I have to secretly work on them to avoid their disapproval; but every time I see my work praised by people online, I feel motivated again.
    COT: happiness -> shame -> fear -> happiness -> positive
    Sentiment: positive
    """,
    """ 
    Review: Just when I was feeling stuck with work; a cheerful song suddenly inspired me; it's a pity there's no one to share this joy with.
    COT: anxiety -> happiness -> loneliness -> negative
    Sentiment: negative
    """,
    """ 
    Review: Suddenly, someone called out my childhood nickname in a public place; my face instantly turned red, worried that others would hear; I turned around and saw it was an old friend I hadn't seen in ages.
    COT: shame -> fear -> happiness -> neutral
    Sentiment: neutral
    """,
    """ 
    Review: Busy with work and life, I hadn't contacted my friends for a long time; today, I suddenly received a call from a good old friend wanting to visit; although my heart raced a bit during the call, once we met, we chatted just as easily as we used to.
    COT: loneliness -> happiness -> anxiety -> happiness -> positive
    Sentiment: positive
    """,
    """ 
    Review: Tom won a set of kitchen knives in a points lottery; when he got home and opened the package, he found the blades were dull and a bit rusty; thinking they might be low-quality recycled products with safety hazards, he threw them away.
    COT: happiness -> anxiety -> fear -> neutral
    Sentiment: neutral
    """,
    """ 
    Review: Tom accidentally scratched a car parked downstairs and hurried home to hide; but the more he thought about it, the more guilty he felt; so he decided to muster the courage to apologize to the car owner; the owner graciously accepted his apology.
    COT: fear -> shame -> anxiety -> happiness -> positive
    Sentiment: positive
    """,
    """ 
    Review: The noisy renovations next door finally stopped; but now the lawn mower from the downstairs property management is buzzing nonstop; I just hope it doesn't wake up my baby, who I just got to sleep.
    COT: happiness -> anxiety -> fear -> neutral
    Sentiment: neutral
    """,
    """
    Review: Tom and his friends went hiking; as they climbed, the mountain path became increasingly steep; lacking protective gear, they slowed down; but they ultimately reached the summit before sunrise.
    COT: happiness -> anxiety -> fear -> happiness -> neutral
    Sentiment: neutral
    """,
    """
    Review: I dreamt of drowning and suddenly woke up in a panic; remembering that it's the weekend and I don't have to work tomorrow, I went back to sleep peacefully; the next morning, my husband told me I was shouting for help all night.
    COT: fear -> happiness -> shame -> neutral
    Sentiment: neutral
    """,
    """
    Review: As a substitute player on the team, Tom rarely gets a chance to show his skills; he can only watch as the main players shine in the games; even though it's a team, he always feels a bit abandoned.
    COT: anxiety -> jealousy -> loneliness -> negative
    Sentiment: negative
    """,
    """
    Review: There are quite a few discounted vegetables at the supermarket today; but last time, I bought too much just because it was cheap and couldn't finish it, and my family scolded me; but if I miss this sale, there might not be another chance.
    COT: happiness -> shame -> anxiety -> negative
    Sentiment: negative
    """,
    """ 
    Review: As graduation approaches, I realize I haven't made any close friends; soon, I'll have to face the unknown world outside; seeing my classmates with great plans and directions, I can't help but feel uncertain about my future.
    COT: loneliness -> fear -> jealousy -> anxiety -> negative
    Sentiment: negative
    """,
]