'''
Created on Oct 7, 2020

@author: mrmopoz
'''

import threading
from utils.log import setup_logger
from process.state import state
from process.video import video
from process.command import command
from brain.controller import controller
from collections import deque

if __name__ == '__main__':
    # 1. Set logs
    # logger for state
    state_logger = setup_logger('state_logger', './logs/tello_state.log')
    # logger for commands and responds from UAV
    command_logger = setup_logger('command_logger', './logs/tello_command.log')
    # logger for errors
    error_logger = setup_logger('error_logger', './logs/tello_error.log')
    # message for bot
    command_queue = deque()
    # respond from bot
    respond_queue = deque()

    # controller thread create
    controllerThread = threading.Thread(target=controller, args=(command_queue, respond_queue))
    controllerThread.start()
    # recvThread create
    recvThread = threading.Thread(target=command, args=(command_queue, respond_queue, command_logger, error_logger))
    recvThread.start()
    # create state Thread
    stateThread = threading.Thread(target=state, args=(state_logger, error_logger))
    stateThread.start()
    # videoThread create
    videoThread = threading.Thread(target=video, args=(command_logger, error_logger))
    videoThread.start()

    recvThread.join()
    controllerThread.join()
    stateThread.join()
    videoThread.join()
