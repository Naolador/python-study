import os

def find_active(all_users):
    print (all_users)


def load_files(all, suspend):
    try:
        with open(all, 'r') as file1:
            all_users = file1.readline().strip()
            return all_users

"""
    try:
        with open(suspend, "r") as file2:
            suspended_users = file2.readline().strip()
    return all_users, suspended_users
"""

print(load_files("all.txt"))