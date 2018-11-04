# bomb_feedback
Real explosions (kinda) for COMP40's bomb assignment

Basically keeps an eye on the bombstats webpage https://www.cs.tufts.edu/comp/40/bombstats.html for changes in defused phases and exploded bombs.
Plays a neat explosion or defuse sound effect when someone explodes/defuses bomb.

# running bomb_feedback
Requires Python 3 and virtualenv to run.
Activate virtualenv by running /bomb_env/Scripts/activate script, and run boom.py.

bombstats webpage requires a Tufts username and password, so you'll also have to substitute login_creds.username and login_creds.password for your own on line
```
auth = HTTPBasicAuth(login_creds.username, login_creds.password)
```

# running vocal_explosive.py
Want to explode a bomb but from a safe distance? Use voice control!
Voice activated bomb trigger device is out now!

Say "Ok, Google", wait for the que sound, and say "Explode bomb", and it explodes a bomb. How wonderful is that.

Same requirements as bomb_feedback; activate the virtualenv the same way.
Before it starts blowing things up it would prompt you to select your microphone.


