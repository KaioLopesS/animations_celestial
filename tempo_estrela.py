from manim import *
import numpy as np
import random


config.pixel_height = 1920 
config.pixel_width = 1080   
config.frame_height = 16.0 
config.frame_width = 9.0 

class LimiteSchenbergChandrasekhar(Scene):
    def construct(self):
        titulo = Tex("Como Calcular o Tempo de Vida de uma Estrela?", font_size=35).set_color_by_gradient(WHITE, GREEN)
        instagram = Tex('@CelestialEquations').scale(0.7).shift(5*UP).set_color_by_gradient(WHITE, GREEN)
        
        
        estrelas_fundo = VGroup(*[
        Dot(point=[np.random.uniform(-config.frame_width/2, config.frame_width/2), 
               np.random.uniform(-config.frame_height/2, config.frame_height/2), 0], 
        radius=np.random.uniform(0.01, 0.05),
        color=WHITE)
        for i in range(300) 
        ])
        
       
        estrela = Circle(radius=1.5, color=GREEN, fill_opacity=0.8)
        
        self.play(FadeIn(estrelas_fundo, run_time=1))
        self.play(Write(titulo))
        self.play(Write(instagram))
        self.wait(1.5)
        self.play(titulo.animate.shift(UP*3))
        self.wait(1)
        self.play(Create(estrela))
        
        
        
        self.play(
            estrela.animate.scale(1.1),
            rate_func=there_and_back,
            run_time=1.5
        )
        self.play(
            estrela.animate.scale(1.1),
            rate_func=there_and_back,
            run_time=1.5
        )
        
        texto_intro = Text(
            "Para entender isso, precisamos conhecer\ncomo as estrelas utilizam seu combustível",
            font_size=28
        ).set_color_by_gradient(WHITE, GREEN)
        texto_intro.next_to(estrela, DOWN, buff=0.7)
        
        self.play(Write(texto_intro)) 
        self.wait(1.5)
        
        
        
        self.play(
            FadeOut(texto_intro),
            FadeOut(estrela),
            FadeOut(titulo)
        )
        
        
        titulo_eq = Text("O princípio da Equivalência Massa-Energia", font_size=26).shift(3*UP).set_color_by_gradient(WHITE, GREEN)
        
        eq_emc2 = MathTex("E = mc^2", font_size=39).set_color(BLUE)
        eq_emc2.next_to(titulo_eq, DOWN, buff=0.6)
        
        texto_fusao = Text(
            "Em uma estrela, parte da massa é convertida\nem energia através da fusão nuclear",
            font_size=25
        ).set_color_by_gradient(WHITE, BLUE)
        texto_fusao.next_to(eq_emc2, DOWN, buff=0.7)
        
        
        nucleos = VGroup()
        for i in range(4):
            nucleo = Circle(radius=0.2, color=BLUE, fill_opacity=0.8)
            nucleo.move_to([-3 + 2*i, -2, 0])
            texto_h = Text(".", font_size=24).move_to(nucleo.get_center()).set_color(BLUE)
            nucleos.add(VGroup(nucleo, texto_h))
        
        self.play(Write(titulo_eq))
        self.wait(6)
        self.play(Write(eq_emc2))
        self.wait(5)
        self.play(Write(texto_fusao))
        self.wait(3)
        self.play(FadeIn(nucleos))
        
        
        self.play(
            *[nucleos[i].animate.move_to([0, -2, 0]) for i in range(len(nucleos))],
            run_time=2
        )
        
        
        flash_circle = Circle(radius=0.1, color=YELLOW, fill_opacity=1).move_to([0, -2, 0])
        energia_text = Text("Hélio", color=BLUE, font_size=30).move_to([1, -2, 0])
        
        self.play(
            flash_circle.animate.scale(15).set_opacity(0),
            rate_func=rush_into,
            run_time=1
        )
        self.play(Write(energia_text))
        
        self.wait(1.5)
        self.play(
            FadeOut(nucleos),
            FadeOut(energia_text),
            FadeOut(titulo_eq),
            FadeOut(eq_emc2),
            FadeOut(texto_fusao)
        )
        
        
        titulo_efic = Text("A Eficiência da Conversão", font_size=30).shift(3.5*UP).set_color_by_gradient(WHITE, GREEN)
        
        
        destaque_07 = Text(
            "0,7% = 7 milésimos da massa que entra na reação\né transformada em energia",
            font_size=25
        ).set_color_by_gradient(WHITE, GREEN)
        destaque_07.next_to(titulo_efic, DOWN, buff=0.6)
        
        
        
        self.play(Write(titulo_efic))
        self.play(Write(destaque_07))
        self.wait(2)
        
        texto_energia = Text(
            "Embora pareça pouco, esta pequena fração representa\numa quantidade enorme de energia",
            font_size=25
        ).set_color_by_gradient(WHITE, GREEN)
        texto_energia.next_to(destaque_07, DOWN, buff=0.7)
        
        self.play(Write(texto_energia))
        self.wait(4.5)
        
        self.play(
            FadeOut(titulo_efic),
            FadeOut(destaque_07),
            FadeOut(texto_energia)
        )
        
        
        titulo_nucleo = Text("O Núcleo Estelar", font_size=36).shift(3.5*UP).set_color_by_gradient(WHITE, GREEN)
        
        
        estrela_corte = VGroup()
        nucleo_raio = 0.8
        estrela_raio = 3
        
        nucleo = Circle(radius=nucleo_raio, color=YELLOW, fill_opacity=1)
        camada1 = Annulus(inner_radius=nucleo_raio, outer_radius=1.5, color=ORANGE, fill_opacity=0.7)
        camada2 = Annulus(inner_radius=1.5, outer_radius=2.2, color="#FF8C00", fill_opacity=0.5)
        camada3 = Annulus(inner_radius=2.2, outer_radius=estrela_raio, color="#FFD700", fill_opacity=0.3)
        
        estrela_corte.add(nucleo, camada1, camada2, camada3)
        
        texto_nucleo = Text(
            "Apenas no núcleo a estrela atinge temperaturas\n suficientemente altas (8 milhões K)",
            font_size=26
        ).shift(3.5*DOWN).set_color_by_gradient(WHITE, GREEN)
        
        
        
        
        self.play(Write(titulo_nucleo))
        self.play(Create(estrela_corte))
        self.wait(4)
        self.play(Write(texto_nucleo))
       
        
    
        
        self.wait(3)
        self.play(
            FadeOut(titulo_nucleo),
            FadeOut(estrela_corte),
            FadeOut(texto_nucleo)
        )
        
        
        titulo_limite = Text("O Limite de Schenberg-Chandrasekhar", font_size=30).shift(3.5*UP).set_color_by_gradient(WHITE, GREEN)
        
        
        destaque_10 = Text(
            "Apenas 10% da massa\n da estrela contribui para\n a geração de energia",
            font_size=25
        )
        destaque_10.shift(4*DOWN)
        
        
        estrela_completa = Circle(radius=3, color=YELLOW, fill_opacity=0.3)
        nucleo_destacado = Circle(radius=0.95, color=ORANGE, fill_opacity=0.8)
        titulo_bio = Text("Mário Schenberg (1914-1990)", font_size=36).shift(5*DOWN)
        
        
        
        
        
        
        self.play(Write(titulo_limite))
        self.play(Create(estrela_completa))
        self.wait(1)
        self.play(Write(destaque_10))
        self.wait(1)
        self.play(Create(nucleo_destacado))
        self.wait(2)
        self.play(Write(titulo_bio))
        
        self.wait(7)
        self.play(
            FadeOut(titulo_limite),
            FadeOut(estrela_completa),
            FadeOut(nucleo_destacado),
            FadeOut(destaque_10),
            FadeOut(titulo_bio)

        )
        
        
        titulo_tempo = Text("Cálculo do Tempo de Vida de uma estrela", font_size=30).shift(3*UP).set_color_by_gradient(WHITE, GREEN)
        
        
        formula = MathTex(
            r"\text{Tempo de vida} \approx \frac{10\% \times \text{Massa total} \times 0.7\% \times c^2}{\text{Luminosidade}}",
            font_size=29
        ).set_color_by_gradient(GREEN, WHITE)
        framebox = SurroundingRectangle(formula, buff=0.1, color=GREEN)
        
        self.play(Write(titulo_tempo))
        self.wait(1)
        self.play(Write(formula))
        self.wait(2)
        self.play(Create(framebox))
        self.wait(13)



        
        
        self.play(
            FadeOut(formula),
            FadeOut(framebox)
        )
        
        titulo_sol = Text("Exemplo: Tempo de vida do Sol", font_size=36).set_color_by_gradient(WHITE, YELLOW).shift(3.5*UP)
        
        
        
        sol = Circle(radius=2, color=YELLOW, fill_opacity=0.8)
        
        
        dados_sol = VGroup(
            Text("Massa do Sol: 2 x 10^30 kg", font_size=28),
            Text("Luminosidade: 3,8 x 10^26 W", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).set_color_by_gradient(WHITE, YELLOW)
        dados_sol.shift(3.5*DOWN)
        
        self.play(ReplacementTransform(titulo_tempo, titulo_sol))
        self.play(Create(sol))
        self.play(Write(dados_sol), run_time=2)
        self.wait(9)
        
        
        self.play(FadeOut(dados_sol))
        
    
        
        resultado1 = MathTex(
            r"\text{Tempo de vida} = \frac{\text{Energia disponível}}{\text{Luminosidade}} = \frac{1,26 \times 10^{44} \text{ J}}{3,8 \times 10^{26} \text{ W}}",
            font_size=33
        ).set_color_by_gradient(WHITE, YELLOW).shift(3.5*DOWN)
        
        resultado2 = MathTex(
            r"\text{Tempo de vida}= \frac{1,26 \times 10^{44} \text{ J}}{3,8 \times 10^{26} \text{ J/s}} = 3,3 \times 10^{17} \text{ s}",
            font_size=33
        ).set_color_by_gradient(WHITE, YELLOW).shift(3.5*DOWN)
        
        resultado3 = MathTex(
            r"\text{Tempo de vida}= 3,3 \times 10^{17} \text{ s} \times \frac{1 \text{ ano}}{3,15 \times 10^7 \text{ s}}",
            font_size=33
        ).set_color_by_gradient(WHITE, YELLOW).shift(3.5*DOWN)

        resultado4 = MathTex(
            r"\text{Tempo de vida} \approx 10^{10} \text{ anos}",
            font_size=33
        ).set_color_by_gradient(WHITE, YELLOW).shift(3.5*DOWN)

        framebox2 = SurroundingRectangle(resultado4, buff=0.1, color=YELLOW)
        
        self.play(Write(resultado1))
        self.wait(5)
        self.play(ReplacementTransform(resultado1,resultado2))
        self.wait(5)
        self.play(ReplacementTransform(resultado2, resultado3))
        self.wait(8)
        self.play(ReplacementTransform(resultado3, resultado4))
        self.wait(5)
        self.play(Create(framebox2))
        self.wait(10)
        
       