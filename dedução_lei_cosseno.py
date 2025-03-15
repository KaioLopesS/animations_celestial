
from manim import *
class lei_cosseno(Scene):
    def construct(Self):
        #VARIAVEIS
        titulo= Tex(r"Dedução - Lei dos cossenos")
        instagram = Tex('@CelestialEquations').scale(0.5).shift(LEFT*5.5+3.5*UP)
        triangulo1 = Triangle(color=WHITE).scale(4)
        b1,b2,b3 = triangulo1.get_vertices()
        ladob1 = Line(b1,b3, color = RED)
        ladob1_ = Line(b1,b3, color = WHITE)
        ladob2 =Line(b1,b2, color = RED)
        ladob3 = Line(b2,b3, color = RED)
        ponto_medio_a = (b2 + b3) / 2
        altura = Line(b1, ponto_medio_a, color = WHITE)
        nome_altura = MathTex('h').next_to(altura, RIGHT)
        ladob1_nome = MathTex('a').shift(RIGHT*2.5)
        ladob2_nome = MathTex('b').shift(2.5*LEFT)
        ladob3_nome = MathTex('c').shift(3.5*DOWN)
        lado_m = MathTex('m').shift(3*DOWN+1.5*LEFT).scale(0.8)
        lado_c_m = MathTex('c-m').shift(3*DOWN+1.5*RIGHT).scale(0.8)
        metade_triangulo_1 = Polygon(b1, ponto_medio_a, b2, color=BLUE, fill_opacity=0.5)
        metade_triangulo_2 = Polygon(b1, ponto_medio_a, b3, color = GREEN, fill_opacity=0.5)
        animacao_triangulo_2 = metade_triangulo_2.animate.shift(LEFT * 3.5)
        animacao_triangulo_1 =metade_triangulo_1.animate.shift(LEFT*2)
        angulo_arco_b3 = Arc(
            radius=0.2, 
            start_angle=PI, 
            angle=-PI/4, 
            color= WHITE
        ).move_arc_center_to(b3)
        angulo_nome_b3 = MathTex(r"\alpha ").next_to(angulo_arco_b3, LEFT+UP*0.5)

        angulo_arco_b2 = Arc(
            radius=0.2, 
            start_angle=PI/4, 
            angle=-PI/4, 
            color= WHITE
        ).move_arc_center_to(b2)
        angulo_nome_b2 = MathTex(r"\theta ").next_to(angulo_arco_b2, RIGHT+UP*0.2)

        Self.play(Write(titulo))
        Self.play(Write(instagram))
        Self.wait(1)
        Self.remove(titulo)
        Self.play(Create(triangulo1))
        Self.wait(0.5)
        Self.play(Create(ladob1), Write(ladob1_nome))
        Self.play(Create(ladob2), Write(ladob2_nome))
        Self.play(Create(ladob3), Write(ladob3_nome))
        Self.play(Create(altura), Write(nome_altura))
        Self.play(Write(lado_m))
        Self.play(Write(lado_c_m))
        Self.wait(0.5)
        Self.play(Create(angulo_arco_b3), Write(angulo_nome_b3))
        Self.play(Create(angulo_arco_b2), Write(angulo_nome_b2) )
        Self.play(Create(metade_triangulo_2))
        Self.play(Create(metade_triangulo_1))
        Self.wait(1)
        Self.remove(triangulo1,ladob1,ladob1_nome,ladob2,ladob2_nome,ladob3,ladob3_nome,altura,nome_altura,lado_m,lado_c_m
                    , angulo_arco_b3,angulo_nome_b3,angulo_arco_b2,angulo_nome_b2,metade_triangulo_2)
        
        #CENA2
        Self.play(animacao_triangulo_1)
        lado_b_2_nome = MathTex('b', color = WHITE).shift(4.5*LEFT)
        nome_altura_2 = MathTex('h').shift(1.6*LEFT)
        lado_m_2_nome = MathTex('m', color = WHITE).shift(3.5*LEFT+3*DOWN)
        equacao_1_2 = MathTex(r'cos(\theta ) = \frac{m}{b} ').move_to(RIGHT * 3+ UP*1.5).scale(0.75)
        equacao_3_2 = MathTex(r'm = bcos(\theta ) ',r'(1)').set_color_by_tex('(1)', color =BLUE).scale(0.75).move_to(RIGHT * 3.3+ UP*0.5)
        texto_2_2 = Tex(r"Aplicando o Teorema de Pitágoras:", color =BLUE).shift(DOWN*0.6+RIGHT*2.7).scale(0.8)
        equacao2_2 = MathTex(r'b^{2} = h^{2}+ m^{2}').scale(0.75).move_to(RIGHT * 3.3+ DOWN*1.8)
        texto_1_2 = Tex(r"Analisando o triângulo, temos:", color =BLUE).shift(UP*3+RIGHT*2.5).scale(0.8)
        equacao_final_2 = MathTex(r'h^2 = b^2 - m^2', r'(2)').set_color_by_tex('(2)', color =BLUE).scale(0.75).move_to(RIGHT * 3.3+ DOWN*2.5)
        angulo_arco_b2_2 = Arc(
            radius=0.2, 
            start_angle=PI/4, 
            angle=-PI/4, 
            color= WHITE
        ).shift(2.7*DOWN+5.5*LEFT)
        angulo_nome_b2_2 = MathTex(r"\theta ").next_to(angulo_arco_b2_2, RIGHT+UP*0.2)
        Self.add(lado_b_2_nome)
        Self.add(nome_altura_2)
        Self.add(lado_m_2_nome)
        Self.play(Create(angulo_arco_b2_2), Write(angulo_nome_b2_2))
        Self.wait(1)
        Self.play(Write(texto_1_2))
        Self.play(Write(equacao_1_2))
        Self.wait(1)
        Self.play(Write(equacao_3_2))
        Self.play(Write(texto_2_2))
        Self.wait(1)
        Self.play(Write(equacao2_2))
        Self.wait(1)
        Self.play(Write(equacao_final_2))
        Self.wait(1)
        Self.remove(metade_triangulo_1,equacao2_2,nome_altura_2,animacao_triangulo_1, lado_b_2_nome, lado_m_2_nome, equacao_1_2,equacao_3_2, texto_2_2, texto_1_2, equacao_final_2,angulo_arco_b2_2,
                    angulo_nome_b2_2)
        

        #CENA 3
        ladob1_ = Line(b1,b3, color = GREEN).shift(LEFT*3.5)
        ladob1_nome_ = MathTex('a', color = WHITE).shift(LEFT)
        lado_c_m_ = MathTex('c-m').shift(3.2*DOWN+2*LEFT).scale(0.8)
        altura_ = Line(b1, ponto_medio_a, color = GREEN).shift(3.5*LEFT)
        nome_altura_ = MathTex('h').next_to(altura_, LEFT)
        angulo_arco_b3_ = Arc(
            radius=0.2, 
            start_angle=PI, 
            angle=-PI/4, 
            color= WHITE
        ).shift(2.7*DOWN)
        angulo_nome_b3_ = MathTex(r"\alpha ").next_to(angulo_arco_b3_, 2*LEFT+UP*0.5)
        texto_1 = Tex(r"Aplicando o Teorema de Pitágoras no 2ºTriângulo:", color =GREEN).shift(UP*3+RIGHT*2.5).scale(0.8)
        equacao1 = MathTex(r'a^{2} = h^{2}+ (c-m)^{2}').move_to(RIGHT * 3+ UP*1.5).scale(0.75)
        equacao2 = MathTex(r'a^2 = h^2 +c^2-2cm+m^2').scale(0.75).move_to(RIGHT * 3.3+ UP*0.8)
        texto_2= Tex(r" Sabendo que \( h^2 = b^2 - m^2 \) (2) \\ e que \( m = bcos(\theta\))\ (1):", color = BLUE).shift(DOWN*0.6+RIGHT*2.7).scale(0.8)
        equacao3 = MathTex(r'a^2 = b^2 - m^2 + c^2 - 2cm + m^2').scale(0.75).move_to(RIGHT * 3.3 + DOWN * 1.4)
        equacao4 = MathTex(r"a^2 = b^2 + c^2 - 2bc \cos(\theta)").scale(1).move_to(RIGHT * 3.3+ DOWN*3)
        equacao5 = MathTex(r'a^2 = b^2 + c^2 - 2c', r'm').set_color_by_tex('m', BLUE).scale(0.75).move_to(RIGHT * 3 + DOWN * 2)
        framebox1 = SurroundingRectangle(equacao4, buff = .1)
        Self.play(animacao_triangulo_2)
        Self.add(lado_c_m_)
        Self.add(nome_altura_)
        Self.add(ladob1_nome_)
        Self.play(Create(angulo_arco_b3_), Write(angulo_nome_b3_))
        Self.play(Write(texto_1))
        Self.play(Write(equacao1))
        Self.wait(1)
        Self.play(Write(equacao2))
        Self.wait(1)
        Self.play(Write(texto_2))
        Self.wait(1.8)
        Self.play(Create(equacao3))
        Self.wait(1.4)
        Self.play(Create(equacao5))
        Self.wait(1.4)
        Self.play(Create(equacao4))
        Self.play(Create(framebox1))
        Self.wait(1.8)




        