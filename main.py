import stations
import route
import fare

while True:
    print("\n*** Delhi metro ticketing system ***")
    print("1. plan journey & buy ticket")
    print("2. view all lines & stations")
    print("3. exit")
    
    choice = input("enter your choice (1-3): ")

    if choice == "2":
        stations.show_available_lines()
        line_num = input("enter line number (1-3) to view stations: ")
        if line_num in stations.metro_lines:
            stations.show_stations_in_line(line_num)
        else:
            print("invalid line selection.")

    elif choice == "1":
        stations.show_available_lines()
        line_choice = input("select the line you want to travel on (1-3): ")

        if line_choice not in stations.metro_lines:
            print("error: invalid line selected. please choose 1, 2, or 3.")
            continue

        selected_line_data = stations.metro_lines[line_choice]
        line_name = selected_line_data["name"]
        active_stations = selected_line_data["stations"]

        stations.show_stations_in_line(line_choice)
        
        start_input = input("\nenter boarding station name: ")
        end_input = input("enter destination station name: ")

        start = stations.find_station(start_input, active_stations)
        end = stations.find_station(end_input, active_stations)

        if start is None or end is None:
            print("error: station name typed incorrectly or does not belong to " + line_name + "!")
            continue

        if start == end:
            print("error: boarding and destination cannot be the same!")
            continue

        hour = int(input("enter travel time (hour 0 to 23): "))
        if hour < 0 or hour > 23:
            print("error: invalid hour. enter between 0 and 23.")
            continue

        path, stops, time = route.get_journey(start, end, active_stations)
        base, extra, total, is_rush = fare.get_ticket_fare(stops, hour)

        print("\n--- your journey details ---")
        print("metro line      :", line_name)
        print("route path      :")
        count = 1
        for s in path:
            print(" ", count, "->", s)
            count = count + 1
            
        print("total stops     :", stops)
        print("estimated time  :", time, "minutes")
        print("base fare       : rs", base)
        if is_rush:
            print("rush hour charge: rs", extra, "(peak hour applied)")
        else:
            print("rush hour charge: rs 0 (normal hours)")
        print("total fare      : rs", total)
        print("----------------------------")

        pay = input("\ndo you want to pay with smart card? (y/n) or cash: ")
        if pay == "y" or pay == "Y":
            card_no = input("enter card number(6 digit no.): ")
            balance = float(input("enter current balance (rs): "))

            success, new_balance = fare.deduct_card(balance, total)

            if success:
                print("\n=============================")
                print("     Delhi metro pass        ")
                print("=============================")
                print("line      :", line_name)
                print("card no   :", card_no)
                print("from      :", start)
                print("to        :", end)
                print("fare paid : rs", total)
                print("remaining : rs", new_balance)
                print("status    : payment successful")
                print("=============================")
            else:
                print("\nfailed: not enough balnce in card!")
        elif(pay == "cash"):
            print(f"Please pay rs {total} at the counter, Thank you")
        else:
            print("booking cancelled.")

    elif choice == "3":
        print("thank you for using Delhi metro!")
        break

    else:
        print("invalid choice, please select 1, 2, or 3.")
