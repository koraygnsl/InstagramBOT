from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, username, password, followUser=0 ):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome("C:\\Users\\murat\\Desktop\\Çalışmalarım\\Programlama\\Exercises\\InstagramBOT\\chromedriver.exe", chrome_options=self.browserProfile)
        self.username = username
        self.password = password
        self.fUser = followUser
        self.browser.maximize_window()

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)

    def getFollewers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(3)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followersCount = len(dialog.find_elements_by_css_selector("li"))

        print(f"first count: {followersCount}")

        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(3)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followersCount != newCount:
                followersCount = newCount
                print(f"New count: {newCount}")
                time.sleep(3)
            else:
                continue
        
            followers = dialog.find_elements_by_css_selector("li")


            i = 0
            for user in followers:
                link = user.find_element_by_css_selector("a").get_attribute("href")
                followerList.append(link)
                i += 1
                if i == followersCount+1:
                    break

    with open("followers.txt", "w", encoding="UTF-8") as file:
        for item in followerList:
            file.write(item + "\n")

    def getFollowing(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(3)

        dialog = self.browser.find_element_by_xpath("/html/body/div[6]/div")
        followingCount = len(dialog.find_elements_by_css_selector("li"))

        print(f"First count: {followingCount}")

        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(3)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followingCount != newCount:
                followingCount = newCount
                print(f"New count: {followingCount}")
                time.sleep(3)
            else:
                break

            following = dialog.find_elements_by_css_selector("li")

            
            
        i = 0
        for user in following:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            followingList.append(link)
            i += 1
            if i == followingCount+1:
                break

        with open("following.txt", "w", encoding="UTF-8") as file:
            for item in followingList:
                file.write(item + "\n")

    def followUser(self, fUser):
        self.browser.get("http://www.instagram.com/"+ fUser)
        time.sleep(3)

        followButton = self.browser.find_element_by_tag_name("button")
        if followButton.text != "Following":
            followButton.click()
            time.sleep(3)
        else:
            print("Already following!")

    def unFollowUser(self):
        followers = open("followers.txt", "r")
        following = open("following.txt", "r")
        dontFollow = []

        for item in followers:
            if item not in following:
                dontFollow.append(item)
            else:
                continue
        time.sleep(3)

        for i in range(len(dontFollow)+1):
            self.browser.get("http://www.instagram.com/"+ i)
            time. sleep(2)

            unfButton = self.browser.find_element_by_tag_name("button")
            if unfButton.txt == "Following":
                unfButton.click()
                time.sleep(2)
                self.browser.find_element_by_xpath('//button[text()="Unfollow"]').clik()
            else:
                print("Already not following!")


print("**************WELCOME TO BEAR INSTAGRAM BOT******* \n****************************")
time.sleep(3)
username = input("ENTER YOUR USERNAME ")
password = input("ENTER YOUR PASSWORD ")
time.sleep(3)
print("***********************************")

choice = 1
followingList = [] 
followerList = []
while choice != 5:
    print("1. LOGIN ACCOUNT \n2. SEE FOLLOWING LIST \n3. SEE FOLLOWERS LIST \n4. FOLLOW A ACCOUNT \n5. UNFOLLOWING DON'T YOU FOLLOW \n6. EXIT")
    choice = int(input("ENTER YOUR COISE: "))
    if choice == 1:
        instagram = Instagram(username, password)
        instagram.signIn()
    elif choice == 2:
        instagram.getFollowing()
        following = open("following.txt", "r")
        for i in following:
            print(i)
    elif choice == 3:
        instagram.getFollewers()
        followers = open("followers.txt", "r")
        for a in followers:
            print(a)
    elif choice == 4:
        acc = input("ENTER ACCOUNT TO FOLLOW")
        instagram.followUser(acc)
        time.sleep(2)
        print(f"FOLLOWİNG {acc} NOW!")
    elif choice == 5:
        instagram.unFollowUser()
    elif choice == 6:
        print("PLEASE COME AGAIN")
        time.sleep(3)
        instagram.browser.close()
        break
    else:
        print("WRONG INPUT. ENTER THE CHOICE")
