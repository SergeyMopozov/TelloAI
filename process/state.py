'''
Created on Oct 7, 2020

@author: mrmopoz
'''

import socket

# get state from TelloAI
def state(logger, error_log):
    
    host = '0.0.0.0'
    
    # Create a UDP socket for recive state
    state_port = 8890
    state_addr = (host,state_port)
    
    sock_state = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_state.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_state.bind(state_addr)
    
    bufsize = 1024

    while True:
        try:
            # get state string
            data, _ = sock_state.recvfrom(bufsize)
            # log state string
            state_string = data.decode(encoding="utf-8").replace('\n', ''.replace('\r' ,''))
            logger.info(state_string)
        except Exception:
            # log exception
            error_log.exception(Exception)
            sock_state.close()
            break