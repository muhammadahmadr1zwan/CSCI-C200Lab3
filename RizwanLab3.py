# This lab was made by Muhammad Ahmad Rizwan on 9/10/2023 for the COMPUTING 1 Lab 3 assignment. This lab will is a BMI (body-mass index) calculator, which calculates whether a person is underweight, normal, or overweight based on inputted height and weight values.


def mainheadings(): # defining the main headings of the program which explain what the lab does into a function
  print('    '); # space for formatting reasons
  print('     This is a BMI Calculator, if you are under 18.5, you are underweight.'); # heading number 1 explaining what you are if your BMI is under 18.5
  print('     If you are at 25, you are a perfect weight. If you are above 25, you are overweight.'); # heading number 2 explaining what you are if your BMI is at 25 and above 25
  print('\n'); # line break for formatting purposes
def main(): # defining the main function of the program, which will contain the code for the BMI calculator
  mainheadings(); # calling main headings in order for it to be apart of the main function code
  name = input('Please enter your name:\n'); # input your name (string)
  height_inches = input('Please enter height in inches:\n'); # input your height (integer value)
  weight_pounds= input('Please enter your weight in pounds:\n'); # input your weight (integer value)
  print('    '); # space for formatting reasons
  print(bmi_calculator(name, height_inches, weight_pounds)); # print function to print the three paramaters of the main function
  print('   ');  # space for formatting reasons


def bmi_calculator(name, height_inches, weight_pounds): # function 'bmi_calculator' is defined with three different paramaters
    weight_pounds= int(weight_pounds); # defining weight_pounds as an integer value for the following code
    height_inches= int(height_inches); # defining height_inches as an integer value for the following code
    bmi_threshold_underweight= 18.5; # global variable for bmi threshold underweight
    bmi_threshold_normal=24.9; # global variable for bmi threshold normal

    bmi= float(weight_pounds/(height_inches * height_inches)* 703); # BMI is given the formula to actually solve it
    print(bmi); # print the BMI formula
    if bmi <= bmi_threshold_underweight: # if the BMI is LESS THAN or EQUAL to 18.5, then the person is underweight
        return name + " is underweight"; # return the name of the person + the 'is underweight' string type
    elif (bmi <= bmi_threshold_normal): # else if the BMI is LESS THAN or EQUAL to 24.9, then the person is normal
        return name + " is normal"  # return the name of the person + the 'is normal' string type
    elif bmi > 25: # else if the BMI is GREATER THAN 25, then the person is overweight
        return name + " is overweight"; # return the name of the person + the 'is overweight' string type



main(); # call the main function in order for all the code, including the mainheadings and bmi_calculator functions, to run








