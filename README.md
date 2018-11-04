# bomb_feedback
Real explosions (kinda) for COMP40's bomb assignment

Basically keeps an eye on the bombstats webpage https://www.cs.tufts.edu/comp/40/bombstats.html for changes in defused phases and exploded bombs.
Plays a neat explosion or defuse sound effect when someone explodes/defuses bomb.

# running bomb_feedback
Requires Python 3 and virtualenv to run.
Activate virtualenv by running /bomb_env/Scripts/activate script, and run boom.py.

bombstats webpage requires a Tufts username and password, so you'll also have to substitute login_creds.username and login_creds.password for your own on line
'''
auth = HTTPBasicAuth(login_creds.username, login_creds.password)
'''
