import sys
import asyncio
# Puppeteer functions.
from webcrawler import login_pixiv, create_post_pixiv, login_twitter, create_post_twitter

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

def application_startup(app, window):
    window.setWindowTitle("Musketeere")
    window.setStyleSheet(open("css/main.css").read())
    window.setGeometry(300, 300, 300, 220)
    window.move(60, 15)
    window.show()
    sys.exit(app.exec_())


def gui_elements(window):
    helloMsg = QLabel("<body><h1>Hello</h1></body>", parent=window)
    helloMsg.move(60, 15)


def main():
    # Passing in variables as parameters here is ok i think?
    # Surely its better than global variables as you know where they are.
    app = QApplication(sys.argv)
    window = QWidget()
    # minor
    gui_elements(window)
    # major
    application_startup(app, window)


if __name__ == "__main__":
    # this but using buttons.
    asyncio.get_event_loop().run_until_complete(create_post_twitter())
    asyncio.get_event_loop().run_until_complete(login_twitter())
    main()
