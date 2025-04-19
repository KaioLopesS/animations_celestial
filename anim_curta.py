from manim import *
import numpy as np


config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 9.0
config.frame_width = config.frame_height * (config.pixel_width / config.pixel_height)

class SenoTrigonometricoReelFinalComImagem(Scene): 
    def construct(self):
        centro_circulo = None
        celestial_equations = None

        try:
           
            celestial_equations = ImageMobject("Prancheta_2-removebg-preview.png").scale(0.4).to_edge(UP, buff=0.1) # Menor buff
            self.play(FadeIn(celestial_equations), run_time=1.5)
            self.wait(0.5) 
            
            self.add(celestial_equations) 

           
            centro_circulo = UP * 0.8 

        
            titulo = Text("O Gráfico da Função Seno", font_size=30).scale(0.7).set_color_by_gradient(BLUE, GREEN)
         
            titulo.next_to(celestial_equations, DOWN, buff=0.3)
            self.play(Write(titulo), run_time=1.0)


        except FileNotFoundError:
            print("AVISO: Imagem 'Prancheta_2-removebg-preview.png' não encontrada. Iniciando animação sem ela.")
            self.wait(0.5)
            
            centro_circulo = UP * 1.5

           
            titulo = Text("A Dança do Seno: Do Círculo ao Gráfico", font_size=30).to_edge(UP, buff=0.5)
            self.play(Write(titulo), run_time=1.0)


        theta = ValueTracker(0)
        raio_circulo = 1.2

      
        circulo = Circle(radius=raio_circulo, color=BLUE).move_to(centro_circulo)
        eixos_circulo = Axes(
            x_range=[-1.5, 1.5, 1], y_range=[-1.5, 1.5, 1],
            x_length=2 * raio_circulo, y_length=2 * raio_circulo,
            axis_config={"include_tip": False, "include_numbers": False},
            tips=False,
        ).move_to(centro_circulo)

        dot_circulo = Dot(color=YELLOW, radius=0.05).move_to(circulo.point_at_angle(0))
        dot_circulo.add_updater(lambda d: d.move_to(circulo.point_at_angle(theta.get_value())))

        linha_raio = Line(centro_circulo, dot_circulo.get_center(), color=WHITE, stroke_width=1.5)
        linha_raio.add_updater(lambda l: l.put_start_and_end_on(centro_circulo, dot_circulo.get_center()))

        linha_seno = always_redraw(
            lambda: Line(
                [dot_circulo.get_center()[0], centro_circulo[1], 0],
                dot_circulo.get_center(), color=RED, stroke_width=4
            )
        )


        eixos_grafico = Axes(
            x_range=[0, 2 * PI + 0.5, PI / 2], y_range=[-1.5, 1.5, 1],
            x_length= config.frame_width * 0.8, y_length=2.0,
            axis_config={"include_numbers": False, "tip_shape": StealthTip}, tips=False,
            x_axis_config={
                           "include_numbers": False
                           },
            y_axis_config={"numbers_to_include":[], "include_numbers": False},
        ).to_edge(DOWN, buff=1.0) 

        labels_grafico = eixos_grafico.get_axis_labels(
            x_label=MathTex(r"\theta", font_size=24), y_label=MathTex(r"\sin(\theta)", font_size=24)
        )
        x_labels = VGroup(
            MathTex("0", font_size=20).next_to(eixos_grafico.c2p(0, 0), DOWN, buff=0.15),
            MathTex(r"\frac{\pi}{2}", font_size=20).next_to(eixos_grafico.c2p(PI/2, 0), DOWN, buff=0.15),
            MathTex(r"\pi", font_size=20).next_to(eixos_grafico.c2p(PI, 0), DOWN, buff=0.15),
            MathTex(r"\frac{3\pi}{2}", font_size=20).next_to(eixos_grafico.c2p(3*PI/2, 0), DOWN, buff=0.15),
            MathTex(r"2\pi", font_size=20).next_to(eixos_grafico.c2p(2*PI, 0), DOWN, buff=0.15)
        )

        seno_graph = always_redraw(
            lambda: eixos_grafico.plot(
                lambda x: np.sin(x), x_range=[0, theta.get_value()], color=YELLOW, stroke_width=2
            )
        )

        dot_grafico = Dot(color=YELLOW, radius=0.04)
        dot_grafico.add_updater(lambda d: d.move_to(eixos_grafico.c2p(theta.get_value(), np.sin(theta.get_value()))))

        linha_projecao = always_redraw(
            lambda: DashedLine(
                dot_circulo.get_center(),
                [eixos_grafico.c2p(theta.get_value(), 0)[0], dot_circulo.get_center()[1], 0],
                stroke_width=1.5, color=RED, dashed_ratio=0.6
            )
        )

      
        elementos_principais = VGroup(
            circulo, eixos_circulo, eixos_grafico, labels_grafico, x_labels
        )

        self.play(Create(elementos_principais), run_time=1.5)

   
        self.add(
            dot_circulo, linha_raio, linha_seno,
            seno_graph, dot_grafico, linha_projecao
        )


        self.play(
            theta.animate.set_value(2 * PI),
            run_time=7,
            rate_func=linear
        )
        self.wait(1)

        pontos_chave = {
            0: 0, 90: PI/2, 180: PI, 270: 3*PI/2, 360: 2*PI
        }

        for ang_deg, ang_rad in pontos_chave.items():
            self.play(theta.animate.set_value(ang_rad), run_time=0.2)
            self.wait(0.1)

            valor_seno = np.sin(ang_rad)
            texto_destaque = MathTex(
                f"\\sin({ang_deg}^\\circ) = {valor_seno:.0f}",
                font_size=28, color=YELLOW
            )
            texto_destaque.to_corner(DR, buff=0.8)

            self.play(Write(texto_destaque), run_time=0.6)
            self.wait(0.8)
            self.play(FadeOut(texto_destaque), run_time=0.4)

        # --- Fim ---
        self.wait(1.5)

      
       