
def get_journey(start, end, stations_list):
    
    start_pos = stations_list.index(start)
    end_pos = stations_list.index(end)
    
    path = []
    
    
    if start_pos < end_pos:
        for i in range(start_pos, end_pos + 1):
            path.append(stations_list[i])
    else:
        for i in range(start_pos, end_pos - 1, -1):
            path.append(stations_list[i])
            
    stops = len(path) - 1
    time = stops * 2  
    
    return path, stops, time