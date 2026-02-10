def main():
    #inputs for credit score and income
    credit_score = int(input("What is your credit score? "))
    income = float(input("What is your annual income? "))

    #Conditional statements to determine loan risk category
    if credit_score >= 720 and income >= 60000:
        risk = "low"
    elif credit_score >= 650 and income >= 40000:
        risk = "medium"
    else:
        risk = "high"
    
    print(f"Loan Risk Category: {risk}")

main()