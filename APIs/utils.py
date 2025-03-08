import requests
from seleniumbase import Driver
from selenium.webdriver.common.by import By
import newspaper
import os
from dotenv import load_dotenv

load_dotenv()

# ✅ Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "models/gemini-1.5-pro-latest"

def get_google_search_results(query, max_results=5):
    driver = Driver(uc=True) 

    search_url = f"https://www.google.com/search?q={query}"
    driver.uc_open_with_reconnect(search_url, 4) 

    results = driver.find_elements(By.CSS_SELECTOR, "div.g.Ww4FFb.vt6azd.tF2Cxc.asEBEc a[jsname='UWckNb']")[:max_results]
    urls = [result.get_attribute("href") for result in results]

    driver.quit()
    return urls

def extract_text_from_url(url):
    try:
        article = newspaper.Article(url)
        article.download()
        article.parse()
        article.nlp()

        return article.summary
    except Exception:
        return "Error extracting text"

def call_gemini_api(text):
    url = f"https://generativelanguage.googleapis.com/v1beta/{GEMINI_MODEL}:generateContent"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": f"Summarize this text in simple terms:\n\n{text}"}]
            }
        ]
    }

    response = requests.post(f"{url}?key={GEMINI_API_KEY}", headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    
    print(f"Error: {response.text}")
    return "Summarization failed"

def split_text(text, max_tokens=5000):
    sentences = text.split(". ")
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) < max_tokens:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def summarize_large_text(text):
    text_chunks = split_text(text)
    summarized_chunks = []

    for chunk in text_chunks:
        summary = call_gemini_api(chunk) 
        summarized_chunks.append(summary)

    final_summary = " ".join(summarized_chunks)  
    return final_summary

def process_urls(urls):
    full_text = ""

    for url in urls:
        text = extract_text_from_url(url)
        full_text += text + "\n\n"  

    if len(full_text) > 5000:
        summary = summarize_large_text(full_text)
    else:
        summary = call_gemini_api(full_text) 

    return summary
