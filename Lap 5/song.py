#
#   Sergio Munguia
#
#   song.py
#
#   processing: 1. def the song
#               2. playsong in main using 5 different animals
#               3. display song
#
#   output: displays song lyrics for Old MacDonal using 5 animals

def main():
    playsong("cow", "moo")
    print()
    playsong("pig", "oink")
    print()
    playsong("hedgehog", "dinsdale")
    print()
    playsong("dog", "arf")
    print()
    playsong("chicken", "cockadoodle")
    print()
        
def playsong(animal, sound):

        print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
        print("And on that farm he had a",animal + ", Ee-igh, Ee-igh, Oh!")
        print("With a",sound + ",",sound,"here and a",sound + ",",sound, "there.")
        print("Here a",sound + ", there a",sound,"everywhere a",sound,sound)
        print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")

main()
    
