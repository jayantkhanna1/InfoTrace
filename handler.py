# sherlock
# email spoof
# location from image
# Name search
# phone number lookup
# email lookup
# ip lookup
# domain lookup
# url lookup
# hash lookup
# social media lookup
# wifi cracking
# password cracking md5,sha256,sha512 etc.



import subprocess
name = input()
command="cd sherlock && python sherlock " +name+" --timeout 1"
print(command)
subprocess = subprocess.Popen(
    command ,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
)

subprocess_return = subprocess.stdout.read()
ans=str(subprocess_return).split('\\n')
for x in ans:
    print (x)