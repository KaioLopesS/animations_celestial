from manim import *
import numpy as np
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class ex(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        instagram = Text('@CelestialEquations').scale(0.4).shift(5*UP).set_color_by_gradient(ORANGE, YELLOW)
        subtitulo = Text('Série de Taylor/MacLaurin').scale(0.4).set_color_by_gradient(ORANGE, YELLOW).move_to(DOWN)
        titulo = Text("Expansão de e^x", font_size=50)
        titulo.set_color_by_gradient(ORANGE, YELLOW)
        self.play(Write(instagram))
        self.play(Write(titulo))
        self.play(Write(subtitulo))

        self.wait(1)
        self.remove(titulo, subtitulo)

        equacao1 = MathTex(r'f(x)= a_{0}+a_{1}x+a_{2}x^2+a_{3}x^3+a_{4}x^4+...').scale(0.9).set_color_by_gradient(ORANGE, YELLOW)
        equacao2 = MathTex(r'f(x)= \sum_{n=0}^{\infty} \frac{f^n(0)}{n!}x^n').scale(0.9).set_color_by_gradient(ORANGE, YELLOW)
        equacao3 = MathTex(r'e^x = \sum_{n=0}^{\infty} \frac{f^n(0)}{n!}x^n').scale(0.9).set_color_by_gradient(ORANGE, YELLOW)
        equacao4 = MathTex(r'e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}').scale(0.9).set_color_by_gradient(ORANGE, YELLOW)
        equacao5 = MathTex(r'e^x = 1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + ...').scale(0.9).set_color_by_gradient(ORANGE, YELLOW)
        framebox = SurroundingRectangle(equacao5, buff=.1).set_color_by_gradient(ORANGE, YELLOW)
        self.play(Write(equacao1))
        self.wait(2)
        self.play(ReplacementTransform(equacao1, equacao2))
        self.wait(2)
        self.play(ReplacementTransform(equacao2, equacao3))
        self.wait(2)
        self.play(ReplacementTransform(equacao3, equacao4))
        self.wait(2)
        self.play(ReplacementTransform(equacao4, equacao5))
        self.wait(1.5)
        self.play(Create(framebox))
        self.wait(1.5)
