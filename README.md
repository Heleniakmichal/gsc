# Google Search Tools with Browser Automation

> A comprehensive Google search analysis tool with AI-powered browser capabilities

This project combines Google Custom Search functionality with advanced browser automation tools. It allows you to perform Google searches, track website rankings, and analyze web pages using AI-powered browser tools through Anthropic's Model Context Protocol (MCP).

## 🔍 What This Project Does

This project provides three integrated tools for web search and analysis:

1. **Google Custom Search Tool** - Perform searches and track website rankings
2. **Browser Tools MCP Server** - AI-powered browser analysis and debugging
3. **Chrome Extension** - Real-time browser monitoring and data capture

### Google Search Features
- Search Google using the Custom Search API
- Track specific website positions in search results
- Generate markdown reports with search results
- Paginate through multiple pages of results (up to 100 results)
- Monitor keyword rankings for specific domains

### Browser Analysis Features
- Console log monitoring
- Network request analysis
- Screenshot capture
- Performance audits (Lighthouse-powered)
- SEO analysis
- Accessibility audits
- Real-time element selection tracking

## 🚀 Quick Start

### Prerequisites

1. **Google Custom Search API Setup**:
   - Get a Google Custom Search API key from [Google Cloud Console](https://console.cloud.google.com/)
   - Create a Custom Search Engine and get the CX ID
   - Create a `.env` file in the `browser-tools-mcp/` directory:
   ```env
   API_KEY=your_google_api_key_here
   CX=your_custom_search_engine_id_here
   ```

2. **Python Requirements**:
   ```bash
   pip install flask requests python-dotenv
   ```

3. **Node.js** (for browser tools) - Version 14 or higher

### Installation & Setup

#### 1. Google Search Tool

```bash
# Navigate to the main directory
cd browser-tools-mcp/

# Install Python dependencies
pip install -r requirements.txt  # or install manually: flask requests python-dotenv

# Create your .env file with API credentials
echo "API_KEY=your_api_key" > .env
echo "CX=your_cx_id" >> .env

# Run the Flask application
python app.py
```

The Google search interface will be available at `http://localhost:5000`

#### 2. Browser Tools Setup

**Install Chrome Extension:**
1. Download the extension: [BrowserTools Chrome Extension v1.2.0](https://github.com/AgentDeskAI/browser-tools-mcp/releases/download/v1.2.0/BrowserTools-1.2.0-extension.zip)
2. Extract the zip file
3. Open Chrome → Extensions → Enable "Developer mode"
4. Click "Load unpacked" and select the extracted folder

**Install Browser Tools Server:**
```bash
# Install and run the browser tools server
npx @agentdeskai/browser-tools-server@latest
```

**Install MCP Server:**
```bash
# Install the MCP server for your IDE
npx @agentdeskai/browser-tools-mcp@latest
```

#### 3. Complete Setup

1. Start the browser tools server:
   ```bash
   npx @agentdeskai/browser-tools-server@latest
   ```

2. Start your IDE with MCP support (Cursor, Claude Desktop, etc.)

3. Open Chrome DevTools → Navigate to "BrowserTools MCP" panel

4. The extension should automatically connect to the server

## 📖 Usage

### Google Search Tool

1. **Access the Interface**: Navigate to `http://localhost:5000`

2. **Perform a Search**:
   - Enter your search phrase (e.g., "best restaurants in NYC")
   - Optionally enter a website domain to track (e.g., "yelp.com")
   - Click "Search"

3. **View Results**:
   - See all search results with positions
   - If tracking a website, see its ranking position
   - Results are automatically saved to a markdown file

4. **Example Use Cases**:
   - Track your website's ranking for specific keywords
   - Monitor competitor positions
   - Generate SEO reports
   - Research keyword difficulty

### Browser Tools

Once the browser tools are connected, you can use various AI commands:

#### Console & Network Analysis
- "Show me the console errors on this page"
- "What network requests failed?"
- "Capture a screenshot of this page"

#### Performance Analysis
- "Run a performance audit on this page"
- "Why is this page loading slowly?"
- "Check the Core Web Vitals"

#### SEO Analysis
- "Run an SEO audit"
- "How can I improve SEO for this page?"
- "Check if this page meets best practices"

#### Accessibility Testing
- "Run an accessibility audit"
- "Are there any WCAG compliance issues?"

#### Comprehensive Analysis
- "Run audit mode" (runs all audits)
- "Enter debugger mode" (runs all debugging tools)

## 🔧 Configuration

### Google Search Configuration

Edit the `.env` file in `browser-tools-mcp/`:
```env
API_KEY=your_google_custom_search_api_key
CX=your_custom_search_engine_id
```

### Browser Tools Configuration

Open Chrome DevTools → BrowserTools MCP panel to configure:
- Log limits and query limits
- Screenshot save path
- Server connection settings
- Request/response header visibility

## 📁 Project Structure

```
GOOGLE SEARCH/
├── browser-tools-mcp/
│   ├── app.py                     # Main Flask application for Google search
│   ├── .env                       # Environment variables (create this)
│   ├── browser-tools-mcp/         # MCP server package
│   ├── browser-tools-server/      # Browser automation server
│   ├── chrome-extension/          # Chrome extension files
│   └── docs/                      # Documentation
├── *.md files                     # Generated search result files
└── README.md                      # This file
```

### Key Components

1. **`app.py`** - Flask web application that:
   - Provides a web interface for Google searches
   - Uses Google Custom Search API
   - Generates markdown reports
   - Tracks website rankings

2. **`browser-tools-mcp/`** - MCP server that:
   - Connects to AI tools (Cursor, Claude, etc.)
   - Provides browser analysis capabilities
   - Handles audit and debugging commands

3. **`browser-tools-server/`** - Node.js server that:
   - Manages browser automation with Puppeteer
   - Runs Lighthouse audits
   - Handles real-time browser communication

4. **`chrome-extension/`** - Browser extension that:
   - Monitors console logs and network requests
   - Captures screenshots
   - Tracks DOM element selection
   - Connects to the browser tools server

## 🎯 Use Cases

### SEO & Marketing
- Track keyword rankings across multiple search terms
- Monitor competitor positions
- Generate automated SEO reports
- Analyze search result trends

### Web Development
- Debug website issues in real-time
- Monitor performance metrics
- Check accessibility compliance
- Analyze network requests and errors

### Research & Analysis
- Gather search data for market research
- Monitor brand mentions in search results
- Track website visibility over time
- Analyze search result patterns

## 🛠️ Advanced Features

### Google Search Advanced Options
- **Pagination**: Automatically fetches up to 100 search results
- **Domain Tracking**: Highlights matches for specific domains
- **Export Options**: Saves results in markdown format with timestamps
- **Custom Queries**: Supports all Google search operators

### Browser Tools Advanced Features
- **Lighthouse Integration**: Professional-grade audits
- **Puppeteer Automation**: Headless browser control
- **Real-time Monitoring**: Live console and network logging
- **AI Integration**: Works with multiple AI coding assistants

## 📄 Generated Files

The Google search tool automatically generates markdown files with results:
- Format: `{search_phrase}_{date}.md`
- Contains ranked list of URLs
- Shows domain match positions
- Includes search metadata

Example: `best_restaurants_nyc_2025-01-15.md`

## 🔍 Troubleshooting

### Google Search Issues
- **"API error"**: Check your API key and CX ID in `.env`
- **"No results"**: Verify your Custom Search Engine configuration
- **"Rate limit"**: Google CSE has daily quotas, check your usage

### Browser Tools Issues
- **Extension not connecting**: Restart Chrome and the browser-tools-server
- **Server not found**: Check that both servers are running
- **Audit failures**: Ensure you have Chrome/Chromium installed

### General Issues
- **Port conflicts**: Default ports are 5000 (Flask) and 3025 (browser server)
- **Permission errors**: Make sure you have write permissions for markdown files
- **Network issues**: Check firewalls and proxy settings

## 📚 Documentation

- [Browser Tools Documentation](https://browsertools.agentdesk.ai/)
- [Google Custom Search API Docs](https://developers.google.com/custom-search/v1/overview)
- [Model Context Protocol Docs](https://modelcontextprotocol.io/)

## 🤝 Contributing

This project combines multiple open-source components. See individual component documentation for contribution guidelines.

## 📜 License

MIT License - see individual component licenses for details.

## 🔗 Related Projects

- [BrowserTools MCP](https://github.com/AgentDeskAI/browser-tools-mcp) - Original browser tools project
- [Google Custom Search](https://developers.google.com/custom-search) - Search API documentation
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) - Web auditing tool
