#El capitulo que trata de Heteroscedasticidad de Gujarin es el 11
from manimlib.imports import *
import os
import numpy as np
import pyclbr
from sklearn.linear_model import LinearRegression
from math import cos, sin, pi
from random import randrange
import pandas as pd

class Supuestos(GraphScene):
    CONFIG = {
        "x_min": -15,
        "x_max": 70,
        "y_min": -15,
        "y_max": 70,
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 10,
        "x_axis_width": 7,
        "y_axis_height": 6,
        "axes_color" : GRAY, 
    }
    ymean = 0

    def construct(self):
        tx1 = TextMobject('Pero...')
        tx2 = TextMobject('¿Que es la covarianza $Cov(X,Y)$?')
        tx2.next_to(tx1, DOWN*2)
        self.play(Write(tx1))
        self.wait(0.2)
        self.play(Write(tx2))
        self.wait(2)
        self.play(FadeOut(tx1),FadeOut(tx2))
        tx1 = TextMobject('$Cov(X, Y)=E[(X-E(X))*(Y-E(Y))]$')
        tx1.shift(UP*3)
        tx1.shift(LEFT*2)
        
        self.graph_origin = 3 * DOWN + 5 * LEFT
        self.setup_axes(animate=True)
        self.play(Write(tx1))
        self.wait(2)
        points = []

        xs = [11  ,23  ,34  ,42, 33, 46,11 ]
        ys = [3   ,25  ,34  ,39 ,22, 11, 46 ]
        xs_less_x = []
        ys_less_x = []
        xs_more_x = []
        ys_more_x = []

        for i in range(len(xs)):
            if xs[i] < np.mean(xs):
                xs_less_x.append(xs[i])
                ys_less_x.append(ys[i])
        for i in range(len(xs)):
            if xs[i] not in xs_less_x:
                xs_more_x.append(xs[i])
                ys_more_x.append(ys[i])

        points_xs_less = []
        
        points_xs_more = []
        
        xs_less_y = []
        ys_less_y = []
        xs_more_y = []
        ys_more_y = []

        for i in range(len(xs)):
            if ys[i] < np.mean(ys):
                xs_less_y.append(xs[i])
                ys_less_y.append(ys[i])
        for i in range(len(ys)):
            if ys[i] not in ys_less_y:
                xs_more_y.append(xs[i])
                ys_more_y.append(ys[i])

        
        points_xs_less_y = []
        points_xs_more_y = []
        


        self.ymean = np.round(np.mean(ys))
        for i in range(len(ys)):
            points.append(Dot(self.coords_to_point((xs[i]),(ys[i]))))

        for i in range(len(ys_less_x)):
            points_xs_less.append(Dot(self.coords_to_point((xs_less_x[i]),(ys_less_x[i])), color = RED))
        for i in range(len(ys_more_x)):
            points_xs_more.append(Dot(self.coords_to_point((xs_more_x[i]),(ys_more_x[i])), color = GREEN))
