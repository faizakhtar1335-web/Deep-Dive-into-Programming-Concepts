"""
Week 2 Task: Deep Dive into Programming Concepts
A beginner-friendly demonstration of:
1. Variables
2. Conditional logic
3. Loops
4. Functions
5. Data structures

Run with: python programming_concepts_demo.py
"""

def calculate_discount(total, threshold=500, discount_rate=0.10):
    """Return the total after applying a discount when the threshold is met."""
    if total >= threshold:  # Conditional logic
        return total * (1 - discount_rate)
    return total


def main():
    # 1. Variables: named values that can be used and updated.
    customer_name = input("Enter your name: ").strip() or "Customer"
    budget = 1000

    # 2. Data structure: a list stores several grocery items.
    cart = [
        {"name": "Bread", "price": 40},
        {"name": "Milk", "price": 60},
        {"name": "Rice", "price": 250},
        {"name": "Fruit", "price": 180},
    ]

    print(f"\\nWelcome, {customer_name}!")
    print(f"Your shopping budget is Rs. {budget}.")
    print("\\nItems in your cart:")

    # 3. Loop: repeat the same action for every item in the list.
    total = 0
    for item in cart:
        print(f"- {item['name']}: Rs. {item['price']}")
        total += item["price"]

    print(f"\\nOriginal total: Rs. {total}")

    # 4. Function: reuse the discount calculation.
    final_total = calculate_discount(total)

    # Conditional logic is also used to explain the outcome.
    if total >= 500:
        print("You qualify for a 10% discount.")
    else:
        print("You do not qualify for a discount.")

    print(f"Final total: Rs. {final_total:.2f}")

    # Another conditional decision: check the budget.
    if final_total <= budget:
        print("Result: Your purchase is within budget.")
    else:
        print("Result: Your purchase is over budget.")

    # Example dictionary: key-value data structure.
    contact = {"name": customer_name, "items_in_cart": len(cart)}
    print(f"\\nSummary: {contact['name']} has {contact['items_in_cart']} items in the cart.")


if __name__ == "__main__":
    main()
