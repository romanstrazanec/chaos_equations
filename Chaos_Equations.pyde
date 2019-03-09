from Equation import Equation

eqs = {
"DPPREG": Equation(-.02, 500, 1e-5, lambda x, y, t: -x*x+x*t+y, lambda x, y, t: x*x-y*y-t*t-x*y+y*t-x+y),
"RMCQDI": Equation(-.26, 500, 1e-6, lambda x, y, t: x*x-y*y-t*t-x-t, lambda x, y, t: y*y+t*t-x*y-y-t),
"LDNMGQ": Equation(.108, 200, 1e-7, lambda x, y, t: -t*t-x*y+t, lambda x, y, t: -x*y+x*t+y+t),
"JJPVDN": Equation(-.45, 500, 1e-7, lambda x, y, t: -y*y-x*t+y, lambda x, y, t: x*x-x*y+t),
"HELPME": Equation(-.18, 100, 1e-5, lambda x, y, t: -x*x+y*y+t*t-x*y+y*t-t, lambda x, y, t: y*y-x+t),
"I_CNJJ": Equation(.09, 1000, 1e-5, lambda x, y, t: -y*y-t*t-x*y-x*t-y*t-x-t, lambda x, y, t: t*t-x*t-y),
"VJQZJG": Equation(-.05, 100, 1e-5, lambda x, y, t: x*x-x*t+y+t, lambda x, y, t: x*x+y*y+t*t-x*t-x+y),
"VKDI_J": Equation(.37, 100, 1e-4, lambda x, y, t: x*x-x*t+y*t-x, lambda x, y, t: -y*y-t*t-x*y-x*t-y*t-y),
"RANDOM": Equation(-1., 100, 1e-4, lambda x, y, t: x+y*t, lambda x, y, t: x-y*t)
}

k = "RANDOM"
speed = eqs[k].i

def setup():
    # fullScreen()
    size(1000, 1000)
    colorMode(HSB)
    eqs[k].create()
    # eqs[k].set_start_time(-.115)
    
def draw():
    background(0)

    eqs[k].i = map(mouseX, 0, width, speed*.01, speed*100)
    eqs[k].update()
    eqs[k].show_change()
    eqs[k].show_pattern()
    print(eqs[k].t, len(eqs[k].xs))
    
