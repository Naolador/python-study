text = '''export MYSQL_VERSION=8.0
export MYSQL_DB=wshop'''

with open('mysql.env', 'w') as file:
    file.write(text)

text2 = '''
export MYSQL_TABLE=users
export MYSQL_USER=micky'''
with open('mysql.env', 'a') as file:
    file.write(text2)