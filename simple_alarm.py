import argparse
import datetime
import pytz
import time
from playsound import playsound


def set_alarm(hour, minute):
    # Get the current time
    current_time = datetime.datetime.now(pytz.timezone('UTC'))
    # Set the alarm time
    alarm_time = current_time.replace(hour=hour, minute=minute, second=0, microsecond=0)
    # Check if the alarm time is in the future
    if alarm_time > current_time:
        # Sleep for the amount of time until the alarm should go off
        time.sleep((alarm_time - current_time).total_seconds())
    # Print a message to indicate that the alarm has gone off
    
    while True:
        # Play the alarm sound
        playsound("alarm_sound.mp3")
        # Ask the user if they want to snooze the alarm
        snooze = input("Snooze for 5 minutes? (y/n) ")
        if snooze == 'y':
            # Set the alarm time to 5 minutes in the future
            alarm_time = datetime.datetime.now(pytz.timezone('UTC')) + datetime.timedelta(minutes=5)
            # Sleep for the amount of time until the snoozed alarm should go off
            time.sleep((alarm_time - current_time).total_seconds())
        else:
            break

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser()
    # Add arguments for the alarm time
    parser.add_argument('--hour', type=int, required=True, help='The hour at which the alarm should go off')
    parser.add_argument('--minute', type=int, required=True, help='The minute at which the alarm should go off')
    # Parse the command line arguments
    args = parser.parse_args()
    # Set the alarm using the arguments provided
    set_alarm(args.hour, args.minute)


