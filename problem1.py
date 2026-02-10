def calculate_discount():
    # Get user input for purchase amount and membership status
    amount = float(input("Purchase Amount: "))
    is_member = input("Are you a member? (yes/no): ").strip().lower()

    # Conditional statements to determine discount based on membership status and purchase amount
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

    # Calculate final price after applying discount
    discount_decimal = discount * 100
    final_price = amount - (amount * discount)

    # Output the discount percentage and final price
    print(f"Discount: {discount_decimal:.0f}%")
    print(f"Final Price: ${final_price:.2f}")

calculate_discount()
