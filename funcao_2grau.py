from manim import *


config.pixel_height = 1920 
config.pixel_width = 1080   
config.frame_height = 16.0 
config.frame_width = 9.0 

class IntroducaoFuncaoQuadratica(Scene):
    def construct(self):
       
        titulo = Tex("A Função Quadrática", font_size=60).set_color_by_gradient(BLUE, WHITE)
        instagram = Tex('@CelestialEquations').scale(0.5).shift(5.5*UP).set_color_by_gradient(BLUE, WHITE)
        self.play(Write(titulo))
        self.wait(1)
        self.play(Write(instagram))
        self.wait(1)
        self.play(FadeOut(titulo))
        eq_geral = MathTex(r"f(x) = ax^2 + bx + c, \quad a \neq 0").set_color_by_gradient(BLUE, WHITE)
        texto_1 = Text("a,b e c são números reais", font_size=28).next_to(eq_geral, DOWN)
        texto_2 = Text("Veja alguns exemplos de Funções Quadráticas:", font_size=28).shift(UP)
        exemplo1= MathTex(r"f(x) = x^2 + 3x+5").next_to(texto_2, DOWN).set_color_by_gradient(BLUE, WHITE).set_color_by_gradient(BLUE, WHITE)    
        exemplo2= MathTex(r"f(x) = -2x^2 + 4x - 1").next_to(exemplo1, DOWN).set_color_by_gradient(BLUE, WHITE).set_color_by_gradient(BLUE, WHITE)
        
        self.play(Write(eq_geral))
        self.wait(2)
        self.play(Write(texto_1))
        self.wait(6)
        
        self.play(
            FadeOut(eq_geral),
            FadeOut(texto_1)
        )

        self.play(Write(texto_2))
        self.wait(2)
        self.play(Write(exemplo1))
        self.wait(5)
        self.play(Write(exemplo2))
        self.wait(15)

config.pixel_height = 1920 
config.pixel_width = 1080   
config.frame_height = 16.0 
config.frame_width = 9.0 

