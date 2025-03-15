from manim import *
import numpy as np
import random



class raio(MovingCameraScene):
    def construct(self):
        instagram = Text('@CelestialEquations').scale(0.4).shift(5*UP).set_color_by_gradient(RED, GOLD)
        titulo = Text("Raio de Schwarzschild", font_size=50).set_color_by_gradient(RED, GOLD)
        subtitulo = Text("Utilizando Conceitos de Mecânica Clássica", font_size = 25).next_to(titulo, DOWN).set_color(GRAY)
        circle = Circle(radius=1, color=WHITE, fill_opacity=1).shift(UP).set_color(GRAY)
        titulo_1 = Text("E se o sol se transformasse\nem um buraco negro...", font_size=50).set_color_by_gradient(RED, GOLD).scale(0.7)
        titulo_2 = Text("Qual seria o seu tamanho ?", font_size=50).set_color_by_gradient(RED, GOLD)

        self.play(Write(titulo_1))
        self.wait(4)
        self.play(ReplacementTransform(titulo_1, titulo_2))
        self.wait(2)
    
        self.play(FadeIn(instagram))
        self.wait(1)
        self.play(ReplacementTransform(titulo_2, titulo), Write(subtitulo))
        self.wait(1)
        self.play(FadeOut(titulo), FadeOut(subtitulo))
        self.wait(1)

        buraco_negro = ImageMobject("buraco_negro.png")
        buraco_negro.scale(1.5)
        buraco_negro.shift(UP)
        #imagem_nasa = Text('Imagem: NASA').shift(DOWN+3*RIGHT).scale(0.5).set_color(GRAY)
        disco = Text("Disco de Acreção", font_size=40).next_to(buraco_negro, DOWN).set_color(BLACK)
        horizonte = Text("Horizonte de Eventos", font_size=40).next_to(disco, DOWN).set_color(GRAY)
        

        self.play(FadeIn(buraco_negro))
        self.wait(5)
        self.play(Write(disco))
        self.wait(4)
        self.play(Write(horizonte))
        self.wait(1)
        self.play(Create(circle))
        self.wait(5)
        self.remove(circle)
        self.wait(2)
        self.remove(disco)
        self.remove(horizonte)
        self.play(FadeOut(buraco_negro))
        self.wait(1)


        event_horizon = Circle(radius=1, color=BLACK, fill_opacity=1)

        
        gradient_circles = VGroup()
        for i in range(20):
            circle = Circle(radius=1.1 + i * 0.1, color=interpolate_color(BLUE, BLACK, i / 20))
            circle.set_opacity(0.7 - i * 0.03)  
            gradient_circles.add(circle)

        
        disk_accretion = VGroup(
            *[
                Circle(radius=1.2 + i * 0.2, color=interpolate_color(RED, ORANGE, i / 10), stroke_opacity=0.8)
                for i in range(10)
            ]
        )
        disk_accretion.rotate(PI / 2)  

        schwarzschild_radius = Line(start=ORIGIN, end=RIGHT, color=WHITE, stroke_width=2)
        label_radius = MathTex(r"R_s", color=WHITE).scale(1)
        label_radius.next_to(schwarzschild_radius, UP)

        grupo_3 = VGroup(gradient_circles, event_horizon, disk_accretion, schwarzschild_radius, label_radius)
        grupo_3.shift(2*LEFT)


        
        self.add(gradient_circles, event_horizon, disk_accretion)
        self.play(Rotate(disk_accretion, angle=2 * PI, run_time=5), rate_func=linear)
        self.play(FadeIn(schwarzschild_radius))
        self.play(Write(label_radius))
        self.wait(5)
        
        velocidade_escape = MathTex(r"v_{\text{escape}} = \sqrt{\frac{2GM}{R}}").shift(4*RIGHT)
        framebox_escape = SurroundingRectangle(velocidade_escape, buff=0.1, color = RED)
        limite_luz = MathTex(r"c = \sqrt{\frac{2GM}{R_s}}").shift(4*RIGHT)
        quadrado = MathTex(r" c^{2} = \frac{2GM}{R_s}").shift(4*RIGHT)
        raio = MathTex(r"R_s = \frac{2GM}{c^{2}}").shift(4*RIGHT)
        framebox_raio = SurroundingRectangle(raio, buff=0.1, color = ORANGE)

        self.play(Write(velocidade_escape))
        self.wait(1)
        self.play(Create(framebox_escape))
        self.wait(4)
        self.play(FadeOut(framebox_escape))
        self.wait(2)
        self.play(ReplacementTransform(velocidade_escape, limite_luz))
        self.wait(2)
        self.play(ReplacementTransform(limite_luz, quadrado))
        self.wait(2)
        self.play(ReplacementTransform(quadrado, raio))
        self.wait(1)
        self.play(Create(framebox_raio))
        self.wait(11)

        grupo = VGroup(gradient_circles, event_horizon, disk_accretion, schwarzschild_radius, label_radius, raio, framebox_raio)

        #e se, de repente, o sol virasse um buraco negro ?#
        self.play(FadeOut(grupo))

        self.wait(1)

        sol = ImageMobject('sol.png')
        sol.scale(1)
        sol_texto = Text('Sol', font_size=40).shift(3*DOWN)

        buraco_negro2 = ImageMobject('buraco_negro_2.png')
        buraco_negro2.scale(0.5)  
        buraco_negro2_texto = Text('Buraco Negro', font_size=40).shift(3*DOWN)

        
        self.play(FadeIn(sol), Write(sol_texto))
        self.wait(2)

        
        self.play(
            FadeOut(sol), 
            FadeOut(sol_texto),
            FadeIn(buraco_negro2), 
            Write(buraco_negro2_texto)
        )
        self.wait(2)
        self.remove(buraco_negro2, buraco_negro2_texto )
        self.wait(1)

        raio2 = MathTex(r"R_s = \frac{2GM}{c^{2}}").shift(2*UP)

        G = MathTex(r"G = 6.674 \times 10^{-11} \, \text{N} \cdot \text{m}^2/\text{kg}^2")
        M = MathTex(r"M_{\odot} = 1.989 \times 10^{30} \, \text{kg}").next_to(G, DOWN, buff=0.1)
        c = MathTex(r"c = 3 \times 10^8 \, \text{m/s}").next_to(M, DOWN, buff=0.1)

        resultado = MathTex(
            r"R_{s} = \frac{2 \times (6.67 \times 10^{-11}) \times (1.989 \times 10^{30})}{(3 \times 10^8)^2}"
        ).shift(3*DOWN)

        resultado2 = MathTex(r"R_{s}\approx 2.95 \, \text{km}").shift(3*DOWN)
        framebox_resultado = SurroundingRectangle(resultado2, buff=0.1, color=ORANGE)

        self.play(Write(raio2))
        self.wait(1)
        self.play(Write(G), Write(M), Write(c))
        self.wait(1)
        self.play(Write(resultado))  
        self.wait(1)
        self.play(ReplacementTransform(resultado, resultado2))  
        self.wait(1)
        self.play(Create(framebox_resultado))
        self.wait(28)
                
        
        

        


        
        






        




    


        



        