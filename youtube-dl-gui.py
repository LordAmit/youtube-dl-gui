#!/usr/bin/python

# Youtube-dl-GUI provides a front-end GUI to youtube-dl
#    Copyright (C) 2013  Amit Seal Ami
#
#    Th== program == free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Th== program == distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with th== program.  If not, see {http://www.gnu.org/licenses/}.
#
from PySide.QtGui import QMessageBox
from PySide import QtGui
from ui.main_window import Ui_MainWindow
import sys
from os import system
from urllib2 import urlopen
from urllib2 import HTTPError

class MyApplication(QtGui.QMainWindow):
    format_selected = 35

    def __init__(self, parent=None):
        """Initializes"""
        QtGui.QMainWindow.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBoxFormats.activated[str].connect(self.combo_formats)
        self.ui.btnDownload.clicked.connect(self.download_button_pressed)

    def download_button_pressed(self):
        if self.ui.textEditDownload is not None:
            if self.check_url(self.ui.textEditDownload.toPlainText()):
                #subprocess.Popen(self.return_youtube_dl_cmd())
                system(self.return_youtube_dl_cmd())
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setText("Error in URL")
                msgBox.setInformativeText("Please check the URL you provided.")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()


    def check_url(self, url_tobe_checked):
        """
        @param url_tobe_checked:
        @return:
        """
        try:
            code = urlopen(url_tobe_checked).code
        except ValueError:
            return False
        except HTTPError:
            return False

        if (code / 100) >= 4:
            return False
        else:
            return True

    def return_youtube_dl_cmd(self):
        from os.path import expanduser
        home = expanduser("~")
        cmd = "gnome-terminal -e "
        cmd += '"youtube-dl -f{0} -c -o {1}/Downloads/%(title)s-%(id)s.%(ext)s {2}"'.format(
            self.format_selected,
            home,
            self.ui.textEditDownload.toPlainText()
        )
        return cmd

    def combo_formats(self, text):
        """
        checks the selected option
        @param text: the selected option's text
        """

        if text == 'H264 MP4 1080p':
            self.format_selected = 37
        if text == 'H264 MP4 720p':
            self.format_selected = 22
        if text == 'WebM 720p':
            self.format_selected = 45
        if text == 'WebM 480p':
            self.format_selected = 43
        if text == 'H264 MP4 480p':
            self.format_selected = 18
        if text == 'H264 FLV 480p':
            self.format_selected = 35
        if text == 'H264 FLV 360p':
            self.format_selected = 34
        if text == 'H263 240p':
            self.format_selected = 5
        if text == '3GP video':
            self.format_selected = 17


if __name__ == "__main__":
    APP = QtGui.QApplication(sys.argv)
    WINDOW = MyApplication()
    WINDOW.show()
    sys.exit(APP.exec_())