from manim import *
class area_figuras_planas(Scene):
    def construct(self):
        quadrado = Square()
        circulo = Circle(color =GREEN).scale(3.5)
        raio = Line(start=circulo.get_center(), end=circulo.point_at_angle(0), color=WHITE)
        raio_label = MathTex("R").next_to(raio, UP)  
        triangulo = Triangle(color=BLUE_B).shift(LEFT*2).scale(3.5)
        p1, p2, p3 = triangulo.get_vertices()
        lado_a = Line(p2, p3, color=RED)
        lado_a_nome = MathTex("a").next_to(lado_a, DOWN)
        ponto_medio_a = (p2 + p3) / 2
        altura = Line(p1, ponto_medio_a, color=WHITE)
        altura_nome = MathTex("h").next_to(altura, RIGHT)
        f1 = MathTex('A = \pi R^2').move_to(UP * 2.4).scale(2)
        f2 = MathTex(r'A = \frac{bh}{2}').move_to(RIGHT * 2).scale(2)
        #CÍRCULO
        self.play(Create(circulo))
        self.wait(1)
        self.play(Create(raio), Write(raio_label))
        self.wait(1)
        self.play(Write(f1))
        self.wait(2)
        self.remove(raio)
        self.remove(raio_label)
        self.remove(f1)
        #TRIANGULO#
        self.play(Transform(circulo,triangulo))
        self.wait(1)
        self.play(Create(lado_a), Write(lado_a_nome))
        self.play(Create(altura), Write(altura_nome))
        self.play(Write(f2))
        self.wait(2)
        
        
        
        
        
 
        

        


        