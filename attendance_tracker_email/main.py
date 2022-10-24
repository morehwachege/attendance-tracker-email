from filetracker import get_emails

def show_attended(dir=""):
    emails = get_emails(dir)
    single_emails = set(emails)
    attendance_days_per_email = {}
    for attended in single_emails:
        count = emails.count(attended)
        attendance_days_per_email[attended] = count

    return attendance_days_per_email