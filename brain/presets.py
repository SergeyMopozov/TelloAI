

import numpy as np

INIT_COMMANDS = ('command', 'streamon', 'takeoff')

END_COMMANDS = ('land', 'streamoff')

COMMANDS_LIST = ('up', 'down', 'left', 'right',
                 'forward', 'back', 'cw', 'ccw',
                 'go')

LINEAR_STEPS = np.arange(20, 500, 10)
ROTATE_STEPS = np.arange(1, 360, 1)

SPEED = 20

READ_COMMANDS = ('speed?', 'battery?', 'time?')

def get_rnd_command():

    com_w = COMMANDS_LIST[np.random.randint(len(COMMANDS_LIST))]
    if com_w in ['cw', 'ccw']:
        com_arg = np.random.randint(len(ROTATE_STEPS))
        command = com_w + ' ' + str(com_arg)
    elif com_w == 'go':
        com_arg_x = np.random.randint(len(ROTATE_STEPS))
        com_arg_y = np.random.randint(len(ROTATE_STEPS))
        com_arg_z = np.random.randint(len(ROTATE_STEPS))
        command = com_w + ' ' + str(com_arg_x) + ' ' + str(com_arg_y) + ' ' + str(com_arg_z) + ' ' + str(SPEED)
    else:
        com_arg = np.random.randint(len(LINEAR_STEPS))
        command = com_w + ' ' + str(com_arg)

    return command

for i in range(10):
    print(get_rnd_command())

