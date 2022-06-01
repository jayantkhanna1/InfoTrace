import subprocess
class Sherlock_Module:
    def __init__(self):
        pass

    def findUser(self,name):
        import subprocess
        command="cd sherlock && python sherlock " +name + " --timeout 1"
        subprocess_output = subprocess.Popen(
            command ,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        lst=[]
        subprocess_return,subprocess_error = subprocess_output.communicate()
        subprocess_return = subprocess_return.decode()
        ans=str(subprocess_return).split('\\n')
        for x in ans:
            lst.append(x)
        for x in lst:
            x.replace('\\r', '')
        return lst
    
    def findUserTimeout(self,name,time):
        import subprocess
        command="cd sherlock && python sherlock " +name + " --timeout "+time
        subprocess_output = subprocess.Popen(
            command ,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        lst=[]
        subprocess_return,subprocess_error = subprocess_output.communicate()
        subprocess_return = subprocess_return.decode()
        ans=str(subprocess_return).split('\\n')
        for x in ans:
            lst.append(x)
        for x in lst:
            x.replace('\\r', '')
        return lst