"""
Computer Class
"""

import logging
import time


class Computer():
    """
    Computer Class
    """
    def __init__(self, status='OFF', volume=0) -> None:
        self.status = status
        self.volume = volume

    def __dir__(self):
        attributes = [attr for attr in dir(self.__class__) if not attr.startswith('__')]
        attributes.extend(self.__dict__)
        return attributes

    def __str__(self):
        return self.status

    def turn_on_computer(self) -> None:
        """
        Turns on the Computer
        :returns: None
        """
        if self.status == 'ON':
            print('Computer is already ON')
            return
        print('Computer turns ON')
        self.status='ON'

    def turn_off_computer(self) -> None:
        """
        Turns off the Computer
        :returns: None
        """
        if self.status == 'OFF':
            print('Computer is already OFF')
            return
        print('Computer turns OFF')
        self.status='OFF'

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

def configure_logging():
    """
    Logger
    """
    logging.basicConfig(
        filename='computer_history.log',
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
    computer = Computer()
    print(dir(computer))
    while True:
        time.sleep(2)
        print("""
TV App

1. Turn On Computer
2. Turn Off Computer
3. Volume Settings

press 'q' to exit
        """)

        option = input('Select the option: ')
        if option == 'q':
            logging.info('Terminating the program...')
            print('Terminating the program...')
            break
        elif option == '1':
            computer.turn_on_computer()
            logging.info('Turn On Computer')
        elif option == '2':
            computer.turn_off_computer()
            logging.info('Turn Off Computer')
        elif option == '3':
            computer.volume_settings()
            logging.info('Volume Settings')
        else:
            logging.error('Invalid input: %s', option)
            print('Invalid input. Please try again.')


if __name__ == "__main__":
    main()
