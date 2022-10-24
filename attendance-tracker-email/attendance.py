from filetracker import get_emails

emails = get_emails()
single_emails = set(emails)
attendance_days_per_email = {}

def show_attended():
    for attended in single_emails:
        count = emails.count(attended)
        attendance_days_per_email[attended] = count
