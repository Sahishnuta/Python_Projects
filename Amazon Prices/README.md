## Problem Statement

**Amazon Price Tracker**

### Core Problem
Online shoppers face the challenge of monitoring price fluctuations on e-commerce platforms like Amazon. Products frequently change prices due to sales, demand, or competition, making it difficult for consumers to:
- Know when prices drop to their desired budget
- Avoid missing limited-time discounts
- Make informed purchasing decisions without constant manual checking

### Key Challenges Addressed
1. **Time-Consuming Manual Monitoring**: Manually checking product prices multiple times daily is inefficient and impractical
2. **Missed Opportunities**: Shoppers often miss price drops and end up paying more than necessary
3. **Lack of Price History**: No easy way to track price trends over time for informed decision-making
4. **Multiple Product Tracking**: Difficulty in monitoring several products simultaneously

### Solution Features
The Amazon Price Tracker automates the process by:
- **Automated Price Monitoring**: Regularly scraping product prices from Amazon
- **Price Drop Alerts**: Sending email notifications when prices fall below a user-defined threshold
- **Price History Tracking**: Maintaining historical price data to identify trends
- **User-Friendly Interface**: Simple command-line interface for easy product addition and management

### Technical Implementation
- **Web Scraping**: Uses BeautifulSoup to extract real-time price data from Amazon product pages
- **Email Automation**: Integrates with SMTP to send price drop alerts
- **Data Persistence**: Stores product URLs and target prices in a JSON file
- **Scheduled Monitoring**: Runs periodic checks to track price changes

### Target Users
- Budget-conscious shoppers
- Deal hunters waiting for specific price points
- People tracking multiple products for price optimization
- Anyone wanting to make informed purchasing decisions based on price trends

This tool essentially solves the problem of "price anxiety" and inefficient manual price monitoring for online shopping on Amazon.