########################################################
        for i in range(len(ys_less_y)):
            points_xs_less_y.append(Dot(self.coords_to_point((xs_less_y[i]),(ys_less_y[i])), color = YELLOW))
        for i in range(len(ys_more_y)):
            points_xs_more_y.append(Dot(self.coords_to_point((xs_more_y[i]),(ys_more_y[i])), color = BLUE))


        dots = VGroup(*points)
        dots1 = VGroup(*points_xs_less)
        dots2 = VGroup(*points_xs_more)

        dots3 = VGroup(*points_xs_less_y)
        dots4 = VGroup(*points_xs_more_y)

        self.play(FadeIn(dots))
        self.wait(2)
        self.ymean2 = 65

        mean_x = TextMobject(r"$E(X)$").scale(0.75)
        mean_y = TextMobject(r"$E(Y)$").scale(0.75)


        ymean_func=self.get_graph(self.func_to_graph_y_mean)
        ymean_func2=self.get_graph(self.func_to_graph_y_mean2)
        mean_y.next_to(ymean_func, RIGHT*1.2)


        self.play(ShowCreation(ymean_func))
        self.wait(0.1)
        self.play(Write(mean_y))
        vert_line = self.get_vertical_line_to_graph(np.mean(xs),ymean_func2,color=YELLOW)
        mean_x.next_to(vert_line, UP*1.2)
        self.play(ShowCreation(vert_line))
        self.wait(0.1)
        self.play(Write(mean_x), FadeOut(tx1))
        self.wait(2)
        self.play(FadeIn(dots1))

        tx2 = TextMobject(r"Estos puntos son $X<E(X)$").scale(0.6)
        tx2.shift(RIGHT*1.5)
        tx2.shift(UP)

        self.play(Write(tx2))
        self.wait(1)
        tx4 = TextMobject(r"Eso significa que para estos $X_i$").scale(0.6)
        tx4.shift(RIGHT*1.5)
        tx4.shift(UP)


        


        self.play(FadeOut(tx2),Write(tx4))
        
        cov_tx0 = TextMobject('$Cov(X, Y) = $').scale(0.6)
        cov_tx0.next_to(tx2, DOWN)
        cov_tx1 = TextMobject('$E[$').scale(0.6)
        cov_tx1.next_to(cov_tx0, RIGHT)
        cov_tx2 = TextMobject('$(X-E(X))$').scale(0.6)
        cov_tx2.next_to(cov_tx1, RIGHT)
        cov_tx3 = TextMobject('$*$').scale(0.6)
        cov_tx3.next_to(cov_tx2, RIGHT)
        cov_tx4 = TextMobject('$(Y-E(Y))$').scale(0.6)
        cov_tx4.next_to(cov_tx3, RIGHT)
        cov_tx5 = TextMobject('$]$').scale(0.6)
        cov_tx5.next_to(cov_tx4, RIGHT)
        cov_tx2_a = TextMobject('$(X-E(X))$', color = RED).scale(0.6)
        cov_tx2_a.next_to(cov_tx1, RIGHT)
        cov_tx4_a = TextMobject('$(Y-E(Y))$', color = RED).scale(0.6)
        cov_tx4_a.next_to(cov_tx3, RIGHT)

        mns1 = TextMobject("$-$", color = RED).scale(1.1)
        mns1.shift(LEFT*4)
        mns1.shift(UP)
        mns2 = TextMobject("$-$", color = RED).scale(1.1)
        mns2.next_to(mns1, DOWN*11)

        pl1 = TextMobject("$+$", color = GREEN).scale(1.1)
        pl1.next_to(mns1, RIGHT*8)
        pl2 = TextMobject("$+$", color = GREEN).scale(1.1)
        pl2.next_to(mns2, RIGHT*8)



        prd1=TextMobject("$*$")
        prd1.next_to(pl2,RIGHT)
        prd2=TextMobject("$*$")
        prd2.next_to(mns2,RIGHT)
        prd3=TextMobject("$*$")
        prd3.next_to(pl1,RIGHT)
        prd4=TextMobject("$*$")
        prd4.next_to(mns1,RIGHT)

        mns3 = TextMobject("$-$", color = YELLOW)
        mns3.next_to(prd1,RIGHT)
        mns4 = TextMobject("$-$", color = YELLOW)
        mns4.next_to(prd2,RIGHT)

        pl3 = TextMobject("$+$", color = BLUE)
        pl3.next_to(prd3,RIGHT)
        pl4 = TextMobject("$+$", color = BLUE)
        pl4.next_to(prd4,RIGHT)


        tx3 = TextMobject('Es negativo, $-$').scale(0.6)
        tx3.shift(RIGHT*1.5)
        tx3.shift(UP)
        tx11 = TextMobject(r"Y estos puntos son $X>E(X)$").scale(0.6)
        tx11.shift(RIGHT*1.5)
        tx11.shift(UP)
        tx10 = TextMobject(r"Entonces, estos $X_i$").scale(0.6)
        tx10.shift(RIGHT*1.5)
        tx10.shift(UP)
        
        self.play(Write(cov_tx0),Write(cov_tx1),Write(cov_tx2),Write(cov_tx3),Write(cov_tx4),Write(cov_tx5))
        self.wait(0.5)
        self.play(FadeIn(cov_tx2_a),FadeOut(cov_tx2))
        self.play(FadeIn(tx3),FadeOut(tx4))
        self.wait(0.1)
        self.play(Write(mns1),Write(mns2))
        self.wait(1.5)
        self.play(FadeOut(cov_tx2_a),FadeIn(cov_tx2))
        cov_tx2_a = TextMobject('$(X-E(X))$', color = GREEN).scale(0.6)
        cov_tx2_a.next_to(cov_tx1, RIGHT)

        

        self.wait(2)
        self.play(FadeOut(dots1))
        self.wait(1)
        self.play(FadeOut(tx3))
        tx3 = TextMobject('Hacen que esta parte sea positiva $+$').scale(0.6)
        tx3.shift(RIGHT*1.5)
        tx3.shift(UP)
        self.wait(0.5)
        self.play(Write(tx11))
        self.play(FadeIn(dots2))
        self.play(FadeIn(cov_tx2_a),FadeOut(cov_tx2))
        self.wait(0.5)
        self.play(FadeOut(tx11))
        self.wait(0.5)
        self.play(Write(tx10))
        self.wait(1)
        self.play(FadeOut(tx10))
        self.wait(0.1)
        self.play(Write(tx3))
        self.wait(0.1)
        self.play(Write(pl1),Write(pl2))
        self.wait(1)
        self.play(FadeOut(dots2))
        self.play(FadeOut(tx3))
        self.play(FadeIn(cov_tx2),FadeOut(cov_tx2_a))
        self.wait(1)

        ytx1 = TextMobject(r'Estos $Y_i < E(Y)$').scale(0.6)
        ytx1.shift(RIGHT*1.5)
        ytx1.shift(UP)

        ytx2 = TextMobject(r'Por lo que estos puntos, hacen que esto').scale(0.6)
        ytx2.shift(RIGHT*1.5)
        ytx2.shift(UP)
        ytx3 = TextMobject(r'Sea negativo $-$').scale(0.6)
        ytx3.shift(RIGHT*1.5)
        ytx3.shift(UP)
        cov_tx4_a = TextMobject('$(Y-E(Y))$', color = YELLOW).scale(0.6)
        cov_tx4_a.next_to(cov_tx3, RIGHT)

        self.play(Write(ytx1))
        self.play(FadeIn(dots3))
        self.wait(1)
        self.play(FadeOut(ytx1))
        self.wait(0.1)
        self.play(Write(ytx2))
        self.play(FadeOut(cov_tx4), FadeIn(cov_tx4_a))
        self.wait(0.5)
        self.play(FadeOut(ytx2))
        self.play(Write(ytx3))
        self.wait(0.1)
        self.play(Write(mns3),Write(prd1),Write(mns4),Write(prd2))
        self.wait(1)
        self.play(FadeOut(ytx3))
        self.play(FadeOut(dots3))
        self.play(FadeOut(cov_tx4_a), FadeIn(cov_tx4))
        self.wait(2)

        ytx1 = TextMobject(r'Estos $Y_i > E(Y)$').scale(0.6)
        ytx1.shift(RIGHT*1.5)
        ytx1.shift(UP)

        ytx2 = TextMobject(r'Por lo que estos puntos, hacen que esto').scale(0.6)
        ytx2.shift(RIGHT*1.5)
        ytx2.shift(UP)
        ytx3 = TextMobject(r'Sea positivo $+$').scale(0.6)
        ytx3.shift(RIGHT*1.5)
        ytx3.shift(UP)
        cov_tx4_a = TextMobject('$(Y-E(Y))$', color = BLUE).scale(0.6)
        cov_tx4_a.next_to(cov_tx3, RIGHT)


        self.play(Write(ytx1))
        self.play(FadeIn(dots4))
        self.wait(1)
        self.play(FadeOut(ytx1))
        self.wait(0.1)
        self.play(Write(ytx2))
        self.play(FadeOut(cov_tx4), FadeIn(cov_tx4_a))
        self.wait(0.5)
        self.play(FadeOut(ytx2))
        self.play(Write(ytx3))
        self.wait(0.1)
        self.play(Write(pl3),Write(prd3),Write(pl4),Write(prd4))
        self.wait(1)
        self.play(FadeOut(ytx3))
        self.play(FadeOut(dots4))
        self.play(FadeOut(cov_tx4_a), FadeIn(cov_tx4))
        self.wait(2)
        self.play(FadeOut(dots))
        self.wait(2)

        rectangle_neg1 = Rectangle(height=2.5, width=2.3,fill_color=RED, fill_opacity=0.4, color=RED )
        rectangle_neg1.next_to(vert_line, LEFT)
        rectangle_neg1.shift(UP*0.85)
        rectangle_neg1.shift(RIGHT*0.2)

        rectangle_neg2 = Rectangle(height=1.8, width=3,fill_color=RED, fill_opacity=0.4, color=RED )
        rectangle_neg2.next_to(vert_line, RIGHT)
        rectangle_neg2.shift(DOWN*1.4)
        rectangle_neg2.shift(LEFT*0.2)
        

        rectangle_pos1 = Rectangle(height=1.8, width=2.3,fill_color=GREEN, fill_opacity=0.4, color=GREEN )
        rectangle_pos1.next_to(vert_line, LEFT)
        rectangle_pos1.shift(DOWN*1.4)
        rectangle_pos1.shift(RIGHT*0.2)

        rectangle_pos2 = Rectangle(height=2.5, width=3,fill_color=GREEN, fill_opacity=0.4, color=GREEN )
        rectangle_pos2.next_to(vert_line, RIGHT)
        rectangle_pos2.shift(UP*0.85)
        rectangle_pos2.shift(LEFT*0.2)



        
        tx_c1 = TextMobject(r"Por regla de signos, entonces").scale(0.6)
        tx_c1.shift(RIGHT*2.5)
        tx_c1.shift(UP)
        tx_c2 = TextMobject(r"Los puntos en estos cuadrantes").scale(0.6)
        tx_c2.shift(RIGHT*2.5)
        tx_c2.shift(UP)
        tx_c3 = TextMobject(r"Suman a la covarianza").scale(0.6)
        tx_c3.shift(RIGHT*2)
        tx_c3.shift(UP)
        tx_c4 = TextMobject(r"Y los puntos en estos").scale(0.6)
        tx_c4.shift(RIGHT*2.5)
        tx_c4.shift(UP)
        tx_c5 = TextMobject(r"Restan a la covarianza").scale(0.6)
        tx_c5.shift(RIGHT*2)
        tx_c5.shift(UP)
        self.play(Write(tx_c1))
        self.wait(0.5)
        self.play(FadeOut(tx_c1),Write(tx_c2))
        self.wait(0.1)
        self.play(ShowCreation(rectangle_pos1),ShowCreation(rectangle_pos2))
        self.wait(0.1)
        self.play(FadeOut(tx_c2),Write(tx_c3))
        self.wait(1)
        self.play(FadeOut(tx_c3))
        self.play(FadeOut(rectangle_pos1),FadeOut(rectangle_pos2))
        
        self.wait(0.1)
        self.play(Write(tx_c4))
        self.wait(0.1)
        self.play(ShowCreation(rectangle_neg1),ShowCreation(rectangle_neg2))
        self.wait(0.1)
        self.play(FadeOut(tx_c4),Write(tx_c5))
        self.wait(2)
        self.play(FadeOut(rectangle_neg1),FadeOut(rectangle_neg2))
        self.play(FadeOut(tx_c5))
        
        self.play(FadeOut(pl1),FadeOut(pl2),FadeOut(pl3),FadeOut(pl4),FadeOut(prd1),
            FadeOut(prd2),FadeOut(prd3),FadeOut(prd4),FadeOut(mns1),FadeOut(mns2),FadeOut(mns3),FadeOut(mns4))
        self.wait(0.5)
        tx_c1 = TextMobject(r"Pero, cuanto suma (o resta) cada punto?").scale(0.6)
        tx_c1.shift(RIGHT*2.5)
        tx_c1.shift(UP)
        self.play(ShowCreation(dots))
        self.wait(0.1)
        self.play(Write(tx_c1))
        self.wait(1)
        self.play(FadeOut(tx_c1))
        tx_c1 = TextMobject(r"Empecemos por aclarar que esto significa").scale(0.6)
        tx_c1.shift(RIGHT*2.5)
        tx_c1.shift(UP)
        self.play(Write(tx_c1))
        self.wait(0.1)
        cov_tx1a = TextMobject('$E[$', color = YELLOW)
        cov_tx1a.next_to(cov_tx0, RIGHT)
        cov_tx5a = TextMobject('$]$', color = YELLOW)
        cov_tx5a.next_to(cov_tx4, RIGHT)
        self.play(FadeOut(cov_tx1),FadeOut(cov_tx5), Write(cov_tx1a), Write(cov_tx5a))
        self.wait(0.6)
        self.play(FadeOut(tx_c1))
        tx_c1 = TextMobject(r"En este caso, sacarle el promedio a").scale(0.6)
        tx_c1.shift(RIGHT*2.5)
        tx_c1.shift(UP)
        self.play(Write(tx_c1))
        self.wait(0.1)
        self.play(FadeOut(cov_tx1a),FadeOut(cov_tx5a), Write(cov_tx1), Write(cov_tx5))
        self.wait(1)
        cov_tx2a = TextMobject('$(X-E(X))*(Y-E(Y))$', color = YELLOW).scale(0.65)
        cov_tx2a.next_to(cov_tx1, RIGHT)
        self.play(FadeOut(cov_tx2),FadeOut(cov_tx3),FadeOut(cov_tx4), 
            Write(cov_tx2a))
        self.wait(1)
        self.play(FadeOut(tx_c1))
        tx_c1 = TextMobject(r"Y cada uno de estos viene de").scale(0.6)
        tx_c1.shift(RIGHT*2.5)
        tx_c1.shift(UP)
        self.wait(0.5)
        
        self.play(Write(tx_c1))
        self.wait(0.1)
        self.play(FadeOut(cov_tx2a), 
            Write(cov_tx2), Write(cov_tx3), Write(cov_tx4))

        

        line1=Line(np.array([-4.1,-1.2,0]),np.array([-4.1,0.3,0]), color = RED)
        line2=Line(np.array([-4.1,0.3,0]),np.array([-2.6,0.3,0]), color = RED)
        txlinex = TextMobject(r"$y_i-E(Y)$", color = RED).scale(0.5)
        txlinex.next_to(line1, LEFT)
        txliney = TextMobject(r"$x_i-E(X)$", color = RED).scale(0.5)
        txliney.next_to(line2, UP)
        self.play(ShowCreation(line1))
        self.wait(0.1)
        self.play(Write(txlinex))
        self.wait(0.1)
        self.play(ShowCreation(line2))
        self.wait(0.1)
        self.play(Write(txliney))
        self.wait(0.1)
        self.play(FadeOut(tx_c1))
        tx_c1 = TextMobject(r"el area es el producto, entonces").scale(0.6)
        tx_c1.shift(RIGHT*2.5)
        tx_c1.shift(UP)
        self.wait(1)
        self.play(Write(tx_c1))
        r1 = Rectangle(height=1.48, width=1.43,fill_color=RED, fill_opacity=0.6, color=RED )
        r1a = Rectangle(height=1.48, width=1.43,fill_color=RED, fill_opacity=0.6, color=RED )

        r1.next_to(line2, DOWN)
        r1.shift(UP*0.25)
        self.play(ShowCreation(r1),FadeOut(line1),FadeOut(line2))
        self.wait(2)
        self.play(FadeOut(tx_c1))
        tx_c1 = TextMobject(r"Entonces sacamos todos las areas").scale(0.6)
        tx_c1.shift(RIGHT*2.5)
        tx_c1.shift(UP*3)
        tx_c2 = TextMobject(r"Las que restan").scale(0.6)
        tx_c2.next_to(tx_c1, DOWN*1.2)
        tx_c2.shift(LEFT)
        r1a.next_to(tx_c2, DOWN*1.2)
        self.wait(0.5)
        self.play(Write(tx_c1))
        self.play(FadeOut(cov_tx0),FadeOut(cov_tx1), 
            FadeOut(cov_tx2), FadeOut(cov_tx3), FadeOut(cov_tx4),FadeOut(cov_tx5))
        self.wait(0.5)
        self.play(Write(tx_c2))

        r2 = Rectangle(height=0.34, width=0.33,fill_color=RED, fill_opacity=0.6, color=RED )
        r2.shift(LEFT*2.45)
        r2.shift(DOWN*1.35)


        r3 = Rectangle(height=1.1, width=1.43,fill_color=RED, fill_opacity=0.6, color=RED )
        r3.shift(LEFT*1.9)
        r3.shift(DOWN*1.75)


        r2a = Rectangle(height=0.34, width=0.33,fill_color=RED, fill_opacity=0.6, color=RED )
        pl1_r = TextMobject(r"$+$")
        pl1_r.next_to(r1a, RIGHT)
        r2a.next_to(pl1_r, RIGHT)

        r3a = Rectangle(height=1.1, width=1.43,fill_color=RED, fill_opacity=0.6, color=RED )
        pl2_r = TextMobject(r"$+$")
        pl2_r.next_to(r2a, RIGHT)
        r3a.next_to(pl2_r, RIGHT)
        
        self.play(ShowCreation(r2))
        self.wait(0.1)
        self.play(ShowCreation(r3))
        self.wait(0.5)
        self.play(Transform(r1,r1a),Transform(r2,r2a),Transform(r3,r3a),FadeOut(txlinex),FadeOut(txliney))
        self.wait(1)
        tx_c3 = TextMobject(r"Las que suman").scale(0.6)
        tx_c3.next_to(ymean_func2,RIGHT)
        tx_c3.shift(DOWN*3.2)


        r4 = Rectangle(height=0.1, width=0.46,fill_color=GREEN, fill_opacity=0.6, color=GREEN )
        r4a = Rectangle(height=0.1, width=0.46,fill_color=GREEN, fill_opacity=0.6, color=GREEN )
        r4.shift(LEFT*2.90)
        r4.shift(DOWN*1.2)

        r5 = Rectangle(height=0.6, width=0.43,fill_color=GREEN, fill_opacity=0.6, color=GREEN )
        r5a = Rectangle(height=0.6, width=0.43,fill_color=GREEN, fill_opacity=0.6, color=GREEN )
        r5.shift(LEFT*2.45)
        r5.shift(DOWN*0.85)

        r6 = Rectangle(height=0.9, width=1.1,fill_color=GREEN, fill_opacity=0.6, color=GREEN )
        r6a = Rectangle(height=0.9, width=1.1,fill_color=GREEN, fill_opacity=0.6, color=GREEN )
        r6.shift(LEFT*2.1)
        r6.shift(DOWN*0.7)

        r7 = Rectangle(height=1.60, width=1.5,fill_color=GREEN, fill_opacity=0.6, color=GREEN )
        r7a = Rectangle(height=1.60, width=1.5,fill_color=GREEN, fill_opacity=0.6, color=GREEN )
        r7.shift(LEFT*3.4)
        r7.shift(DOWN*2)

        r4a.next_to(tx_c3, DOWN)
        r4a.shift(LEFT)
        pl3_r = TextMobject(r"$+$")
        pl3_r.next_to(r4a,RIGHT)
        r5a.next_to(pl3_r,RIGHT)
        pl4_r = TextMobject(r"$+$")
        pl4_r.next_to(r5a,RIGHT)
        r6a.next_to(pl4_r,RIGHT)
        pl5_r = TextMobject(r"$+$")
        pl5_r.next_to(r6a,RIGHT)
        r7a.next_to(pl5_r, RIGHT)
        
            


        self.play(Write(tx_c3))
        self.wait(0.1)
        self.play(ShowCreation(r4))
        self.play(ShowCreation(r5))
        self.play(ShowCreation(r6))
        self.play(ShowCreation(r7))
        self.wait(0.5)
        self.play(Transform(r4,r4a),Transform(r5,r5a),Transform(r6,r6a),Transform(r7,r7a))


        self.wait(2)
        self.play(FadeOut(tx_c1))
        self.play(FadeOut(tx_c2))
        self.play(FadeOut(tx_c3))
        tx_c1 = TextMobject(r"Sumamos y restamos").scale(0.6)
        tx_c1.shift(RIGHT*2.5)
        tx_c1.shift(UP*3)
        
        self.play(Write(tx_c1))
        rarea = np.sqrt(np.abs((0.1*0.45+0.6*0.43+0.9*1.1+1.6*1.5)-(1.48*1.43 + 0.34*0.33 + 1.1*1.43)))
        
        covar_rect = Rectangle(height=rarea, width=rarea,fill_color=RED, fill_opacity=0.6, color=RED )
        covar_rect.next_to(tx_c1, DOWN*2)
        self.play(Transform(r1,covar_rect),Transform(r2,covar_rect),Transform(r3,covar_rect),
            Transform(r4,covar_rect),Transform(r5,covar_rect),Transform(r6,covar_rect),Transform(r7,covar_rect))
        self.play(FadeOut(r2),FadeOut(r3),FadeOut(r4),FadeOut(r5),FadeOut(r6),FadeOut(r7))
        self.wait(2)
        self.play(FadeOut(tx_c1))

        tx_c1 = TextMobject(r"Y dividimos por la cantidad de puntos").scale(0.6)
        tx_c1.shift(RIGHT*2.5)
        tx_c1.shift(UP*3)
        tx_c2 = TextMobject(r"Para obtener la covarianza").scale(0.6)
        tx_c2.next_to(tx_c1, DOWN)
        self.play(Write(tx_c1))
        self.play(Write(tx_c2))
        covar_recta_a = Rectangle(height=rarea/7, width=rarea/7,fill_color=RED, fill_opacity=0.6, color=RED)
        covar_recta_a.next_to(tx_c2, DOWN)
        self.play(Transform(r1,covar_recta_a))
        cvf = np.cov(xs,ys)
        print(cvf)

        tx_c3 = TextMobject(r"$ = -0.48$").scale(0.6)
        tx_c3.next_to(r1, RIGHT)
        self.play(Write(tx_c3))

        self.wait(2)
        self.play(FadeOut(tx_c3),FadeOut(tx_c2),FadeOut(tx_c1))
        self.play(FadeOut(dots),FadeOut(r1))
        xs1 = np.sort(xs)
        ys1 = np.sort(ys)
        points1 = []

        for i in range(len(ys1)):
            points1.append(Dot(self.coords_to_point((xs1[i]),(ys1[i]))))
        dots_alt = VGroup(*points1)
        self.wait(1)
        tx_c1 = TextMobject(r"Si los puntos fueran").scale(0.6)
        tx_c1.shift(RIGHT*2.5)
        tx_c1.shift(UP*3)
        self.play(Write(tx_c1))
        self.play(ShowCreation(dots_alt))
        self.wait(1)
        self.play(FadeOut(tx_c1))
        tx_c1 = TextMobject(r"La covarianza seria").scale(0.6)
        tx_c1.shift(RIGHT*2.5)
        tx_c1.shift(UP*3)
        self.wait(0.1)
        self.play(Write(tx_c1))



        r4 = Rectangle(height=0.6, width=0.4,fill_color=GREEN, fill_opacity=0.6, color=GREEN )
        r4.shift(LEFT*2.45)
        r4.shift(DOWN*0.84)
        
        r5 = Rectangle(height=0.22, width=0.42,fill_color=GREEN, fill_opacity=0.6, color=GREEN )
        r5.shift(LEFT*2.9)
        r5.shift(DOWN*1.3)

        r6 = Rectangle(height=1, width=1.42,fill_color=GREEN, fill_opacity=0.6, color=GREEN )
        r6.shift(LEFT*3.35)
        r6.shift(DOWN*1.70)

        r7 = Rectangle(height=0.9, width=1.1,fill_color=GREEN, fill_opacity=0.6, color=GREEN )
        r7.shift(LEFT*2.15)
        r7.shift(DOWN*0.73)
        

        r8 = Rectangle(height=1.60, width=1.42,fill_color=GREEN, fill_opacity=0.6, color=GREEN )
        r8.shift(LEFT*3.35)
        r8.shift(DOWN*1.95)



        r9 = Rectangle(height=1.4, width=1.43,fill_color=GREEN, fill_opacity=0.6, color=GREEN )
        r9.shift(LEFT*1.9)
        r9.shift(DOWN*0.45)

        r10 = Rectangle(height=0.1, width=0.3,fill_color=RED, fill_opacity=0.6, color=RED )
        r10.shift(LEFT*2.45)
        r10.shift(DOWN*1.25)

        arear1 = (0.6*0.4+0.22*0.42+1*1.42+0.9*1.1+1.6*1.42+1.4*1.43-0.1*0.3)
        arear11 = np.sqrt(arear1)

        r11 = Rectangle(height=arear11, width=arear11,fill_color=GREEN, fill_opacity=0.6, color=GREEN)
        r11.next_to(tx_c1, DOWN)
        r11a = Rectangle(height=arear11/7, width=arear11/7,fill_color=GREEN, fill_opacity=0.6, color=GREEN)
        r11a.next_to(tx_c1, DOWN)
        


        self.play(ShowCreation(r4))
        self.play(ShowCreation(r5))
        self.play(ShowCreation(r6))
        self.play(ShowCreation(r7))
        self.play(ShowCreation(r8))
        self.play(ShowCreation(r9))
        self.play(ShowCreation(r10))
        self.wait(0.5)
        self.play(Transform(r4,r11),Transform(r5,r11),Transform(r6,r11),
            Transform(r7,r11),Transform(r8,r11),Transform(r9,r11),
            Transform(r10,r11))
        self.play(FadeOut(r5),FadeOut(r6),FadeOut(r7),FadeOut(r8),
            FadeOut(r9),FadeOut(r10))
        self.wait(1)
        self.play(Transform(r4, r11a))
        self.wait(0.1)
        igq = TextMobject(r"$ = 208.69$")
        igq.next_to(r11a, RIGHT)
        self.play(Write(igq))
        
        self.wait(2)




            
        





        
        
        

        #













        

    def NormDistr(self, x):
        first = 1/(self.sigma*np.sqrt(2*np.pi))
        powere = (-1/2)*np.power(((x-self.mu)/self.sigma),2)
        return first*np.power(np.e, powere)
    def NormDistr2(self, x):
        first = 1/(self.sigma2*np.sqrt(2*np.pi))
        powere = (-1/2)*np.power(((x-self.mu)/self.sigma2),2)
        return first*np.power(np.e, powere)
    def NormDistr3(self, x):
        first = 1/(self.sigma3*np.sqrt(2*np.pi))
        powere = (-1/2)*np.power(((x-self.mu)/self.sigma3),2)
        return first*np.power(np.e, powere)
    def func_to_graph_y_mean(self, x):
        return (0*x+self.ymean)
    def func_to_graph_y_mean2(self, x):
        return (0*x+self.ymean2)
