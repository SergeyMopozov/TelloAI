'''
Created on Oct 7, 2020

@author: mrmopoz
'''

import socket
import time


# get respond from TelloAI
def command(command_statement, respond, logger, error_log):
    # set net params
    host = '0.0.0.0'
    tello_address = ('192.168.10.1', 8889)

    # Create a UDP socket for command send
    com_port = 9000
    com_addr = (host, com_port)

    sock_command = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_command.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_command.bind(com_addr)

    print('command socket start')
    bufsize = 1024

    # start main cycle
    while True:
        try:
            # if not empty get a message
            if command_statement:
                msg = command_statement.popleft()

                # TODO: process "end" msg

                # send msg
                msg = msg.encode(encoding="utf-8")
                _ = sock_command.sendto(msg, tello_address)
                print('Sent message: ' + str(msg))
                logger.info('Sent message: ' + str(msg))

                # get respond
                data, _ = sock_command.recvfrom(bufsize)
                resp = data.decode(encoding="utf-8")
                # print and log respond
                print('Respond: ' + str(resp))
                logger.info('Respond: ' + str(resp))
                # add respond to respond deque
                respond.append(resp)

            # if empty wait
            else:
                continue

        except Exception:
            # log exception (Exception)
            error_log.exception(Exception)
            sock_command.close()
            break
