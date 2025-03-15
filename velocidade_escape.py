from manim import *
import numpy as np

config.pixel_height = 1920 
config.pixel_width = 1080   
config.frame_height = 16.0 
config.frame_width = 9.0  

class escape(MovingCameraScene):
    def construct(self):
        instagram = Text('@CelestialEquations').scale(0.4).shift(5*UP).set_color_by_gradient(BLUE, RED)
        
        self.play(Write(instagram))
        titulo = Text("Velocidade de Escape", font_size=50).set_color_by_gradient(BLUE, RED)

        self.wait(3)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))
        
        mass_M = Circle(radius=2, color=BLUE, fill_opacity=0.8).shift(LEFT * 2)
        mass_label_M = MathTex("M").move_to(mass_M.get_center()+UP)

        mass_m = Circle(radius=0.4, color=RED, fill_opacity=0.8).next_to(mass_M, 0.5*RIGHT)
        mass_label_m = MathTex("m").move_to(mass_m.get_center())

        mass_m2 = Circle(radius=0.4, color=RED, fill_opacity=0.8).next_to(mass_M, 0.5*RIGHT)
        mass_label_m2 = MathTex("m").move_to(mass_m.get_center())

        radius_R = Line(start=mass_M.get_center(), end=mass_M.get_center() + RIGHT *2, color=WHITE)
        radius_label_R = MathTex("R").next_to(radius_R, UP)

        V_inicial = MathTex("V_inicial").next_to(mass_m2, UP).scale(0.7)
        V_escape = MathTex("V_escape").next_to(mass_m2, UP).scale(0.7)

    
        self.add(mass_M, mass_label_M, mass_m, mass_label_m,mass_m2, mass_label_m2, radius_R, radius_label_R)
        self.wait(22)
        self.play(Write(V_inicial))
        self.wait(2)
        self.play(ReplacementTransform(V_inicial, V_escape ))
        self.wait(9)

        massa_mc_compact_1 = VGroup(mass_m, mass_label_m)
        self.play(massa_mc_compact_1.animate.shift(RIGHT *3), run_time=3, rate_func=smooth)
        self.wait(1)
        V_nula = MathTex("V = 0").next_to(mass_m, UP).scale(0.7)
        self.play(Write(V_nula))
        self.wait(4)

        grupo_total = VGroup(mass_M,mass_label_M, mass_m, mass_label_m, mass_m2, mass_label_m2, radius_R, radius_label_R,
                             V_inicial, V_escape, V_nula )
        
        self.play(grupo_total.animate.shift(2*UP+2*LEFT).scale(0.5), run_time =2)
        self.wait(1)


        equacao_1 = MathTex(r" E_{mi} = E_{mf}").shift(DOWN)
        equacao_2 = MathTex(r"K_{i}+U_{i} = K_{f}+U_{f}").next_to(equacao_1, DOWN)
        equacao_3 = MathTex(r"K_{i}+U_{i} = 0").next_to(equacao_2, DOWN)
        K = MathTex(r"K = \frac{mv^{2}}{2}").shift(3*UP+2.5*RIGHT).set_color(BLUE)
        U = MathTex(r"U = \frac{-GMm}{R} ").next_to(K, 2*DOWN).set_color(BLUE)
        self.play(Write(equacao_1))
        self.wait(7)
        self.play(Write(equacao_2))
        self.wait(7)
        self.play(Write(equacao_3))
        self.wait(13)
        self.play(Write(K))
        self.wait(1)
        self.play(Write(U))
        self.wait(13)

        equacao_4 = MathTex(r"\frac{mv_{esc}^{2}}{2}-\frac{GMm}{R} = 0").shift(4*DOWN)
        equacao_5 = MathTex(r"\frac{mv_{esc}^{2}}{2}= \frac{GMm}{R} ").shift(4*DOWN)
        equacao_6 = MathTex(r"\frac{\not mv_{esc}^{2}}{2}= \frac{GM\not m}{R}  ").shift(4*DOWN)
        equacao_7 = MathTex(r"v_{esc}^{2} = \frac{2GM}{R}").shift(4*DOWN)
        equacao_8 = MathTex(r"v_{esc} = \sqrt{\frac{2GM}{R}}").shift(4*DOWN)
        framebox = SurroundingRectangle(equacao_8, buff=.2, color = RED)
        self.play(Write(equacao_4))
        self.wait(12)
        self.play(ReplacementTransform(equacao_4, equacao_5))
        self.wait(5)
        self.play(ReplacementTransform(equacao_5, equacao_6))
        self.wait(1)
        self.play(ReplacementTransform(equacao_6, equacao_7))
        self.wait(1)
        self.play(ReplacementTransform(equacao_7, equacao_8))
        self.wait(2)
        self.play(Create(framebox))
        self.wait(20)

        

        