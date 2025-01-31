# Boulder County Meeting Scraper

A Python script to scrape meeting information from Boulder County's eScribe platform. This is the first step in a larger project to collect meeting information and monitor agendas for specific topics of concern to lobbyists and their clients. Phase 2 will use NLP, LLM and possibly RAG to monitor agendas for specific topics of concern and provide alerts.
## Description
This scraper collects meeting information including:
- Meeting titles
- Dates and times
- Locations
- HTML and PDF agenda links

## Requirements
- Python 3.x
- - pip (Python package installer)
- Write permissions in your home directory
Chrome or Chromium browser
- Required packages:
  - selenium
  - pandas
  - webdriver_manager

## Installation
1. Install Python dependencies:

## Output
The script creates a CSV file containing:
- Meeting details
- Links to agendas
- Timestamps of data collection

## Platform Support

### macOS (Primary Development Platform)
- Tested on macOS
- Default Chrome installation location assumed
- Uses standard Unix-style paths

### Windows
- Should work with minimal changes
- Ensure Chrome is in your PATH
- If using PowerShell or Command Prompt:
  ```bash
  pip3 install -r requirements.txt
  ```

### Linux
- Not currently tested
- Should work with Chrome/Chromium installed
- May need to adjust Chrome binary location

## Installation
1. Install Python dependencies:
   ```bash
   # Mac/Linux:
   pip install -r requirements.txt
   
   # Windows:
   pip3 install -r requirements.txt
   ```

2. Ensure Chrome/Chromium is installed on your system


## Author
FlyingCloudHealth

## License
[Your chosen license]