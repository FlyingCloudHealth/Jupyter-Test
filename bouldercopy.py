#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install webdriver-manager')


# In[ ]:


def bouldercounty_scraper():
    """Scrape Boulder County meeting information from eScribe platform."""
    driver = None
    try:
        print("Starting Boulder County scraper...")
        
        # Initialize driver with options
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        wait = WebDriverWait(driver, 20)
        
        # Load the Boulder County meetings page
        print("Loading page...")
        driver.get("https://pub-bouldercounty.escribemeetings.com/?Year=2025&Expanded=Board%20of%20County%20Commissioners%20-%20Regular%20Meeting")
        
        time.sleep(5)  # Wait for JavaScript to render
        
        data = []
        crawl_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            # Find the past meetings region
            meetings_region = driver.find_element(By.CLASS_NAME, "past-meetings-region")
            print("Found past meetings region")
            
            # Find all meeting type lists
            meeting_lists = meetings_region.find_elements(By.CLASS_NAME, "MeetingTypeList")
            print(f"Found {len(meeting_lists)} meeting type lists")
            
            for meeting_list in meeting_lists:
                try:
                    # Find all meetings in this list
                    meetings = meeting_list.find_elements(By.CSS_SELECTOR, "div.Year0 > div")
                    print(f"Found {len(meetings)} meetings in list")
                    
                    for meeting in meetings:
                        try:
                            # Extract meeting details using relative selectors
                            title = meeting.find_element(By.CSS_SELECTOR, "div:nth-child(2) > div:nth-child(1) > h3 > a").text
                            title = title.split("Thursday")[0].strip()  # Clean up title
                            
                            date_time = meeting.find_element(By.CSS_SELECTOR, "div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)").text
                            location = meeting.find_element(By.CSS_SELECTOR, "div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)").text
                            
                            # Get meeting link
                            meeting_link = meeting.find_element(By.CSS_SELECTOR, "div:nth-child(2) > div:nth-child(1) > h3 > a").get_attribute('href')
                            
                            # Get HTML agenda link
                            try:
                                html_agenda = meeting.find_element(
                                    By.CSS_SELECTOR, 
                                    'a[aria-label*="HTML Agenda"]'
                                ).get_attribute('href')
                            except Exception as e:
                                print(f"Could not find HTML agenda link: {str(e)}")
                                html_agenda = ""

                            # Get PDF agenda link
                            try:
                                pdf_agenda = meeting.find_element(
                                    By.CSS_SELECTOR, 
                                    'a[aria-label*="PDF Agenda for Board of County Commissioners"]'
                                ).get_attribute('href')
                            except Exception as e:
                                print(f"Could not find PDF agenda link: {str(e)}")
                                pdf_agenda = ""
                            
                            meeting_data = {
                                "Title": title,
                                "Date": date_time,
                                "Location": location,
                                "Meeting Link": meeting_link,
                                "HTML_Agenda_Link": html_agenda,
                                "PDF_Agenda_Link": pdf_agenda,
                                "Agenda_contents": "",
                                "County": "Boulder",
                                "Crawl_Timestamp": crawl_timestamp
                            }
                            
                            data.append(meeting_data)
                            print(f"Successfully scraped meeting: {title}")
                            
                        except Exception as e:
                            print(f"Error scraping individual meeting: {str(e)}")
                            continue
                            
                except Exception as e:
                    print(f"Error processing meeting list: {str(e)}")
                    continue
            
            print(f"Total meetings scraped: {len(data)}")
            
        except Exception as e:
            print(f"Error finding meetings region: {str(e)}")
            print("\nPage source preview:")
            print(driver.page_source[:1000])
            
    except Exception as e:
        print(f"Boulder County scraper failed with error: {str(e)}")
        return False
        
    finally:
        if driver:
            driver.quit()
        
        if data:
            # Save to CSV
            df = pd.DataFrame(data)
            with open(filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["Title", "Date", "Location", 
                                                        "Meeting Link", "HTML_Agenda_Link", 
                                                        "PDF_Agenda_Link", "Agenda_contents", 
                                                        "County", "Crawl_Timestamp"])
                writer.writeheader()
                writer.writerows(data)
            print(f"Saved {len(data)} meetings to {filename}")
            return True
        return False


# In[ ]:


#run the scraper
success = bouldercounty_scraper()

