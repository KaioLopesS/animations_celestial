from manim import *

class TeoremaTrabalhoEnergia(Scene):
    def construct(self):
        
        titulo = Text("Teorema Trabalho-Energia Cinética via Cálculo", font_size=40)
        instagram = Tex('@CelestialEquations').scale(0.5).shift(LEFT*5.5 + 3.7*UP)
        subtitulo = Text("W = ΔK", font_size=30, color=RED).next_to(titulo, DOWN)
        grupo_titulo = VGroup(titulo, subtitulo)
        self.play(Write(instagram))
        self.play(Write(titulo), run_time=1.5)
        self.play(Write(subtitulo), run_time=1)
        self.wait(1)
        self.play(
            grupo_titulo.animate.scale(0.6).to_edge(UP),
            run_time=1
        )
        
        
        bloco = Square(side_length=1, color=BLUE, fill_opacity=0.5)
        massa = MathTex("m", color=WHITE).scale(0.8)
        vel_i = MathTex("v_i", color=GREEN).scale(0.7).next_to(bloco, DOWN, buff=0.1)
        grupo_bloco = VGroup(bloco, massa, vel_i).shift(LEFT*4 + UP*0.5)
        
  
        chao = Line(
            start=LEFT*6,
            end=RIGHT*6,
            stroke_width=3
        ).shift(DOWN*0.5)
        
      
        
        
        self.play(
            FadeIn(grupo_bloco),
            Create(chao),
            
            run_time=1
        )
        
  
        forca = Arrow(
            start=grupo_bloco.get_right(),
            end=grupo_bloco.get_right() + RIGHT*1.5,
            color=RED,
            buff=0,
        )
        texto_forca = MathTex("F", color=RED).next_to(forca, UP, buff=0.1)
        grupo_forca = VGroup(forca, texto_forca)
        self.play(Create(grupo_forca))
        
        
        self.play(
            grupo_bloco.animate.shift(RIGHT*8),
            grupo_forca.animate.shift(RIGHT*8),
            rate_func=linear,
            run_time=2
        )
        vel_f = MathTex("v_f", color=GREEN).scale(0.7).next_to(grupo_bloco, DOWN, buff=0.1)
        self.play(ReplacementTransform(vel_i.copy(), vel_f))
        
        self.play(
            grupo_bloco.animate.scale(0.7).move_to(LEFT*5 + DOWN*5),
            FadeOut(grupo_forca),
            FadeOut(vel_f),
            chao.animate.scale(0.7).shift(DOWN*5)
        )
    
        
        self.remove(titulo, subtitulo)
        
       
        equations = [
            MathTex("F = ma"),
            MathTex("F = m\\frac{dv}{dt}"),
            MathTex("F\\,dx = m\\frac{dv}{dt}\\,dx"),
            MathTex("F\\,dx = mv\\,dv"),
            MathTex("\\int F\\,dx = \\int mv\\,dv"),
        ]
        
        explanations = [
            Text("Segunda Lei de Newton", font_size=20, color=RED),
            Text("Aceleração como taxa de variação da velocidade", font_size=20, color=RED),
            Text("Multiplicando ambos os lados por dx", font_size=20, color=RED),
            Text("Usando dx/dt = v", font_size=20, color=RED),
            Text("Integrando ambos os lados", font_size=20, color=RED),
        ]
        
        for i, (eq, exp) in enumerate(zip(equations, explanations)):
            eq.shift(UP*1.2*(2.7-i)+LEFT*1.5)
            exp.next_to(eq, RIGHT, buff=0.5)
            self.play(Write(eq), run_time=2)
            self.play(FadeIn(exp), run_time=0.5)
            
           
            self.play(
                grupo_bloco.animate.shift(RIGHT*5),
                rate_func=linear,
                run_time=0.8
            )
        
       
        resultado = MathTex(
            "W = \\frac{1}{2}mv_f^2 - \\frac{1}{2}mv_i^2 = K_f - K_i",
            color=WHITE
        ).next_to(equations[-1], DOWN, buff=0.5)
        
        box = SurroundingRectangle(resultado, color=RED, buff=0.2)
        bg_box = BackgroundRectangle(resultado, color=BLUE_E, fill_opacity=0.2)
        
        self.play(
            FadeIn(bg_box),
            Write(resultado),
            run_time=1.5
        )
        self.play(
            Create(box),
            resultado.animate.set_color_by_tex("K_f", RED),
            resultado.animate.set_color_by_tex("K_i", RED),
            run_time=1
        )
        
       
        self.play(
            grupo_bloco.animate.shift(RIGHT*4),
            rate_func=smooth,
            run_time=2
        )
        
        
        self.play(
            *[FadeOut(obj) for obj in self.mobjects],
            run_time=1.5
        )
        
        self.wait(1)