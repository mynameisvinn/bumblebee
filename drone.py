import sys, select, termios, tty
import time

moveBindings = {
        'i':100,
        'm':-100,
            }

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
        try:
            change = moveBindings[key]
        except:
            change = 0
            pass
    else:
        change = 0
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return change


if __name__=="__main__":
    
    SLEEP = .01
    THRUST = 1000
    print '>>> reading at %s hz', 1/SLEEP

    settings = termios.tcgetattr(sys.stdin)
    while(1):
        THRUST += getKey() 
        now = time.strftime("%H:%M", time.localtime(time.time()))
        print now, '>>> thrust:', THRUST
        time.sleep(SLEEP)