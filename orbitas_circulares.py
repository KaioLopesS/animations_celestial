from manim import *
import numpy as np
import random

class orbitas_circulares(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        instagram = Tex('@CelestialEquations').scale(0.5).shift(LEFT*5.5+3.5*UP)
        #titulo = Text("A Órbita Circular", font_size=40).set_color_by_gradient(RED, WHITE)
        self.play(Write(instagram))
        self.wait(1)

        
        massa_maior = Dot(point=ORIGIN, color=WHITE, radius=0.3)
        label_M = Tex("M").next_to(massa_maior, UP).set_color(WHITE)
        self.play(FadeIn(massa_maior), Write(label_M))
        self.wait(1)

        
        raio_orbita = 3
        orbita = Circle(radius=raio_orbita, color=WHITE)
        self.play(Create(orbita))
        self.wait(1)

        
        massa_menor = Dot(point=orbita.point_at_angle(0), color=WHITE, radius=0.1)
        label_m = Tex("m").next_to(massa_menor, RIGHT).set_color(WHITE)
        self.play(FadeIn(massa_menor), Write(label_m))
        self.wait(1)

    
        raio = Line(start=massa_maior.get_center(), end=massa_menor.get_center(), color=WHITE)
        label_R = Tex("R").next_to(raio, UP).set_color(WHITE)
        self.play(Create(raio), Write(label_R))
        self.wait(1)

        vetor_forca = Arrow(start=massa_menor.get_center(), end=massa_menor.get_center()+LEFT, buff=0, color=YELLOW)
        label_f = Tex("Fc").next_to(vetor_forca, DOWN).set_color(YELLOW)
        
        
        vetor_velocidade = Arrow(start=massa_menor.get_center(), end=massa_menor.get_center() + UP, buff=0, color=RED)
        label_v = Tex("v").next_to(vetor_velocidade, RIGHT).set_color(RED)
        

        grupo = VGroup(massa_maior, label_M, massa_menor, label_m, raio, label_R, vetor_velocidade, label_v, orbita, vetor_forca, label_f)

        self.add(massa_menor, label_m, raio, label_R)
        self.wait(1)
        self.play(FadeIn(vetor_velocidade), FadeIn(label_v))
        self.play(Create(vetor_forca), Write(label_f))
        self.wait(10)

        self.play(grupo.animate.shift(LEFT*4).scale(0.5), run_time=2)
        self.wait(1)

        velocidade_orbital = Text('Velocidade Orbital', font_size=40).shift(3*UP+2*RIGHT).set_color_by_gradient(RED, WHITE)
        forca_centripeta = MathTex(r"F_{\text{centrípeta}} = F_g").shift(2*UP+2*RIGHT)
        equacao_2 = MathTex(r"\frac{mv^{2}}{R} = \frac{GMm}{R^{2}}").next_to(forca_centripeta, DOWN)
        equacao_3 = MathTex(r"v^{2} = \frac{GM}{R}").next_to(equacao_2, DOWN)
        equacao_4 = MathTex(r"v = \sqrt{\frac{GM}{R}}").next_to(equacao_3, DOWN)
        framebox =SurroundingRectangle(equacao_4, buff = .2)
        equacao_5 = MathTex(r"v = \frac{2\pi R}{T}").next_to(equacao_4, DOWN).set_color(RED)
        equacao_6 = MathTex(r"\frac{2\pi R}{T} = \sqrt{\frac{GM}{R}}").shift(2*UP+2*RIGHT)
        equacao_int = equacao_4.animate.shift(3*UP)
        equacao_7 = MathTex(r"\frac{4\pi^{2}R^{2}}{T^{2}} = \frac{GM}{R}").shift(2*UP+2*RIGHT)
        equacao_8 = MathTex(r"T^{2} = \frac{4\pi^{2}R^{3}}{GM}").next_to(equacao_7, DOWN)
        equacao_9 = MathTex(r"\frac{T^{^{2}}}{R^{3}} = \frac{4\pi^{2} }{GM}").next_to(equacao_8, DOWN)
        framebox_2 = SurroundingRectangle(equacao_9, buff = .2)
        kepler_3 = Text("3ª Lei de Kepler", font_size=30).next_to(equacao_9, 2*DOWN).set_color(YELLOW)
       
        self.play(Write(velocidade_orbital))
        self.wait(10)
        self.play(Write(forca_centripeta))
        self.wait(4)
        self.play(Write(equacao_2))
        self.wait(10)
        self.play(Write(equacao_3))
        self.wait(4)
        self.play(Write(equacao_4))
        self.wait(1)
        self.play(Create(framebox))
        self.wait(10)
        self.remove(velocidade_orbital, forca_centripeta, equacao_2, equacao_3, framebox)
        self.wait(1)
        self.play(equacao_int)
        self.wait(10)
        self.play(Write(equacao_5))
        self.wait(10)
        self.play(ReplacementTransform(equacao_4, equacao_6))
        self.remove(equacao_5)
        self.wait(6)
        self.play(ReplacementTransform(equacao_6, equacao_7))
        self.wait(6)
        self.play(Write(equacao_8))
        self.wait(2)
        self.play(Write(equacao_9))
        self.play(Create(framebox_2))
        self.wait(2)
        self.play(Write(kepler_3))
        self.wait(20)
        

        
