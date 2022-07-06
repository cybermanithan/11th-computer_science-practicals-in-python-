print("Gross salary")
basic_salary = float(input("enter the basic salary : "))


def gross(basic):
    if basic_salary < 25000:
        hra = basic_salary*20/100
        da = basic_salary*80/100
        return f"basic salary : {basic} \nhra : {hra} \nda : {da} \n ------------------------- \ngross_salary : {basic+hra+da}"
    elif basic_salary >= 25000 and basic_salary < 400000:
        hra = basic_salary*25/100
        da = basic_salary*90/100
        return f"basic salary : {basic} \nhra : {hra} \nda : {da} \n ------------------------- \ngross_salary : {basic+hra+da}"
    elif basic_salary >= 400000:
        hra = basic_salary*30/100
        da = basic_salary*95/100
        return f"basic salary : {basic} \nhra : {hra} \nda : {da} \n ------------------------- \ngross_salary : {basic+hra+da}"


gross_salary = gross(basic_salary)
print(gross_salary)
