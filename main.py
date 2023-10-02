import random

from  PyQt5.QtWidgets import  *
from PyQt5 import  QtCore,QtGui
from PyQt5.QtGui import  *
from  PyQt5.QtCore import  *
import sys

from PyQt5.uic.properties import QtWidgets


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe Game")
        self.setGeometry(100, 100, 392, 420)
        self.create_menu()
        self.UiComponents()
        self.click_counter = 0
        self.turn = 0
        self.twoplayersmode_status =True
        self.oneplayermode_status = False
        # self.two_players_mode()
        self.one_player_mode()
        self.btn_list = [self.push_list[0][0], self.push_list[0][1], self.push_list[0][2],
                               self.push_list[1][0], self.push_list[1][1], self.push_list[1][2],
                               self.push_list[2][0], self.push_list[2][1], self.push_list[2][2],]
        self.show()


    def create_menu(self):
        self.menubar = self.menuBar()
        button_action = QAction( "One player", self)
        button_action.triggered.connect(lambda : [self.reset_game(),self.one_player_mode()])

        button_action2 = QAction("Two players", self)
        button_action2.triggered.connect(lambda : [self.reset_game(), self.two_players_mode()])

        actionFile = self.menubar.addMenu("Choose player")
        actionFile.addAction( button_action)
        actionFile.addAction(button_action2)
    def UiComponents(self):
        self.turn = 0
        self.times = 0
        self.push_list = []
        for _ in range(3):
            temp = []
            for _ in range(3):
                temp.append((QPushButton(self)))
            self.push_list.append(temp)
        x=130
        y=130
        for i in range(3):
            for j in range(3):
                self.push_list[i][j].setGeometry(x * i ,
                                                                 y * j  + 30,
                                                                  130,130)

                self.push_list[i][j].setFont(QFont(QFont('Times', 55)))
                self.push_list[i][j].clicked.connect(self.action_called)
                self.push_list[i][j].setStyleSheet('''
                                QPushButton:disabled{
                                    color: #000000;
                                }
                            ''')
    def reset_game(self):
        self.turn = 0
        self.click_counter = 0
        for buttons in self.push_list:
            for button in buttons:
                button.setEnabled(True)
                button.setText('')
    def two_players_mode(self):
        # self.menubar.setTitle('Two Players ')
        self.oneplayermode_status = False
        self.twoplayersmode_status = True
        self.check_winner()

    def one_player_mode(self):
        self.oneplayermode_status = True
        self.twoplayersmode_status = False
        def show_move(next_move):
            next_move.setStyleSheet('''
                                                                    QPushButton{
                                                                        color: blue;
                                                                    }
                                                                ''')
            next_move.setText('o')
            self.turn = 0
            next_move.setEnabled(False)
            self.click_counter += 1

        def win_move():
            if (self.push_list[0][0].text() == 'o') and (self.push_list[0][1].text() == 'o') and (self.push_list[0][2].isEnabled() == True):
                next_move = self.push_list[0][2]
            elif (self.push_list[0][0].text() == 'o') and (self.push_list[0][2].text() == 'o') and (self.push_list[0][1].isEnabled() == True):
                next_move = self.push_list[0][1]
            elif (self.push_list[0][1].text() == 'o') and (self.push_list[0][2].text() == 'o') and (self.push_list[0][0].isEnabled() == True):
                next_move = self.push_list[0][0]

            if (self.push_list[2][0].text() == 'o') and (self.push_list[2][1].text() == 'o') and (self.push_list[2][2].isEnabled() == True):
                next_move = self.push_list[2][2]
            elif (self.push_list[2][0].text() == 'o') and (self.push_list[2][2].text() == 'o') and (self.push_list[2][1].isEnabled() == True):
                next_move = self.push_list[2][1]
            elif (self.push_list[2][1].text() == 'o') and (self.push_list[2][2].text() == 'o') and (self.push_list[2][0].isEnabled() == True):
                next_move = self.push_list[2][0]

            if (self.push_list[0][0].text() == 'o') and (self.push_list[1][0].text() == 'o') and (self.push_list[2][0].isEnabled() == True):
                next_move = self.push_list[2][0]
            elif (self.push_list[0][0].text() == 'o') and (self.push_list[2][0].text() == 'o') and (self.push_list[1][0].isEnabled() == True):
                next_move = self.push_list[1][0]
            elif (self.push_list[1][0].text() == 'o') and (self.push_list[2][0].text() == 'o') and (self.push_list[0][0].isEnabled() == True):
                next_move = self.push_list[0][0]

            if (self.push_list[0][2].text() == 'o') and (self.push_list[1][2].text() == 'o') and (self.push_list[2][2].isEnabled() == True):
                next_move = self.push_list[2][2]
            elif (self.push_list[0][2].text() == 'o') and (self.push_list[2][2].text() == 'o') and (self.push_list[1][2].isEnabled() == True):
                next_move = self.push_list[1][2]
            elif (self.push_list[1][2].text() == 'o') and (self.push_list[2][2].text() == 'o') and (self.push_list[0][2].isEnabled() == True):
                next_move = self.push_list[0][2]

            # first oblique (1,5,9)
            if (self.push_list[0][0].text() == 'o') and (self.push_list[1][1].text() == 'o') and (self.push_list[2][2].isEnabled() == True):
                next_move = self.push_list[2][2]
            elif (self.push_list[0][0].text() == 'o') and (self.push_list[2][2].text() == 'o') and (self.push_list[1][1].isEnabled() == True):
                next_move = self.push_list[1][1]
            elif (self.push_list[1][1].text() == 'o') and (self.push_list[2][2].text() == 'o') and (self.push_list[0][0].isEnabled() == True):
                next_move = self.push_list[0][0]

            # second oblique (3,5,7)
            if (self.push_list[0][2].text() == 'o') and (self.push_list[1][1].text() == 'o') and (self.push_list[2][0].isEnabled() == True):
                next_move = self.push_list[2][0]
            elif (self.push_list[0][2].text() == 'o') and (self.push_list[2][0].text() == 'o') and (self.push_list[1][1].isEnabled() == True):
                next_move = self.push_list[1][1]
            elif (self.push_list[1][1].text() == 'o') and (self.push_list[2][0].text() == 'o') and (self.push_list[0][2].isEnabled() == True):
                next_move = self.push_list[0][2]

            else:
                return  False

            show_move(next_move)

        def prevent():
            #First row
            if (self.push_list[0][0].text() == 'x') and (self.push_list[0][1].text() == 'x') and (self.push_list[0][2].isEnabled() == True):
                next_move = self.push_list[0][2]
            elif (self.push_list[0][0].text() == 'x') and (self.push_list[0][2].text() == 'x') and (self.push_list[0][1].isEnabled() == True):
                next_move = self.push_list[0][1]
            elif (self.push_list[0][1].text() == 'x') and (self.push_list[0][2].text() == 'x') and (self.push_list[0][0].isEnabled() == True):
                next_move = self.push_list[0][0]

            # second row
            elif (self.push_list[1][0].text() == 'x') and (self.push_list[1][1].text() == 'x') and (
                    self.push_list[1][2].isEnabled() == True):
                next_move = self.push_list[1][2]
            elif (self.push_list[1][0].text() == 'x') and (self.push_list[1][2].text() == 'x') and (
                    self.push_list[1][1].isEnabled() == True):
                next_move = self.push_list[1][1]
            elif (self.push_list[1][1].text() == 'x') and (self.push_list[1][2].text() == 'x') and (
                    self.push_list[1][0].isEnabled() == True):
                next_move = self.push_list[1][0]
            # Third row
            elif (self.push_list[2][0].text() == 'x') and (self.push_list[2][1].text() == 'x') and (
                    self.push_list[2][2].isEnabled() == True):
                next_move = self.push_list[2][2]
            elif (self.push_list[2][0].text() == 'x') and (self.push_list[2][2].text() == 'x') and (
                    self.push_list[2][1].isEnabled() == True):
                next_move = self.push_list[2][1]
            elif (self.push_list[2][1].text() == 'x') and (self.push_list[2][2].text() == 'x') and (
                    self.push_list[2][0].isEnabled() == True):
                next_move = self.push_list[2][0]

            # First column
            elif (self.push_list[0][0].text() == 'x') and (self.push_list[1][0].text() == 'x') and (
                    self.push_list[2][0].isEnabled() == True):
                next_move = self.push_list[2][0]
            elif (self.push_list[0][0].text() == 'x') and (self.push_list[2][0].text() == 'x') and (
                    self.push_list[1][0].isEnabled() == True):
                next_move = self.push_list[1][0]
            elif (self.push_list[1][0].text() == 'x') and (self.push_list[2][0].text() == 'x') and (
                    self.push_list[0][0].isEnabled() == True):
                next_move = self.push_list[0][0]
            #Second column
            elif (self.push_list[0][1].text() == 'x') and (self.push_list[1][1].text() == 'x') and (
                    self.push_list[2][1].isEnabled() == True):
                next_move = self.push_list[2][1]
            elif (self.push_list[0][1].text() == 'x') and (self.push_list[2][1].text() == 'x') and (
                    self.push_list[1][1].isEnabled() == True):
                next_move = self.push_list[1][1]
            elif (self.push_list[1][1].text() == 'x') and (self.push_list[2][1].text() == 'x') and (
                    self.push_list[0][1].isEnabled() == True):
                next_move = self.push_list[0][1]
                # Third column
            elif (self.push_list[0][2].text() == 'x') and (self.push_list[1][2].text() == 'x') and (
                    self.push_list[2][2].isEnabled() == True):
                next_move = self.push_list[2][2]
            elif (self.push_list[0][2].text() == 'x') and (self.push_list[2][2].text() == 'x') and (
                    self.push_list[1][2].isEnabled() == True):
                next_move = self.push_list[1][2]
            elif (self.push_list[1][2].text() == 'x') and (self.push_list[2][2].text() == 'x') and (
                    self.push_list[0][2].isEnabled() == True):
                next_move = self.push_list[0][2]

            # First oblique
            elif (self.push_list[0][0].text() == 'x') and (self.push_list[1][1].text() == 'x') and (
                    self.push_list[2][2].isEnabled() == True):
                next_move = self.push_list[2][2]
            elif (self.push_list[0][0].text() == 'x') and (self.push_list[2][2].text() == 'x') and (
                    self.push_list[1][1].isEnabled() == True):
                next_move = self.push_list[1][1]
            elif (self.push_list[1][1].text() == 'x') and (self.push_list[2][2].text() == 'x') and (
                    self.push_list[0][0].isEnabled() == True):
                next_move = self.push_list[0][0]
            # Second oblique
            elif (self.push_list[0][2].text() == 'x') and (self.push_list[1][1].text() == 'x') and (
                    self.push_list[2][0].isEnabled() == True):
                next_move = self.push_list[2][0]
            elif (self.push_list[0][0].text() == 'x') and (self.push_list[2][0].text() == 'x') and (
                    self.push_list[1][1].isEnabled() == True):
                next_move = self.push_list[1][1]
            elif (self.push_list[1][1].text() == 'x') and (self.push_list[2][0].text() == 'x') and (
                    self.push_list[0][2].isEnabled() == True):
                next_move = self.push_list[0][2]
            else:
                return  True

            show_move(next_move)

        if self.click_counter % 2 != 0:
            if self.click_counter == 1:
                for i in range(len(self.btn_list)):
                    next_move = random.choice(self.btn_list)
                    if next_move.isEnabled() == False:
                        break
                    break
                show_move(next_move)
            elif self.click_counter == 3:
                if prevent() == True:
                    if (self.push_list[0][0].text() == 'o'):
                        if (self.push_list[0][1].isEnabled() == True) and ( self.push_list[0][2].isEnabled() == True):
                            next_move = self.push_list[0][2]
                        elif (self.push_list[1][0].isEnabled() == True) and ( self.push_list[2][0].isEnabled() == True):
                            next_move = self.push_list[2][0]
                        elif (self.push_list[1][1].isEnabled() == True) and ( self.push_list[2][2].isEnabled() == True):
                            next_move = self.push_list[1][1]

                    elif (self.push_list[0][2].text() == 'o'):
                        if (self.push_list[0][1].isEnabled() == True) and ( self.push_list[0][0].isEnabled() == True):
                            next_move = self.push_list[0][0]
                        elif (self.push_list[1][2].isEnabled() == True) and ( self.push_list[2][0].isEnabled() == True):
                            next_move = self.push_list[2][2]
                        elif (self.push_list[1][1].isEnabled() == True) and ( self.push_list[2][0].isEnabled() == True):
                            next_move = self.push_list[1][1]

                    elif (self.push_list[2][0].text() == 'o'):
                        if (self.push_list[0][0].isEnabled() == True) and ( self.push_list[1][0].isEnabled() == True):
                            next_move = self.push_list[0][0]
                        elif (self.push_list[2][1].isEnabled() == True) and ( self.push_list[2][2].isEnabled() == True):
                            next_move = self.push_list[2][2]
                        elif (self.push_list[1][1].isEnabled() == True) and ( self.push_list[0][2].isEnabled() == True):
                            next_move = self.push_list[1][1]

                    elif (self.push_list[2][2].text() == 'o'):
                        if (self.push_list[2][0].isEnabled() == True) and ( self.push_list[2][1].isEnabled() == True):
                            next_move = self.push_list[2][0]
                        elif (self.push_list[0][2].isEnabled() == True) and ( self.push_list[1][2].isEnabled() == True):
                            next_move = self.push_list[0][2]
                        elif (self.push_list[1][1].isEnabled() == True) and ( self.push_list[0][0].isEnabled() == True):
                            next_move = self.push_list[1][1]

                    show_move(next_move)

            elif self.click_counter == 5:
                if win_move() == False:
                    if prevent() == True:
                        # First row
                        if (self.push_list[0][0].text() == 'o') and (self.push_list[0][1].isEnabled() == True) and (
                                self.push_list[0][2].isEnabled() == True):
                            next_move = self.push_list[0][2]
                        elif (self.push_list[0][0].text() == 'o') and (self.push_list[2][0].isEnabled() == True) and (
                                self.push_list[1][0].isEnabled() == True):
                            next_move = self.push_list[2][0]
                        elif (self.push_list[0][0].text() == 'o') and (self.push_list[1][1].isEnabled() == True) and (
                                self.push_list[2][2].isEnabled() == True):
                            next_move = self.push_list[1][1]


                        elif (self.push_list[0][2].text() == 'o') and (self.push_list[0][1].isEnabled() == True) and (
                                self.push_list[0][0].isEnabled() == True):
                            next_move = self.push_list[0][0]
                        elif (self.push_list[0][2].text() == 'o') and (
                                self.push_list[2][2].isEnabled() == True) and (
                                self.push_list[1][2].isEnabled() == True):
                            next_move = self.push_list[2][2]
                        elif (self.push_list[0][2].text() == 'o') and (
                                self.push_list[1][1].isEnabled() == True) and (
                                self.push_list[2][0].isEnabled() == True):
                            next_move = self.push_list[1][1]

                        elif (self.push_list[2][0].text() == 'o') and (self.push_list[0][0].isEnabled() == True) and (
                                self.push_list[1][0].isEnabled() == True):
                            next_move = self.push_list[0][0]
                        elif (self.push_list[2][0].text() == 'o') and (
                                self.push_list[2][1].isEnabled() == True) and (
                                self.push_list[2][2].isEnabled() == True):
                            next_move = self.push_list[2][2]
                        elif (self.push_list[2][0].text() == 'o') and (
                                self.push_list[1][1].isEnabled() == True) and (
                                self.push_list[0][2].isEnabled() == True):
                            next_move = self.push_list[1][1]

                        elif (self.push_list[2][2].text() == 'o') and (self.push_list[2][0].isEnabled() == True) and (
                                self.push_list[2][1].isEnabled() == True):
                            next_move = self.push_list[2][0]
                        elif (self.push_list[2][2].text() == 'o') and (
                                self.push_list[1][2].isEnabled() == True) and (
                                self.push_list[0][2].isEnabled() == True):
                            next_move = self.push_list[0][2]
                        elif (self.push_list[2][2].text() == 'o') and (
                                self.push_list[1][1].isEnabled() == True) and (
                                self.push_list[0][0].isEnabled() == True):
                            next_move = self.push_list[1][1]
                        # Center
                        elif (self.push_list[1][1].text() == 'o') and (self.push_list[0][1].isEnabled() == True) and (
                                self.push_list[2][1].isEnabled() == True):
                            if (self.push_list[0][0].text() == 'o') or (self.push_list[0][3].text() == 'o'):
                                next_move = self.push_list[0][1]
                            elif (self.push_list[2][0].text() == 'o') or (self.push_list[2][2].text() == 'o'):
                                next_move = self.push_list[2][1]

                        elif (self.push_list[1][1].text() == 'o') and (self.push_list[1][0].isEnabled() == True) and (
                                self.push_list[1][2].isEnabled() == True):
                            if (self.push_list[0][0].text() == 'o') or (self.push_list[2][0].text() == 'o'):
                                next_move = self.push_list[1][0]
                            elif (self.push_list[0][2].text() == 'o') or (self.push_list[2][2].text() == 'o'):
                                next_move = self.push_list[1][2]

                        elif (self.push_list[1][1].text() == 'o') and (self.push_list[0][0].isEnabled() == True) and (
                                self.push_list[2][2].isEnabled() == True):
                            if (self.push_list[1][0].text() == 'o') or (self.push_list[2][0].text() == 'o') or (self.push_list[0][1].text() == 'o') or (self.push_list[0][2].text() == 'o'):
                                next_move = self.push_list[0][0]
                            elif (self.push_list[2][1].text() == 'o') and (self.push_list[2][0].text() == 'o') or (self.push_list[0][2].text() == 'o') and (self.push_list[1][2].text() == 'o'):
                                next_move = self.push_list[2][2]

                        elif (self.push_list[1][1].text() == 'o') and (self.push_list[0][2].isEnabled() == True) and (
                                self.push_list[2][0].isEnabled() == True):
                            if (self.push_list[1][2].text() == 'o') or (self.push_list[2][2].text() == 'o') or (self.push_list[0][0].text() == 'o') or (self.push_list[0][1].text() == 'o'):
                                next_move = self.push_list[0][2]
                            elif (self.push_list[2][1].text() == 'o') and (self.push_list[2][2].text() == 'o') or (self.push_list[1][0].text() == 'o') and (self.push_list[0][0].text() == 'o'):
                                next_move = self.push_list[2][0]
                        # middle (2)
                        elif (self.push_list[0][1].text() == 'o') and (self.push_list[0][0].isEnabled() == True) and (
                                self.push_list[0][2].isEnabled() == True):
                            next_move = random.choice([self.push_list[0][0], self.push_list[0][2]])
                        # middle (4)
                        elif (self.push_list[1][0].text() == 'o') and (self.push_list[0][0].isEnabled() == True) and (
                                self.push_list[2][0].isEnabled() == True):
                            next_move = random.choice([self.push_list[0][0], self.push_list[2][0]])

                        # middle (6)
                        elif (self.push_list[1][2].text() == 'o') and (self.push_list[0][2].isEnabled() == True) and (
                                     self.push_list[2][2].isEnabled() == True):
                            next_move = random.choice([self.push_list[0][2], self.push_list[2][2]])

                        # middle (8)
                        elif (self.push_list[1][2].text() == 'o') and (
                                    self.push_list[2][0].isEnabled() == True) and (
                                     self.push_list[2][2].isEnabled() == True):
                            next_move = random.choice([self.push_list[2][0], self.push_list[2][2]])

                        else:
                            next_move = self.push_list[0][0]
                            while next_move.isEnabled() == False:
                                next_move = random.choice(self.btn_list)
                        show_move(next_move)

                self.check_winner()

            elif self.click_counter == 7:
                self.check_winner()
                if self.click_counter == 7:
                    if win_move() == False:
                        if prevent() == False:
                            next_move = self.push_list[0][0]
                            while next_move.isEnabled() == False:
                                next_move = random.choice(self.btn_list)

                self.check_winner()
            elif self.click_counter == 9:
                self.check_winner()

    def action_called(self):

        self.click_counter += 1
        button = self.sender()
        if self.click_counter % 2 == 0:
            self.turn = 0
            button.setText('o')
            button.setStyleSheet('''
                                                        QPushButton{
                                                            color: blue;
                                                        }
                                                    ''')
        else:
            self.turn = 1
            button.setText('x')
            button.setStyleSheet('''
                                            QPushButton{
                                                color: red;
                                            }
                                        ''')
        button.setEnabled(False)

        if self.twoplayersmode_status == True:
            self.two_players_mode()
        elif self.oneplayermode_status == True:
            self.one_player_mode()

    def check_winner(self):
        def show_winner(winner):
            msg = QMessageBox()
            msg.setWindowTitle('YOU WON!')
            msg.setIcon(QMessageBox.Information)
            text =''

            if winner == True:
                if self.turn == 0:
                    text = ' player O Won'
                else:
                    text = ' player x Won'
                msg.setText(text)
                x = msg.exec_()
                for buttons in self.push_list:
                    for button in buttons:
                        button.setEnabled(False)
                self.reset_game()

            elif self.click_counter == 9:
                text = "Match is Draw"
                msg.setText(text)
                x = msg.exec_()
                self.reset_game()




        for i in range(3):
            if self.push_list[0][i].text() == self.push_list[1][i].text() \
                and self.push_list[0][i].text() == self.push_list[2][i].text() \
                and self.push_list[0][i].text() != '':
                show_winner(True)

        for i in range(3):
            if self.push_list[i][0].text() == self.push_list[i][1].text() \
                and self.push_list[i][0].text() == self.push_list[i][2].text() \
                and self.push_list[i][0].text() != '':
                show_winner(True)

        if self.push_list[0][0].text() == self.push_list[1][1].text() \
                and self.push_list[0][0].text() == self.push_list[2][2].text() \
                and self.push_list[0][0].text() != '':
                show_winner(True)

        if self.push_list[0][2].text() == self.push_list[1][1].text() \
                and self.push_list[0][2].text() == self.push_list[2][0].text() \
                and self.push_list[0][2].text() != '':
                show_winner(True)
        show_winner(False)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())


