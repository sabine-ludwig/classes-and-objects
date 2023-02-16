'''
What is a Class?
A class is a template for an object. It defines what the object is made up of (instance variables)
and what actions the object can perform (methods).
What is an Object?
An object is an instance of a class. Each instance of a class (object) contains the same class 
properties and methods. This means each instance of a class (object) has the same makeup. What 
differs between the objects is what values are set equal to the member variables. 

You create an object from a class by
Declaring a variable that will hold the object
Setting the variable equal to the name of the class with a set of parenthesis directly after.

'''

# from alarm_clock import AlarmClock

# my_alarm = AlarmClock("1:30", True, "6:30")
# my_alarm.set_time("1:45")
# my_alarm.turn_on_off()
# my_alarm.set_alarm("6:45")
# my_alarm.turn_on_off()

from person import Person

person_one = Person("Sabine", 100)
person_two = Person("Koll", 100)

person_two.send_transfer(100)
person_one.receive_transfer("Koll", 100)




