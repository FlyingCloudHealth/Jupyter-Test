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
- Required packages:
  - selenium
  - pandas
  - webdriver_manager


## Output
The script creates a CSV file containing:
- Meeting details
- Links to agendas
- Timestamps of data collection

## Author
FlyingCloudHealth

## License
[Your chosen license]