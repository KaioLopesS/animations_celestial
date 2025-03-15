from manim import *
import numpy as np
import random

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class pi_fatorial(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        instagram = Text('@CelestialEquations').scale(0.4).shift(4*UP).set_color_by_gradient(BLUE, WHITE)
        titulo = Text(" Quanto é π! ?", font_size=70)
        titulo.set_color_by_gradient(BLUE, WHITE)
        self.play(Write(titulo))
        self.play(Write(instagram))
        self.wait(4)
        self.remove(titulo)

        o_fatorial1 = Text("n!", font_size=70)
        o_fatorial1.set_color_by_gradient(BLUE, WHITE)
        o_fatorial2 = MathTex(r"n! = n.(n-1).(n-2).(n-3).3.2.1")
        o_fatorial2.set_color_by_gradient(BLUE, WHITE)

        self.play(Write(o_fatorial1))
        self.wait(2)
        self.play(ReplacementTransform(o_fatorial1, o_fatorial2))

        self.wait(5)

        self.remove(o_fatorial2)


        

        fatorial_list = BulletedList(
            "3! = 3.2.1 = 6",
            "2! = 2.1 = 2",
            "1! = 1 = 1",
            "0! = 1"
        ).scale(1).shift(DOWN*0.5)
        fatorial_list.set_color_by_gradient(BLUE, WHITE)

        
        self.play(Write(fatorial_list), run_time =4)
        self.wait(6)
        self.remove(fatorial_list)
        self.wait(2)


        
        numero2 = Text('1,5!', font_size=70)
        numero2.set_color(BLUE)
        pi_fatorial = Text('π!', font_size=70).shift(2*UP)
        pi_fatorial.set_color(WHITE)
        numero3 = Text('0,5!', font_size=70).shift(2*DOWN)

        self.play(Write(numero2))
        self.wait(1)
        self.play(Write(numero3))
        self.wait(1)
        self.play(Write(pi_fatorial))
        self.wait(5)

        self.remove(numero2, numero3, pi_fatorial)

        funcao_gama_titulo = Text('Função Gama', font_size = 60)
        funcao_gama_titulo.set_color_by_gradient(BLUE, WHITE)
        funcao_gama_titulo.shift(2*UP)
        funcao_gama = MathTex(r"\Gamma (n+1)= n!", font_size = 60)
        funcao_gama2 =MathTex(r'\Gamma (n+1)= \int_{0}^{\infty} x^n e^{-x} dx').shift(2*DOWN)
        funcao_gama3 =MathTex(r'n!= \int_{0}^{\infty} x^n e^{-x} dx').shift(2*DOWN)
        pi = MathTex(r'\pi ! = \int_{0}^{\infty} x^{\pi} e^{-x} \, dx')
        pi2 = MathTex(r'\pi ! \approx 7.1881')
        framebox = SurroundingRectangle(pi2, buff = .2, color = BLUE)
        youtube = Text('Acesse nosso canal no youtube ', font_size=30).shift(3*DOWN).set_color_by_gradient(BLUE, WHITE)
        self.play(Write(funcao_gama_titulo))
        self.wait(3)
        self.play(Write(funcao_gama))
        self.wait(6)
        self.play(Write(funcao_gama2))
        self.wait(6)
        self.play(ReplacementTransform(funcao_gama2, funcao_gama3))
        self.wait(6)
        self.remove(funcao_gama3, funcao_gama, funcao_gama_titulo)
        self.play(Write(pi))
        self.wait(5)
        self.play(ReplacementTransform(pi, pi2), run_time = 2)
        self.wait(1)
        self.play(Create(framebox))
        self.wait(5)
        self.play(Write(youtube))
        self.wait(15)
        

        
    
        
        


