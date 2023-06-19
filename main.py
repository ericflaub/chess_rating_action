import berserk

from datetime import date, timedelta
import logging
import logging.handlers
import os


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

#account = knowledge.account()
try:
    token = os.environ["TOKEN"]
except KeyError:
    token = "Token not available!"
    logger.info("Token not available!")
    raise
#session = berserk.TokenSession(account.token)
session = berserk.TokenSession(token)
client = berserk.Client(session=session)
eric = client.account.get()
start_date = date.today() - timedelta(days=1)
end_date = date.today()
data = client.users.get_public_data('icererci')
blitz_rating = data['perfs']['blitz']['rating']







#if __name__ == "__main__":
    #logger.info(f"Token value: {SOME_SECRET}")

logger.info(f'Eric\'s blitz rating: {blitz_rating}')
#games = client.games.export_by_player('icererci', since=start_date, until=end_date)

