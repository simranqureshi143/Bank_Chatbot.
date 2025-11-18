import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class BankingChatbot:
    def __init__(self):
        data = json.load(open("intents.json"))
        self.tags = []
        self.patterns = []
        self.responses = {}

        for intent in data["intents"]:
            tag = intent["tag"]
            self.tags.append(tag)
            self.responses[tag] = intent["responses"]
            for p in intent["patterns"]:
                self.patterns.append(p)
        
        self.vectorizer = TfidfVectorizer()
        X = self.vectorizer.fit_transform(self.patterns)

        y = []
        for intent in data["intents"]:
            for _ in intent["patterns"]:
                y.append(intent["tag"])

        self.model = LogisticRegression()
        self.model.fit(X, y)

    def get_response(self, user_input):
        X = self.vectorizer.transform([user_input])
        tag = self.model.predict(X)[0]
        return random.choice(self.responses[tag])
