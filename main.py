import time
import os
from getpass import getpass
from selenium import webdriver
#dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)
class InstaBot:
    def __init__(self, username, pw):
        self.username = username
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.instagram.com/')
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw) #Hasta aca funciona
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
            .click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(),'Ahora no')]")\
            .click()
        time.sleep(2)
        #self.driver.quit()
    def get_unfollowers(self):
        self.driver.get('http://www.instagram.com/'+self.username)
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/followers')]".format(self.username))\
            .click()
        followers = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/following')]".format(self.username))\
            .click()
        following = self._get_names()
        unfollowers = [i for i in following if i not in followers]
        print(unfollowers)
    def _get_names(self):
        time.sleep(1)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(2)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text !='']
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        return names
    def exit(self):
        time.sleep(5)
        self.driver.quit()
Usuario = input("Usuario:")
Password = getpass("pw:")

bot = InstaBot(Usuario,Password)
bot.get_unfollowers()
bot.exit()
