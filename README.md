# Personalized_Diet_Recommendation_System
### A Flask-based web application leveraging the power of Machine Learning to suggest personalized dietary recommendations.

https://github.com/RawfurJim/Personalized_Diet_Recommendation_System/assets/64610564/8fe6577e-c752-47e3-9a71-c5251b0a510c

## Table of Contents

###### General Information
###### Development	
###### Technologies
###### Future Scope

#### General Information
##### Motivation

With the rising awareness of the importance of maintaining a healthy lifestyle, people across the globe are more interested than ever in their dietary habits. However, maintaining a balanced diet isn't as easy as it seems and often requires more than just avoiding junk food and doing physical exercises. It necessitates a deeper understanding of an individual's nutritional requirements based on their height, weight, age, gender, and activity level. To cater to this need, this project presents a personalized diet recommendation system that uses Machine Learning algorithms to suggest appropriate food items based on a user's personal details and daily caloric requirements.

##### What is the Personalized Diet Recommendation System?
The Personalized Diet Recommendation System is a flask web application that calculates user's Body Mass Index (BMI) and Basal Metabolic Rate (BMR) based on the inputs provided, and recommends a list of foods that aligns with the calculated daily caloric requirement. This is achieved by using the K-nearest Neighbors (KNN) algorithm, a type of instance-based learning, or lazy learning, where the function is only approximated locally and all computation is deferred until function evaluation.
The recommendation system goes beyond merely suggesting foods by considering the user's activity level and adjusts the caloric intake accordingly. The system provides distinct recommendations for breakfast, lunch, and dinner, making it a truly personalized and comprehensive dietary guide.

#### Development

##### Data Acquisition and Preprocessing
The system uses RapidApi to fetch food data in JSON format. The received data is then cleaned and reshaped into a CSV file for further usage. The detailed process is thoroughly documented in the code.

##### Model Development
The system uses the K-nearest Neighbors algorithm to recommend foods based on the calculated BMR. Furthermore, it incorporates adjustments based on the BMI to account for underweight, overweight, or severely underweight conditions, which assists in guiding the user towards their ideal weight range.

##### Flask Web Application
To facilitate user-friendly interaction with the recommendation system, a Flask web application has been developed. The user inputs their details, and the system computes the BMR and recommends a list of suitable food items.

#### Technologies

•	Python: 3.x
•	Flask: 2.x
•	Scikit-learn: 0.24.x
•	Pandas: 1.x
•	Numpy: 1.x
•	RapidAPI
•	Requests: 2.x

#### Future Scope

In future versions, we aim to further personalize the recommendations by considering factors such as dietary restrictions, allergies, or specific dietary preferences (e.g., vegan, pescatarian, etc.). We also plan to incorporate a feature that would allow users to track their progress over time.
Please feel free to fork this repository and contribute to this project. Any contributions you make are greatly appreciated!


