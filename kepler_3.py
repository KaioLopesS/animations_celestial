from manim import *
import numpy as np
import pandas as pd
 

config.pixel_height = 1920 
config.pixel_width = 1080   
config.frame_height = 16.0 
config.frame_width = 9.0 




class KeplerThirdLawDerivation(Scene):
    def construct(self):
        instagram = Text('@CelestialEquations').scale(0.4).shift(4*UP).set_color_by_gradient(GREEN, WHITE)
        #self.camera.background_color = "#1C1C1C"
        
        title = Text("Terceira Lei de Kepler", font_size=40).set_color_by_gradient(GREEN, WHITE)
        self.play(Write(title))
        self.play(Write(instagram))
        self.wait(1)
        
        
        intro_text = Text("A terceira lei de Kepler relaciona o período orbital e o semieixo maior da órbita", 
                          font_size=24).set_color_by_gradient(GREEN, WHITE)
        intro_text.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(intro_text))
        self.wait(1)
        self.play(FadeOut(intro_text))
        self.play(FadeOut(title))
        
        
        newton_title = Text("Lei da Gravitação Universal de Newton", font_size=32).set_color_by_gradient(GREEN, WHITE).shift(2*UP)
        self.play(Write(newton_title))
        self.wait(2)
        
        newton_eq = MathTex(r"F = G \frac{m_1 m_2}{r^2}", font_size=40).set_color_by_gradient(GREEN, WHITE)
        newton_eq.next_to(newton_title, DOWN, buff=0.5)
        self.play(Write(newton_eq))
        self.wait(1)
        
        newton_explanation = Text("Onde F é a força gravitacional, G é a constante gravitacional,", font_size=22).set_color_by_gradient(GREEN, WHITE)   
        newton_explanation2 = Text("m₁ e m₂ são as massas, e r é a distância entre os corpos.", font_size=22).set_color_by_gradient(GREEN, WHITE)
        newton_explanation.next_to(newton_eq, DOWN, buff=0.3)
        newton_explanation2.next_to(newton_explanation, DOWN, buff=0.1)
        
        self.play(FadeIn(newton_explanation), FadeIn(newton_explanation2))
        self.wait(6)
        self.play(FadeOut(newton_title), FadeOut(newton_eq), 
                  FadeOut(newton_explanation), FadeOut(newton_explanation2))
        
        
        centripetal_title = Text("Força Centrípeta para Órbitas Circulares", font_size=32).set_color_by_gradient(GREEN, WHITE).shift(3*UP) 
        self.play(Write(centripetal_title))
        self.wait(15)
        centripetal_eq = MathTex(r"F = \frac{m v^2}{r}", font_size=40).set_color_by_gradient(GREEN, WHITE)  
        centripetal_eq.next_to(centripetal_title, DOWN, buff=0.5)
        self.play(Write(centripetal_eq))
        self.wait(5)
        
        
        velocity_eq = MathTex(r"v = \frac{2\pi r}{T}", font_size=40).set_color_by_gradient(GREEN, WHITE)
        velocity_eq.next_to(centripetal_eq, DOWN, buff=0.5)
        velocity_explanation = Text("Onde v é a velocidade orbital e T é o período orbital", font_size=22).set_color_by_gradient(GREEN, WHITE)  
        velocity_explanation.next_to(velocity_eq, DOWN, buff=0.3)
        
        self.play(Write(velocity_eq))
        self.play(FadeIn(velocity_explanation))
        self.wait(2)
        
        
        substituted_eq = MathTex(r"F = \frac{m (2\pi r/T)^2}{r}", font_size=40).set_color_by_gradient(GREEN, WHITE)
        substituted_eq.next_to(centripetal_title, DOWN, buff=0.5)
        
        self.play(Transform(centripetal_eq, substituted_eq))
        self.wait(1)
        
        simplified_eq = MathTex(r"F = \frac{4\pi^2 m r}{T^2}", font_size=40).set_color_by_gradient(GREEN, WHITE)
        simplified_eq.next_to(centripetal_title, DOWN, buff=0.5)
        
        self.play(Transform(centripetal_eq, simplified_eq))
        self.wait(4)
        self.play(FadeOut(centripetal_title), FadeOut(centripetal_eq), 
                  FadeOut(velocity_eq), FadeOut(velocity_explanation))
        
        
        equal_forces_title = Text("Igualando Força Gravitacional e Centrípeta", font_size=32).set_color_by_gradient(GREEN, WHITE).shift(3*UP)
        self.play(Write(equal_forces_title))
        self.wait(6)
        
        
        step1 = MathTex(r"G \frac{M m}{r^2} = \frac{4\pi^2 m r}{T^2}", font_size=40).set_color_by_gradient(GREEN, WHITE)
        step2 = MathTex(r"G M m = \frac{4\pi^2 m r^3}{T^2}", font_size=40).set_color_by_gradient(GREEN, WHITE)
        step3 = MathTex(r"G M = \frac{4\pi^2 r^3}{T^2}", font_size=40).set_color_by_gradient(GREEN, WHITE)
        step4 = MathTex(r"T^2 = \frac{4\pi^2}{G M} r^3", font_size=40).set_color_by_gradient(GREEN, WHITE)
        step5 = MathTex(r"T^2 \propto r^3", font_size=40).set_color_by_gradient(GREEN, WHITE)
        
        self.play(Write(step1))
        self.wait(3)
        self.play(ReplacementTransform(step1, step2))
        self.wait(3)
        self.play(ReplacementTransform(step2,step3))
        self.wait(3)
        self.play(ReplacementTransform(step3, step4))
        self.wait(4)
        self.play(ReplacementTransform(step4, step5))
        self.wait(4)
        
        
        
        conclusion_box = SurroundingRectangle(step5, buff=0.2, color=GREEN)
        self.play(Create(conclusion_box))
        
        conclusion_text = Text(" O Quadrado do Período Orbital é proporcional ao cubo do semieixo maior", 
                              font_size=15).set_color_by_gradient(GREEN, WHITE)
        conclusion_text.next_to(conclusion_box, DOWN, buff=0.5)
        self.play(Write(conclusion_text))
        self.wait(1)
        
        
        final_eq = MathTex(r"T^2 = K \cdot a^3", font_size=48).set_color_by_gradient(GREEN, WHITE)
        explanation = Text("Onde K é uma constante e a é o semieixo maior da órbita", font_size=24).set_color_by_gradient(GREEN, WHITE)
        final_group = VGroup(final_eq, explanation).arrange(DOWN, buff=0.5)
        final_group.move_to(ORIGIN)

        self.wait(2)
        
        self.play(FadeOut(equal_forces_title), FadeOut(step5), 
                  FadeOut(conclusion_box), FadeOut(conclusion_text))
        self.play(FadeIn(final_eq), FadeIn(explanation))
        self.wait(5)
        
        
        elliptical_text = Text("Para órbitas elípticas, a é o semieixo maior da elipse", font_size=24).set_color_by_gradient(GREEN, WHITE)
        elliptical_text.next_to(explanation, DOWN, buff=0.5)
        self.play(FadeIn(elliptical_text))
        self.wait(20)
        
        
        self.play(FadeOut(final_eq), FadeOut(explanation), FadeOut(elliptical_text))
        
        
        orbit_title = Text("Demonstração visual: Duas órbitas com períodos diferentes", font_size=15).set_color_by_gradient(GREEN, WHITE).shift(3*UP)
        orbit_title.next_to(title, UP, buff=0.5)
        self.play(Write(orbit_title))
        self.wait(1)
        self.remove(orbit_title)
        self.wait(1)
        
       
        sun = Dot(color=YELLOW, radius=0.2).move_to(ORIGIN)
        sun_label = Text("Sol", font_size=20, color=YELLOW).next_to(sun, DOWN, buff=0.1)
        self.play(FadeIn(sun), Write(sun_label))
        
       
        orbit1 = Circle(radius=1.5, color=BLUE)
        planet1 = Dot(color=BLUE_C, radius=0.1).move_to(orbit1.point_at_angle(0))
        planet1_label = Text("Planeta 1", font_size=16, color=BLUE_C).next_to(planet1, UP, buff=0.1)
        
        
        
        orbit2 = Circle(radius=3, color=RED)
        planet2 = Dot(color=RED_C, radius=0.1).move_to(orbit2.point_at_angle(0))
        planet2_label = Text("Planeta 2", font_size=16, color=RED_C).next_to(planet2, UP, buff=0.1)
        
        
        self.play(Create(orbit1), Create(orbit2))
        self.play(FadeIn(planet1), Write(planet1_label), 
                  FadeIn(planet2), Write(planet2_label))
        
        
        
        verification = Text("Verificação da Lei: T₁²/r₁³ = T₂²/r₂³", font_size=24).shift(4*DOWN)
        
        self.play(Write(verification))
        
        
        time_tracker = ValueTracker(0)
        
       
        w1 = 2 * PI / 1.84
        w2 = 2 * PI / 5.2
        
        
        def update_planet1(mob):
            
            angle = w1 * time_tracker.get_value()
            mob.move_to(sun.get_center() + np.array([1.5 * np.cos(angle), 1.5 * np.sin(angle), 0]))
            planet1_label.next_to(mob, UP, buff=0.1)
            
       
        def update_planet2(mob):
            
            angle = w2 * time_tracker.get_value()
            mob.move_to(sun.get_center() + np.array([3 * np.cos(angle), 3 * np.sin(angle), 0]))
            planet2_label.next_to(mob, UP, buff=0.1)
            
        
        planet1.add_updater(update_planet1)
        planet2.add_updater(update_planet2)
        
        
        self.play(time_tracker.animate.set_value(32), run_time=32, rate_func=linear)
        
       
        planet1.remove_updater(update_planet1)
        planet2.remove_updater(update_planet2)
        
        
        
        self.play(FadeOut(orbit1), FadeOut(orbit2), 
                  FadeOut(planet1), FadeOut(planet1_label),
                  FadeOut(planet2), FadeOut(planet2_label),
                  FadeOut(sun), FadeOut(sun_label),
                  FadeOut(verification))
        
       
        