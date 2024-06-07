# -*- coding: utf-8 -*-
"""
Created on Sun May 26 10:57:01 2024

@author: Ali Aminu
A Program for scraping Job Post on Linkedin 
"""
#importing the required packages 
import requests
from bs4 import BeautifulSoup
import pandas as pd

# a function to extract web pages 
def get_page(page):
   headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
   
   url = f'https://www.linkedin.com/jobs/search/?&keywords=machine%20learning&location=New%20Zealand&start={page}'
   # Send a GET request to the URL
   req = requests.get(url, headers)
   
   sp = BeautifulSoup(req.content, 'html.parser')
   #print(soup)
   return sp

# a list to store job listing
job_list = []

# a function to transform extracted web pages
def transform_page(sp):
    job_listings = sp.find_all('li')
    #print(len(job_listings))
    for job in job_listings:
        divs = job.find_all('div', class_ ='base-card')
        for item in divs:
            try:
                title = item.find('h3', class_='base-search-card__title').text.strip()
            except: 
                time_posted = None
            try:
                job_Url = item.find('a', class_='base-card__full-link').get('href')
            except: 
                time_posted = None
            try:
                company = item.find('a', class_='hidden-nested-link').text.strip()
            except: 
                time_posted = None
            #print(company)
            company_Url = item.find('a',class_='hidden-nested-link').get('href')
            
            location = item.find('span', class_='job-search-card__location').text.strip()
            #print(location)
            try:
                time_posted = item.find('time', class_='job-search-card__listdate').text.strip()
            except: 
                time_posted = None
            
            #print(time_posted)
                     
            #creating a dictionary 
            job = {
             'Title':title,
             'Job_Url':job_Url,
             'Company':company,
            'Company_Url':company_Url,
            'Time_posted':time_posted, 
            'Location':location
                        }
            job_list.append(job)
    return

#loop through first n pages of Jobs on Linkedin
for i in range(0,50,25):
    #call the extract fuction
    print(f'Getting Page,{i}') 
    sp = get_page(i)
    #call the transform_page fuction
    transform_page(sp)
#print the job list
#print(job_list)

#adding job list to a pandas dataframe
jobs_df = pd.DataFrame(job_list)
#print(jobs_df)

#saving job_list to csv file
jobs_df.to_csv('ML_jobs_in_NewZealand2.csv',index = False)

