import random
import smtplib
HR_EMAIL="ENTER HR EMAIL HERE"
PASSWORD="PASSWORD FOR TWO FACTOR WHEN USING GMAIL"
SMTP_ADDRESS="smtp.gmail.com CHANGE SMTP  TYPE BASED ON COMPANY EMAIL"
# Dictionary of employee names and email addresses
employees = {
  'Jennifer': 'Jenifer@example.com',
  'Jane': 'jane@example.com',
  'Bob': 'bob@example.com',
  'Sally': 'sally@example.com',
  'Mary': 'mary@example.com',
  'Mike': 'mike@example.com'
}

# Randomly assign each employee to another employee
gift_assignments = {}
for employee in employees:
  # Select a random employee to give a gift to
  gift_recipient = random.choice(list(employees.keys()))

  # Make sure the employee doesn't give a gift to themselves
  while gift_recipient == employee:
    gift_recipient = random.choice(list(employees.keys()))

  # Assign the gift recipient to the employee
  gift_assignments[employee] = gift_recipient

# Print the gift assignments
print('Gift assignments:')
for employee, recipient in gift_assignments.items():
  print(f'{employee} will give a gift to {recipient}')



# Send an email to each employee with their gift assignment
for employee, recipient in gift_assignments.items():
  recipient_email = employees[recipient]
  email = f'Dear {employee},\n\nYou have been assigned to give a gift to {recipient} ({recipient_email}) for the end-of-year gift exchange.\n\nBest regards,\nThe HR team'
  sender_email=employees[employee]
  with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
            connection.starttls()
            result = connection.login(HR_EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=HR_EMAIL,
                to_addrs=sender_email,
                msg=email
            )

