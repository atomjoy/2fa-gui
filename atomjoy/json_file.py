#!/usr/bin/python3

import os, sys, time, json, shutil, base64, pyotp

class JsonFile:
    data = []    
    filename = ""
    app_path = ""

    def __init__(self, file="secrets.json"):
        self.app_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.filename = file
        self.__loadJson()

    def getAppPath(self):
        return self.app_path
    
    def getData(self):
        return self.data

    def loadJson(self):
        try:            
            with open(os.path.join(self.app_path, self.filename), "r") as f:
                secrets = json.load(f) # tuples
                self.data = list(secrets.items()) # array
                print("Loaded", self.data)
        except (ImportError, Exception):
            print("Load json error")

    def addItem(self, name, secret):
        if len(name) >= 3:
            if len(secret) >= 16:
                if self.isBase32(secret):
                    self.removeItem(name)
                    item = tuple([name, secret])
                    self.data.append(item)                    
                    self.saveJson()                    
                else:
                    raise Exception("Invalid characters (base32 chars allowed)")
            else:
                raise Exception("Invalid secret length (16 min)")
        else:
            raise Exception("Invalid name length (3 min)")
        
    def saveJson(self):
        json_obj = {}
        for key, secret in self.data:
            json_obj[key] = secret
        try:
            self.backupFile()            
            with open(os.path.join(self.app_path, self.filename), "w") as outfile:
                json.dump(json_obj, outfile)           
        except (ImportError, Exception) as ex:
            print("Save json error", ex)

    def removeItem(self, name):
        if len(name) >= 1:
            res = [i for i in self.data if i[0] != name]
            self.data = res
            self.saveJson()

    def createDir(self, path):
        p = os.path.join(self.app_path, path)
        if not os.path.exists(p):
            os.makedirs(p)

    def backupFile(self):
        tm = str(time.time()).replace(".", "_")
        self.createDir("backup")
        shutil.copy(self.filename, "backup/secrets_" + tm + ".json")

    def isBase32(self, str):
        try:
            base64.b32decode(str)
            return True
        except Exception:
            print("Invalid base32:", str)
            return False
        
    def getRandomBase32(self):
        return pyotp.random_base32() # 16 chars: "JBSWY3DPEHPK3PXD"

    def removeItem(self, name):
        res = [i for i in self.data if i[0] != name]
        self.data = res
        self.saveJson()
    
    def getCodeArray(self):
        codes = []
        for tuple_val in self.data:
            item = list(tuple_val)
            item.append(JsonFile.createOtpCode(str(item[1])))
            codes.append(tuple(item))
        return codes

    @staticmethod
    def createOtpCode(secret):
        try:
            return pyotp.TOTP(secret).now()
        except Exception:
            print("Otp code error")
        return "INVALID_SECRET"

    __loadJson = loadJson  # private copy of original update() method    