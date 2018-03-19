
Setup
1) To run the code properly make sure you have Python3 installed.
    apt-get update
    apt-get install python3 python3-pip


2) run this below command

        pip3 install --upgrade pip
        pip3 install -r requirements.txt
OR
        pip3 install bs4


Running

        python linkExtractor.py
 Enter the link.
























Code basic blocks

file = open('testing.txt','r')
lines = f.readlines()
clean = [line.split('\n')[0] for line in lines]

string = ''
for line in clean:
    string = string+line+' '

# windows
os.system("echo {} | clip".format(string))

# linux (ubuntu)
apt-get install xclip
https://stackoverflow.com/questions/5130968/how-can-i-copy-the-output-of-a-command-directly-into-my-clipboard

~/.bashrc
alias clip='xclip -selection clipboard'
alias cpaste='xclip -selection clipboard -o'

Python command
os.system("echo {} | clip".format(string))




