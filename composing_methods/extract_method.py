
# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

def print_stat():
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", calc_average(grade_list))
    print('The population standard deviation of grades is: ', round(calc_sd(grade_list), 3))
    print('****** END ******')

    # Calculate the mean and standard deviation of the grades
def calc_average(grade_list):
    summation = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
    for grade in grade_list:
        sum = sum + grade
    average = summation / len(grade_list)
    return average
def calc_sd(garde_list):
    sd = 0 # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))
    return sd


print_stat()
