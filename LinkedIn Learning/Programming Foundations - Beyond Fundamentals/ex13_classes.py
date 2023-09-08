# Object oriented programming. The division into smaller parts makes it easier to maintain and reuse.

# Class is the blueprint, it describes the parameters (arguments) and methods.

flips = [ # this is a list, it inherits the methods belonging to its class.
    'heads',
    'tails',
    'tails',
    'heads',
    'tails'
]

print(flips.count('heads'))
print(flips.pop()) # returns the last item of the list (array).

# How to make a class?

class Attendee:
    'Common base class for all attendees.'

    def __init__(self,name,tickets)
        self.name = name
        self.tickets = tickets

    def displayAttendee(self):
        print('Name: {}, Tickets: {}'.format(self.name, self.tickets))

    def addTicket(self):
        self.tickets += 1
        print('{} tickets increased to {}'.format(self.name, self.tickets))

attendee1 = Attendee('B. Giles', 2)
attendee2 = Attendee('Roman Carlos',1)

attendee2.addTicket()

attendee1.displayAttendee() # this method displays the information with tags
attendee2.displayAttendee()