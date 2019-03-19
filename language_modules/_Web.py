"""
MI_START
External_Libs
- webbrowser
- os
Args
- open=coords,link
- open_new=coords,link
Custom_Name
- open=WEB
- open_new=WEB_NEW
MI_END
"""

import webbrowser

def open(coords,link):
    if "http" not in link:
        link = "http://" + link
    print(f"[scripts] {link}    Open website {link} in default browser, try to make a new window")
    webbrowser.open_new(link)
    
def open_new(coords,link):
    if "http" not in link:
        link = "http://" + link
    print(f"[scripts] {link}    Open website {link} in default browser, try to make a new window")
    webbrowser.open_new(link)
