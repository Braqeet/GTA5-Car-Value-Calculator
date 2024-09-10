def calculate_full_value():
    base_value = float(input("Enter the purchase price: "))  # Input the price you paid for the car
    sell_value = float(input("Enter the sell price: "))  # Input the price you see when you try to sell

    base_resale_value = 0.60 * base_value  # 60% of the original base price
    upgrade_resale_value = sell_value - base_resale_value  # Remaining part is from the upgrades
    full_upgrade_value = upgrade_resale_value / 0.50  # Reverse the 50% deduction to find the full upgrade value

    full_value = base_value + full_upgrade_value  # The full price is the sum of the base price and the full value of the upgrades

    print(f"The full price of the car, including upgrades, is: ${full_value:,.2f}")

calculate_full_value()
