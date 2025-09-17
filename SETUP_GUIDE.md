# Complete Setup Guide for Google Search Tools

## Step-by-Step Installation

### 1. Google API Setup (Required for Search Functionality)

1. **Get Google Custom Search API Key**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing one
   - Enable the "Custom Search API"
   - Go to "Credentials" and create an API key
   - Copy your API key

2. **Create Custom Search Engine**:
   - Go to [Google Custom Search](https://cse.google.com/cse/)
   - Click "Add" to create a new search engine
   - Enter `www.google.com` as the site to search (for web-wide search)
   - Give it a name and create it
   - Copy the "Search engine ID" (CX)

3. **Configure Environment Variables**:
   ```bash
   cd browser-tools-mcp/
   
   # Create .env file
   echo "API_KEY=your_actual_api_key" > .env
   echo "CX=your_actual_cx_id" >> .env
   ```

### 2. Python Environment Setup

```bash
# Install Python dependencies
cd browser-tools-mcp/
pip install -r requirements.txt

# Or install manually:
pip install flask requests python-dotenv
```

### 3. Browser Tools Setup (Optional but Recommended)

#### Install Chrome Extension
1. Download: [BrowserTools v1.2.0](https://github.com/AgentDeskAI/browser-tools-mcp/releases/download/v1.2.0/BrowserTools-1.2.0-extension.zip)
2. Extract the zip file
3. Open Chrome → `chrome://extensions/`
4. Enable "Developer mode" (top right toggle)
5. Click "Load unpacked" and select the extracted extension folder

#### Install Browser Tools Servers
```bash
# Terminal 1: Browser Tools Server
npx @agentdeskai/browser-tools-server@latest

# Terminal 2: MCP Server (for AI tools)
npx @agentdeskai/browser-tools-mcp@latest
```

### 4. Running the Application

#### Start Google Search Tool
```bash
cd browser-tools-mcp/
python app.py
```
- Open: `http://localhost:5000`

#### Connect Browser Tools
1. Open Chrome DevTools (F12)
2. Navigate to "BrowserTools MCP" tab
3. Should automatically connect to server

### 5. Testing the Setup

#### Test Google Search
1. Go to `http://localhost:5000`
2. Enter search: "test search"
3. Enter domain: "wikipedia.org"
4. Click Search
5. Should see results and generate a markdown file

#### Test Browser Tools
1. Open any website in Chrome
2. Open DevTools → BrowserTools MCP panel
3. Check connection status (should be green)
4. In your AI tool (Cursor, etc.), try: "Take a screenshot"

## Configuration Options

### Google Search Configuration

Edit `browser-tools-mcp/.env`:
```env
API_KEY=your_google_api_key
CX=your_search_engine_id
```

### Browser Tools Configuration

In Chrome DevTools → BrowserTools MCP panel:
- **Log Limit**: Number of console logs to keep (default: 50)
- **Query Limit**: Max characters for queries (default: 30000)
- **String Size Limit**: Max length for log strings (default: 500)
- **Screenshot Path**: Where to save screenshots
- **Server Settings**: Host/port for browser tools server

## Troubleshooting

### Google Search Issues

**"Missing API_KEY or CX"**:
- Check your `.env` file exists in `browser-tools-mcp/`
- Verify API key and CX are correct
- No quotes needed around values in .env

**"API Error 403"**:
- API key may be invalid or restricted
- Check API quotas in Google Cloud Console
- Ensure Custom Search API is enabled

**"No results found"**:
- Check your Custom Search Engine settings
- Ensure it's set to search the entire web
- Try a common search term like "python"

### Browser Tools Issues

**Extension not loading**:
- Check Chrome extensions page for errors
- Ensure Developer mode is enabled
- Try refreshing the extension

**Server connection failed**:
- Ensure both browser-tools-server and MCP server are running
- Check ports 3025 (browser server) and others aren't blocked
- Try restarting Chrome

**MCP tools not working in IDE**:
- Verify MCP server is configured in your IDE
- Check IDE's MCP configuration documentation
- Ensure IDE supports MCP protocol

### Permission Issues

**File write errors**:
- Check write permissions in project directory
- On Windows, try running as administrator
- Ensure antivirus isn't blocking file creation

**Port conflicts**:
- Flask uses port 5000 (configurable)
- Browser tools use port 3025 (auto-configurable)
- Close other applications using these ports

## Advanced Usage

### Custom Search Operators

Use Google search operators in the search field:
- `site:example.com python` - Search within a specific site
- `"exact phrase"` - Search for exact phrases
- `python -java` - Exclude terms
- `filetype:pdf python` - Search for specific file types

### Automation Scripts

Create automation scripts using the APIs:

```python
# Example: Automated ranking check
import requests
import time

def check_ranking(keyword, domain):
    response = requests.post('http://localhost:5000', data={
        'phrase': keyword,
        'website': domain
    })
    # Parse response to get ranking position
    return response

# Check rankings every hour
while True:
    position = check_ranking("python tutorial", "example.com")
    print(f"Current position: {position}")
    time.sleep(3600)  # 1 hour
```

### Integration with AI Tools

Example queries for AI assistants:
- "Check the ranking of example.com for 'python tutorial'"
- "Run a performance audit on this page and suggest improvements"
- "Take a screenshot and analyze the page layout"
- "Monitor console errors while I navigate this site"

## API Quotas and Limits

### Google Custom Search API
- **Free tier**: 100 queries per day
- **Paid tier**: $5 per 1000 queries (up to 10k/day)
- **Rate limit**: 10 queries per second

### Browser Tools
- No external API calls (runs locally)
- Limited by system resources
- Lighthouse audits may take 10-30 seconds

## Security Considerations

1. **API Keys**: Never commit `.env` file to version control
2. **Local Only**: Browser tools run locally, no data sent externally
3. **HTTPS**: Use HTTPS for production deployments
4. **Firewall**: Browser tools server is accessible on local network

## Getting Help

1. Check this guide first
2. Look at example markdown files generated by successful searches
3. Check browser console for JavaScript errors
4. Review server logs for detailed error messages
5. Open an issue with specific error messages and steps to reproduce
