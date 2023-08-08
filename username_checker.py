import requests
import re

with open('usernames.txt', 'r') as file:
    usernames = [line.strip() for line in file]

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"

invalid_lines = 0
channels_lines = 0
groups_lines = 0
users_lines = 0

channels_file = open('channels.txt', 'w')
groups_file = open('groups.txt', 'w')
users_file = open('users.txt', 'w')
invalid_file = open('invalid.txt', 'w')

for username in usernames:
    user = 'https://t.me/' + username
    response = requests.get(user)
    content = response.text
    
    if re.search('tgme_page_photo_image', content):
        if re.search('subscribers', content):
            print(GREEN + '[+] @' + username + ' [channel]' + RESET)
            channels_file.write(username + '\n')
            channels_lines += 1
        elif re.search('members', content):
            print(GREEN + '[+] @' + username + ' [group]' + RESET)
            groups_file.write(username + '\n')
            groups_lines += 1
        else:
            print(GREEN +  '[+] @' + username + ' [user]' + RESET)
            users_file.write(username + '\n')
            users_lines += 1
    else:
        print(RED + '[-] @' + username + ' [invalid]'  + RESET)
        invalid_file.write(username + '\n')
        invalid_lines += 1

channels_file.close()
groups_file.close()
users_file.close()
invalid_file.close()

print(f"channels: {channels_lines}")
print(f"groups: {groups_lines}")
print(f"users: {users_lines}")
print(f"invalid: {invalid_lines}")
