#if you live for 90 years and now youre age is 12 how many days and years and month youre left with
age=input("what is youre current age?")
age_as_int= int(age)
remaning_lives=50-age_as_int
no_days=remaning_lives*365
no_weeks=remaning_lives*52
no_months=remaning_lives*12
print(f"number of day {no_days}, weeks {no_weeks}, months  {no_months}")