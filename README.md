

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




