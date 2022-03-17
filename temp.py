import os

'''
IDEA: write logfiles for each use to a /home/user/.logs/key-press.log dir

- if dir or file does not exist, create them first
'''

if __name__ == "__main__":
    # print(os.environ["HOME"])
    # print(os.getlogin())
    print(os.path.isdir("/home/{}/.logs".format(os.getlogin())))
    if not os.path.isdir("/home/{}/.logs".format(os.getlogin())):
        os.mkdir("/home/{}/.logs".format(os.getlogin()))
    # os.mkdir("/home/.logs")
    print(os.path.isfile("/home/{}/.logs/key-press.log".foramt(os.getlogin())))
    if not os.path.isfile("/home/{}/.logs/key-press.log".format(os.getlogin())):
    open("/home/{}/.logs/key-press.log".format(os.getlogin()), mode='x')
