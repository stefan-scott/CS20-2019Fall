import random
#formatted string demo

nouns = ["cat", "aardvark", "emu", "tricerotops"]
adjective = "lonesome"
color = "chartreuse"
sound_past_tense = "growled"

my_string = f"The {adjective} {nouns[random.randint(0,3)]} sat outside"
print(my_string)

my_string_two = f"""The {adjective}
{nouns[2]}
{sound_past_tense} at the
{color} chesterfield. """
print(my_string_two)

