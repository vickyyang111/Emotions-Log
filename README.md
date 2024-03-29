# Emotions-Log
This is the final project for BCOG200 class by Vicky Yang.

Imagine having a companion like Emotions-Log, a chatbot that is designed to recognize and respond to your emotional cues, provide personalized responses, and deliver weekly insights into your emotional well-being. With the help of NLP and sentiment analysis, Emotions-Log offers a unique interaction experience that empowers you to better understand and manage your emotions. Get to know yourself better with this friendly chatbot!

Features include :

a. **Emotion Recognition**: By analyzing user input through sentiment analysis techniques, the emotion_recognize(input_text) function identifies the user's current emotional state, such as happiness, sadness, or anger.
Arguments: input_text (string) - the user input to analyze.
Returns: The identified emotion.

b. **Emotion Logging**: The emotion_log(emotion, timestamp) function logs the results of the emotional analysis for each interaction, along with a timestamp, to track emotional trends and support data-driven insights.
Arguments: emotion (string) - the recognized emotion, timestamp (datetime) - the time of the interaction.
Functionality: Logs the emotion and timestamp in the database.

c. **Emotion-Responsive Replies**: Based on the identified emotion, the generate_response(emotion) function selects and delivers an appropriate response from its repertoire to support or uplift the user.
Arguments: emotion (string) - the emotion to respond to.
Returns: A text response tailored to the identified emotion.

d. **Emotion Trend Analysis and Reporting**: The trend_analysis(start_date, end_date) function performs an analysis of the logged emotional data every seven days to identify patterns and trends, generating a visual report for the user that provides insight into their emotional dynamics over time.
Arguments: start_date and end_date (datetime) - the period for the emotional trend analysis.
Returns: A visual report of emotional trends over the specified period.

Example Use Cases:

Understanding Emotional Patterns: Users can interact with Emotions-Log daily. The system will recognize emotions, provide supportive feedback, and log these interactions. Over time, users can request a report to see their emotional trends.
Immediate Emotional Support: When feeling a strong emotion, a user can express this to Emotions-Log and receive an immediate empathetic response, tailored to their current state.
Data Input Requirements
Input Format: Text input should be in plain text format, ideally in English for accurate sentiment analysis.
Data Structure: Emotional log entries should include:
emotion: string (e.g., "happy", "sad", "angry")
Timestamp: datetime in ISO 8601 format
