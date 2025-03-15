from manim import *
import numpy as np



config.pixel_height = 1920 
config.pixel_width = 1080   
config.frame_height = 16.0 
config.frame_width = 9.0 
class IntegralSenXCosX(Scene):
    def construct(self):
    
        instagram = Tex('@CelestialEquations').scale(0.5).shift(5.5*UP).set_color_by_gradient(BLUE, WHITE, RED)
        self.play(Write(instagram))
        self.wait(0.5)

        
        integral = MathTex(r"\int \sin(x) \cdot \cos(x) \, dx", font_size = 80).set_color_by_gradient(BLUE, WHITE, RED)
        self.play(FadeIn(integral))
        self.wait(1)
        self.play(Circumscribe(integral, color = RED, run_time=2))
        self.wait(2)
        self.play(FadeOut(integral))
        self.wait(1)

        

        
        approach2 = Text("Usando o Método da  Substituição", font_size=32).shift(3*UP)
        self.play(Write(approach2))
        self.wait(1)

        
        sub1 = MathTex(r"\text{Fazendo } u = \sin(x)")
        sub1.next_to(approach2, DOWN, buff=0.5)
        self.play(Write(sub1))
        self.wait(1)

        sub2 = MathTex(r"\Rightarrow du = \cos(x) \, dx")
        sub2.next_to(sub1, DOWN, buff=0.3)
        self.play(Write(sub2))
        self.wait(15)

        sub3 = MathTex(
        r"\int", 
        r"\sin(x)", 
        r"\cdot", 
        r"\cos(x)", 
        r"\, dx",
        ).set_color_by_gradient(BLUE, WHITE, RED).shift(DOWN+2*LEFT)

        sub7 = MathTex(r"=", 
        r"\int", 
        r"u", 
        r"\, du",).set_color_by_gradient(BLUE, WHITE, RED).next_to(sub3, RIGHT)

        sub8 = MathTex(r"= \frac{u^{2}}{2}").set_color_by_gradient(BLUE, WHITE, RED).next_to(sub7, RIGHT)
        brace_sin = Brace(sub3[1], UP)
        u_text = MathTex("u").next_to(brace_sin, UP, buff=0.1)

        brace_cos_dx = Brace(sub3[3:5], UP)
        du_text = MathTex("du").next_to(brace_cos_dx, UP, buff=0.1)

        
        rect_sin = SurroundingRectangle(sub3[1], color=YELLOW)
        rect_cos_dx = SurroundingRectangle(sub3[3:5], color=YELLOW)

        
        self.play(Write(sub3))
        self.wait(1)
        self.play(FadeIn(rect_sin), FadeIn(rect_cos_dx))
        self.wait(1)
        self.play(FadeIn(brace_sin), FadeIn(u_text))
        self.wait(1)
        self.play(FadeIn(brace_cos_dx), FadeIn(du_text))
        self.wait(3)
        self.play(FadeIn(sub7))
        self.wait(12)
        self.play(FadeIn(sub8))
        self.wait(2)
        
    
        sub5 = MathTex(r"\int \sin(x) \cdot \cos(x) \, dx= \frac{\sin^2(x)}{2} + C").set_color_by_gradient(BLUE, WHITE, RED)
        sub5.shift(3*DOWN)
        self.play(Write(sub5))
        self.wait(3)

        framebox2 = SurroundingRectangle(sub5, buff = .1, color = RED)
        self.play(Create(framebox2))
        self.wait(20)

        
      

        
        
        
        

