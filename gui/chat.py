from time import strftime

from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition

from app_logger import logger
from settings import settings

Window.size = (200, 130)


class IndividualChat(Screen):
    def send_message(self, message):

        # Update the Chat log and send the message if it contains any info
        if message:
            self.update_chat(message, self.manager.user)
        else:
            logger.info('Blank Message')

        # Clear the last sent message
        self.ids['message'].text = ''

        # Refocus to the message box
        self.ids['message'].focus = True

    def update_chat(self, message, user):
        # Get current Chat and Time
        current_chat = self.ids['chat_logs'].text
        current_time = strftime(settings.time_format)

        # Create the new chat line
        new_line = settings.chat_line.format(time=current_time, user=user, message=message)
        logger.info('Chat Line added: {}'.format(new_line))

        # Add the new line to chat
        new_chat = current_chat + '\n' + new_line
        self.ids['chat_logs'].text = new_chat

    def disconnect(self):
        logger.info('Disconnecting')


class Login(Screen):
    def connect(self, user, server):
        self.manager.user = user
        logger.info('Connecting to: {} as {}'.format(server, user))


class Manager(ScreenManager):

    user = StringProperty()
    individual_chat = ObjectProperty(None)


class ChatApp(App):
    def build(self):
        manager = Manager(transition=NoTransition())
        return manager


if __name__ == '__main__':
    ChatApp().run()