# from functools import partial
#
# def hours_per_day(hours):
#     return lambda days: hours * days
#
# result = hours_per_day(8)(20)
# print(result)
#
# def bonus_percentage(percentage):
#     return lambda salary: salary * percentage//100
#
# result = bonus_percentage(10)(3000)
# print(result)
#
#
#
# def net_salary(gross_salary, tax_rate):
#     return gross_salary - (gross_salary * tax_rate)
#
# tax_20 = partial(net_salary, tax_rate=0.20)
# result = tax_20(5000)  # 5000 - (5000 * 0.20) = 4000
# print(result)
#
# def final_salary(base_salary, bonus):
#     return base_salary + bonus
# bonus_500 = partial(final_salary, bonus=500)
# result = bonus_500(3000)  # 3000 + 500 = 3500
# print(result)
#

def calculate_hours(hours_per_day, days):
    return hours_per_day * days

def calculate_gross_salary(hours, hourly_rate):
    return hours * hourly_rate

def composed_salary_function(hours_per_day, days, hourly_rate):
    return calculate_gross_salary(calculate_hours(hours_per_day, days), hourly_rate)


result = composed_salary_function(8, 20, 25)  # (8 * 20) * 25 = 4000
print(result)

def calculate_net_salary(gross_salary):
    return gross_salary - (gross_salary*0.2)

def apply_bonus(salary, bonus):
    return calculate_net_salary(salary) + bonus


def final_salary_composition(gross_salary, bonus):
    return apply_bonus(gross_salary,bonus)


result = final_salary_composition(4000, 300)  # 3500

print(result)