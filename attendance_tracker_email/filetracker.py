import os

email_list = []
def get_emails(dir):
    for files in os.listdir(dir):
        f= os.path.join(dir, files)
        if os.path.isfile(f):
            # print(f)
            with open(f, "r") as email_file:
                [email_list.append(line.strip("\n")) for line in email_file.readlines()]
    return email_list

