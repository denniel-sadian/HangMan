"""
An original design of Denniel Luis Saway Sadian
Date: July 16, 2017

Update your python to the latest version
"""

from tkinter import *
from tkinter import ttk, font, messagebox
from turtle import TK, RawTurtle, TurtleScreen


class HangMan(ttk.Notebook):

    def __init__(self, master, **kwargs):
        ttk.Notebook.__init__(self, master, **kwargs)
        self.root = master
        self.grid(column=0, row=0, sticky='NEWS', columnspan=4, rowspan=10)
        # pages
        self.p2 = ttk.Frame(self, relief='flat')
        self.p1 = ttk.Frame(self, relief='flat')
        self.add(self.p2, text="Start here!", padding=2)
        self.add(self.p1, text="Let's play!", padding=2)
        # fonts
        self.heading = font.Font(family='Chiller', size=35,
                                 weight='bold')
        self.text = font.Font(family='Segoe Print', size=12, weight='bold')
        # styles
        self.style = ttk.Style()
        self.style.configure('TNotebook', background='green')
        self.style.configure('TButton', font=self.text, width=5)
        self.style.configure('TLabel', background='lightgreen',
                             font=self.text)
        self.style.configure('TFrame', background='lightgreen')
        # canvas, screen & turtle
        self.c_ = TK.Canvas(self.p1, width=500, height=300, bg="#ddffff")
        self.s_ = TurtleScreen(self.c_)
        self.s_.bgcolor('lightgreen')
        self.t_ = RawTurtle(self.s_)
        self.t_.shape('turtle')
        # objects
        self.py = PhotoImage(file='py.png', width=50, height=50)
        self.guess = StringVar()
        self.hint = StringVar()
        self.hint1 = StringVar()
        self.guess1 = dict()
        self.good_word = []
        self.attempts = 0
        # buttons
        self._a = ttk.Button(self.p1, text='A', command=self.a)
        self._b = ttk.Button(self.p1, text='B', command=self.b)
        self._c = ttk.Button(self.p1, text='C', command=self.c)
        self._d = ttk.Button(self.p1, text='D', command=self.d)
        self._e = ttk.Button(self.p1, text='E', command=self.e)
        self._f = ttk.Button(self.p1, text='F', command=self.f)
        self._g = ttk.Button(self.p1, text='G', command=self.g)
        self._h = ttk.Button(self.p1, text='H', command=self.h)
        self._i = ttk.Button(self.p1, text='I', command=self.i)
        self._j = ttk.Button(self.p1, text='J', command=self.j)
        self._k = ttk.Button(self.p1, text='K', command=self.k)
        self._l = ttk.Button(self.p1, text='L', command=self.l)
        self._m = ttk.Button(self.p1, text='M', command=self.m)
        self._n = ttk.Button(self.p1, text='N', command=self.n)
        self._o = ttk.Button(self.p1, text='O', command=self.o)
        self._p = ttk.Button(self.p1, text='P', command=self.p)
        self._q = ttk.Button(self.p1, text='Q', command=self.q)
        self._r = ttk.Button(self.p1, text='R', command=self.r)
        self._s = ttk.Button(self.p1, text='S', command=self.s)
        self._t = ttk.Button(self.p1, text='T', command=self.t)
        self._u = ttk.Button(self.p1, text='U', command=self.u)
        self._v = ttk.Button(self.p1, text='V', command=self.v)
        self._w = ttk.Button(self.p1, text='W', command=self.w)
        self._x = ttk.Button(self.p1, text='X', command=self.x)
        self._y = ttk.Button(self.p1, text='Y', command=self.y)
        self._z = ttk.Button(self.p1, text='Z', command=self.z)
        self.buttons = [
            self._a, self._b, self._c, self._d, self._e,
            self._f, self._g, self._h, self._i, self._j,
            self._k, self._l, self._m, self._n, self._o,
            self._p, self._q, self._r, self._s, self._t,
            self._u, self._v, self._w, self._x, self._y,
            self._z
        ]
        self.disabled_buttons = []
        # geometry management
        for row in range(16):
            self.rowconfigure(row, weight=1)
            self.p1.rowconfigure(row, weight=1)
            self.p2.rowconfigure(row, weight=1)
        for col in range(13):
            self.columnconfigure(col, weight=1)
            self.p1.columnconfigure(col, weight=1)
            self.p2.columnconfigure(col, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.widgets()

    def process_guess(self):
        self.attempts = 0
        self.disabled_buttons = []
        self.t_.reset()
        if self.guess.get() and self.hint.get():
            self.guess1 = {}
            self.t_.reset()
            self.disable_buttons()
            self.hint1.set('Hint: ' + self.hint.get())
            self.hint.set('')
            for i in self.guess.get():
                self.good_word.append(
                    i.lower() in 'abcdefghijklmnopqrstuvwxyz ')
            if False not in self.good_word:
                self.t_.up()
                self.t_.setposition(-220, -120)
                for i in self.guess.get():
                    self.t_.pensize(3)
                    if i is ' ':
                        self.t_.up()
                        self.t_.fd(15)
                    else:
                        if i.upper() not in self.guess1:
                            self.guess1[i.upper()] = [self.t_.pos()]
                        else:
                            self.guess1[i.upper()].append(self.t_.pos())
                        self.t_.down()
                        self.t_.fd(10)
                        self.t_.up()
                        self.t_.fd(10)
                self.guess.set('')
            else:
                messagebox.showinfo('Information',
                                    'Words must only contain letters and spaces.')
                self.guess.set('')
                self.hint.set('')
                self.good_word = []
            # drawing the stand
            self.t_.up()
            self.t_.pensize(10)
            self.t_.setpos(-90, -70)
            self.t_.down()
            self.t_.fd(100)
            self.t_.lt(90)
            self.t_.fd(20)
            self.t_.lt(90)
            self.t_.fd(100)
            self.t_.lt(90)
            self.t_.fd(20)
            self.t_.lt(90)
            self.t_.fd(50)
            self.t_.up()
            self.t_.lt(90)
            self.t_.fd(20)
            self.t_.down()
            self.t_.fd(160)
            self.t_.rt(90)
            self.t_.fd(70)
            self.t_.rt(90)
            self.t_.fd(20)
            self.t_.setposition(30.00, 90.00)
            self.t_.pensize(10)
            self.t_.up()
            self.disable_buttons(False)
            self.t_.hideturtle()
        else:
            messagebox.showinfo('Information',
                                'Please fill-in the fields properly.')

    def draw(self):
        self.t_.pencolor('red')
        if len(self.guess1) is 0:
            # draws these if guessing was successful
            self.t_.setpos(50.00, 90.00)
            self.t_.pensize(5)
            self.t_.pencolor('blue')
            self.t_.lt(135)
            self.t_.down()
            self.t_.fd(20)
            self.t_.bk(20)
            self.t_.rt(45)
            self.t_.fd(100)
            self.t_.lt(90)
            self.t_.fd(50)
            self.t_.lt(90)
            self.t_.fd(85)
            self.t_.lt(90)
            self.t_.fd(34)
            self.t_.up()
            self.t_.lt(90)
            self.t_.fd(30)
            self.t_.lt(90)
            self.t_.fd(25)
            self.t_.down()
            self.t_.pencolor('green')
            self.t_.bk(20)
            self.t_.rt(90)
            self.t_.up()
            self.t_.fd(20)
            self.t_.lt(90)
            self.t_.down()
            self.t_.fd(20)
            self.t_.up()
            self.t_.bk(20)
            self.t_.rt(90)
            self.t_.fd(20)
            self.t_.rt(90)
            self.t_.down()
            self.t_.fd(8)
            self.t_.rt(90)
            self.t_.fd(60)
            self.t_.rt(90)
            self.t_.fd(8)
            self.t_.hideturtle()
            self.attempts = 0
            self.disabled_buttons = []
            messagebox.showinfo('You won', 'You survived! Good guessing.')
            self.hint1.set('')
            self.t_.reset()
        elif self.attempts is 0:
            self.disable_buttons(False)
        elif self.attempts is 1:
            self.t_.setpos(30.00, 90.00)
            self.t_.down()
            self.t_.pencolor('red')
            self.t_.rt(90)
            self.t_.circle(15)
            self.t_.up()
            self.t_.lt(90)
            self.t_.fd(30)
            self.t_.up()
            self.disable_buttons(False)
        elif self.attempts is 2:
            self.t_.setpos(30.00, 60.00)
            self.t_.down()
            self.t_.fd(50)
            self.t_.bk(40)
            self.t_.up()
            self.disable_buttons(False)
        elif self.attempts is 3:
            self.t_.setpos(30.00, 50.00)
            self.t_.down()
            self.t_.rt(45)
            self.t_.fd(20)
            self.t_.bk(20)
            self.t_.lt(45)
            self.t_.up()
            self.disable_buttons(False)
        elif self.attempts is 4:
            self.t_.setpos(30.00, 50.00)
            self.t_.down()
            self.t_.lt(45)
            self.t_.fd(20)
            self.t_.bk(20)
            self.t_.rt(45)
            self.t_.fd(40)
            self.t_.up()
            self.disable_buttons(False)
        elif self.attempts is 5:
            self.t_.setpos(30.00, 10.00)
            self.t_.down()
            self.t_.rt(35)
            self.t_.fd(25)
            self.t_.bk(25)
            self.t_.lt(35)
            self.t_.up()
            self.disable_buttons(False)
        elif self.attempts is 6:
            self.t_.setpos(30.00, 10.00)
            self.t_.down()
            self.t_.lt(35)
            self.t_.fd(25)
            self.t_.bk(25)
            self.t_.rt(35)
            self.t_.up()
            # game over dialog
            self.t_.setpos(50.00, 90.00)
            self.t_.pensize(5)
            self.t_.pencolor('blue')
            self.t_.lt(135)
            self.t_.down()
            self.t_.fd(20)
            self.t_.bk(20)
            self.t_.rt(45)
            self.t_.fd(100)
            self.t_.lt(90)
            self.t_.fd(50)
            self.t_.lt(90)
            self.t_.fd(85)
            self.t_.lt(90)
            self.t_.fd(34)
            self.t_.up()
            self.t_.lt(90)
            self.t_.fd(30)
            self.t_.lt(90)
            self.t_.fd(25)
            self.t_.down()
            self.t_.pencolor('green')
            self.t_.bk(20)
            self.t_.rt(90)
            self.t_.up()
            self.t_.fd(20)
            self.t_.lt(90)
            self.t_.down()
            self.t_.fd(20)
            self.t_.up()
            self.t_.bk(20)
            self.t_.rt(90)
            self.t_.fd(20)
            self.t_.rt(90)
            self.t_.fd(15)
            self.t_.lt(180)
            self.t_.down()
            self.t_.fd(8)
            self.t_.lt(90)
            self.t_.fd(60)
            self.t_.lt(90)
            self.t_.fd(8)
            self.t_.up()
            self.t_.pencolor('red')
            self.t_.left(90)
            for key, i in self.guess1.items():
                for x in i:
                    self.t_.setposition(i[i.index(x)][0], i[i.index(x)][1])
                    self.t_.write(key, align='Left', font=("Arial", 12,
                                                           "normal"))
            self.t_.hideturtle()
            if messagebox.askyesno('Game Over',
                                   'Hanged! NABITAY - hanged in '
                                   'Filipino\nPlay again?'):
                self.attempts = 0
                self.disabled_buttons = []
                self.t_.reset()
                self.hint1.set('')
            else:
                self.root.destroy()
        self.t_.pencolor('black')

    def disable_buttons(self, should=True):
        if should:
            for i in self.buttons:
                if i['text'] not in self.disabled_buttons:
                    i.state(['disabled'])
        else:
            for i in self.buttons:
                if i['text'] not in self.disabled_buttons:
                    i.state(['!disabled'])

    def master_key(self, char):
        self.disable_buttons()
        self.t_.showturtle()
        if char in self.guess1:
            for i in self.guess1[char]:
                self.t_.setposition(i[0], i[1])
                self.t_.write(char, align='Left',
                              font=("Arial", 12, "normal"))
            del self.guess1[char]
            self.t_.setposition(30.00, 90.00)
            self.draw()
        else:
            self.attempts += 1
            self.draw()
        self.t_.hideturtle()

    def a(self):
        self._a.state(['disabled'])
        self.disabled_buttons.append('A')
        self.master_key('A')

    def b(self):
        self._b.state(['disabled'])
        self.disabled_buttons.append('B')
        self.master_key('B')

    def c(self):
        self._c.state(['disabled'])
        self.disabled_buttons.append('C')
        self.master_key('C')

    def d(self):
        self._d.state(['disabled'])
        self.disabled_buttons.append('D')
        self.master_key('D')

    def e(self):
        self._e.state(['disabled'])
        self.disabled_buttons.append('E')
        self.master_key('E')

    def f(self):
        self._f.state(['disabled'])
        self.disabled_buttons.append('F')
        self.master_key('F')

    def g(self):
        self._g.state(['disabled'])
        self.disabled_buttons.append('G')
        self.master_key('G')

    def h(self):
        self._h.state(['disabled'])
        self.disabled_buttons.append('H')
        self.master_key('H')

    def i(self):
        self._i.state(['disabled'])
        self.disabled_buttons.append('I')
        self.master_key('I')

    def j(self):
        self._j.state(['disabled'])
        self.disabled_buttons.append('J')
        self.master_key('J')

    def k(self):
        self._k.state(['disabled'])
        self.disabled_buttons.append('K')
        self.master_key('K')

    def l(self):
        self._l.state(['disabled'])
        self.disabled_buttons.append('L')
        self.master_key('L')

    def m(self):
        self._m.state(['disabled'])
        self.disabled_buttons.append('M')
        self.master_key('M')

    def n(self):
        self._n.state(['disabled'])
        self.disabled_buttons.append('N')
        self.master_key('N')

    def o(self):
        self._o.state(['disabled'])
        self.disabled_buttons.append('O')
        self.master_key('O')

    def p(self):
        self._p.state(['disabled'])
        self.disabled_buttons.append('P')
        self.master_key('P')

    def q(self):
        self._q.state(['disabled'])
        self.disabled_buttons.append('Q')
        self.master_key('Q')

    def r(self):
        self._r.state(['disabled'])
        self.disabled_buttons.append('R')
        self.master_key('R')

    def s(self):
        self._s.state(['disabled'])
        self.disabled_buttons.append('S')
        self.master_key('S')

    def t(self):
        self._t.state(['disabled'])
        self.disabled_buttons.append('T')
        self.master_key('T')

    def u(self):
        self._u.state(['disabled'])
        self.disabled_buttons.append('U')
        self.master_key('U')

    def v(self):
        self._v.state(['disabled'])
        self.disabled_buttons.append('V')
        self.master_key('V')

    def w(self):
        self._w.state(['disabled'])
        self.disabled_buttons.append('W')
        self.master_key('W')

    def x(self):
        self._x.state(['disabled'])
        self.disabled_buttons.append('X')
        self.master_key('X')

    def y(self):
        self._y.state(['disabled'])
        self.disabled_buttons.append('Y')
        self.master_key('Y')

    def z(self):
        self._z.state(['disabled'])
        self.disabled_buttons.append('Z')
        self.master_key('Z')

    def widgets(self):
        # p1
        ttk.Label(self.p1, image=self.py).grid(column=0, row=0, sticky='NEWS',
                                               rowspan=2)
        ttk.Label(self.p1, text="Hang Man (X_X)",
                  font=self.heading).grid(column=1, row=0, columnspan=12)
        ttk.Label(self.p1, textvariable=self.hint1).grid(column=1,
                                                         row=1, columnspan=12)
        self.c_.grid(column=0, row=2, sticky="NEWS", columnspan=13,
                     rowspan=12)
        self._a.grid(column=0, row=14, sticky='NEWS')
        self._b.grid(column=1, row=14, sticky='NEWS')
        self._c.grid(column=2, row=14, sticky='NEWS')
        self._d.grid(column=3, row=14, sticky='NEWS')
        self._e.grid(column=4, row=14, sticky='NEWS')
        self._f.grid(column=5, row=14, sticky='NEWS')
        self._g.grid(column=6, row=14, sticky='NEWS')
        self._h.grid(column=7, row=14, sticky='NEWS')
        self._i.grid(column=8, row=14, sticky='NEWS')
        self._j.grid(column=9, row=14, sticky='NEWS')
        self._k.grid(column=10, row=14, sticky='NEWS')
        self._l.grid(column=11, row=14, sticky='NEWS')
        self._m.grid(column=12, row=14, sticky='NEWS')
        self._n.grid(column=0, row=15, sticky='NEWS')
        self._o.grid(column=1, row=15, sticky='NEWS')
        self._p.grid(column=2, row=15, sticky='NEWS')
        self._q.grid(column=3, row=15, sticky='NEWS')
        self._r.grid(column=4, row=15, sticky='NEWS')
        self._s.grid(column=5, row=15, sticky='NEWS')
        self._t.grid(column=6, row=15, sticky='NEWS')
        self._u.grid(column=7, row=15, sticky='NEWS')
        self._v.grid(column=8, row=15, sticky='NEWS')
        self._w.grid(column=9, row=15, sticky='NEWS')
        self._x.grid(column=10, row=15, sticky='NEWS')
        self._y.grid(column=11, row=15, sticky='NEWS')
        self._z.grid(column=12, row=15, sticky='NEWS')
        self.disable_buttons()
        # p2
        ttk.Label(self.p2, text='Create a Game (0_o)',
                  font=self.heading).grid(column=0, row=0, columnspan=13)
        ttk.Label(self.p2, text='Thing that you want them to guess').grid(
            column=3, row=2, columnspan=7)
        ttk.Entry(self.p2, textvariable=self.guess).grid(column=3, row=3,
                                                         columnspan=7,
                                                         sticky='NEWS')
        ttk.Label(self.p2, text='Hint').grid(column=3, row=4, columnspan=7,
                                             pady='20 0')
        ttk.Entry(self.p2, textvariable=self.hint).grid(column=3, row=5,
                                                        columnspan=7,
                                                        sticky='NEWS')
        ttk.Button(self.p2, text='Hang them up!',
                   command=self.process_guess).grid(column=3, row=6,
                                                    columnspan=7,
                                                    sticky='NEWS',
                                                    pady='20 0')
        ttk.Label(self.p2, text='About:').grid(column=3, row=8,
                                               columnspan=2, pady='20 0')
        ttk.Label(self.p2, text='This game was originally written by '
                                'Denniel Luis Saway Sadian. '
                                'July 16, 2017').grid(
            column=4, row=9, columnspan=5)


if __name__ == "__main__":
    root = Tk()
    game = HangMan(root, padding='3 5 3 3')
    root.title('Hang Man')
    root.mainloop()
