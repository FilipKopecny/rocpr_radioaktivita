import RPi.GPIO as GPIO
import time as t
import easygraphics as g
geiger_pin = 15
pocet_cvaknuti = 0
x=2

def nakresli_ciary():
    g.set_line_width(1)
    g.set_color(g.Color.CYAN)
    g.set_line_style(g.LineStyle.DASH_LINE)
    g.draw_line(0,700,1600,700)
    g.draw_line(0,600,1600,600)
    g.draw_line(0,500,1600,500)
    g.draw_line(0,400,1600,400)
    g.draw_text(1570, 690, "10")
    g.draw_text(1570, 590, "20")
    g.draw_text(1570, 490, "30")
    g.draw_text(1460, 390, "DANGER ZONE")
    # znacka radioaktivity. Tri trojuholniky a cierny maly kruh uprostred
    g.set_color(g.Color.LIGHT_YELLOW)
    g.set_fill_color(g.Color.LIGHT_YELLOW)
    g.draw_pie(800, 60, 60, 120, 40, 40)
    g.draw_pie(800, 60, 180, 240, 40, 40)
    g.draw_pie(800, 60, 300, 360, 40, 40)
    g.set_color(g.Color.BLACK)
    g.set_fill_color(g.Color.BLACK)
    g.draw_circle(800, 60, 10)

def nastav_farbu(kolko_cvaknuti):
    g.set_color(g.Color.DARK_MAGENTA) 
    if (kolko_cvaknuti<40):
        g.set_color(g.Color.DARK_RED) 
    if (kolko_cvaknuti<30):
        g.set_color(g.Color.RED) 
    if (kolko_cvaknuti<20):
        g.set_color(g.Color.YELLOW)
    if (kolko_cvaknuti<10):
        g.set_color(g.Color.GREEN)

def geiger_cvakol(sender):
    global pocet_cvaknuti;
    global x
    nastav_farbu(pocet_cvaknuti/10)
    g.draw_line(x,800 - pocet_cvaknuti,x,790 - pocet_cvaknuti)    
    pocet_cvaknuti = pocet_cvaknuti + 10; 

def hlavny_program(): 
    global x
    global pocet_cvaknuti
    while True:
        pocet_cvaknuti=0
        t.sleep(5)
        x=x+4
           
def start():
    g.init_graph(1600, 800)
    g.clear_device()
    nakresli_ciary()
    g.set_line_width(5)
    g.set_line_style(g.LineStyle.SOLID_LINE)
    GPIO.add_event_detect(geiger_pin, GPIO.FALLING, callback=geiger_cvakol, bouncetime=5)
    hlavny_program()
    g.close_graph()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(geiger_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

g.easy_run(start)