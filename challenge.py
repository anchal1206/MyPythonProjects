from distutils.command.build_scripts import first_line_re


two_digit_no=input("Enter a two digit no?")
first_digit= two_digit_no[0]
second_digit= two_digit_no[1]
result= int(first_digit)+int(second_digit)
print(result)