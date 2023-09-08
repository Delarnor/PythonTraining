# We are going to create a CLASS, in object oriented programming we use them to represent
# real world things and situations. A class is a blueprint of how other objects are created.

class puppy():
    def __init__ (self, name, favourite_toy): 
        self.name = name
        self.favourite_toy = favourite_toy

    def play(self):
        print(self.name + " is playing with the " + self.favourite_toy)

mika = puppy("Mika","bone")
mika.play()

onyx = puppy("Onyx","rubber gnome")
onyx.play()