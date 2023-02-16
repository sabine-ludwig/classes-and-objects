class AlarmClock:

    def __init__(self, passed_in_bool):
        self.current_time = input("What time is it? > ")
        self.alarm_on_off = passed_in_bool 
        self.alarm_time = input("What time would you like to set your alarm for? > ")

#Method #1: Will change the current time (by giving the current time instance variable a new value) 
# and print that new value to the console.

    def set_time(self, new_time):
        self.current_time = new_time 
        print(f"Current time: {new_time}.")

# Method 2: Will toggle the alarm clock on or off by changing the boolean instance variable between true or false.

    def turn_on_off(self):

        if self.alarm_on_off == True:
            print("Your alarm is now off.")
            self.alarm_on_off = False
            return self.alarm_on_off
        elif self.alarm_on_off == False:
            print("Your alarm is now on.")
            self.alarm_on_off = True
            return self.alarm_on_off

# Method #3: Will set or change the current alarm time by assigning a new 
# value to the alarm time instance variable and printing the new time to the console.

    def set_alarm(self, new_time):
        self.alarm_time = new_time
        print(f"Alarm time is now set to {new_time}.")

my_alarm = AlarmClock(True)
# my_alarm.set_time("1:45")
# my_alarm.turn_on_off()
# my_alarm.set_alarm("6:45")
# my_alarm.turn_on_off()
print(my_alarm.current_time)
print(my_alarm.alarm_time)