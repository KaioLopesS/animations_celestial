from manim import *

class DilatacaoTemporal(Scene):
    def construct(self):
        # Introdução com pergunta engajadora
        title = Text("O tempo passa igual para todos?", font_size=48)
        subtitle = Text("A fascinante dilatação temporal de Einstein", font_size=36)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.wait(2)
        self.play(Write(subtitle))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Apresentação da analogia
        analogia_texto = Text("Imagine uma lanterna em um trem em alta velocidade...", font_size=32)
        self.play(Write(analogia_texto))
        self.wait(2)
        self.play(FadeOut(analogia_texto))
        
        # Criação do trem
        trem = Rectangle(height=2, width=5, color=BLUE)
        vagao_interno = Rectangle(height=1.5, width=4.5, color=WHITE)
        vagao_interno.move_to(trem.get_center())
        trem_completo = VGroup(trem, vagao_interno)
        trem_completo.move_to(ORIGIN)
        
        # Observador dentro do trem
        observador_trem = Dot(color=RED).move_to(trem.get_center())
        observador_trem_label = Text("Alice", font_size=24, color=RED)
        observador_trem_label.next_to(observador_trem, DOWN, buff=0.2)
        
        # Lanterna no teto do trem
        lanterna = Triangle(color=YELLOW, fill_opacity=1).scale(0.2)
        lanterna.move_to(trem.get_center() + UP*0.5)
        lanterna.rotate(PI)  # Apontando para baixo
        
        # Detector no piso do trem
        detector = Rectangle(width=0.5, height=0.1, color=YELLOW)
        detector.move_to(trem.get_center() + DOWN*0.5)
        
        # Criação do cenário
        trilhos = Line(LEFT*7, RIGHT*7, color=GRAY)
        trilhos.next_to(trem, DOWN, buff=1)
        
        # Observador externo
        observador_externo = Dot(color=GREEN).move_to(DOWN*3 + RIGHT*3)
        observador_externo_label = Text("Bob", font_size=24, color=GREEN)
        observador_externo_label.next_to(observador_externo, DOWN, buff=0.2)
        
        # Adicionando elementos à cena
        self.play(
            Create(trilhos),
            Create(trem_completo),
            Create(observador_trem),
            Write(observador_trem_label),
            Create(observador_externo),
            Write(observador_externo_label),
            Create(lanterna),
            Create(detector)
        )
        self.wait(2)
        
        # Explicação do experimento com a lanterna
        explicacao = Text("Alice aciona uma lanterna no teto do vagão", font_size=28)
        explicacao.to_edge(UP)
        self.play(Write(explicacao))
        self.wait(2)
        
        # Visão de Alice (observadora dentro do trem)
        visao_alice = Text("Como Alice vê o raio de luz:", font_size=28)
        visao_alice.to_edge(UP)
        
        self.play(ReplacementTransform(explicacao, visao_alice))
        self.wait(1)
        
        # Raio de luz vertical (visão de Alice)
        raio_vertical = DashedLine(lanterna.get_center(), detector.get_center(), color=YELLOW)
        
        # Animação do pulso de luz vertical
        pulso = Dot(color=YELLOW, radius=0.1)
        pulso.move_to(lanterna.get_center())
        self.play(Create(raio_vertical, run_time=0.5))
        self.add(pulso)
        
        # Trajetória simples vertical
        self.play(
            pulso.animate.move_to(detector.get_center()),
            run_time=1.5
        )
        self.wait(1)
        
        # Equação do tempo para Alice
        tempo_alice = MathTex(r"\Delta t' = \frac{d}{c}")
        tempo_alice.next_to(visao_alice, DOWN)
        self.play(Write(tempo_alice))
        self.wait(2)
        
        # Limpando para mostrar a visão de Bob
        self.play(
            FadeOut(pulso),
            FadeOut(raio_vertical),
            FadeOut(tempo_alice),
            FadeOut(visao_alice)
        )
        
        # Visão de Bob (observador externo)
        visao_bob = Text("Como Bob vê o mesmo raio de luz:", font_size=28)
        visao_bob.to_edge(UP)
        self.play(Write(visao_bob))
        self.wait(1)
        
        # Movimento do trem durante a emissão do raio
        trem_inicial = trem_completo.copy()
        trem_inicial.set_color(BLUE_E).set_opacity(0.5)
        
        # Animação do movimento do trem
        self.play(
            trem_completo.animate.shift(RIGHT*2),
            run_time=2
        )
        
        # Mostrar a posição inicial do trem
        self.play(Create(trem_inicial))
        
        # Marcando o ponto inicial (lanterna) e final (detector) para Bob
        ponto_inicial = Dot(color=YELLOW).move_to(trem_inicial.get_center() + UP*0.5)
        ponto_final = Dot(color=YELLOW).move_to(trem_completo.get_center() + DOWN*0.5)
        
        # Trajetória diagonal do raio de luz (visão de Bob)
        raio_diagonal = DashedLine(ponto_inicial.get_center(), ponto_final.get_center(), color=YELLOW)
        
        self.play(
            Create(ponto_inicial),
            Create(ponto_final),
            Create(raio_diagonal)
        )
        self.wait(1.5)
        
        # Destacando o triângulo retângulo formado
        triangulo = Polygon(
            ponto_inicial.get_center(),
            ponto_final.get_center(),
            ponto_final.get_center() + LEFT*2,
            color=WHITE
        )
        
        # Pythagorean triangle
        self.play(Create(triangulo))
        self.wait(1)
        
        # Aplicando o teorema de Pitágoras
        pitagoras_title = Text("Aplicando o Teorema de Pitágoras", font_size=28)
        pitagoras_title.to_edge(UP)
        
        self.play(
            FadeOut(visao_bob),
            Write(pitagoras_title)
        )
        self.wait(1)
        
        # Destacando os lados do triângulo
        cateto_vertical = Line(
            ponto_final.get_center() + LEFT*2,
            ponto_final.get_center(),
            color=RED
        )
        cateto_horizontal = Line(
            ponto_inicial.get_center(),
            ponto_final.get_center() + LEFT*2,
            color=GREEN
        )
        hipotenusa = Line(
            ponto_inicial.get_center(),
            ponto_final.get_center(),
            color=YELLOW
        )
        
        self.play(
            Create(cateto_vertical),
            Create(cateto_horizontal),
            Create(hipotenusa)
        )
        self.wait(1)
        
        # Rótulos dos lados
        d_label = MathTex("d", color=RED)
        d_label.next_to(cateto_vertical, RIGHT)
        
        v_t_label = MathTex("v \cdot \Delta t", color=GREEN)
        v_t_label.next_to(cateto_horizontal, DOWN)
        
        c_t_label = MathTex("c \cdot \Delta t", color=YELLOW)
        c_t_label.next_to(hipotenusa, UP+RIGHT, buff=0.3)
        
        self.play(
            Write(d_label),
            Write(v_t_label),
            Write(c_t_label)
        )
        self.wait(2)
        
        # Fórmulas matemáticas usando Pitágoras
        pitagoras_eq = MathTex(r"(c \cdot \Delta t)^2 = d^2 + (v \cdot \Delta t)^2")
        pitagoras_eq.to_edge(DOWN, buff=1.5)
        
        self.play(Write(pitagoras_eq))
        self.wait(1.5)
        
        # Manipulação algébrica
        eq1 = MathTex(r"c^2 \cdot \Delta t^2 = d^2 + v^2 \cdot \Delta t^2")
        eq1.to_edge(DOWN, buff=1.5)
        
        self.play(ReplacementTransform(pitagoras_eq, eq1))
        self.wait(1)
        
        eq2 = MathTex(r"c^2 \cdot \Delta t^2 - v^2 \cdot \Delta t^2 = d^2")
        eq2.to_edge(DOWN, buff=1.5)
        
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(1)
        
        eq3 = MathTex(r"\Delta t^2 \cdot (c^2 - v^2) = d^2")
        eq3.to_edge(DOWN, buff=1.5)
        
        self.play(ReplacementTransform(eq2, eq3))
        self.wait(1)
        
        eq4 = MathTex(r"\Delta t^2 = \frac{d^2}{c^2 - v^2}")
        eq4.to_edge(DOWN, buff=1.5)
        
        self.play(ReplacementTransform(eq3, eq4))
        self.wait(1)
        
        # Relação com o tempo próprio
        eq5 = MathTex(r"\Delta t' = \frac{d}{c}")
        eq5.to_edge(DOWN, buff=2.5)
        
        self.play(Write(eq5))
        self.wait(1)
        
        # Quadrando a equação do tempo próprio
        eq6 = MathTex(r"\Delta t'^2 = \frac{d^2}{c^2}")
        eq6.to_edge(DOWN, buff=2.5)
        
        self.play(ReplacementTransform(eq5, eq6))
        self.wait(1)
        
        # Isolando d²
        eq7 = MathTex(r"d^2 = c^2 \cdot \Delta t'^2")
        eq7.to_edge(DOWN, buff=2.5)
        
        self.play(ReplacementTransform(eq6, eq7))
        self.wait(1)
        
        # Substituindo na equação
        eq8 = MathTex(r"\Delta t^2 = \frac{c^2 \cdot \Delta t'^2}{c^2 - v^2}")
        eq8.to_edge(DOWN, buff=1.5)
        
        self.play(
            ReplacementTransform(eq4, eq8),
            FadeOut(eq7)
        )
        self.wait(1.5)
        
        # Simplificando
        eq9 = MathTex(r"\Delta t^2 = \Delta t'^2 \cdot \frac{c^2}{c^2 - v^2}")
        eq9.to_edge(DOWN, buff=1.5)
        
        self.play(ReplacementTransform(eq8, eq9))
        self.wait(1)
        
        eq10 = MathTex(r"\Delta t^2 = \Delta t'^2 \cdot \frac{1}{1 - \frac{v^2}{c^2}}")
        eq10.to_edge(DOWN, buff=1.5)
        
        self.play(ReplacementTransform(eq9, eq10))
        self.wait(1.5)
        
        # Tirando a raiz quadrada
        eq11 = MathTex(r"\Delta t = \Delta t' \cdot \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}")
        eq11.to_edge(DOWN, buff=1.5)
        
        self.play(ReplacementTransform(eq10, eq11))
        self.wait(1.5)
        
        # Limpando a cena para mostrar o resultado final
        self.play(
            FadeOut(triangulo),
            FadeOut(cateto_vertical),
            FadeOut(cateto_horizontal),
            FadeOut(hipotenusa),
            FadeOut(d_label),
            FadeOut(v_t_label),
            FadeOut(c_t_label),
            FadeOut(trem_inicial),
            FadeOut(ponto_inicial),
            FadeOut(ponto_final),
            FadeOut(raio_diagonal),
            FadeOut(pitagoras_title)
        )
        
        # Fórmula final da dilatação temporal
        formula_final = MathTex(r"\Delta t = \frac{\Delta t'}{\sqrt{1 - \frac{v^2}{c^2}}}")
        formula_final.scale(1.5)
        formula_final.move_to(ORIGIN)
        
        self.play(
            ReplacementTransform(eq11, formula_final)
        )
        self.wait(2)
        
        # Explicação final do significado físico
        gamma = MathTex(r"\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}")
        gamma.next_to(formula_final, DOWN, buff=0.7)
        
        conclusao = Text("O tempo passa mais devagar para observadores em movimento!", font_size=32)
        conclusao.next_to(gamma, DOWN, buff=0.7)
        
        self.play(Write(gamma))
        self.wait(1.5)
        self.play(Write(conclusao))
        self.wait(3)
        
        # Implicações práticas
        implicacoes = Text("Na prática, isso significa que...", font_size=32)
        implicacoes.to_edge(UP)
        
        self.play(
            FadeOut(formula_final),
            FadeOut(gamma),
            FadeOut(conclusao),
            Write(implicacoes)
        )
        
        # Relógios em movimento
        relogio_texto = Text("• Relógios em movimento marcam o tempo mais lentamente", font_size=26)
        relogio_texto.next_to(implicacoes, DOWN, buff=0.5)
        
        # Viajante espacial
        viajante_texto = Text("• Um viajante espacial em alta velocidade envelhece menos", font_size=26)
        viajante_texto.next_to(relogio_texto, DOWN, buff=0.3)
        
        # GPS
        gps_texto = Text("• O GPS precisa corrigir este efeito para funcionar corretamente", font_size=26)
        gps_texto.next_to(viajante_texto, DOWN, buff=0.3)
        
        self.play(Write(relogio_texto))
        self.wait(1)
        self.play(Write(viajante_texto))
        self.wait(1)
        self.play(Write(gps_texto))
        self.wait(2.5)
        
        # Mensagem final
        self.play(
            FadeOut(implicacoes),
            FadeOut(relogio_texto),
            FadeOut(viajante_texto),
            FadeOut(gps_texto),
            FadeOut(trem_completo),
            FadeOut(trilhos),
            FadeOut(observador_trem),
            FadeOut(observador_trem_label),
            FadeOut(observador_externo),
            FadeOut(observador_externo_label),
            FadeOut(lanterna),
            FadeOut(detector)
        )
        
        mensagem_final = Text("Einstein revolucionou nossa compreensão do tempo", font_size=36)
        mensagem_final.move_to(ORIGIN)
        
        self.play(Write(mensagem_final))
        self.wait(2)
        
        pergunta_final = Text("E você, já pensou que seu tempo pode passar diferente do meu?", font_size=32)
        pergunta_final.next_to(mensagem_final, DOWN, buff=0.8)
        
        self.play(Write(pergunta_final))
        self.wait(5)
        
        # Fade out final
        self.play(
            FadeOut(mensagem_final),
            FadeOut(pergunta_final)
        )