class ConstrucaoGrafico(Scene):
    def construct(self):
        
        titulo = Tex("O Gráfico da Função Quadrática:\n A Parábola", font_size=38).to_edge(UP).set_color_by_gradient(BLUE,WHITE)
        instagram = Tex('@CelestialEquations').scale(0.5).shift(5.5*UP).set_color_by_gradient(BLUE, WHITE)
        self.play(Write(titulo))
        self.add(instagram)
        self.wait(1)
    
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-4, 8, 1],
            axis_config={"include_tip": True},
        ).scale(0.8)
        
        labels = axes.get_axis_labels(x_label="x")
        self.play(Create(axes), Write(labels))
        self.wait(2)
        self.play(FadeOut(titulo))
        
        funcao = lambda x: x**2
        grafico = axes.plot(funcao, color=BLUE)
        eq = MathTex(r"f(x) = x^2").shift(UP+5*LEFT)
        
        self.play(Write(eq))
        self.play(Create(grafico), run_time=2)
        
        eixo = DashedLine(
            start=axes.c2p(0, -2),
            end=axes.c2p(0, 8),
            color=YELLOW
        )
        self.play(Create(eixo))
        self.wait(1)
        
        
        a_tracker = ValueTracker(1)
        
        def update_grafico_a():
            a = a_tracker.get_value()
            nova_funcao = lambda x: a * x**2
            return axes.plot(nova_funcao, color=BLUE)
        
        grafico_updater = always_redraw(update_grafico_a)
        self.remove(grafico)
        self.add(grafico_updater)
        
        eq_a = MathTex(r"f(x) = ", r"a", r" \cdot x^2", substrings_to_isolate=["a"])
        eq_a[1].set_color(BLUE) 
        eq_a.shift(4*DOWN)
        a_valor = DecimalNumber(1, num_decimal_places=1).set_color(BLUE)
        a_texto = Text("a = ", font_size=24).next_to(eq_a, DOWN).set_color(BLUE)
        a_valor.next_to(a_texto, RIGHT)
        
        self.play(
            ReplacementTransform(eq, eq_a),
            Write(a_texto),
            Write(a_valor)
        )
        
        
        a_valor.add_updater(lambda d: d.set_value(a_tracker.get_value()))
        
        
        self.play(a_tracker.animate.set_value(2), run_time=2)
        self.wait(2)
        self.play(a_tracker.animate.set_value(0.5), run_time=2)
        self.wait(2)
        self.play(a_tracker.animate.set_value(-1), run_time=2)
        self.wait(5)
        
        
        self.play(a_tracker.animate.set_value(1), run_time=1)
        
        
        a_valor.clear_updaters()
        self.remove(grafico_updater)
        
        
        
        b_tracker = ValueTracker(0)
        

        

        def update_grafico_b():
            b = b_tracker.get_value()
            nova_funcao = lambda x: x**2 + b*x
            return axes.plot(nova_funcao, color=GREEN)
        
        grafico_b = always_redraw(update_grafico_b)
        self.add(grafico_b)
        
        eq_b = MathTex(r"f(x) = x^2 + ", r"b", r" \cdot x", substrings_to_isolate=["b"])
        eq_b[1].set_color(GREEN) 
        eq_b.shift(4*DOWN)

        b_valor = DecimalNumber(0, num_decimal_places=1).set_color(GREEN)
        b_texto = Text("b = ", font_size=24).next_to(eq_b, DOWN).set_color(GREEN)
        b_valor.next_to(b_texto, RIGHT)
        
        self.play(
            ReplacementTransform(eq_a, eq_b),
            ReplacementTransform(a_texto, b_texto),
            ReplacementTransform(a_valor, b_valor)
        )
        
        self.wait(3)
        
        b_valor.add_updater(lambda d: d.set_value(b_tracker.get_value()))
        
        
        self.play(b_tracker.animate.set_value(2), run_time=2)
        self.wait(5)
        self.play(b_tracker.animate.set_value(-2), run_time=2)
        self.wait(5)
        
        
        self.play(b_tracker.animate.set_value(0), run_time=1)
        b_valor.clear_updaters()
        self.remove(grafico_b)
        
        
        c_tracker = ValueTracker(0)
        
        def update_grafico_c():
            c = c_tracker.get_value()
            nova_funcao = lambda x: x**2 + c
            return axes.plot(nova_funcao, color=YELLOW)
        
        grafico_c = always_redraw(update_grafico_c)
        self.add(grafico_c)
        
        eq_c = MathTex(r"f(x) = x^2 +", r"c", substrings_to_isolate=['c']).shift(5*DOWN)
        eq_c[1].set_color(YELLOW)

        c_valor = DecimalNumber(0, num_decimal_places=1).set_color(YELLOW)
        c_texto = Text("c = ", font_size=24).next_to(eq_c, DOWN).set_color(YELLOW)
        c_valor.next_to(c_texto, RIGHT)
        
        self.play(
            ReplacementTransform(eq_b, eq_c),
            ReplacementTransform(b_texto, c_texto),
            ReplacementTransform(b_valor, c_valor)
        )
        
        self.wait(10)
        c_valor.add_updater(lambda d: d.set_value(c_tracker.get_value()))
        
        
        self.play(c_tracker.animate.set_value(3), run_time=2)
        self.wait(3)
        self.play(c_tracker.animate.set_value(-2), run_time=2)
        self.wait(10)
        
        self.play(FadeOut(VGroup(
            eq_c, c_texto, c_valor, grafico_c,
            eixo, axes, labels
        )))        
        
        
        
config.pixel_height = 1920 
config.pixel_width = 1080   
config.frame_height = 16.0 
config.frame_width = 9.0 




