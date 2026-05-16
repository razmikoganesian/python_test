def friendship_score(name1, name2):
    name1, name2 = name1.lower(),  name2.lower()
    score = 0
    shared_letters = set(name1) & set(name2)
    vowels = set("aeoiuye")

    score += len(shared_letters) * 5
    score += len(vowels & shared_letters) * 10
    
    return min(score, 100)

def run_friendship_calculator():
    print("❤️ Friendship Compatibility Calculator")
    name1 = input("Enter first friend name:  ")
    name2 = input("Enter second friend name:  ")

    score = friendship_score(name1, name2)
    if score > 80:
        print(f"\n Amazing you are super compatible {score} ")
    else: 
        print(f"Well it can be better {score}")
run_friendship_calculator()