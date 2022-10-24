from filetracker import get_emails

emails = get_emails()
single_emails = set(emails)
attendance_days_per_email = {}

for attended in single_emails:
    count = emails.count(attended)
    attendance_days_per_email[attended] = count













if __name__ == "__main__":
    for key, val in attendance_days_per_email.items():
        print(f"{key}\t{val}")