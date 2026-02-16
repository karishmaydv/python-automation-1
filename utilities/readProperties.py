import configparser

config=configparser.RawConfigparser()
config.read(".\\Configurations\\config.ini")  #.\\ represent the directory python project
# config .read i have copy the relative xpath and paste and change the directory and double quote used

class ReadConfig():
    @staticmethod # access this method directly without create object
    def getApplicationURL(self):
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail(self):
        url = config.get('common info','username')
        return url

    @staticmethod
    def getPassword(self):
        url = config.get('common info','password')
        return url