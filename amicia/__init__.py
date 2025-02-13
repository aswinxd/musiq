from amicia.core.bot import Anony
from amicia.core.dir import dirr
from amicia.core.git import git
from amicia.core.userbot import Userbot
from amicia.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Telegram = TeleAPI()
YouTube = YouTubeAPI()
Carbon = CarbonAPI()