class VerticeParabola(Scene):
    def construct(self):
        
        titulo = Text("Vértice da Parábola", font_size=42).to_edge(UP).set_color_by_gradient(BLUE, WHITE)
        instagram = Tex('@CelestialEquations').scale(0.5).shift(6*DOWN).set_color_by_gradient(BLUE, WHITE)
        self.add(instagram)
        self.play(Write(titulo))
        self.wait(1)
        
       
        definicao = Text("O vértice é o ponto máximo ou mínimo da parábola", font_size=28)
        definicao.next_to(titulo, DOWN)
        self.play(Write(definicao))
        self.wait(2)
        texto = Text("Dedução dessas Equações em BREVE", font_size=28).shift(3.5*DOWN).set_color(RED)
        
        
        formulas = VGroup(
            MathTex(r"x_v = \frac{-b}{2a}"),
            MathTex(r"y_v = f(x_v) = \frac{-\Delta}{4a}"),
            MathTex(r"\Delta = b^2 - 4ac")
        ).arrange(DOWN).next_to(definicao, 2*DOWN, buff=0.8).set_color_by_gradient(BLUE, WHITE)
        
        for formula in formulas:
            self.play(Write(formula))
            self.wait(2)
        
        self.wait(5)
        self.play(Write(texto))
        self.wait(5)
        self.play(FadeOut(definicao), FadeOut(formulas), FadeOut(texto))
        
        
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-2, 6, 1],
            axis_config={"include_tip": True},
        ).scale(0.8)
        
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        self.play(Create(axes), Write(labels))
        
        
        funcao = lambda x: 2*x**2 - 4*x + 1
        grafico = axes.plot(funcao, color=BLUE, x_range=[-1, 4])
        eq = MathTex(r"f(x) = 2x^2 - 4x + 1", font_size = 35).shift(5.5*UP+LEFT).set_color_by_gradient(BLUE, WHITE)
        
        self.play(Write(eq))
        self.play(Create(grafico))
        self.wait(1)
        self.play(FadeOut(titulo))

        grafico = VGroup(grafico, axes, labels)

        
        
        t = ValueTracker(-1)
        
        dot = Dot(color=RED)
        dot.add_updater(lambda d: d.move_to(axes.c2p(t.get_value(), funcao(t.get_value()))))
        
        coord_text = MathTex(r"(x, f(x))").add_background_rectangle()
        coord_text.add_updater(
            lambda c: c.become(
                MathTex(
                    r"(" + str(round(t.get_value(), 2)) + ", " + 
                    str(round(funcao(t.get_value()), 2)) + ")"
                ).add_background_rectangle().next_to(dot, UP)
            )
        )
        
        self.play(Create(dot))
        self.play(t.animate.set_value(4), run_time=6, rate_func=linear)
        self.wait(2)

        self.play(grafico.animate.shift(2*LEFT).scale(0.7))
        self.wait(3)
        
      
        calculo_x_1 = MathTex(
            r"x_v = \frac{-b}{2a}"
        ).shift(DOWN * 2)

        calculo_x_2 = MathTex(r"x_v =\frac{-(-4)}{2 \cdot 2} ").shift(DOWN * 2)
        calculo_x_3 = MathTex(r"x_v = \frac{4}{4}").shift(DOWN * 2)
        calculo_x_4 = MathTex(r"x_v = 1").shift(DOWN * 2)

        framebox_1 = SurroundingRectangle(calculo_x_4, buff=0.1, color = BLUE)
        
        
        self.play(Write(calculo_x_1))
        self.wait(2)
        self.play(ReplacementTransform(calculo_x_1, calculo_x_2))
        self.wait(2)
        self.play(ReplacementTransform(calculo_x_2, calculo_x_3))
        self.wait(2)
        self.play(ReplacementTransform(calculo_x_3, calculo_x_4))
        self.wait(3)
        self.play(Create(framebox_1))
        self.wait(2)
        
        calculo_y_1 = MathTex(
            r"y_v = f(1)"
        ).next_to(calculo_x_1, DOWN)

        calculo_y_2 = MathTex(r"y_v = 2 \cdot 1^2 - 4 \cdot 1 + 1 ").next_to(calculo_x_1, DOWN)
        calculo_y_3 = MathTex(r"y_v = 2-4+1").next_to(calculo_x_1, DOWN)
        calculo_y_4 = MathTex(r"y_v = -1").next_to(calculo_x_1, DOWN)
        framebox_2 = SurroundingRectangle(calculo_y_4, buff=0.1, color = WHITE)

        
        self.play(Write(calculo_y_1))
        self.wait(2)
        self.play(ReplacementTransform(calculo_y_1, calculo_y_2))
        self.wait(2)
        self.play(ReplacementTransform(calculo_y_2, calculo_y_3))
        self.wait(2)
        self.play(ReplacementTransform(calculo_y_3, calculo_y_4))
        self.wait(2)
        self.play(Create(framebox_2))
        self.wait(2)
        
   
        vertice = Dot(axes.c2p(1, -1), color=RED, radius=0.1)
        vertice_text = MathTex(r"V(1, -1)").next_to(vertice, UP).scale(0.8)
        
        self.play(t.animate.set_value(1))
        self.play(
            ReplacementTransform(dot, vertice),
            
            Write(vertice_text)
        )
        
 
        destaque = Circle(radius=0.2, color=YELLOW).move_to(vertice.get_center())
        self.play(Create(destaque))
        self.play(destaque.animate.scale(1.5), rate_func=there_and_back)
        self.wait(20)
        
        self.play(FadeOut(VGroup(
             eq, calculo_x_4, calculo_y_4, grafico, 
            vertice, vertice_text, destaque, axes, labels
        )))


