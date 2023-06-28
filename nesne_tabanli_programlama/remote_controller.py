"""
RemoteController Module

This module defines the RemoteController class which represents a remote controller for a TV.

"""
import random
import time
import logging


class RemoteController():
    """
    RemoteController Class

    This class represents a remote controller for a TV.
    """
    def __init__(self, status='Off', volume=0,
                 channel_list=None, channel='National Geographic') -> None:
        if channel_list is None:
            self.channel_list = ['National Geographic']
        else:
            self.channel_list = channel_list
        self.status=status
        self.volume=volume
        self.channel=channel
        self.channel_history = []

    def turn_on_tv(self) -> None:
        """
        Turns on the TV.

        :returns: None
        """
        if self.status == 'On':
            print('TV is already on')
            return
        print('TV turns on')
        self.status='On'
        self.channel_history.append(self.channel)

    def turn_off_tv(self) -> None:
        """
        Turns off the TV.

        :returns: None
        """
        if self.status == "Off":
            print('TV is already off')
            return

        print('TV turns off')
        self.status="Off"

    def volume_settings(self) -> None:
        """
        Volume Settings

        :returns: None
        :rtype: None
        """
        while True:
            answer=input("""
    Turn down the TV volume: <
    Turn up the TV volume:   >
    Exit: q
            """)

            if answer == '<':
                if self.volume != 0:
                    self.volume -= 1
                    print(f"Volume: {self.volume}")
            elif answer == '>':
                if self.volume != 31:
                    self.volume += 1
                    print(f'Volume: {self.volume}')
            elif answer == 'q':
                print(f'Volume Updated: {self.volume}')
                break
            else:
                print('Invalid input. Please try again.')

    def add_channel(self, channel_name) -> None:
        """
        Add Channel

        :returns: None
        """
        print('Adding Channel...')
        time.sleep(1)
        self.channel_list.append(channel_name)
        print('Added Channel')

    def random_channel(self):
        """
        Set a random channel.

        :returns: None
        """
        rand=random.randint(0, len(self.channel_list)-1)
        self.channel=self.channel_list[rand]
        print(f'The current channel is: {self.channel}')
        self.channel_history.append(self.channel)

    def get_channel_history(self):
        """
        Channel History

        :return: list
        """
        return self.channel_history

    def __len__(self) -> int:
        """
        Learn the number of channels

        :return: int
        """
        return len(self.channel_list)

    def __str__(self) -> str:

        return f"""
    TV status: {self.status}
    TV Volume: {self.volume}
    Current Channel: {self.channel_list}
        """

def configure_logging():
    """
    Logger
    """
    logging.basicConfig(
        filename='remote_controller.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.getLogger()
    #logger.addHandler(logging.StreamHandler())
def main():
    """
    Def main
    """

    configure_logging()

    remote_controller = RemoteController()

    print("""
    TV App

    1. Turn On TV
    2. Turn Off TV
    3. Volume Settings
    4. Add Channel
    5. Learn the number of channels
    6. Random channel switch
    7. TV Settings
    8. Channel History

    press 'q' to exit
    """)

    while True:
        option = input('Select the option: ')

        if option == 'q':
            logging.info('Terminating the program...')
            print('Terminating the program...')
            break
        elif option == '1':
            remote_controller.turn_on_tv()
            logging.info('Turn On TV')
        elif option == '2':
            remote_controller.turn_off_tv()
            logging.info('Turn Off TV')
        elif option == '3':
            remote_controller.volume_settings()
            logging.info('Volume Settings')
        elif option == '4':
            channel_names = input('Enter channel names separated by ,: ')
            channel_list = channel_names.split(',')
            for additional in channel_list:
                remote_controller.add_channel(additional)
            logging.info('Add Channel: %s',channel_names)
        elif option == '5':
            num_channels = len(remote_controller)
            logging.info('Number of channels: %d', num_channels)
            # print(f'Number of channels: {num_channels}')
        elif option == '6':
            remote_controller.random_channel()
            logging.info('Switched to a random channel')
        elif option == '7':
            logging.info('TV settings:\n%s', remote_controller)
            print(remote_controller)
        elif option == '8':
            channel_history = remote_controller.get_channel_history()
            print('Channel History:')
            i = 1
            for channel in channel_history:
                print(str(i) + " - " + channel)
                i += 1
        else:
            logging.error('Invalid input: %s', option)
            print('Invalid input. Please try again.')


if __name__ == '__main__':
    main()
