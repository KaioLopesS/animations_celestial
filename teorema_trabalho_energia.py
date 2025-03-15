from manim import *

class TeoremaTrabalhoEnergia_2(Scene):
    def construct(self):
        # Título
        titulo = Text("Teorema Trabalho-Energia Cinética", font_size=40)
        instagram = Tex('@CelestialEquations').scale(0.5).shift(LEFT*5.5 + 3.7*UP)
        subtitulo = Text("W = ΔK", font_size=30, color=BLUE).next_to(titulo, DOWN)
        grupo_titulo = VGroup(titulo, subtitulo)
        self.play(Write(instagram))
        self.play(Write(titulo), Write(subtitulo))
        self.wait(1)
        self.play(
            grupo_titulo.animate.scale(0.6).to_edge(UP),
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
        
        self.play(Create(chao), FadeIn(grupo_bloco))
        
        
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
      
        deducao = VGroup()
        self.wait(0.5)
        
        eq1 = MathTex("W = Fd")
        exp1 = Text("Trabalho é força × distância", font_size=24, color=BLUE)
        grupo1 = VGroup(eq1, exp1).arrange(RIGHT, buff=0.5)
        deducao.add(grupo1)
        
        
  
        eq2 = MathTex("F = ma")
        exp2 = Text("Força é massa × aceleração", font_size=24, color=BLUE)
        grupo2 = VGroup(eq2, exp2).arrange(RIGHT, buff=0.5)
        deducao.add(grupo2)
        
        
      
        eq3 = MathTex("v_f^2 = v_i^2 + 2ad")
        exp3 = Text("Equação de Torricelli", font_size=24, color=BLUE)
        grupo3 = VGroup(eq3, exp3).arrange(RIGHT, buff=0.5)
        deducao.add(grupo3)
        
    
        eq4 = MathTex("a = \\frac{v_f^2 - v_i^2}{2d}")
        exp4 = Text("Isolando a aceleração", font_size=24, color=BLUE)
        grupo4 = VGroup(eq4, exp4).arrange(RIGHT, buff=0.5)
        deducao.add(grupo4)
        
        
  
        eq5 = MathTex("W = Fd = m \\frac{v_f^2 - v_i^2}{2}")
        exp5 = Text("Substituindo os valores", font_size=24, color=BLUE)
        grupo5 = VGroup(eq5, exp5).arrange(RIGHT, buff=0.5)
        deducao.add(grupo5)
        
        

        deducao.arrange(DOWN, buff=0.5).shift(UP*1)
        
        
        for i, grupo in enumerate(deducao):
            self.play(Write(grupo), run_time=1)
            
            if i < len(deducao)-1:
                self.play(
                    grupo_bloco.animate.shift(RIGHT*2),
                    rate_func=linear,
                    run_time=1.8
                )
        
       
        resultado = MathTex(
            "W = \\frac{1}{2}mv_f^2 - \\frac{1}{2}mv_i^2 = K_f - K_i",
            color=WHITE
        ).next_to(deducao, DOWN, buff=0.5)
        box = SurroundingRectangle(resultado, color=YELLOW, buff=0.2)
        
        self.play(Write(resultado))
        self.play(Create(box))
        
       
        self.play(
            resultado.animate.set_color_by_tex_to_color_map({
                "K_f": BLUE,
                "K_i": BLUE
            })
        )
        
        self.wait(2)
        
       
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )

        