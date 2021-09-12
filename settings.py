import os
import tokens
# The prefix that will be used to parse commands.
# It doesn't have to be a single character!
COMMAND_PREFIX = "!"

# The bot token. Keep this secret!
BOT_TOKEN = tokens.BOT_TOKEN

# The now playing game. Set this to anything false-y ("", None) to disable it
NOW_PLAYING = "Eating smoll kids."

# Base directory. Feel free to use it if you want.
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
