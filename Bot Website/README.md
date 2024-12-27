README

Overview

This Python script is a comprehensive automation tool that combines Selenium, Tor, and various other libraries to perform tasks such as web browsing, IP switching, location detection, and human-like interaction with websites. The script aims to mimic human behavior, randomize actions, and ensure privacy using the Tor network.

Features

Tor Integration:

Routes web traffic through the Tor network for anonymity.

Dynamically switches IP addresses using the Tor controller.

Web Automation with Selenium:

Automates web browsing, including scrolling, clicking, and interacting with website elements.

Simulates human-like mouse movements and typing.

Geolocation and IP Detection:

Retrieves the current IP address and fetches geolocation details.

Human-like Behavior:

Randomized user-agent selection.

Simulated mouse movements, typing, and browsing behavior.

Time Zone Handling:

Retrieves and formats local time based on specified time zones.

Determines if the current time falls within typical waking hours.

Prerequisites

Python: Ensure Python 3.6 or higher is installed.

Tor: Install and configure the Tor network on your system. Ensure the Tor ControlPort (9051) is enabled and a password is set.

Selenium: Install the Selenium library (pip install selenium).

Additional Libraries:

pip install undetected-chromedriver pyautogui pytz fake-useragent requests beautifulsoup4 stem

Setup

Configure Tor Password:

Set your Tor ControlPort password in the switch_tor_ip function:

controller.authenticate(password='YOUR_PASSWORD')

Install Geckodriver:

Download and install the Geckodriver for Firefox from Mozilla's website.

Ensure the executable is in your system's PATH.

Usage

Main Functions

Switch Tor IP:

Call switch_tor_ip() to change the current IP address through Tor.

Get Current IP:

Use get_current_ip() to retrieve the current IP address.

Retrieve Location Details:

Call get_location(ip) to get the country, region, city, and timezone for a given IP address.

Simulate Human-like Web Browsing:

Use visit_website(driver) to automate web interactions, including scrolling and clicking.

Check Waking Hours:

Use is_waking_time(timezone) to determine if the current time in a specified timezone falls within typical waking hours.

Example Workflow

from selenium import webdriver

def main():
    driver = create_driver_with_tor()
    switch_tor_ip()

    current_ip = get_current_ip()
    print(f"Current IP: {current_ip}")

    location = get_location(current_ip)
    if location:
        print(f"Location: Country={location[0]}, Region={location[1]}, City={location[2]}, Timezone={location[3]}")

    visit_website(driver)
    driver.quit()

if __name__ == "__main__":
    main()

Notes

Ensure the Tor service is running before executing the script.

Configure the Selenium driver to match your preferred browser and proxy settings.

The script may require fine-tuning depending on specific website structures and user requirements.

Disclaimer

This script is intended for educational and ethical purposes only. Ensure compliance with local laws and website terms of service before using this script. Misuse of this tool for malicious purposes is strictly prohibited.
