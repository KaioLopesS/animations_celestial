from manim import *
import numpy as np

class trigonometria(Scene):
    def construct(self):
    
        titulo_tipos = Text("Tipos de Triângulos", font_size=42).shift(3*UP).set_color_by_gradient(PURPLE, WHITE)
        instagram = Tex('@CelestialEquations').scale(0.5).shift(LEFT*5.5+3.5*UP).set_color_by_gradient(PURPLE, WHITE)
        background_color = "GRAY"
        self.play(Write(titulo_tipos))
        self.play(Write(instagram))
        self.wait(1)

        
        tri_ret = Polygon(
            [-5, -1, 0], [-5, 1, 0], [-3, -1, 0],
            color=BLUE
        )
        angulo_ponto = [-5, -1, 0]  
        tamanho_linhas = 0.2
        linha_horizontal = Line(
        angulo_ponto + np.array([0, 0, 0]),
        angulo_ponto + np.array([tamanho_linhas, 0, 0]),
        color=WHITE
        )
        linha_vertical = Line(
        angulo_ponto + np.array([0, 0, 0]),
        angulo_ponto + np.array([0, tamanho_linhas, 0]),
        color=WHITE
        )
        angulo_reto = VGroup(linha_horizontal, linha_vertical)

        label_tri_ret = Text("Triângulo Retângulo", font_size=24).next_to(tri_ret, DOWN)

        
        tri_equi = Polygon(
            [-1, -1, 0], [1, -1, 0], [0, 0.73, 0],
            color=RED
        )
        label_tri_equi = Text("Triângulo Equilátero", font_size=24).next_to(tri_equi, DOWN)

       
        tri_iso = Polygon(
            [2, -1, 0], [4, -1, 0], [3, 1, 0],
            color=YELLOW
        )
        label_tri_iso = Text("Triângulo Isósceles", font_size=24).next_to(tri_iso, 0.5*RIGHT)

        
        tri_esc = Polygon(
            [-3, -3, 0], [-1, -3, 0], [-2.3, -1.5, 0],
            color=GREEN
        )
        label_tri_esc = Text("Triângulo Escaleno", font_size=24).next_to(tri_esc, DOWN)

        
        self.play(Create(tri_ret), Create(angulo_reto))
        self.play(Write(label_tri_ret))
        self.wait(1)

        self.play(Create(tri_equi))
        self.play(Write(label_tri_equi))
        self.wait(1)

        self.play(Create(tri_iso))
        self.play(Write(label_tri_iso))
        self.wait(1)

        self.play(Create(tri_esc))
        self.play(Write(label_tri_esc))
        self.wait(2)

        
        self.play(
            FadeOut(VGroup(tri_equi, label_tri_equi, label_tri_ret,
                        tri_iso, label_tri_iso, tri_esc, label_tri_esc))
        )
        tri_ret = VGroup(tri_ret, angulo_reto)
        self.wait(1)
        triangulo_ret = Text("Triângulo Retângulo", font_size=42).shift(3*UP).set_color_by_gradient(BLUE, WHITE)
        self.play(ReplacementTransform(titulo_tipos,triangulo_ret))
        self.wait(1)
        self.play(tri_ret.animate.scale(2).shift(RIGHT*5))
        self.wait(3)

        