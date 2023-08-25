
flight_table = [
    {"P_ID": "P1", "Process": "VSCode", "Start Time (ms)": 100, "Priority": "MID"},
    {"P_ID": "P23", "Process": "Eclipse", "Start Time (ms)": 234, "Priority": "MID"},
    {"P_ID": "P93", "Process": "Chrome", "Start Time (ms)": 189, "Priority": "High"},
    {"P_ID": "P42", "Process": "JDK", "Start Time (ms)": 9, "Priority": "High"},
    {"P_ID": "P9", "Process": "CMD", "Start Time (ms)": 7, "Priority": "High"},
    {"P_ID": "P87", "Process": "NotePad", "Start Time (ms)": 23, "Priority": "Low"},
]


def print_table(table):
    print("{:<5} {:<10} {:<20} {:<10}".format("P_ID", "Process", "Start Time (ms)", "Priority"))
    for row in table:
        print("{:<5} {:<10} {:<20} {:<10}".format(row["P_ID"], row["Process"], row["Start Time (ms)"], row["Priority"]))


def sort_by_pid(table):
    return sorted(table, key=lambda x: x["P_ID"])


def sort_by_start_time(table):
    return sorted(table, key=lambda x: x["Start Time (ms)"])


def sort_by_priority(table):
    return sorted(table, key=lambda x: x["Priority"])

while True:
    print("\nOptions:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")
    print("4. Quit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        sorted_table = sort_by_pid(flight_table)
        print("\nFlight Table Sorted by P_ID:")
        print_table(sorted_table)
    elif choice == "2":
        sorted_table = sort_by_start_time(flight_table)
        print("\nFlight Table Sorted by Start Time:")
        print_table(sorted_table)
    elif choice == "3":
        sorted_table = sort_by_priority(flight_table)
        print("\nFlight Table Sorted by Priority:")
        print_table(sorted_table)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")
