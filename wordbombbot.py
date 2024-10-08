from selenium import webdriver
from selenium.webdriver.common.by import By
import tkinter as tk
import random
import nltk
nltk.download('words')
from nltk.corpus import words
from selenium.webdriver.common.keys import Keys

global driver
global root

def wordWith(syllable):
    word_list = words.words()
    filtered_words = [word for word in word_list if syllable.lower() in word.lower()]
    sort=sorted(filtered_words,key=len)   
    shorts=sort[0:100]
    sample=random.sample(shorts,1)[0]
    return sample
def on_button_click():
    global driver
    iframes=driver.find_elements(By.TAG_NAME, "iframe")
    for iframe in iframes:
        if iframe.get_attribute('src')=="https://phoenix.jklm.fun/games/bombparty":
            driver.switch_to.frame(iframe)
            break
    syllableElement=driver.find_element(By.CLASS_NAME, "syllable")
    syllable=syllableElement.text
    word=wordWith(syllable)
    driver.switch_to.active_element.send_keys(word)
    driver.switch_to.active_element.send_keys(Keys.ENTER)

def start():
    global root
    global driver
    url=f"https://jklm.fun/{entry.get()}"
    root.destroy()
    driver=webdriver.Chrome()
    driver.get(url)

    root = tk.Tk()
    root.title("Wordbombbot")
    button = tk.Button(root, text="Enter Word", command=on_button_click)
    button.pack(pady=20)
    root.mainloop()

root = tk.Tk()
root.title("Wordbombbot")
label = tk.Label(root, text="WORD-BOMB BOT!")
label.grid(row=0, column=1)
label2 = tk.Label(root, text="Enter Your Game Code: ")
label2.grid(row=1, column=0)
label3=tk.Label(root,text="                                      ")
label3.grid(row=0, column=2)
entry = tk.Entry(root)
entry.grid(row=1, column=1)
button = tk.Button(root, text="Start Bot", command=start)
button.grid(row=2, column=1)
root.mainloop()