config.pixel_height = 1920 
config.pixel_width = 1080   
config.frame_height = 16.0 
config.frame_width = 9.0 




class ZerosFuncao(Scene):
    def construct(self):
        
        titulo = Tex("Raizes da Função Quadrática", font_size=42).to_edge(UP).set_color_by_gradient(BLUE, WHITE)
        instagram = Tex('@CelestialEquations').scale(0.5).shift(6*DOWN).set_color_by_gradient(BLUE, WHITE)
        self.add(instagram)
        self.play(Write(titulo))
        self.wait(1)
        
        
        definicao = Text("Os zeros são os valores de x para os quais f(x) = 0", font_size=28).set_color_by_gradient(BLUE, WHITE)
        definicao.next_to(titulo, DOWN)
        self.play(Write(definicao))
        self.wait(7)
        
       
        formula = MathTex(r"x = \frac{-b \pm \sqrt{\Delta}}{2a}, \quad \Delta = b^2 - 4ac").set_color_by_gradient(BLUE, WHITE)
        formula.next_to(definicao, DOWN, buff=0.8)
        self.play(Write(formula))
        self.wait(10)
        
        self.play(FadeOut(definicao), FadeOut(formula))
        
        
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-2, 6, 1],
            axis_config={"include_tip": True},
        ).scale(0.8)
        
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        self.play(Create(axes), Write(labels))
        
        #
        funcao = lambda x: 2*x**2 - 4*x + 1
        grafico = axes.plot(funcao, color=BLUE, x_range=[-1, 4])
        eq = MathTex(r"f(x) = 2x^2 - 4x + 1").shift(3.5*DOWN).set_color_by_gradient(BLUE, WHITE)
        
        self.play(Write(eq))
        self.wait(1)
        self.play(Create(grafico))
        self.wait(1)
        
       
        
        delta = MathTex(r"\Delta = b^2 - 4ac").shift(UP*5).set_color_by_gradient(BLUE, WHITE)
        delta_2 = MathTex(r"\Delta = (-4)^2 - 4 \cdot 2 \cdot 1").shift(UP*5).set_color_by_gradient(BLUE, WHITE)
        delta_3 = MathTex(r"\Delta = 8").shift(5*UP).set_color_by_gradient(BLUE, WHITE)
        
        self.play(Write(delta))
        self.wait(4)
        self.play(ReplacementTransform(delta, delta_2))
        self.wait(4)
        self.play(ReplacementTransform(delta_2, delta_3))
        self.wait(4)
        self.play(eq.animate.next_to(delta_3, DOWN))
        self.wait(5)

        
    
        
        
        
        x1 = MathTex(r"x_1 = \frac{-(-4) + \sqrt{8}}{2 \cdot 2}").set_color_by_gradient(BLUE, WHITE).shift(3.3*DOWN)
        x1_2 =   MathTex(r"x_1 = \frac{4 + 2,83}{4} \approx 1,71").set_color_by_gradient(BLUE, WHITE).shift(3.3*DOWN)
        self.play(Write(x1))
        self.wait(2)
        self.play(ReplacementTransform(x1, x1_2))
        self.wait(2)
        
        
        x2= MathTex(r"x_2 = \frac{-(-4) - \sqrt{8}}{2 \cdot 2}").shift(4.5*DOWN).set_color_by_gradient(BLUE, WHITE)
        x2_2 =MathTex(r"x_2 = \frac{4 - 2,83}{4} \approx 0,29").shift(4.5*DOWN).set_color_by_gradient(BLUE, WHITE)
        
        self.play(Write(x2))
        self.wait(2)
        self.play(ReplacementTransform(x2, x2_2))
        self.wait(2)
        
        
        
        
        zero1 = Dot(axes.c2p(0.29, 0), color=RED)
        zero2 = Dot(axes.c2p(1.71, 0), color=RED)
        
        zero1_text = MathTex(r"x_1 \approx 0,29", font_size = 30).next_to(zero1, UP+RIGHT)
        zero2_text = MathTex(r"x_2 \approx 1,71", font_size = 30).next_to(zero2, UP+2*RIGHT)
        
        self.play(
            Create(zero1),
            Create(zero2),
            Write(zero1_text),
            Write(zero2_text)
        )
        self.wait(7)
        
        
        self.play(FadeOut(VGroup(
            zero1_text, zero2_text, x1_2, x2_2, x1, x2, eq, grafico, axes, labels, zero1, zero2, delta_3
        )))
        
        
        analise_titulo = Text("Análise do Discriminante", font_size=32)
        analise_titulo.shift(UP*2)
        self.play(Write(analise_titulo))
        
        casos = VGroup(
            Text("• Δ > 0: duas raízes reais distintos", font_size=24),
            Text("• Δ = 0: uma raiz real (raiz dupla)", font_size=24),
            Text("• Δ < 0: sem raizes reais", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(analise_titulo, DOWN, buff=0.5)
        
        for caso in casos:
            self.play(Write(caso))
            self.wait(2)
        
        self.wait()
        
        self.wait(10)
        self.play(FadeOut(VGroup(
            casos, analise_titulo
            
        )))
        
       
        axes_novos = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 6, 1],
            axis_config={"include_tip": True},
        ).scale(0.8)
        
        labels_novos = axes_novos.get_axis_labels(x_label="x", y_label="f(x)")
        self.play(Create(axes_novos), Write(labels_novos))
        
        
        f1 = lambda x: x**2 - x - 2  
        g1 = axes_novos.plot(f1, color=BLUE, x_range=[-4, 4])
        eq1 = MathTex(r"f(x) = x^2 - x -2").next_to(titulo, 3*DOWN).set_color_by_gradient(BLUE, WHITE)
        delta1 = MathTex(r"\Delta > 0 \Rightarrow \text{Duas raízes reais}").shift(3.5*DOWN)
        
        self.play(Write(eq1), Write(delta1))
        self.play(Create(g1))
        
        
        r1 = Dot(axes_novos.c2p(-1, 0), color=GREEN)
        r2 = Dot(axes_novos.c2p(2, 0), color=GREEN)
        self.play(Create(r1), Create(r2))
        self.wait(3)
        
        self.play(FadeOut(g1), FadeOut(r1), FadeOut(r2), FadeOut(eq1), FadeOut(delta1))
        
        
        f2 = lambda x: x**2 - 2*x + 1  # tem uma raiz (x=1)
        g2 = axes_novos.plot(f2, color=PURPLE, x_range=[-4, 4])
        eq2 = MathTex(r"f(x) = x^2 - 2x + 1").next_to(titulo, 3*DOWN).set_color_by_gradient(PURPLE, WHITE)
        delta2 = MathTex(r"\Delta = 0 \Rightarrow \text{Uma raiz real (duplicidade)}").shift(3.5*DOWN)
        
        self.play(Write(eq2))
        self.wait(1)
        self.play(Write(delta2))
        self.play(Create(g2))
        
      
        r = Dot(axes_novos.c2p(1, 0), color=GREEN, radius=0.1)
        self.play(Create(r))
        self.wait(2)
        
        self.play(FadeOut(g2), FadeOut(r), FadeOut(eq2), FadeOut(delta2))
        
     
        f3 = lambda x: x**2 + 1  # não tem raízes reais
        g3 = axes_novos.plot(f3, color=RED, x_range=[-4, 4])
        eq3 = MathTex(r"f(x) = x^2 + 1").next_to(titulo, 3*DOWN).set_color_by_gradient(RED, WHITE)
        delta3 = MathTex(r"\Delta < 0 \Rightarrow \text{Sem raízes reais}").shift(3.5*DOWN)
        
        self.play(Write(eq3))
        self.wait(1)
        self.play(Write(delta3))
        self.play(Create(g3))
        self.wait(5)
        
        self.play(FadeOut(VGroup(
            titulo, eq3, delta3, g3, axes_novos, labels_novos
        )))


