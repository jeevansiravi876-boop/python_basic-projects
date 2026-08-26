import random
football_cricket_data = [
    {'name': 'Cristiano Ronaldo', 'followers': '640M', 'place': 'Portugal', 'occupation': 'Football Player'},
    {'name': 'Lionel Messi', 'followers': '505M', 'place': 'Argentina', 'occupation': 'Football Player'},
    {'name': 'Neymar Jr', 'followers': '220M', 'place': 'Brazil', 'occupation': 'Football Player'},
    {'name': 'Virat Kohli', 'followers': '270M', 'place': 'India', 'occupation': 'Cricket Player'},
    {'name': 'Kylian Mbappe', 'followers': '130M', 'place': 'France', 'occupation': 'Football Player'},
    {'name': 'MS Dhoni', 'followers': '55M', 'place': 'India', 'occupation': 'Cricket Player'},
    {'name': 'Rohit Sharma', 'followers': '35M', 'place': 'India', 'occupation': 'Cricket Player'},
    {'name': 'Sachin Tendulkar', 'followers': '40M', 'place': 'India', 'occupation': 'Cricket Player'},
    {'name': 'Erling Haaland', 'followers': '45M', 'place': 'Norway', 'occupation': 'Football Player'},
    {'name': 'Mohamed Salah', 'followers': '65M', 'place': 'Egypt', 'occupation': 'Football Player'},
    {'name': 'Babar Azam', 'followers': '20M', 'place': 'Pakistan', 'occupation': 'Cricket Player'},
    {'name': 'Rishabh Pant', 'followers': '20M', 'place': 'India', 'occupation': 'Cricket Player'},
    {'name': 'Sunil Chhetri', 'followers': '5M', 'place': 'India', 'occupation': 'Football Player'},
    {'name': 'Jasprit Bumrah', 'followers': '20M', 'place': 'India', 'occupation': 'Cricket Player'},
    {'name': 'Kevin De Bruyne', 'followers': '45M', 'place': 'Belgium', 'occupation': 'Football Player'},
    {'name': 'Shubman Gill', 'followers': '15M', 'place': 'India', 'occupation': 'Cricket Player'},
    {'name': 'Sergio Ramos', 'followers': '65M', 'place': 'Spain', 'occupation': 'Football Player'},
    {'name': 'Hardik Pandya', 'followers': '25M', 'place': 'India', 'occupation': 'Cricket Player'},
    {'name': 'Harry Kane', 'followers': '55M', 'place': 'England', 'occupation': 'Football Player'},
]
score = 0
print("hello to higher lower game in this you have to select the person with most followers")

while True:
    def get_follower_count(player):
        return float(player['followers'].replace('M', ''))

    def show_player(player):
        print(f"Name: {player['name']}")
        print(f"Place: {player['place']}")
        print(f"Occupation: {player['occupation']}")
        
    def player_name(player):
        return (f"{player['name']}")

    def pick_two_players(data):
        return random.sample(data, 2)

    def compare_players(player1, player2, choice):
        count1 = get_follower_count(player1)
        count2 = get_follower_count(player2)

        if (count1 >= count2 and choice == "A") or (count1 <= count2 and choice == "B"):
            return True
        else:
            return False

    player1, player2 = pick_two_players(football_cricket_data)

    print("Compare A :")
    show_player(player1)
    print("vs")
    print("Compare B :")
    show_player(player2)

    print(f"ur score is {score}")
    choice = input("who has more follower type A or B:").upper()

    if compare_players(player1, player2, choice):
        score += 1
        print("you get 1 point you can continue")
        print(f"oyur score is {score}")
    else:
        print("Wrong guess. Game over!")
        print(f"Final score: {score}")
        print(f"{player_name(player1)} has {get_follower_count(player1)}M followers while {player_name(player2)} has {get_follower_count(player2)}M followers")
        break