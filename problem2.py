def main():
    annual_salary = float(input("What is your annual salary? "))
    score = int(input("What is your performance score? "))

    if score >= 90:
        bonus = 0.2
    elif score >= 80:
        bonus = 0.1
    elif score >= 70:
        bonus = 0.05
    else:
        bonus = 0

    
    bonus_amount = annual_salary * bonus
    print(f"Your bonus amount is: ${bonus_amount:.2f}")
    print(f"Your performance bonus: {bonus * 100:.0f}%")


main()