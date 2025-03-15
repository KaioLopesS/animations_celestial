from manim import *
import numpy as np


config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class grafico_youtube(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        instagram = Text('@CelestialEquations').scale(0.4).shift(5*UP).set_color_by_gradient(RED, WHITE)
        subtitulo = Text('Da Aproximação à Pefeição').scale(0.5).set_color_by_gradient(RED, WHITE).move_to(DOWN)
        titulo = Text("O Gráfico de e^x", font_size=50)

        titulo.set_color_by_gradient(RED, WHITE)
        self.play(Write(instagram))
        self.play(Write(titulo))
        self.play(Write(subtitulo))

        self.wait(1)
        self.remove(titulo, subtitulo)

        eixos = Axes(
            x_range=[-6, 6, 2],
            y_range=[-2, 10, 2],
            axis_config={
                "include_numbers": False
            }
        )

        eixos.scale(0.8)
        self.play(Create(eixos), run_time=2)

        
        grafico_ex = eixos.plot(lambda x: np.exp(x), x_range=[-5, np.log(10)], color=RED)
        grafico_label = MathTex(r"e^x").next_to(grafico_ex, UP+RIGHT).set_color(RED)

        grafico_ex3 = eixos.plot(lambda x: np.exp(x), x_range=[-5, np.log(10)], color=RED)
        grafico_label3 = MathTex(r"e^x").next_to(grafico_ex, UP+RIGHT).set_color(RED)
        self.play(Create(grafico_ex3), run_time=0.5)
        self.play(Write(grafico_label3))
        self.play(Create(grafico_ex), run_time=0.1)
        self.play(Write(grafico_label))
        
        self.wait(2)

        series_colors = [RED, GRAY, BLUE, ORANGE, PURPLE, TEAL, GOLD, GREEN]
        series_functions = [
            lambda x: 1 + x,
            lambda x: 1 + x + x**2 / 2,
            lambda x: 1 + x + x**2 / 2 + x**3 / 6,
            lambda x: 1 + x + x**2 / 2 + x**3 / 6 + x**4 / 24,
            lambda x: 1 + x + x**2 / 2 + x**3 / 6 + x**4 / 24 + x**5 / 120,
            lambda x: 1 + x + x**2 / 2 + x**3 / 6 + x**4 / 24 + x**5 / 120 + x**6 / 720,
            lambda x: 1 + x + x**2 / 2 + x**3 / 6 + x**4 / 24 + x**5 / 120 + x**6 / 720 + x**7 / 5040,
            lambda x: np.exp(x)
        ]
        series_labels = [
            r"e^x \approx  1 + x",
            r"e^x \approx  1 + x + \frac{x^2}{2!}",
            r"e^x \approx  1 + x + \frac{x^2}{2!} + \frac{x^3}{3!}",
            r"e^x \approx  1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!}",
            r"e^x \approx  1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \frac{x^5}{5!}",
            r"e^x \approx  1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \frac{x^5}{5!} + \frac{x^6}{6!}",
            r"e^x \approx 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \frac{x^5}{5!} + \frac{x^6}{6!} + \frac{x^7}{7!}",
            r"e^x = 1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + ..."
        ]


        label_position = 4 * DOWN   

        for func, color, label in zip(series_functions, series_colors, series_labels):
            grafico_taylor = eixos.plot(func, x_range=[-5, np.log(10)], color=color)
            grafico_taylor_label = MathTex(label).move_to(label_position).set_color(color).scale(0.7)
            self.play(Transform(grafico_ex, grafico_taylor), Transform(grafico_label, grafico_taylor_label), run_time = 0.8)
            self.wait(2)
        
        
        