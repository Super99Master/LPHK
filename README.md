# Base LPHK + AutoImporterFunction

Just added a ModuleImporter that import all function in language_modules folder.\
When importing a function it checks if the dependencies are in the pc and if they are not it will try to install it.\
If it fail, it will skip the file and will not implement function in that file.\
To disable MI prints change _debug in script.py from True to False.
## How: 
### To import custom function
```python
"""		
MI_START
External_Libs
- lib1(es. webbrowser)	
- lib2(es. os)	
Args
- [function name]=[coords,args1,args2]	
- (es. open_new=coords,link)	
Custom_Name
- [function_name]=[CustomName]	
- (es. open_new=WEB_NEW)	
MI_END	
"""
```
Add this code anywhere in the file.	

## Warning
To import a function in LPHK you need to create a **Custom_Name** for each function and LPHK will always give **coords** as first arg.
