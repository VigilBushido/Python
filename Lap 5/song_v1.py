#
#   Sergio Munguia
#
#   song.py
#
#   processing: 1. show the lyrics of the song "Old MacDonald."
#               2. 5 different animals
#               3. display
#
#

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

# def sound():
#    studio = [space, moo, oink, dinsdale, arf, cockadoodle]
#    for i in studio:
#        sound = studio[i+1]
#    return sound
#
#
#    
#
#   sound = ["space", "moo", "oink", "dinsdale", "arf", "cockadoodle"]
#
 #   for i in sound: 
  #      sound = sound[i+1]
        
    
