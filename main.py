# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 17:03:55 2018

@author: tsattgast
"""

import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

USERNAME = ''
PASSWORD = ''

class InstaBot():
    def __init__(self, email, password):
        
        prefs = {"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096 }
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('prefs', prefs)
        self.browser = webdriver.Chrome('C:/Users/tsattgast/webdrivers/chromedriver.exe')
        self.email = email
        self.password = password
        
        
    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        wait = WebDriverWait(self.browser, 3.5)
        wait.until(lambda browser: browser.find_element_by_css_selector('form input'))
        email_input = self.browser.find_elements_by_css_selector("form input")[0]
        password_input = self.browser.find_elements_by_css_selector("form input")[1]
        email_input.send_keys(self.email)
        password_input.send_keys(self.password)
        #throwing random wait to prevent insta from detecting and banning us
        sleep_time = 3 * random.random()
        time.sleep(sleep_time)
        password_input.send_keys(Keys.ENTER)
        time.sleep(3 * random.random())
        
    def unfollowUser(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(1.5 * random.random())
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text == 'Following'):
            followButton.click()
            time.sleep(2 * random.random())
            confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
            confirmButton.click()
        else:
            print("You are not following this user")
        
        
    def followUser(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2 + random.random())
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text != 'Following'):
            followButton.click()
            time.sleep(2 + random.random())
        else:
            print("You are already following this user")
        
    def getUserFollowers(self, username, max):
        self.browser.get('https://www.instagram.com/' + username)
        followersLink = self.browser.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(3*random.random())
        followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    
        followersList.click()
        actionChain = webdriver.ActionChains(self.browser)
        while (numberOfFollowersInList < max):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)
        
        followers = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(userLink)
            followers.append(userLink)
            if (len(followers) == max):
                break
        return followers
    
    
#    def getUserFollowing(self, username, max):
#        self.browser.get('https://www.instagram.com/' + username)
#        followingLink = self.broswer.find_elements_by_css_selector('ul li a')[1]
#        followingLink.click()
#        time.sleep(2 + random.random())
        
        
        
        
    def get_followers(self):
        self.browser.get('https://www.instagram.com/accounts/access_tool/accounts_following_you')
        
        moreButton = self.browser.find_element_by_css_selector('button')
        self.browser.execute_script("return arguments[0].scrollIntoView();", moreButton)
        time.sleep(1 + random.random())
        

        #while (moreButton.is_displayed) and (moreButton.text =='View More'):
            
        try:
            while (moreButton.is_displayed) and (moreButton.text =='View More'):
                time.sleep(2 + random.random())
                moreButton.click()
        except:
            pass

        followersList = self.browser.find_elements_by_class_name('-utLf')
        
        return [element.text for element in followersList]
            
    
    def get_following(self):
        self.browser.get('https://www.instagram.com/accounts/access_tool/accounts_you_follow')
        
        moreButton = self.browser.find_element_by_css_selector('button')
        self.browser.execute_script("return arguments[0].scrollIntoView();", moreButton)
        time.sleep(1 + random.random())
        
        try:
            while (moreButton.is_displayed) and (moreButton.text =='View More'):
                time.sleep(2 + random.random())
                self.browser.execute_script("return arguments[0].scrollIntoView();", moreButton)
                moreButton.click()
        except:
            pass
    
        followingList = self.browser.find_elements_by_class_name('-utLf')
        #followingList =self.browser.find_elements_by_xpath(
        #        '//*[@id="react-root"]/section/main/div/article/main/section/div').text
        
        return [element.text for element in followingList]
    
        
    
    def closeBrowser(self):
        self.browser.close()


    def __exit__(self, exc_type, exc_value, traceback):
        self.closeBrowser()
        



my_bot = InstaBot(USERNAME, PASSWORD)
my_bot.signIn()

followers = my_bot.get_followers()
following = my_bot.get_following()



fuckers = list(set(following) - set(followers))
# insta catches on after a few automated drops and stops dropping after a few
#fuckers = fuckers[31:60]
#print(fuckers)




#for num, user in enumerate(fuckers):
#    my_bot.unfollowUser(user)
#    print('unfollowed {}. What a fucker! {} left'.format(user, len(fuckers)-num-1))
#    time.sleep(random.random())
    

my_bot.closeBrowser()


