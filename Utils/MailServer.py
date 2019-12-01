class MailServer(object):
    def __init__(self, email, to, subject):
      self.email = email
      self.to = to
      self.subject = subject

    def return_email_sender(self):
        infos_email = {
            'from': self.email,
            'to': self.to,
            'subject': self.subject,
        }

        return infos_email