

import numpy as np

INIT_COMMANDS = ['command', 'streamon', 'takeoff']

END_COMMANDS = ['land', 'streamoff']

COMMANDS_LIST = ['up', 'down', 'left', 'right',
                 'forward', 'back', 'cw', 'ccw',
                 'go']

LINEAR_STEPS = np.arange(20, 500, 10)
ROTATE_STEPS = np.arange(1, 360, 1)


def get_rnd_command():

    com_w = COMMANDS_LIST[np.random.randint(len(COMMANDS_LIST))]
    if com_w in ['cw', 'ccw']:
        com_arg = np.random.randint(len(ROTATE_STEPS))

    else:
        com_arg = np.random.randint(len(LINEAR_STEPS))

    return com_w + ' ' + str(com_arg)



