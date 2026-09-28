metro_lines = {
    "1": {
        "name": "yellow line",
        "stations": [
            "samaypur badli",
            "kashmere gate",
            "chandni chowk",
            "New Delhi",
            "rajiv chowk",
            "central secretariat",
            "INA",
            "hauz khas",
            "saket",
            "huda city centre"
        ]
    },
    "2": {
        "name": "blue line",
        "stations": [
            "dwarka sector 21",
            "janakpuri west",
            "rajouri garden",
            "karol bagh",
            "rajiv chowk",
            "mandi house",
            "mayur vihar 1",
            "noida sector 18",
            "noida electronic city"
        ]
    },
    "3": {
        "name": "red line",
        "stations": [
            "rithala",
            "netaji subhash place",
            "kashmere gate",
            "shastri park",
            "welcome",
            "dilshad garden",
            "shaheed sthal"
        ]
    }
}

def show_available_lines():
    print("\n--- available metro lines ---")
    print("1. yellow line")
    print("2. blue line")
    print("3. red line")
    print("-----------------------------")

def show_stations_in_line(line_choice):
    selected_line = metro_lines[line_choice]
    print("\n--- stations on " + selected_line["name"] + " ---")
    num = 1
    for s in selected_line["stations"]:
        print(num, ".", s)
        num = num + 1
    print("----------------------------------------")

def find_station(user_input, stations_list):
    clean_input = user_input.strip().lower()
    for s in stations_list:
        if s.lower() == clean_input:
            return s
    return None