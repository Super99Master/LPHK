import os

def _checklib(lib):
    try:
        exec(f"import {lib}")
        return True
    except:
        return False

def _requestinstall(lib):
    if input(f"MI: {lib} not found in your pc.\nDo you want to install it?\n y(Yes) | n(No)\n>")=="y":
        os.system(f"pip install {lib}")
        if not _checklib(lib):
            return False
        else:
            return True
    return False

def _debug(val,msg):
    if val:
        print(msg)

def GetFunction(FDebug):
    files=[]
    FuncName={}
    FuncArgs={}
    for x in os.listdir("language_modules/"):
        if x[:2]!="__":
            files.append(x)
    for x in files:
        FMI=False
        FError=False
        FCustom=False
        with open(f"language_modules/{x}",'r') as f:
            y=f.readlines()
        i=0
        while True:
            k=y[i][:-1]
            if FMI:
                if k=="External_Libs":
                    i+=1
                    k=y[i][:-1]
                    while k[0]=="-":
                        k=k[2:]
                        _debug(FDebug,f"MI: Importing {k}")
                        if not(_checklib(k) or _requestinstall(k)):
                            _debug(FDebug,f"MI: Unable to install {k}")
                            FError=True
                            break
                        i+=1
                        k=y[i][:-1]
                    if FError:
                        break
                    else:
                        _debug(FDebug,"MI: External lib(s) checked and imported")
                        _debug(FDebug,f'MI: Executing "import language_modules.{x[:-3]}"')
                        exec(f"import language_modules.{x[:-3]}")
                elif k=="Args":
                    i+=1
                    k=y[i][:-1]
                    while k[0]=="-":
                        k=k[2:].split("=")
                        FuncArgs[k[0]]=k[1].split(",")
                        i+=1
                        k=y[i][:-1]
                    _debug(FDebug,f"MI: FuncArgs created with {len(FuncArgs)} entry")
                elif k=="Custom_Name":
                    i+=1
                    k=y[i][:-1]
                    while k[0]=="-":
                        k=k[2:].split("=")
                        _debug(FDebug,f'MI: Executing "FuncName["{k[1]}"]=language_modules.{x[:-3]}.{k[0]}"')
                        exec(f"FuncName[k[1]]=language_modules.{x[:-3]}.{k[0]}")
                        i+=1
                        k=y[i][:-1]
                    _debug(FDebug,f"MI: FuncName created with {len(FuncArgs)} entry")
                elif k=="MI_END":
                    break
                i-=1
            else:
                if k=="MI_START":
                    FMI=True
            i+=1
    return [FuncName,FuncArgs]

if __name__=='__main__':
    cfunction=GetFunction(True)
    print(len(cfunction[1][cfunction[0]['WEB'].__name__]))
    #cfunction[0]['WEB']('x','www.google.com')
                    



