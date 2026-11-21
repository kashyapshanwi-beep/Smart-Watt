# ==========================================
#              SMARTWATT
#       SMART ELECTRICITY BILLING SYSTEM
# ==========================================

FIXED_CHARGE = 50
TAX_RATE = 0.05


def calculate_energy_charge(units):

    if units <= 100:
        first = units * 3
        second = 0
        third = 0

    elif units <= 200:
        first = 100 * 3
        second = (units - 100) * 5
        third = 0

    else:
        first = 100 * 3
        second = 100 * 5
        third = (units - 200) * 8

    energy = first + second + third

    return first, second, third, energy


def generate_bill(name, units):

    first, second, third, energy = calculate_energy_charge(units)

    fixed = FIXED_CHARGE
    tax = (energy + fixed) * TAX_RATE
    total = energy + fixed + tax

    print("\n" + "=" * 45)
    print("              SMARTWATT")
    print("        ELECTRICITY BILL RECEIPT")
    print("=" * 45)

    print("Consumer Name :", name)
    print("Units Consumed:", units, "kWh")

    print("-" * 45)
    print("             CHARGE DETAILS")
    print("-" * 45)

    print("First 100 Units :", f"Rs. {first:.2f}")
    print("Next 100 Units  :", f"Rs. {second:.2f}")
    print("Above 200 Units :", f"Rs. {third:.2f}")

    print("-" * 45)

    print("Energy Charge :", f"Rs. {energy:.2f}")
    print("Fixed Charge  :", f"Rs. {fixed:.2f}")
    print("Tax (5%)      :", f"Rs. {tax:.2f}")

    print("-" * 45)

    print("TOTAL BILL    :", f"Rs. {total:.2f}")

    print("=" * 45)

    # Smart Usage Analysis

    print("\n          SMART USAGE ANALYSIS")
    print("-" * 45)

    if units <= 100:
        print("Usage Category: LOW")
        print("Excellent! Keep saving electricity.")

    elif units <= 200:
        print("Usage Category: MODERATE")
        print("Tip: Switch off unused appliances.")

    else:
        print("Usage Category: HIGH")
        print("Tip: Reduce unnecessary electricity usage.")

    print("-" * 45)
    print("       THANK YOU FOR USING SMARTWATT!")
    print("=" * 45)

print("=" * 45)
print("         WELCOME TO SMARTWATT")
print("      SMART ELECTRICITY SYSTEM")
print("=" * 45)

name = input("Enter Consumer Name: ")

try:

    units = float(input("Enter Units Consumed: "))

    if units < 0:
        print("Invalid units. Enter a non-negative number.")

    else:
        generate_bill(name, units)

except ValueError:
    print("Invalid units. Enter a non-negative number.")