config.pixel_height = 1920 
config.pixel_width = 1080   
config.frame_height = 16.0 
config.frame_width = 9.0 

class AplicacoesPropriedades(Scene):
    def construct(self):
        instagram = Tex('@CelestialEquations').scale(0.5).shift(5.5*UP).set_color_by_gradient(BLUE, WHITE)
        titulo = Text("Concavidade Da Parábola", font_size=42).to_edge(UP).set_color_by_gradient(BLUE, RED)
        self.add(instagram)
        self.play(Write(titulo))
        self.wait(1)
    
       
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            axis_config={"include_tip": True},
        ).scale(0.8)
        
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        self.play(Create(axes), Write(labels))
        
       
        f_up = lambda x: 0.5*x**2
        g_up = axes.plot(f_up, color=BLUE, x_range=[-4, 4])
        eq_up = MathTex(r"f(x) = 0.5x^2 \quad (a > 0)").shift(4*DOWN).set_color(BLUE)
        conc1 = Text("Concavidade para cima", font_size=25).next_to(eq_up, DOWN).set_color(BLUE)
        
        self.play(Write(eq_up))
        self.play(Create(g_up))
        self.wait(1)
        self.play(Write(conc1))
        self.wait(2)
        
        
        
        
        self.play(FadeOut(VGroup(
            g_up, eq_up, conc1
        )))

        self.wait(2)
        
        f_down = lambda x: -0.5*x**2
        g_down = axes.plot(f_down, color=RED, x_range=[-4, 4])
        eq_down = MathTex(r"f(x) = -0.5x^2 \quad (a < 0)").shift(4*UP).set_color(RED)
        conc2 = Text("Concavidade para baixo", font_size=30).shift(4*DOWN).set_color(RED)
        
        self.play(Write(eq_down))
        self.play(Create(g_down))
        self.wait(1)
        self.play(Write(conc2))
        self.wait(2)
    
        self.wait(2)
        
        self.play(FadeOut(VGroup(
            g_down, eq_down, conc2 
        )))
        
    

