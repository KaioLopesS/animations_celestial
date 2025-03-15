from manim import *
import numpy as np

class MovimentoCircular(Scene):
    def construct(self):
       
        titulo = Text("Movimento Circular Uniforme", font_size=40)
        instagram = Tex('@CelestialEquations').scale(0.5).shift(LEFT*5.5 + 3.7*UP)
        subtitulo = Text("(MCU)", font_size=30, color=BLUE).next_to(titulo, DOWN)
        grupo_titulo = VGroup(titulo, subtitulo)
        self.play(Write(instagram))
        self.play(Write(grupo_titulo))
        self.wait(2)  
        self.play(
            grupo_titulo.animate.scale(0.6).to_edge(UP),
        )

      
        circulo = Circle(radius=2, color=BLUE)
        self.play(Create(circulo))
        self.wait(1)

        
        particula = Dot(radius=0.15, color=RED)
        particula.move_to(circulo.point_from_proportion(0))

     
        raio = always_redraw(
            lambda: Line(
                circulo.get_center(),
                particula.get_center(),
                color=YELLOW,
            )
        )

       
        def get_vel_vector():
            radius_vector = raio.get_vector()
            length = np.sqrt(radius_vector[0]**2 + radius_vector[1]**2)
            if length > 0:
                normalized = radius_vector / length
                tangent = np.array([-normalized[1], normalized[0], 0])
                return Arrow(
                    start=particula.get_center(),
                    end=particula.get_center() + tangent * 0.8,
                    color=WHITE,
                    buff=0
                )
            return Arrow(start=ORIGIN, end=ORIGIN)

        velocidade = always_redraw(get_vel_vector)

       
        def get_force_vector():
            radius_vector = raio.get_vector()
            length = np.sqrt(radius_vector[0]**2 + radius_vector[1]**2)
            if length > 0:
                normalized = -radius_vector / length
                return Arrow(
                    start=particula.get_center(),
                    end=particula.get_center() + normalized * 0.8,
                    color=RED,
                    buff=0
                )
            return Arrow(start=ORIGIN, end=ORIGIN)

        forca_centripeta = always_redraw(get_force_vector)

      
        texto_v = always_redraw(
            lambda: MathTex("\\vec{v}", color=WHITE)
            .next_to(velocidade.get_end(), UR, buff=0.1)
        )
        texto_fc = always_redraw(
            lambda: MathTex("\\vec{a_c}", color=RED)
            .next_to(forca_centripeta.get_end(), DL, buff=0.1)
        )
        texto_r = always_redraw(
            lambda: MathTex("R", color=YELLOW)
            .next_to(raio.get_center(), UR, buff=0.1)
        )

      
        self.play(
            FadeIn(particula),
            Create(raio),
            Create(velocidade),
            Create(forca_centripeta),
            Write(texto_v),
            Write(texto_fc),
            Write(texto_r)
        )
        self.wait(2)

       
        trajetoria = TracedPath(particula.get_center, stroke_width=2, stroke_color=RED_A)
        self.add(trajetoria)

     
        self.play(
            Rotating(
                particula,
                about_point=circulo.get_center(),
                angle=2*PI,
                rate_func=linear,
                run_time=5  
            )
        )

       
        self.wait(2)

        
        self.play(
            FadeOut(velocidade),
            FadeOut(forca_centripeta),
            FadeOut(texto_v),
            FadeOut(texto_fc),
            FadeOut(trajetoria)
        )
        self.wait(2)

        
        equacoes_1 = VGroup(
            MathTex("\\omega = \\frac{2\\pi}{T} = 2\\pi f", color=WHITE),
            MathTex("v = \\omega R", color=GREEN)
        ).arrange(DOWN, buff=0.5).shift(RIGHT*4)

        explicacoes_1 = VGroup(
            Text("Velocidade Angular", font_size=24, color=WHITE),
            Text("Velocidade Linear", font_size=24, color=GREEN)
        ).arrange(DOWN, buff=0.7).shift(LEFT*4)

       
        for eq, exp in zip(equacoes_1, explicacoes_1):
            self.play(
                Write(eq),
                FadeIn(exp),
                run_time=2  
            )
            self.wait(2)  

        self.wait(2)

        
        equacoes_2 = VGroup(
            MathTex("F_c = m\\omega^2R = \\frac{mv^2}{R}", color=RED),
            MathTex("a_c = \\omega^2R = \\frac{v^2}{R}", color=ORANGE)
        ).arrange(4*DOWN, buff=0.5).shift(RIGHT*4)

        explicacoes_2 = VGroup(
            Text("Força Centrípeta", font_size=24, color=RED),
            Text("Aceleração Centrípeta", font_size=24, color=ORANGE)
        ).arrange(4*DOWN, buff=0.7).shift(LEFT*4)

        
        for eq, exp in zip(equacoes_2, explicacoes_2):
            self.play(
                Write(eq),
                FadeIn(exp),
                run_time=2
            )
            self.wait(2)

        self.wait(2)

       

        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2  
        )
