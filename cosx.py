import numpy as np
from manim import *
  
config.pixel_height = 1920 
config.pixel_width = 1080   
config.frame_height = 16.0 
config.frame_width = 9.0  

class cosx(MovingCameraScene):
    def construct(self):
        titulo = Tex('Expansão de cos(x) - Série de Taylor/MacLaurin ').scale(0.7)
        instagram = Tex('@CelestialEquations').scale(0.5).shift(LEFT*3 + 3.7*UP)
        
        equacao1 = MathTex(r'f(x)= a_{0}+a_{1}x+a_{2}x^2+a_{3}x^3+a_{4}x^4+...').scale(0.7)
        equacao2 = MathTex(r'f(x)= \sum_{n=0}^{\infty} \frac{f^n(0)}{n!}x^n')
        equacao3 = MathTex(r'cos(x)= \sum_{n=0}^{\infty} \frac{f^n(0)}{n!}x^n')
        derivada1 = MathTex(r'f(0) = a_{0} = 1').scale(0.7).shift(UP+RIGHT*1)
        derivada2 = MathTex(r"f'(0) = -\sin(x) = 0").scale(0.7).shift(RIGHT*1)
        derivada3 = MathTex(r"f''(0) = -\cos(x) = -1").scale(0.7).shift(DOWN+RIGHT*1)
        derivada4 = MathTex(r"f'''(0) = \sin(x) = 0").scale(0.7).shift(2*DOWN+RIGHT*1)
        derivada5 = MathTex(r"f''''(0) = \cos(x) = 1").scale(0.7).shift(3*DOWN+RIGHT*1)
        texto_1 = Tex('Calculando as n derivadas de f(0), temos:').scale(0.7).shift(UP*3+RIGHT*1)
        texto_2 = Tex('Substituindo em cos(x):').scale(0.7).shift(UP*3+RIGHT*1)
        valor_1 = MathTex(r'f(0) = 1').shift(3*LEFT+UP*0.5).scale(0.7)
        valor_2 = MathTex(r"f'(0) = 0").shift(3*LEFT).scale(0.7)
        valor_3 = MathTex(r"f''(0) = -1").shift(3*LEFT+DOWN*0.5).scale(0.7)
        valor_4 = MathTex(r"f'''(0) = 0").shift(3*LEFT+DOWN*1).scale(0.7)
        valor_5 = MathTex(r"f''''(0) =1").shift(3*LEFT+DOWN*1.5).scale(0.7)
        equacao4 = MathTex(r"cos(x) = f(0) + \frac{f'(0)}{1!}x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \frac{f''''(0)}{4!}x^4+...").scale(0.5).shift(UP*0.5+RIGHT*1.4)
        equacao5 = MathTex(r"cos(x) = 1 + \frac{0}{1!}x + \frac{(-1)}{2!}x^2 + \frac{0}{3!}x^3 + \frac{1}{4!}x^4+...").scale(0.5).shift(DOWN*0.5+RIGHT)
        equacao6 = MathTex(r"cos(x)= 1 - \frac{x^2}{2!} +\frac{x^4}{4!}-\frac{x^6}{6!}+\frac{x^8}{8!}+...").scale(0.5).shift(RIGHT+1.5*DOWN)
        equacao7 = MathTex(r"\cos(x) = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!} x^{2n}").scale(0.7).shift(RIGHT+DOWN*3)
        framebox = SurroundingRectangle(equacao7, buff = .1)
        self.play(Write(titulo))
        self.play(Write(instagram))
        self.wait(1)
        self.play(ReplacementTransform(titulo,equacao1))
        self.wait(1.5)
        self.play(ReplacementTransform(equacao1,equacao2))
        self.wait(1.5)
        self.play(ReplacementTransform(equacao2,equacao3))
        self.wait(1.5)
        self.play(equacao3.animate.shift(2.7*LEFT+UP*2).scale(0.7))
        self.wait(1)
        self.play(Write(texto_1))
        self.wait(1)
        self.play(Write(derivada1), Write(derivada2), Write(derivada3), Write(derivada4), Write(derivada5))
        self.wait(1.8)
        self.remove(derivada1, derivada2, derivada3, derivada4, derivada5)
        self.play(Write(valor_1), Write(valor_2), Write(valor_3), Write(valor_4), Write(valor_5))
        self.wait(1)
        self.play(ReplacementTransform(texto_1, texto_2 ))
        self.wait(1)
        self.play(equacao3.animate.shift(4*RIGHT))
        self.wait(1)
        self.play(Write(equacao4))
        self.wait(1.5)
        self.play(Write(equacao5))
        self.wait(1.5)
        self.play(Write(equacao6))
        self.wait(1.5)
        self.play(Write(equacao7))
        self.wait(1)
        self.play(Create(framebox))
        self.wait(1.5)


       
