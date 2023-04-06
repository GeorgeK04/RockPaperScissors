import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('dataset.csv')
X = pd.get_dummies(data.drop('winner', axis=1))
y = data['winner']

model = DecisionTreeClassifier()
model.fit(X.values, y)

player_score = 0
computer_score = 0

while True:
    try:
        num_rounds = int(input("Πόσους γύρους θέλετε να παίξετε; "))
        break
    except ValueError:
        print("Μη έγκυρη εισαγωγή. Παρακαλώ εισαγάγετε έναν αριθμό.")

outcomes = {
    'rock': {'rock': 'tie', 'paper': 'lose', 'scissors': 'win'},
    'paper': {'rock': 'win', 'paper': 'tie', 'scissors': 'lose'},
    'scissors': {'rock': 'lose', 'paper': 'win', 'scissors': 'tie'}
}

for i in range(num_rounds):
    while True:
        player_move = input("Κάντε την κίνηση σας (rock, paper, scissors): ").lower()
        if player_move not in X.columns:
            print("Μη έγκυρη κίνηση. Παρακαλώ πληκτρολογήστε rock, paper, or scissors.")
            continue
        break

    player_move_num = X.loc[0, player_move]

    computer_move_num = model.predict([X.iloc[0]])[0]
    computer_move = X.columns[computer_move_num]

    outcome = outcomes[player_move][computer_move]
    if outcome == 'win':
        player_score += 1
    elif outcome == 'lose':
        computer_score += 1

    if outcome == 'tie':
        round_result = 'Ισοπαλία!'
    elif outcome == 'win':
        round_result = 'Κέρδισες!'
    else:
        round_result = 'Ο υπολογιστής κέρδισε!'

    print(f"Round {i+1}: Έπαιξες {player_move}, ο υπολογιστής έπαιξε {computer_move}")
    print(f"Αποτέλεσμα Γύρου: {round_result}")
    print(f"Score: ΠΑΙΚΤΗΣ {player_score} - {computer_score} ΥΠΟΛΟΓΙΣΤΗΣ")

print(f"Τελικό αποτέλεσμα: ΠΑΙΚΤΗΣ {player_score} - {computer_score} ΥΠΟΛΟΓΙΣΤΗΣ")
