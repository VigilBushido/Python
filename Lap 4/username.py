#
#   Sergio Munguia
#
#   username.py    
#   
#   Generate user names based on first and last names
#   input: Please enter user's first name:
#          Please enter user's last name:
#
#   processing:1. extract the first character from the first name (first)
#              2. extract the first seven characters from the last name (last)
#              3. generate username:
#                       username = first + last
#              4. Display username
#
#   output: username based on first and last names

def main():
    # prompt user for first and last names
        first = input("Please enter user's first name: ")
        last = input("Please enter user's last name: ")
        
    # generate the username
        username = first[0] + last[0:7]
    # display user name
        print("Your user name is ", username)

main()
