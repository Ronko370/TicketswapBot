import logging
import time
import util
from bot import Bot

# google-chrome --remote-debugging-port=9042 --user-data-dir="/home/koldaniel/temp"


def main():
    logging.basicConfig(format="%(levelname)s: %(asctime)s - %(message)s",
                        datefmt="%I:%M:%S", level=logging.INFO)
    logging.info("Starting bot")

    settings = util.get_settings()
    ticket = settings['ticket']
    notification = settings['notification']
    logging.info("Retrieved data from json file")

    bot = Bot(ticket["magicLink"].strip())
    logging.info("Initialized a bot instance")

    time.sleep(1)

    bot.jump_to_ticket_page()

    time.sleep(1)
    bot.login()

    time.sleep(2)
    logging.info("Starting to look for available tickets...")
    timer=0.3 # ms
    counter=0
    limit=60/timer
    while bot.find_available() is False:
        #logging.warning("No tickets found, trying again...")
        counter+=1
        time.sleep(timer)
        if counter > limit:
           # time.sleep(30)
            counter=0
            logging.warning("Refreshing page")
            while bot.refresher() is False:
                time.sleep(30)
                logging.error("Page broken after refreshing")

    logging.info("Ticket(s) found!")

    logging.info("Reserving ticket")
    bot.reserve_ticket()

    logging.info("Ticket reserved")

    logging.info("Waiting for checkout completion")
    time.sleep(900) # 15 minutes of buffer time to complete checkout

    logging.info("Closing bot")
    bot.quit()


if __name__ == "__main__":
    main()
