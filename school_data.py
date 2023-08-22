# school_data.py
# Maheen Raza UCID: 30137445, ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and provided csv files.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.

import numpy as np
import matplotlib.pyplot as plt

# The following class is provided and should not be modified.
class School:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, name, code):
        self.name = name 
        self.code = code

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None

        """
        print("School Name: {0}, School Code: {1}".format(self.name, self.code))

 # These three arrays are used to import the data for all of the respective schools
data_2018 = np.genfromtxt('SchoolData_2018-2019.csv', delimiter = ',', skip_header = True)
data_2019 = np.genfromtxt('SchoolData_2019-2020.csv', delimiter = ',', skip_header = True)
data_2020 = np.genfromtxt('SchoolData_2020-2021.csv', delimiter = ',', skip_header = True)

# These two lists are then used for the dictionary, where each school name corresponds to the school code, and vice versa
school_names = ['Centennial High School', 'Robert Thirsk High School', 'Louise Dean School', 'Queen Elizabeth High School', 'Forest Lawn High School', 'Crescent Heights High School', 'Western Canada High School', 'Central Memorial High School', 'James Fowler High School', 'Ernest Manning High School', 'William Aberhart High School', 'National Sport School', 'Henry Wise Wood High School', 'Bowness High School', 'Lord Beaverbrook High School', 'Jack James High School', 'Sir Winston Churchill High School', 'Dr. E. P. Scarlett High School', 'John G Diefenbaker High School', 'Lester B. Pearson High School']
school_codes = ['1224', '1679', '9626', '9806', '9813', '9815', '9816', '9823', '9825', '9826', '9829', '9830', '9836', '9847', '9850', '9856', '9857', '9858', '9860', '9865']

# school_dict1 maps the names to the codes
# school_dict2 maps the codes to the names
school_dict1 = dict(zip(school_names, school_codes))
school_dict2 = dict(zip(school_codes, school_names))

# Add your code within the main function. A docstring is not required for this function.
def main():
        print("ENDG 233 School Enrollment Statistics\n")

        #these all print the respective arrays for all the years from 2018-2021
        print('Array data for 2020-2021')    
        print(data_2020)

        print('Array data for 2019-2020')
        print(data_2019)

        print('Array data for 2018-2019')
        print(data_2018)

        # this while loop will check if what the user inputs is valid or not. If it is valid, then it'll escape the while loop and continue the code, or else it'll ask the user to input something valid
        x = 0
        while x == 0:
            user_input = input('Please enter the high school name or school code: ')
            if user_input in school_dict1.keys():
                break
            elif user_input in school_dict2.keys():
                break
            else: 
                print('You must enter a valid school name or code')


        print("\n***Requested School Statistics***\n")

        # Print school name and code using the given class
        # The if statement checks if the user inputs a school name or a code
        if user_input in school_names:  
            # if user inputs a school name, that will be saved to the variable for the name
            school_name = user_input
             # the code will be taken from the respective dictionary     
            school_code = school_dict1[user_input] 
            # it will then go through the class and assign the value and print out the stats in the respective layout given in the class
            school_input = School(school_name, school_code) 
            school_input.print_all_stats()

            # this variable assigns where the index is at the specific code
            my_index = school_codes.index(school_code)
            # this will add up all the amount of students in grade 10 and calculate the average and will print it out
            grade_10 = ((data_2018[my_index][1]) + (data_2019[my_index][1]) + (data_2020[my_index][1])) // 3
            print(f'Mean enrollment for grade 10:  {grade_10:.0f}')

            # this will add up all the amount of students in grade 11 and calculate the average and will print it out
            grade_11 = ((data_2018[my_index][2]) + (data_2019[my_index][2]) + (data_2020[my_index][2])) // 3
            print(f'Mean enrollment for grade 11:  {grade_11:.0f}')

            # this will add up all the amount of students in grade 12 and calculate the average and will print it out
            grade_12 = ((data_2018[my_index][3]) + (data_2019[my_index][3]) + (data_2020[my_index][3])) // 3
            print(f'Mean enrollment for grade 12:  {grade_12:.0f}')

            # this will calculate the total amount of graduates, assuming that everyone enrolled has graduated in the span of the 3 years
            grad_12 = (data_2018[my_index][3]) + (data_2019[my_index][3]) + (data_2020[my_index][3])
            print(f'Total number of students who graduated in the past 3 years:  {grad_12:.0f}')
            
            # these variables are assigned to the respective points that will be shown in the graph for each grade
            points_2019 = [data_2018[my_index][1], data_2018[my_index][2], data_2018[my_index][3]]
            points_2020= [data_2019[my_index][1], data_2019[my_index][2], data_2019[my_index][3]]
            points_2021 = [data_2020[my_index][1], data_2020[my_index][2], data_2020[my_index][3]]
            print(points_2019)

            # the plt.plots will show the x axis as the grades, and will have the corresponding colours 
            plt.plot([10, 11, 12], points_2021, 'bo', label = '2021 enrollment')
            plt.plot([10, 11, 12], points_2020, 'go', label = '2020 enrollment')
            plt.plot([10, 11, 12], points_2019, 'ro', label = '2019 enrollment')
            #this will show the legend in the upper left corner
            plt.legend(shadow=True, loc="upper left")
            # the x axis will have 10, 11, and 12 for the 'ticks'
            plt.xticks([10, 11, 12])
            # shows the title of the graph on the top
            plt.title('Grade enrollment by year')
            # shows the x axis
            plt.xlabel('Grade level')
            # shows the y label
            plt.ylabel('Number of students')
            # will show the graph in a small window
            plt.show()

            # for the bonus, these variables are assigned in order to graph the data for students in enrolled in each grade
            points_for_bonus10 = [data_2018[my_index][1], data_2019[my_index][1], data_2020[my_index][1]]
            points_for_bonus11 = [data_2018[my_index][2], data_2019[my_index][2], data_2020[my_index][2]]
            points_for_bonus12 = [data_2018[my_index][3], data_2019[my_index][3], data_2020[my_index][3]]

            # this will show three different graphs and the three grades and the relationship for their enrollments
            plt.subplot(3,1,1)
            plt.plot([2019, 2020, 2021], points_for_bonus10, 'y--', label = 'Grade 10')
            plt.ylabel('Number of students')
            plt.xticks([2019, 2020, 2021])
            plt.legend(shadow = True, loc = "upper right")

            plt.subplot(3,1,2)
            plt.plot([2019, 2020, 2021], points_for_bonus11, 'm--', label = 'Grade 11')
            plt.ylabel('Number of students')
            plt.xticks([2019, 2020, 2021])
            plt.legend(shadow = True, loc = "upper right")

            plt.subplot(3,1,3)
            plt.plot([2019, 2020, 2021], points_for_bonus12, 'c--', label = 'Grade 12')
            plt.ylabel('Number of students')
            plt.xticks([2019, 2020, 2021])
            plt.xlabel('Enrollment year')
            plt.legend(shadow = True, loc = "upper right")

            plt.show()
        # the code will go through this statement if the user inputs a code instead of a name
        elif user_input in school_codes:
            # the school name will be the key of the respective dictionary
            given_name = school_dict2[user_input]
            given_code = user_input
            # it will then go through the class and assign the value and print out the stats in the respective layout given in the class
            given_school = School(given_name, given_code)
            given_school.print_all_stats()

            # this variable assigns where the index is at the specific code
            my_index = school_codes.index(user_input)

            # this will add up all the amount of students in grade 10 and calculate the average and will print it out
            grade_10 = ((data_2018[my_index][1]) + (data_2019[my_index][1]) + (data_2020[my_index][1])) // 3
            print(f'Mean enrollment for grade 10:  {grade_10:.0f}')

            # this will add up all the amount of students in grade 11 and calculate the average and will print it out
            grade_11 = ((data_2018[my_index][2]) + (data_2019[my_index][2]) + (data_2020[my_index][2])) // 3
            print(f'Mean enrollment for grade 11:  {grade_11:.0f}')

            # this will add up all the amount of students in grade 12 and calculate the average and will print it out
            grade_12 = ((data_2018[my_index][3]) + (data_2019[my_index][3]) + (data_2020[my_index][3])) // 3
            print(f'Mean enrollment for grade 12:  {grade_12:.0f}')
            
            # this will calculate the total amount of graduates, assuming that everyone enrolled has graduated in the span of the 3 years
            grad_12 = (data_2018[my_index][3]) + (data_2019[my_index][3]) + (data_2020[my_index][3])
            print(f'Total number of students who graduated in the past 3 years:  {grad_12:.0f}')

            # these variables are assigned to the respective points that will be shown in the graph for each grade
            points_2019 = [data_2018[my_index][1], data_2018[my_index][2], data_2018[my_index][3]]
            points_2020= [data_2019[my_index][1], data_2019[my_index][2], data_2019[my_index][3]]
            points_2021 = [data_2020[my_index][1], data_2020[my_index][2], data_2020[my_index][3]]

            # the plt.plots will show the x axis as the grades, and will have the corresponding colours 
            plt.plot([10, 11, 12], points_2021, 'bo', label = '2021 enrollment')
            plt.plot([10, 11, 12], points_2020, 'go', label = '2020 enrollment')
            plt.plot([10, 11, 12], points_2019, 'ro', label = '2019 enrollment')
            #this will show the legend in the upper left corner
            plt.legend(shadow=True, loc="upper left")
            # the x axis will have 10, 11, and 12 for the 'ticks'
            plt.xticks([10, 11, 12])
            # shows title
            plt.title('Grade enrollment by year')
            # shows x label
            plt.xlabel('Grade level')
            # shows y label
            plt.ylabel('Number of students')
            # shows the graph
            plt.show()

            # for the bonus, these variables are assigned in order to graph the data for students in enrolled in each grade
            points_for_bonus10 = [data_2018[my_index][1], data_2019[my_index][1], data_2020[my_index][1]]
            points_for_bonus11 = [data_2018[my_index][2], data_2019[my_index][2], data_2020[my_index][2]]
            points_for_bonus12 = [data_2018[my_index][3], data_2019[my_index][3], data_2020[my_index][3]]

            # this will show three different graphs and the three grades and the relationship for their enrollments
            plt.subplot(3,1,1)
            plt.plot([2019, 2020, 2021], points_for_bonus10, 'y--', label = 'Grade 10')
            plt.ylabel('Number of students')
            plt.xticks([2019, 2020, 2021])
            plt.legend(shadow = True, loc = "upper right")

            plt.subplot(3,1,2)
            plt.plot([2019, 2020, 2021], points_for_bonus11, 'm--', label = 'Grade 11')
            plt.ylabel('Number of students')
            plt.xticks([2019, 2020, 2021])
            plt.legend(shadow = True, loc = "upper right")

            plt.subplot(3,1,3)
            plt.plot([2019, 2020, 2021], points_for_bonus12, 'c--', label = 'Grade 12')
            plt.ylabel('Number of students')
            plt.xticks([2019, 2020, 2021])
            plt.xlabel('Enrollment year')
            plt.legend(shadow = True, loc = "upper right")

            plt.show()


# Do not modify the code below
if __name__ == '__main__':
    main()