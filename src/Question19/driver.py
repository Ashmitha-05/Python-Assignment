from util import filter_mail

n = int(input())

emails = []

for i in range(n):
    email = input()
    emails.append(email)

valid_emails = filter_mail(emails)

print(sorted(valid_emails))