from time import sleep
from clicknium import clicknium as cc, locator

def scrapFacebookPosts():
    tab = cc.chrome.open("https://www.facebook.com/facebook")
    tab.wait_appear(locator.facebook.posts)
    postsText={} 
    while cc.is_existing(locator.facebook.posts):
        uis = cc.find_elements(locator.facebook.posts)
        for ui in uis:
            text = ui.get_property("innertext")
            id = ui.get_property("ancestorid")
            if id not in postsText:
                postsText[id]=text
                print(text)
                print("\n")
        ui.send_hotkey("{PGDN}")
        ui.send_hotkey("{PGDN}")
        sleep(1)


if __name__ == "__main__":
    scrapFacebookPosts()