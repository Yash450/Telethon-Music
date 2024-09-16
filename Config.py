import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "28744929"))
    API_HASH = os.environ.get("API_HASH", "cdb2b26dc41cdda251c34944eeaa6768")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6593823316:AAEIxxxekhmLxuhCmLgdd0Ag1IkRF5iCzzA)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOMcBu44y4NBo4ppZeKaF4SWzC0jRdUkdFIOJTlx3pZiH0VMsyBGPVqAc_VbQDfSiwCKULdKVsXEKkmon8yyFjMzxz9Hv6njClRTNP4GG_E9MkIyFF6dSMvb9F1xQ9puEmqfeF6tRwqwUx56cNEJi1WOUmPB4GsGfREWrhta2XLtCIhvB0IbMWkeo2_pxu-n94ntiVqzL6h-5tTJ6KkWPheWQ_YwfLAgnKh7hH-2QXC1zf15zcC_G5WXJRcc-3pwafryKrnprbmrxrTn37krB1WzepLB1ObJVI2RMhFilRy9m6hBCybBNCdmBSlLzwNoaO5dmK1Y42iJ9YFk7K_ymIZKF7k0=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@unite_musixbot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "@unite_assistant")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
