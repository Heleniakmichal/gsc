from flask import Flask, request, render_template_string
import requests
import re
import os
from dotenv import load_dotenv
import datetime

# Load environment variables from .env file
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)

API_KEY = os.getenv('API_KEY')
CX = os.getenv('CX')

app = Flask(__name__)

HTML = '''
<!doctype html>
<title>Google Custom Search</title>
<h2>Google Custom Search</h2>
<form method=post>
  <label>Search phrase: <input name=phrase></label><br>
  <label>Website (domain or part): <input name=website></label><br>
  <input type=submit value=Search>
</form>
{% if results %}
  <h3>Results for "{{ phrase }}":</h3>
  <ol>
  {% for pos, link in results %}
    <li>{% if website and website in link %}<b style="color:green">{{ link }} (MATCH)</b>{% else %}{{ link }}{% endif %}</li>
  {% endfor %}
  </ol>
  {% if website %}
    {% if website_position %}
      <p><b>{{ website }}</b> found at position <b>{{ website_position }}</b>.</p>
    {% else %}
      <p><b>{{ website }}</b> not found in the available search results.</p>
    {% endif %}
  {% endif %}
  <p>Saved to: {{ filename }}</p>
{% endif %}
'''

def search_google(query, api_key, cx, start=1):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cx,
        'q': query,
        'start': start
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Google API error: {response.status_code} - {response.text}")
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    filename = None
    phrase = ''
    website = ''
    website_position = None
    if request.method == 'POST':
        phrase = request.form['phrase']
        website = request.form['website']
        found = False
        position = 1
        start = 1
        links = []
        MAX_START = 91  # Google CSE max start index
        while True:
            if start > MAX_START:
                break
            data = search_google(phrase, API_KEY, CX, start)
            items = data.get('items', [])
            if not items:
                break
            for item in items:
                link = item.get('link', '')
                links.append((position, link))
                if website and not website_position and website.lower() in link.lower():
                    website_position = position
                position += 1
            if 'nextPage' in data.get('queries', {}):
                start = data['queries']['nextPage'][0]['startIndex']
            else:
                break
        # Save to markdown file
        safe_phrase = re.sub(r'[^a-zA-Z0-9_-]', '_', phrase)
        today = datetime.date.today().isoformat()
        filename = f"{safe_phrase}_{today}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# Results for '{phrase}'\n\n")
            if website:
                if website_position:
                    f.write(f"Website '{website}' found at position {website_position}.\n\n")
                else:
                    f.write(f"Website '{website}' not found in the available search results.\n\n")
            for pos, link in links:
                f.write(f"{pos}. {link}\n")
        results = links
    return render_template_string(HTML, results=results, phrase=phrase, website=website, website_position=website_position, filename=filename)

if __name__ == '__main__':
    app.run(debug=True) 