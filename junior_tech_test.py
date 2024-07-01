import csv
def read_csv_file(file_path):
    """
    Read a CSV file and return its content as a list of dictionaries.
    """
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    
    return data

def get_unique_teams(data):
    """
    Return a set of unique team names from the provided data.
    """
    team = set()
    for i in data:
        team.add(i['possession_team_name'])
    return team

def get_most_common_event_type(data):
    """
    Return the most common event type name from the provided data.
    """

    dic_item = {}
    max_count = 0
    max_item = None
    for item in data:
        if item['event_type_name'] in dic_item:
            dic_item[item['event_type_name']] +=1
        else:
            dic_item[item['event_type_name']] = 1

        if dic_item[item['event_type_name']] > max_count:
            max_count = dic_item[item['event_type_name']]
            max_item = item['event_type_name']


    return max_item

def filter_by_team(data, team_name):
    """
    Filter the data by the provided team name and return the filtered data.
    """
    filter_data = [row for row in data if 'team_name' in row and row['team_name'] == team_name and 'team_name' != None]
        
    return filter_data

def count_event_type_by_team(data, team_name, event_type_name):
    """
    Count the number of events of a specific type for a given team.
    """
    event_dic = {}
    
    for i in [row for row in data if 'team_name' in row and row['team_name'] == team_name]:
    
        if i['event_type_name'] in event_dic:
            event_dic[i['event_type_name']] +=1
        else:
            event_dic[i['event_type_name']] = 1
        
    return event_dic[event_type_name]

def average_pass_length_by_team(data, team_name):
    """
    Calculate the average pass length for the provided team to 1 decimal place
    """

    length = [float(row['pass_length']) for row in data if row['team_name'] == team_name and row['pass_length']]
    
    return round(sum(length) / len(length), 1)

def filter_players_by_position(data, position_name):
    """
    Return a list of player names who play at the provided position.
    """
    lst = {row['player_name'] for row in data if 'player_position_name' in row and row['player_position_name'] != None and row['player_position_name'] == position_name}
    return lst

def count_successful_passes(data):
    """
    Count the number of successful passes (not considering pass outcome).
    """
    successful_passes = 0  
    for i in range(len(data) - 1):
        current_event = data[i]
        next_event = data[i + 1]

        if current_event['team_name'] == next_event['team_name'] and current_event["event_type_name"] == "Pass" and next_event["event_type_name"] == "Ball Receipt*" :
            successful_passes += 1

    return successful_passes

def filter_by_period(data, period):
    """
    Return a list of events that occurred in the provided period (e.g., 1 or 2).
    """
    lst = list(set([row['event_type_name'] for row in data if row['period'] != None and int(row['period']) == period]))
    return lst

def count_shots_by_player(data, player_name):
    """
    Count the number of shots taken by the provided player.
    """
    shots = 0
    index = set()
    for row in data:
        if row["player_name"] == player_name and row["event_type_name"] == "Shot":
            if row["index"] not in index:
                index.add(row["index"])  
                shots += 1

    return shots
