from constants import PLAYERS, TEAMS
#todo  add exceptions

def sentence_to_bool(sentence):
    if sentence == "YES":
        return True
    elif sentence == "NO":
        return False
    else:
        raise ValueError("We expect either YES or NO as a parameter")


def height_to_int(height):
    return int(height.split(" ")[0])


def clean_data(players):
    cleaned_list = []
    for player in players:
        clean_player = {}
        clean_player["name"] = player["name"]
        clean_player["guardians"] = player["guardians"].split("and ")
        clean_player["experience"] = sentence_to_bool(player["experience"])
        clean_player["height"] = height_to_int(player["height"])
        cleaned_list.append(clean_player)
    return cleaned_list


def balance_teams(players, teams):

    experienced = [player for player in players if player["experience"] == True]
    inexperienced = [player for player in players if player["experience"] == False]

    team_composition = {}
    num_players_team = len(players) / len(teams)
    num_exp = len(experienced) / len(teams)
    num_inexp = len(inexperienced) / len(teams)

    for i in range(0, len(teams)):
        team_composition[teams[i]] = [player for player in experienced[i * int(num_exp):(i + 1) * int(num_exp)]]
        team_composition[teams[i]].extend([player for player in inexperienced[i * int(num_inexp):(i + 1) * int(num_inexp)]])
    return team_composition

def average_height(team,balanced_teams) :
    return float(sum([player["height"] for player in balanced_teams[team]])/len([player["height"] for player in balanced_teams[team]]))


# dunder automatically executes when script is run but not imported

if __name__ == "__main__":

    cleaned_players = clean_data(PLAYERS)
    print(cleaned_players,"\n\n\n\n\n\n\n")
    bal_teams = balance_teams(cleaned_players, TEAMS)
    num_players = int(len(PLAYERS) / len(TEAMS))
    num_exp = int(len([player for player in PLAYERS if player["experience"] == "YES"])/len(TEAMS))
    num_inexp = int(len([player for player in PLAYERS if player["experience"] == "NO"])/len(TEAMS))

    first_choice_menu = 1

    print("BASKETBALL TEAMS STATS TOOL :\n")
    print("----------MENU--------------:\n")
    print("Here are your choices : \n1) Display Team Stats \n2) Quit \n")
    first_choice_menu = int(input("Enter a choice >"))

    while(first_choice_menu == 1) :

        print("1) Panthers \n")
        print("2) Bandits \n")
        print("3) Warriors \n")
        team_choice = int(input("Enter a choice >"))
        if team_choice == 1:
            print("Team: Panthers Stats")
            print("\n--------------------\n")
            print("the number of players is :", num_players)
            print("the number of experienced players is :", num_exp)
            print("the number of inexperienced players is :", num_inexp)
            print("the average height of the team is", average_height("Panthers", bal_teams))
            print("\n")
            print("The list of the players is :",end="")
            for player_dictionnary in bal_teams["Panthers"]:
                print(player_dictionnary["name"], ",", end="")
            print("\n")
            print("The list of the guardians is :", end="")
            for player_dictionnary in bal_teams["Panthers"]:
                print(player_dictionnary["guardians"], ",", end="")

        elif team_choice == 2:
            print("Team: Bandits Stats")
            print("\n--------------------")
            print("the number of players is :", num_players)
            print("the number of experienced players is :", num_exp)
            print("the number of inexperienced players is :", num_inexp)
            print("the average height of the team is", average_height("Bandits", bal_teams))
            print("\n")
            print("The list of the players is :", end="")
            for player_dictionnary in bal_teams["Bandits"]:
                print(player_dictionnary["name"], ",", end="")
            print("\n")
            print("The list of the guardians is :", end="")
            for player_dictionnary in bal_teams["Panthers"]:
                print(player_dictionnary["guardians"], ",", end="")

        elif team_choice == 3:
            print("Team: Warriors Stats")
            print("--------------------")
            print("the number of players is :", num_players)
            print("the number of experienced players is :", num_exp)
            print("the number of inexperienced players is :", num_inexp)
            print("the average height of the team is",average_height("Warriors", bal_teams))
            print("\n")
            print("The list of the players is :",end="")
            for player_dictionnary in bal_teams["Warriors"]:
                print(player_dictionnary["name"], ",", end="")
            print("\n")
            print("The list of the guardians is :",end="")
            for player_dictionnary in bal_teams["Panthers"]:
                print(",".join(player_dictionnary["guardians"]), ",", end="")
        input("\nPress Enter to continue...")
        print("BASKETBALL TEAMS STATS TOOL :\n")
        print("----------MENU--------------:\n")
        print("Here are your choices : \n1) Display Team Stats \n2) Quit \n")
        first_choice_menu = int(input("Enter a choice >"))

    else:
        print("See you soon !")
