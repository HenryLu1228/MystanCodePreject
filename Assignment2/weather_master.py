"""
File: weather_master.py
Name:呂沅翰
-----------------------
This program implements a console-based application that
asks the user to enter weather data and computes summary
statistics based on the inputs.

The program calculates the average, highest, and lowest
temperatures, as well as the number of cold days. The
output format should match the sample run shown in the
Assignment 2 handout.
"""


# This constant controls when to stop
EXIT = -100


def main():
    """
    When the user enters some temperatures, this file can
    find the maximum, minimum temperature, calculate the
    average temperature, and show how many day(s)'s
    temperature is lower than 16 degree
    """
    print('stanCode "Weather Master 4.0"!')
    tem = int(input('Next temperature: (or ' + str(EXIT) + ' to quit) '))
    if tem == EXIT:
        print('No temperatures were entered.')
    else:
        maximum = tem
        minimum = tem
        mean = tem
        # "cold" is used to calculate how many days the temperatures are lower than 16 degrees
        cold = 0
        # "num" is used to calculate how many temperatures the user enters
        num = 1
        while True:
            if tem < 16:
                cold = cold + 1
            tem = int(input('Next temperature: (or ' + str(EXIT) + ' to quit) '))
            if tem == EXIT:
                break
            mean = mean + tem
            num = num + 1
            if tem > maximum:
                maximum = tem
            if tem < minimum:
                minimum = tem
        average = mean / num
        print('Highest temperature = ' + str(maximum))
        print('Lowest temperature = ' + str(minimum))
        print('Average = ' + str(average))
        print(str(cold) + ' cold day(s)')



# DO NOT EDIT CODE BELOW THIS LINE #



if __name__ == "__main__":
	main()
