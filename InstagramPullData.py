#!/usr/bin/env python3

# Imported packages
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 
import sys 
import csv

POST_LIMIT = 24 

def getAllInfo(accounts):
    def instaPageQuery(queryAccount, webdriverVar):

        # TODO Refactor Code
        # Used to convert numbers scraped from instagram page
        def convertInstaNum(number):
            if number.replace(',', '').isdigit():
                return int(number.replace(',', ''))
            else:
                multiplier = {'k':10**3,'m':10**6}
                number_split = number[:-1].split('.') 

                if len(number_split) < 2:
                    number_split.append(0)

                return (int(number_split[0]) * multiplier[number[-1]]) + int(number_split[1]) * (multiplier[number[-1]]/10)
                

        driver.get(f"https://www.instagram.com/{account['Account_tag']}/")
        elem = driver.find_elements_by_xpath("//span[@class='g47SY ']")

        queryAccount["posts"] = convertInstaNum(elem[0].text)
        queryAccount["followers"] = convertInstaNum(elem[1].text)
        queryAccount["following"] = convertInstaNum(elem[2].text)

        # TODO Refactor code to make more efficient and readable
        count = 1
        for row in range(1,(POST_LIMIT//3)+1):
            for column in range(1,4):
                elem = driver.find_element_by_xpath(f"//div[@class='Nnq7C weEfm'][{row}]/div[@class='v1Nh3 kIKUG  _bz0w'][{column}]")
                driver.execute_script(f"arguments[0].scrollIntoView();", elem)

                hover = ActionChains(driver).move_to_element(elem)
                hover.perform()
                queryAccount[f"Post{count}"] = convertInstaNum(driver.find_element_by_xpath("//li[@class='-V_eO'][1]/span[1]").text)

                count += 1

        return queryAccount

    with webdriver.Firefox() as driver:
        for account in accounts:
            account = instaPageQuery(account, driver) 

    return accounts

def populateCsv(accounts):
    with open('dataset.csv', 'w') as dataFile:
        # TODO Look for possible means to refactor code
        fieldNames = list(accounts[0].keys()) 
        csv_writer = csv.DictWriter(dataFile, fieldnames=fieldNames)

        csv_writer.writeheader()

        # TODO Refactor to make more efficient 
        for account in accounts:
            csv_writer.writerow(account)

def parseAccounts(filename):
    accounts = []

    # Retrieving each account name from 'filename'
    with open(filename, 'r') as f:
        accounts = [tuple(el.strip() for el in acc.split(':')) for acc in f.readlines()]

    return [{"ID": ID, "Account_tag": acc[0], "Account_type": acc[1]} for ID, acc in enumerate(accounts, 1)]

# Main
if __name__ == "__main__":
    filename = sys.argv[1]
    
    if filename[-4:] == ".txt":
        accounts = parseAccounts(filename)
        populateCsv(getAllInfo(accounts))
    else:
       raise Exception('Incorrect File Format')
