from constants import PLAYERS, TEAMS

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

def display_team_stat(team):
    print("Team: {} Stats".format(team))
    print("\n--------------------\n")
    print("the number of players is :", num_players)
    print("the number of experienced players is :", num_exp)
    print("the number of inexperienced players is :", num_inexp)
    print("the average height of the team is", average_height(team, bal_teams))
    print("\n")
    print("The list of the players is :", end="")
    for player_dictionnary in bal_teams[team]:
        print(player_dictionnary["name"], ",", end="")
    print("\n")
    print("The list of the guardians is :", end="")
    for player_dictionnary in bal_teams[team]:
        print(",".join(player_dictionnary["guardians"]), ",", end="")


def display_all_teams() :
    print("1) Panthers \n")
    print("2) Bandits \n")
    print("3) Warriors \n")

# dunder automatically executes when script is run but not imported

if __name__ == "__main__":

    cleaned_players = clean_data(PLAYERS)
    print(cleaned_players,"\n\n\n\n\n\n\n")
    bal_teams = balance_teams(cleaned_players, TEAMS)
    num_players = int(len(PLAYERS) / len(TEAMS))
    num_exp = int(len([player for player in PLAYERS if player["experience"] == "YES"])/len(TEAMS))
    num_inexp = int(len([player for player in PLAYERS if player["experience"] == "NO"])/len(TEAMS))

    first_choice_menu = 0

    retry_menu_1 = True
    retry_menu_2 = True



# Iterating on the choice of 1 or 2 until we get a valid input
    while(retry_menu_1) :
        print("BASKETBALL TEAMS STATS TOOL :\n")
        print("----------MENU--------------:\n")
        print("Here are your choices : \n1) Display Team Stats \n2) Quit \n")
        try :
            first_choice_menu = int(input("Enter a choice >"))
            if first_choice_menu > 2 :
                raise ValueError("You should type 1 or 2")

        except ValueError :
            print("You should type 1 or 2")
        else :
            retry_menu_1 = False

        while(first_choice_menu == 1) :

            display_all_teams()

            # Iterating on the choice of the teams until we get a valid input
            while (retry_menu_2):
                try:
                    team_choice = int(input("Enter a choice >"))
                    if team_choice > 3:
                        raise ValueError("You should type 1, 2 or 3")
                except ValueError:
                    print("You should type 1, 2 or 3")
                else:
                    retry_menu_2 = False


            if team_choice == 1:
                display_team_stat("Panthers")


            elif team_choice == 2:
                display_team_stat("Bandits")

            elif team_choice == 3:
                display_team_stat("Warriors")

            input("\nPress Enter to continue...")

            first_choice_menu = 0
            retry_menu_1 = True
            retry_menu_2 = True



    print("See you soon !")
