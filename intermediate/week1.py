# caian 05/01/2016

class Hour(object):
    """
    Simple hour object.
    """
    def __init__(self, hour, minutes, seconds):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    def moment(self):
        """
        Return a string of the moment.
        """
        return str(self.hour) + ":" + str(self.minutes) + ":" + str(self.seconds)

class Event():
    """
    Simple event object.
    """
    def __init__(self, name, hour, description=None):
        self.name = name
        self.hour = hour
        self.description = "No description."
        if description != None:
            self.description = description

    @property
    def show(self):
       return self.hour.moment() + "   " + self.name + "\n" + self.description + "\n"
        
class Scheduler(object):
    """
    Simple scheduler.
    """
    def __init__(self):
        self.events = {}
        self.count = 0

    def schedule(self, name, hour, description=None):
        """
        Schedule some event.
        """
        event = Event(name, hour, description)
        self.count += 1
        self.events[self.count] = event
        print("Event: " + str(self.count) + "  " + str(event.show))
        return

    def cancel(self, name):
        """
        Cancel a schedule event.
        """
        for each in list(self.events.keys()):
            if self.events[each].name == name:
                del self.events[each]
        return

    def show_events(self):
        """
        Show the schedule events
        """
        r = "Events:\n"
        for each in list(self.events.keys()):
            r += str(each) + "   " + self.events[each].show + "\n"
        return r

def menu():
    op = -1
    while(op < 0 or op > 4):
        print("What do you wanna do?")
        print("  0 - exit")
        print("  1 - show scheduled events")
        print("  2 - create a new event")
        print("  3 - cancel a event")
        print("  4 - ...(future features?)")
        op = int(input("> "))
    return op

def create_event():
    n = input("What's the name of event?\n> ")
    h = input("What's the hour of event?(hour, minute, second)\n> ")
    m = input("> ")
    s = input("> ")
    des = input("What's the description of event?\n> ")

    hr = Hour(h, m, s)
    sch_ev = Event(n, hr, des)
    return sch_ev

"""
Program starts here.
"""
print("This is a simple Scheduler - version 0.1")
option = -1
sch = Scheduler()
while(option != 0):
    option = menu()
    if option == 1:
        ev = sch.show_events()
        print(ev)
    elif option == 2:
        ne = create_event()
        sch.schedule(ne.name, ne.hour, ne.description)
    elif option == 3:
        name = input("What's the event name:\n> ")
        sch.cancel(name)
        
print("bye!")
