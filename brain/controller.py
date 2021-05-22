'''
Created on Oct 7, 2020

@author: mrmopoz
'''


from collections import deque
import presets

MISSION_COMPLETE = False
STEPS_LIMIT = 20


def controller(command, respond, fly_mode, program_path):
    
    print('Start controller')
    count = 0

    # command backlog
    command_queue = deque()
    presets.initialization(command_queue)
    if fly_mode == 'program':
        # load fly program
        presets.read_command_from_file(program_path, command_queue)
        presets.end_mission(command_queue)



    # main cycle
    while True:
        # first init command
        if count == 0:
            msg = command_queue.popleft()
            command.append(msg)
            count += 1

        # check tha we get respond, it is not empty
        if respond:
            resp = respond.popleft()
            # if it ok get next command
            if 'ok' in resp:
                # check command_queue not empty and get next command
                if command_queue:
                    msg = command_queue.popleft()
                    command.append(msg)
                    print(msg + ' put in queue')
                    count += 1
                else:
                    break

            # if respond error repeat last command
            if 'error' in resp:
                command.append(msg)
                print(msg + ' repeat put in queue')
            
        else:
            continue

