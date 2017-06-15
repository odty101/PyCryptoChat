class Settings(object):
    def __init__(self):
        # GUI Settings
        self.chat_line = '{time} - {user}: {message}'
        self.time_format = '%d %b %H:%M %Z'

        # Network Settings
        self.port = 8080


# Initialize the Settings
settings = Settings()
