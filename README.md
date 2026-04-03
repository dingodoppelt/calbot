## Configuration
Put a config file named `.env` in the root folder containing the following keys:  


```
user =					# username
password = 				# password
url = 					# url of calendar, usually https://<domain>:5232/<user>/<calendar-hash>
allowed_sender = 		# mail address of allowed sender
target_filename = 		# filename to allow, all others discarded
```

## Installation and deployment
Copy this script in a folder of your choice accessible to the user running your mailserver.
To forward incoming mail to this script simply put a user you want to receive the email and forward it to this script like so:  
```
$ cat /etc/aliases
# See man 5 aliases for format
postmaster:    root
calbot:        "|/etc/postfix/mailhooks/calbot-mail.py"
```

Incoming mail to this account is now forwarded to and processed by calbot-mail.py to extract the attached .ics calendar file.
Curl is then invoked to send the calendar over an http request to radicale.
