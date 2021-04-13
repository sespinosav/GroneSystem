import os
class KernelService():

    def turnOn(self):
        """
        Turn on all modules: GUI, Application and FilesManager
        """
        self.turnOnFilesManager()
        self.turnOnApplications()

    def turnOnApplications(self):
        os.system("cmd /c start /min initApplications.bat")
    
    def turnOnFilesManager(self):
        os.system("cmd /c start /min initFilesManager.bat")
