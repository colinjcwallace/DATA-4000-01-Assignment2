def calculate_discount():
    amount = float(input("Purchase Amount: "))
    is_member = input("Are you a member? (yes/no): ").strip().lower()

    if is_member == 'yes':
        if amount >= 100: 
            discount = 0.15
        elif amount < 100:
            discount = 0.05
    elif is_member == 'no':
        if amount >= 100:
            discount = 0.10
    else:
        print("No discount applicable.")
        discount = 0 

    discount_decimal = discount * 100
    final_price = amount - (amount * discount)

    print(f"Discount: {discount_decimal:.0f}%")
    print(f"Final Price: ${final_price:.2f}")

calculate_discount()
