import decimal
import heapq

def find_path(details):
    print_bill = []
    
    # Convert details into a list of tuples for heap processing
    heap = []
    for person, amount in details.items():
        heapq.heappush(heap, (amount, person))  # Min-heap, will extract the min value first

    while len(heap) > 1:
        # Get the person who owes money (min_value)
        min_value, min_key = heapq.heappop(heap)
        
        # Get the person who should receive money (max_value) by using nlargest
        max_value, max_key = heapq.nlargest(1, heap)[0]

        # Ensure that max_value and min_value are still valid
        if max_value == 0 or min_value == 0:
            break

        result = max_value + min_value
        result = round(result, 1)

        if result >= 0.0:
            print(f"{min_key} needs to pay {max_key}: {round(abs(min_value), 2)}")
            details[max_key] = result
            details[min_key] = 0.0
        else:
            print(f"{min_key} needs to pay {max_key}: {round(abs(max_value), 2)}")
            details[max_key] = 0.0
            details[min_key] = result

        # Rebuild the heap after updating values
        heap = []
        for person, amount in details.items():
            if amount != 0:
                heapq.heappush(heap, (amount, person))

def get_key_from_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

def round(value, places):
    if places < 0:
        raise ValueError("Places must be non-negative")

    bd = decimal.Decimal(value)
    bd = bd.quantize(decimal.Decimal('1e-{0}'.format(places)), rounding=decimal.ROUND_HALF_UP)
    return float(bd)

def get_user_input():
    details = {}
    total_spent = 0.0
    while True:
        person = input("Enter the person's name (or type 'done' to finish): ")
        if person.lower() == 'done':
            break
        try:
            amount = float(input(f"Enter the amount for {person} (the amount they spent): "))
            details[person] = amount
            total_spent += amount
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    
    return details, total_spent

def calculate_individual_share(total_spent, num_people):
    return total_spent / num_people

def sort_details(details):
    # Sort the details dictionary by value in descending order (highest spenders first)
    sorted_details = sorted(details.items(), key=lambda x: x[1], reverse=True)
    return sorted_details

# Get input from the user
details, total_spent = get_user_input()

# Calculate the individual share
num_people = len(details)
individual_share = calculate_individual_share(total_spent, num_people)

# Adjust the amounts so that each person is either positive (they need to get money) or negative (they need to pay)
for person in details:
    details[person] -= individual_share

# Sorting the details before processing
sorted_details = sort_details(details)
print("Sorted details by amount spent:")
for person, amount in sorted_details:
    print(f"{person}: {round(amount, 2)}")

# Call the function to process the input
find_path(details)
