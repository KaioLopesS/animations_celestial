from manim import *
import random
class cinematicaconceito(Scene):
    def construct(self):

        titulo = Tex("Cinemática - Aula 1", font_size=50)

        instagram = Tex('@CelestialEquations').scale(0.5).shift(LEFT*5.5 + 3.7*UP).set_color(BLUE)
        subtitle = Tex("Bases da Cinemática ", font_size=40)
        subtitle.next_to(titulo, DOWN)
        self.play(Write(instagram))
        self.play(Write(titulo))
        self.play(Write(subtitle))
        self.wait(1)
        self.remove(titulo)
        self.play(subtitle.animate.to_edge(UP))
        self.wait(1)
        
        
        
        topics = VGroup(
    Text("1. Referencial", font_size=36),
    Text("2. Movimento e Repouso", font_size=36),
    Text("3. Distância Percorrida", font_size=36),
    Text("4. Velocidade Escalar Média", font_size=36),
    Text("5. Velocidade Instantânea", font_size=36),
    Text("6. Função Horária da Posição (MU)", font_size=36)
    ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        topics.next_to(4*LEFT+DOWN*0.5, buff=0.8)


        self.wait(0.5)

        for topic in topics:
            self.play(
        Write(topic),
        run_time=1     
    )
            self.wait(10)
            self.play(topic.animate.set_color(BLUE))


        
        
        
       
        

       
        
      