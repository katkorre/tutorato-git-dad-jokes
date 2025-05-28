import json

def load_known_jokes():
    with open("/content/tutorato-git-dad-jokes/dad_jokes.json") as f:
        return json.load(f)

def classify_joke(joke, known_jokes):
    joke = joke.lower()
    if joke in known_jokes:
        return "Dad Joke ✅"
    elif "pun" in joke or "knee" in joke:
        return "So Bad It's Good"
    else:
        return "Not a Dad Joke ❌"

if __name__ == "__main__":
    joke = input("Tell me a joke: ")
    known_jokes = load_known_jokes()
    result = classify_joke(joke, known_jokes)
    print(f"\nResult: {result}")
