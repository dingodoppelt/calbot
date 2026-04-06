## Configuration
Put a config file named `.env` in the same folder as `calbot-mail.py` folder containing the following keys:  


```
user =					# username
password = 				# password
url = 					# url of calendar, usually https://<domain>:5232/<user>/<calendar-hash>
allowed_sender = 		# mail address of allowed sender
target_filename = 		# filename to allow, all others discarded
```

## Installation and deployment
Copy this script and the `.env` file into a folder of your choice accessible to the user running your mailserver.
Forward incoming mail for a certain user to this script by ceating line like the following in `/etc/aliases` :  
```
$ cat /etc/aliases
# See man 5 aliases for format
postmaster:    root
# The next line forwards all mail received by "calbot" to calbot-mail.py.
# The user is virtual and doesn't need to exist in the system
calbot:        "|/etc/postfix/mailhooks/calbot-mail.py"
```

Incoming mail to the `calbot` account is now forwarded to and processed by calbot-mail.py to extract the attached .ics calendar file.
Curl is then invoked to send the calendar over an http request to radicale.
