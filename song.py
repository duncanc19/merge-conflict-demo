def sing_song():
    animals = ["fly", "spider", "bird", "cat", "dog", "cow", "horse"]
    first_line = "There was an old lady who swallowed a"
    last_line = f"I don't know why she swallowed a {animals[0]} - perhaps she'll die!"
    song = f"""{first_line} {animals[0]}.
        {last_line}

        {first_line} {animals[1]};
        That wriggled and wiggled and tickled inside her.
        {_reason_for_swallowing_the_animal(1, animals)};
        {last_line}

        {first_line} {animals[2]};
        How absurd to swallow a {animals[2]}.
        {_reason_for_swallowing_the_animal(2, animals)};
        {last_line}

        {first_line} {animals[3]};
        Fancy that to swallow a {animals[3]}!
        {_reason_for_swallowing_the_animal(3, animals)};
        {last_line}

        {first_line} {animals[4]};
        What a hog, to swallow a {animals[4]}!
        {_reason_for_swallowing_the_animal(4, animals)};
        {last_line}

        {first_line} {animals[5]};
        I don't know how she swallowed a {animals[5]}!
        {_reason_for_swallowing_the_animal(5, animals)};
        {last_line}

        {first_line} {animals[6]}...
        ...She's dead, of course!"""
    return song

def _reasoning_for_swallowing_an_animal(index, animals):
    return f"She swallowed the {animals[index]} to catch the {animals[index-1]}"

def _reason_for_swallowing_the_animal(animal_number, animals):
    reasons = ""
    for index in range(animal_number,1,-1):
        reasons += _reasoning_for_swallowing_an_animal(index, animals)+",\n        "
        
    reasons += _reasoning_for_swallowing_an_animal(1, animals)  
    return reasons