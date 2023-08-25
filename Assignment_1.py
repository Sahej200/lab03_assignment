flight_table1 = [
    {"P_ID": "P1", "Process": "VSCode", "Start Time (ms)": 100, "Priority": "MID"},
    {"P_ID": "P23", "Process": "Eclipse", "Start Time (ms)": 234, "Priority": "MID"},
    {"P_ID": "P93", "Process": "Chrome", "Start Time (ms)": 189, "Priority": "High"},
    {"P_ID": "P42", "Process": "JDK 9", "Start Time (ms)": 9, "Priority": "High"},
    {"P_ID": "P9", "Process": "CMD", "Start Time (ms)": 7, "Priority": "High"},
    {"P_ID": "P87", "Process": "NotePad", "Start Time (ms)": 23, "Priority": "Low"},
]



def print_flight_table1(table):
    print("{:<5} {:<10} {:<15} {:<8}".format("P_ID", "Process", "Start Time (ms)", "Priority"))
    for entry in table:
        print("{:<5} {:<10} {:<15} {:<8}".format(
            entry["P_ID"], entry["Process"], entry["Start Time (ms)"], entry["Priority"]))



def sort_flight_table1(table, sort_option):
    if sort_option == 1:
        return sorted(table, key=lambda x: x["P_ID"])
    elif sort_option == 2:
        return sorted(table, key=lambda x: x["Start Time (ms)"])
    elif sort_option == 3:
        return sorted(table, key=lambda x: x["Priority"])
    else:
        return table




print("Flight Table:")
print_flight_table1(flight_table)

while True:
    try:
        sort_option = int(input("\nEnter sorting option (1. Sort by P_ID, 2. Sort by Start Time, 3. Sort by Priority, 0. Exit): "))
        if sort_option == 0:
            break
        elif sort_option < 0 or sort_option > 3:
            print("Invalid option. Please select a valid sorting option.")
        else:
            sorted_table = sort_flight_table(flight_table, sort_option)
            print("\nSorted Flight Table:")
            print_flight_table(sorted_table)
    except ValueError:
        print("Invalid input. Please enter a number.")

print("Exiting the program.")


