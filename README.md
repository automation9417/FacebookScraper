# Facebook Scraper
This is a sample to scrape Facebook posts using Clicknium.

## Preparation
- Python 3.7+
- Windows 7 SP1+
- Chrome browser
- VS Code
- [Clicknium](https://www.clicknium.com/documents#set-up-clicknium-visual-studio-code-extension) 
- [Clicknium Chrome extension](https://www.clicknium.com/documents/tutorial/extensions/chromeextension#install)

## Scrape Facebook posts
We will scrape the post of the Facebook company page as an example.

### Create a Python project
Create a Python file, for example, `sample.py`, under a project folder.  
Show `Locators` under the VS Code Explorer:  
![locators](/pic/project.png)  

### Capture locator
A locator is a tool that targets the UI elements.
1. Login and open the Facebook company page: https://www.facebook.com/facebook  
2. Click the `Capture` button in VS Code.    
   ![capture](/pic/capture.png)
3. Click [similar elements](https://www.clicknium.com/documents/tutorial/recorder/capture_similar_elements)      
   This feature lets you get all the posts on the page that have the same structure.     
   ![recorder](/pic/Recorder.png)  

- Use `Ctrl + Click` to capture the first post words on Facebook:  
![first element](/pic/elements1.png)  
- Capture the second post in the same way:  
![second elements](/pic/elements2.png)  
You will see there are five elements matched. Click the save button and finish. 

### Get the text via Locator:
To get the locator targets, we can use [find_element](https://www.clicknium.com/documents/references/python/globalfunctions/find_element) function. In our scenario, we need to get multiple posts so we can use [find_elements](https://www.clicknium.com/documents/references/python/globalfunctions/find_elements) function to get a result array. 
```python
UIs = cc.find_elements(locator.facebook.posts)
```
In the Python code, we can use `Locator.` to use the locators we captured using Clicknium in this project. If there is a need to use the same Locator across projects, you can make the locator store into a cloud locator store, and you can reference it anywhere.  
![cloud](/pic/cloudlocator.png)  
When we get the UI elements, we need to find an element property that can contain the text info. Check the [Web elements property](https://www.clicknium.com/documents/concepts/web#web-element-properties). The property `innertext` is what we need.  
```python
    uis = cc.find_elements(locator.facebook.posts)
    for ui in uis:
        text = ui.get_property("innertext")
```
we can print the text to check if it works or not.  
If it doesn't work, we need to check the locator page to tune the property. The Locator uses the identity UI elements.  
![locator](/pic/locator.png)
On the above page, you can do some quick validation and action to check if the Locator can work or not. And you can also select and modify which attribute you want to use to locate the UI elements. 

### Go to the next page
The Facebook content will be loaded when you scroll down the page. So if we capture once, we can't get all the information. So we have to capture each page. If we mimic the scroll action of the mouse, it would be hard to control. So the best choice would be to use the `PageDown` button in the keyboard. The [send_hotkey](https://www.clicknium.com/documents/references/python/uielement/send_hotkey) function can do it easily. we can find the `Code` for `PageDown` is `{PGDN}`.
```python
cc.send_hotkey("{PGDN}")
```
We can use a while loop the get all the posts. Since the multiple capture would get the same post for times, we can use a dictionary to store the post and use `ancestorid` as the key. 
## Source code
[GitHub](https://github.com/automation9417/FacebookScraper)







