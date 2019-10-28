#!/usr/bin/env python3

# Imported packages
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 
import sys 
import csv

POST_LIMIT = 24 

def getAllInfo(account):
    def instaPageQuery(accountName, val_dict, webdriverVar):
        # Used to convert numbers scraped from instagram page
        """
        def convertInstaNum(number):
            if number.isdigit():
                return int(number)
            else:
                
                return 0
        """
                

        driver.get(f"https://www.instagram.com/{accountName}/")
        elem = driver.find_elements_by_xpath("//span[@class='g47SY ']")

        val_dict["posts"] = elem[0].text 
        val_dict["followers"] = elem[1].text 
        val_dict["following"] = elem[2].text 

         
        for row in range(1,(POST_LIMIT//3)+1):
            for column in range(1,4):
                elem = driver.find_element_by_xpath(f"//div[@class='Nnq7C weEfm'][{row}]/div[@class='v1Nh3 kIKUG  _bz0w'][{column}]")
                driver.execute_script(f"arguments[0].scrollIntoView();", elem)

                hover = ActionChains(driver).move_to_element(elem)
                hover.perform()
                val_dict[f"Post{row*column}"] = driver.find_element_by_xpath("//li[@class='-V_eO'][1]/span[1]").text

        return val_dict

    with webdriver.Firefox() as driver:
        for key, value in account.items():
            value = instaPageQuery(key, value, driver) 


    return account

def populateCsv():
    pass

def parseAccounts(filename):
    accounts = []

    # Retrieving each account name from 'filename'
    with open(filename, 'r') as f:
        accounts = [tuple(el.strip() for el in acc.split(':')) for acc in f.readlines()]

    account_names = [acc[0] for acc in accounts]
    account_info = [{"Account_type": acc[1]} for acc in accounts]

    # 'Account Name' : {Dictionary with Account Informaiton}
    return dict(zip(account_names, account_info)) 

# Main
if __name__ == "__main__":
    filename = sys.argv[1]
    
    if filename[-4:] == ".txt":
        accounts = parseAccounts(filename)
        print(getAllInfo(accounts))
        #populateCsv(getAllInfo(accounts))
    else:
       raise Exception('Incorrect File Format')
