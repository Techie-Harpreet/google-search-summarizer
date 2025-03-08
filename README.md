# Search & Summarize

A Django-based web application that allows users to enter a query, fetches the top Google search results, and generates a concise summary using AI.

## 🚀 Features

- Fetches top 5 URLs from Google based on the user query.
- Extracts text content from the URLs using `newspaper3k`.
- Uses `SeleniumBase` to scrape search results.
- Generates a summary using AI (Gemini API).
- Simple and attractive front-end with API integration.

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework (DRF)
- **Frontend:** HTML, CSS, JavaScript
- **Libraries:** SeleniumBase, Newspaper3k
- **API Integration:** Google Search, AI Summarization (Gemini API)

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/search-summary-api.git
   cd search-summary-api
   ```
2. **Create a virtual environment & activate it:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables:**
   Create a `.env` file in the project root and add:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```
5. **Run migrations & start the server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## 🔥 Usage

1. Start the Django server:
   ```bash
   python manage.py runserver
   ```
2. Open your browser and go to:  
   ```
   http://127.0.0.1:8000/
   ```
3. Enter a search query and click "Search".
4. The system fetches search results using `SeleniumBase`, extracts content using `newspaper3k`, and generates a summary with Gemini API.

## 📸 Screenshots

1. **Search Page:**  
   ![Search Page](https://raw.githubusercontent.com/Techie-Harpreet/google-search-summarizer/refs/heads/main/resources/search%20page.png)
   
2. **Search Results & Summary:**  
   ![Search Results](https://raw.githubusercontent.com/Techie-Harpreet/google-search-summarizer/refs/heads/main/resources/home%20page.png)

## 📌 API Endpoints

- **POST /api/scrape-summarize/** → Accepts a JSON body `{ "query": "your search term" }` and returns a summary.

## 📜 License

This project is open-source and available under the MIT License.

## 🤝 Contributing

Feel free to fork the repository and submit pull requests! 😊

## 📬 Contact

For any queries, reach out to:
- **Email:** contact@harpreetsinghbansal.com
- **LinkedIn:**  [Click Here](https://www.linkedin.com/in/harpreetsinghbansal/)

