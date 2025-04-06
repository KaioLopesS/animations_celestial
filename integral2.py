from manim import *
import numpy as np




class IntegralXSinX(Scene):
    def construct(self):
   
        celestial_equations = ImageMobject("Prancheta_2-removebg-preview.png")
        celestial_equations.scale(0.5)
        celestial_equations.shift(LEFT*5.5+3*UP)
        self.play(FadeIn(celestial_equations))
        self.wait(0.5)

        integral_display = MathTex(r"\int x \sin(x) \, dx", font_size=80).set_color_by_gradient(GREEN, BLUE)
        self.play(FadeIn(integral_display))
        self.wait(1)
        self.play(Circumscribe(integral_display, color=GREEN, run_time=2))
        self.wait(1)
        self.play(FadeOut(integral_display))
        self.wait(1)

        approach = Text("Usando Integração por Partes", font_size=32).shift(4.5*UP)
        self.play(Write(approach))
        self.wait(1)

        product_rule_diff = MathTex(r"d(uv)", r"=", r"u \, dv", r"+", r"v \, du", font_size=44).set_color(WHITE).next_to(approach, DOWN, buff=0.5)
        rearranged1 = MathTex(r"d(uv)", r"-", r"v \, du", r"=", r"u \, dv", font_size=44).set_color(WHITE).next_to(approach, DOWN, buff=0.5)
        integrated_form = MathTex(r"\int", r"d(uv)", r"-", r"\int", r"v \, du", r"=", r"\int", r"u \, dv", font_size=44).set_color(WHITE).next_to(approach, DOWN, buff=0.5)
        evaluated_integral = MathTex(r"uv", r"-", r"\int", r"v \, du", r"=", r"\int", r"u \, dv", font_size=44).set_color(WHITE).next_to(approach, DOWN, buff=0.5)
        formula = MathTex(r"\int u \, dv = uv - \int v \, du", font_size=48).set_color_by_gradient(GREEN, BLUE)
        formula.next_to(approach, DOWN, buff=0.5)
        self.play(Write(product_rule_diff))
        self.wait(7)
        self.play(ReplacementTransform(product_rule_diff, rearranged1))
        self.wait(4)
        self.play(ReplacementTransform(rearranged1, integrated_form))
        self.wait(5)
        self.play(ReplacementTransform(integrated_form, evaluated_integral))
        self.wait(6)
        self.play(ReplacementTransform(evaluated_integral, formula))
        self.wait(4)
        
        choices_title = Text("Escolhendo as partes (LIATE):", font_size=28)
        choices_title.next_to(formula, DOWN, buff=0.7)
        self.play(FadeOut(approach),Write(choices_title))
        self.wait(15)

        choices_eqs = VGroup(
            MathTex(r"u = x", font_size=40),
            MathTex(r"dv = \sin(x) \, dx", font_size=40)
        ).arrange(RIGHT, buff=1.0).set_color(YELLOW)
        choices_eqs.next_to(choices_title, DOWN, buff=0.3)
        self.play(Write(choices_eqs))
        self.wait(14)

        derivations_title = Text("Calculando du e v:", font_size=28)
        derivations_title.next_to(choices_eqs, DOWN, buff=0.7)
        self.play(Write(derivations_title))
        self.wait(3)

        derivations_eqs = VGroup(
             MathTex(r"\Rightarrow du = dx", font_size=40 ),
             MathTex(r"\Rightarrow v = \int \sin(x) \, dx = -\cos(x)", font_size=40)
        ).arrange(RIGHT, buff=0.5).set_color_by_gradient(GREEN, WHITE, BLUE)
        derivations_eqs.next_to(derivations_title, DOWN, buff=0.3)
        self.play(Write(derivations_eqs))
        self.wait(15)

        explanation_group = VGroup(approach, formula, choices_title, choices_eqs, derivations_title, derivations_eqs)

        self.play(explanation_group.animate.shift(1.5*UP))
        self.wait(1)

        step1_lhs = MathTex(r"\int", r"x", r"\sin(x) \, dx").set_color_by_gradient(GREEN, BLUE).scale(0.9)
        step1_lhs.shift(DOWN*2+LEFT*3)
        self.play(Write(step1_lhs))
        self.wait(1)

        rect_u = SurroundingRectangle(step1_lhs[1], color=YELLOW, buff=0.05)
        rect_dv = SurroundingRectangle(step1_lhs[2], color=YELLOW, buff=0.05)
        label_u = MathTex("u", color=YELLOW).next_to(rect_u, DOWN, buff=0.1)
        label_dv = MathTex("dv", color=YELLOW).next_to(rect_dv, DOWN, buff=0.1)
        self.play(Create(rect_u), Create(rect_dv))
        self.play(Write(label_u), Write(label_dv))
        self.wait(2)
        self.play(FadeOut(rect_u), FadeOut(rect_dv), FadeOut(label_u), FadeOut(label_dv))
        self.wait(0.5)

        step1_rhs = MathTex(r"=", r"u", r"v", r"-", r"\int", r"v", r"du").scale(1).next_to(step1_lhs, RIGHT, buff=0.2).set_color_by_gradient(GREEN, BLUE)

        step2_rhs = MathTex(
            r"=",                
            r"(x)",             
            r"(-\cos(x))",     
            r"-",               
            r"\int",           
            r"(-\cos(x))",      
            r"(dx)"             
        ).scale(0.8).next_to(step1_lhs, RIGHT, buff=0.2).set_color_by_gradient(GREEN, BLUE)

       
        current_eq = VGroup(step1_lhs, step1_rhs)
        target_eq = VGroup(step1_lhs.copy(), step2_rhs) 
        self.play(TransformMatchingTex(current_eq, target_eq, transform_mismatched_indices=True, run_time=2)) 
        self.wait(2)
        self.wait(15)


   
        step3_rhs = MathTex(
            r"=",               
            r"-x \cos(x)",      
            r"+",               
            r"\int \cos(x) \, dx" 
        ).scale(1).next_to(step1_lhs, RIGHT, buff=0.2).set_color_by_gradient(GREEN, BLUE)

        current_eq = VGroup(step1_lhs, step2_rhs) 
        target_eq = VGroup(step1_lhs, step3_rhs)  
        self.play(TransformMatchingTex(current_eq, target_eq, transform_mismatched_indices=True))
        self.wait(4)

       
        step4_rhs = MathTex(
            r"=",              
            r"-x \cos(x)",     
            r"+",               
            r"\sin(x)"          
        ).scale(1).next_to(step1_lhs, RIGHT, buff=0.2).set_color_by_gradient(GREEN, BLUE)

        current_eq = VGroup(step1_lhs, step3_rhs) 
        target_eq = VGroup(step1_lhs, step4_rhs)  
        self.play(TransformMatchingTex(current_eq, target_eq, transform_mismatched_indices=True))
        self.wait()
        self.play(FadeOut(step1_lhs))

        full_equation_no_C = VGroup(step1_lhs, step4_rhs)
        

       
        self.play(FadeOut(explanation_group))
        self.wait(2)

       
        final_result = MathTex(r"\int x \sin(x) \, dx = -x \cos(x) + \sin(x) + C").set_color_by_gradient(GREEN, BLUE).scale(1)
        final_result.move_to(ORIGIN + UP) 

        
        self.play(TransformMatchingTex(full_equation_no_C, final_result, transform_mismatched_indices=True), run_time=2)
        self.wait(2)
        obrigado = Text("Obrigado por assistir!", font_size=24).next_to(final_result, 6*DOWN, buff=0.5)
        
        self.wait(2)

        framebox_final = SurroundingRectangle(final_result, buff=0.2, color=GREEN)
        self.play(Create(framebox_final))
        self.wait(5)
        self.play(ReplacementTransform(step1_lhs, obrigado ))
        self.wait(15)

     
        self.wait(1) 