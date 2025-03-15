from manim import *
import random

class ondas(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        instagram = Text('@CelestialEquations').scale(0.4).shift(LEFT*5.5+3.5*UP).set_color(BLUE)
        titulo = Text("Ondas", font_size=50)
        titulo.move_to(ORIGIN)
        titulo.set_color_by_gradient(BLUE, GREEN)
        instagram.set_color_by_gradient(BLUE, GREEN)
        self.play(Write(titulo))
        self.play(Write(instagram), run_time = 0.3)
        self.wait(1)
        self.remove(titulo)

        plano = Axes(
            x_range=[-2*PI, 2*PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={
                "include_numbers": False 
            }
        )
        plano.scale(1)  
        self.play(Create(plano), run_time = 2)
        onda = plano.plot(lambda x: np.sin(x), color=GREEN)
        self.play(Create(onda), run_time = 2)
        self.wait(2)

        crista_pos = plano.c2p(PI/2, 1)  
        self.play(self.camera.frame.animate.move_to(crista_pos).set(width=4), run_time=0.5)
        
        
        dot = Dot(crista_pos, color=BLUE)
        label = Text("Crista", font_size=24).next_to(dot, UP+RIGHT)
        label.set_color_by_gradient(BLUE, GREEN)
        self.add(dot)
        self.play(Write(label))
        self.wait(2)

        
        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=config.frame_width), run_time=0.5)
        self.wait(2)
        
        vale_pos = plano.c2p(-PI/2, -1)
        self.play(self.camera.frame.animate.move_to(vale_pos).set(width=4), run_time = 0.5)
        
        dot_2 = Dot(vale_pos, color = BLUE)
        label_2 = Text('Vale', font_size = 24).next_to(dot_2, DOWN+RIGHT)
        label_2.set_color_by_gradient(BLUE, GREEN)
        self.play(Write(label_2))
        self.add(dot_2)
        self.wait(2)
        self.play(self.camera.frame.animate.move_to(dot).set(width = 6), run_time = 0.5)
        self.wait(0.5)
        self.remove(label, label_2)

        eixo_x = plano.c2p(PI/2,0)
        linha = Line(start=eixo_x, end=crista_pos, color=BLUE_C)
        self.play(Create(linha))
    
       
        amplitude_label = Text("Amplitude", font_size=20).next_to(dot, RIGHT+UP)
        amplitude_label.set_color_by_gradient(BLUE, GREEN)
        self.play(Write(amplitude_label))
        self.wait(2)