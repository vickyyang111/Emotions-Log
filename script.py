import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob
import datetime
import matplotlib.pyplot as plt

# Class to recognize emotion from text
class EmotionRecognizer:
    def analyze_emotion(self, text):
        # Use TextBlob to get sentiment polarity
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        # Return emotion based on sentiment value
        if sentiment > 0.5:
            return "happy"
        elif sentiment < -0.5:
            return "sad"
        else:
            return "neutral"

# Class to log emotions
class EmotionLogger:
    def __init__(self, log_file_path):
        # Initialize with path to log file
        self.log_file_path = log_file_path

    def log_emotion(self, emotion, timestamp):
        # Open log file and append emotion with timestamp
        with open(self.log_file_path, 'a') as log_file:
            log_file.write(f"{timestamp.isoformat()} - {emotion}\n")

    def get_emotions(self):
        # Open log file and read emotions
        with open(self.log_file_path, 'r') as log_file:
            emotions = [line.split(' - ')[1].strip() for line in log_file.readlines()]
        return emotions

# Class to generate chatbot response based on emotion
class ChatbotResponseGenerator:
    def __init__(self, response_rules):
        # Initialize with response rules
        self.response_rules = response_rules

    def generate_response(self, emotion):
        # Return response based on emotion
        return self.response_rules.get(emotion, "I'm not sure how to respond to that.")

# Class to analyze emotion trends
class EmotionTrendAnalyzer:
    def __init__(self, log_file_path):
        # Initialize with path to log file
        self.log_file_path = log_file_path

    def analyze_trends(self, emotions):
        # Count occurrences of each emotion
        emotion_counts = {emotion: emotions.count(emotion) for emotion in set(emotions)}
        return emotion_counts

    def plot_trend(self, emotion_counts):
        # Plot emotion counts
        emotions = list(emotion_counts.keys())
        counts = list(emotion_counts.values())

        plt.bar(emotions, counts)
        plt.xlabel('Emotion')
        plt.ylabel('Count')
        plt.title('Emotion Trend in the Past Week')
        plt.show()

# Class for the main application
class EmotionLogApp:
    def __init__(self, recognizer, logger, responder, analyzer):
        # Initialize with recognizer, logger, responder, and analyzer
        self.recognizer = recognizer
        self.logger = logger
        self.responder = responder
        self.analyzer = analyzer
        self.create_gui()

    def create_gui(self):
        # Create GUI for the application
        self.root = tk.Tk()
        self.root.title("Emotion Log")

        label = tk.Label(self.root, text="How are you feeling today?")
        label.pack()

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack()

        button = tk.Button(self.root, text="Log Emotion", command=self.log_emotion)
        button.pack()

        self.root.mainloop()

    def log_emotion(self):
        # Get user input and log emotion
        user_input = self.entry.get()
        if not user_input:
            messagebox.showerror("Error", "Please enter your emotion.")
            return

        identified_emotion = self.recognizer.analyze_emotion(user_input)
        self.logger.log_emotion(identified_emotion, datetime.datetime.now())
        response = self.responder.generate_response(identified_emotion)
        messagebox.showinfo("Response", response)

        emotions = self.logger.get_emotions()
        emotion_counts = self.analyzer.analyze_trends(emotions)

        # Plot trend every 7 emotions
        if len(emotions) % 7 == 0:
            self.analyzer.plot_trend(emotion_counts)

# Initialize the application
if __name__ == "__main__":
    recognizer = EmotionRecognizer()
    logger = EmotionLogger("emotion_logs.txt")
    responder = ChatbotResponseGenerator({"happy": "Great to see you happy!", "sad": "Sorry to hear that. Hope you feel better soon.", "neutral": "I understand."})
    analyzer = EmotionTrendAnalyzer("emotion_logs.txt")

    app = EmotionLogApp(recognizer, logger, responder, analyzer)
