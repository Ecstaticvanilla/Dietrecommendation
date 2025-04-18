# AI-Powered Diet Recommendation App

Welcome to the AI-Powered Diet Recommendation App—a personalized nutrition assistant that calculates your Basal Metabolic Rate (BMR) and Total Daily Energy Expenditure (TDEE) to generate tailored meal plans using Google's Gemini AI.

#Features 

User Authentication: Secure login system to personalize user experience.

BMR & TDEE Calculator: Computes your daily caloric needs based on personal metrics.

Customizable Meal Plans: Select specific meals (e.g., Breakfast, Lunch, Dinner) to include in your plan.

AI-Generated Recommendations: Utilizes Gemini AI to provide balanced meal suggestions with calorie estimates.

Interactive UI: Built with Streamlit for a responsive and user-friendly interface.

Demo

Will add in the future

# Installation

Clone the Repository:

bash
Copy
Edit
git clone https://github.com/Ecstaticvanilla/Dietrecommendation.git
cd Dietrecommendation
Create a Virtual Environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Configure API Keys:

Create a .streamlit/secrets.toml file:

toml
Copy
Edit
gemini_apikey = "your_gemini_api_key_here"
Run the Application:

bash
Copy
Edit
streamlit run app.py
Project Structure
graphql
Copy
Edit
Dietrecommendation/
├── app.py             # Main Streamlit application
├── bot.py             # Gemini AI integration
├── requirements.txt   # Python dependencies
├── .streamlit/
│   └── secrets.toml   # API keys and secrets
└── screenshots/
    └── demo.gif       # Application demo

# Technologies Used

Python 3.10+

Streamlit: Web application framework

Google Generative AI (Gemini): AI-powered content generation

HTML/CSS: Custom styling within Streamlit


# Contributors :
Swayam Kelkar : https://github.com/Ecstaticvanilla  
Rachel Fernandes : https://github.com/Rachelferns  
Nitin Gawde : https://github.com/NitinGawde26  
Mithilesh Deshmukh : https://github.com/blast678  

# License
This project is licensed under the MIT License.
