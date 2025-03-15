import numpy as np
from manim import *





class MovimentoObliquo1(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        titulo = Tex('Lançamento Oblíquo').set_color_by_t2c({"Oblíquo": BLUE})
        instagram = Tex('@CelestialEquations').scale(0.5).shift(LEFT*5.5 + 3.7*UP)
        angulo = Arc(       
            radius=0.2, 
            start_angle=PI/4, 
            angle=-PI/4, 
            color= WHITE).shift(LEFT*6+DOWN*3)
        angulo_nome = MathTex(r"\theta ").next_to(angulo, 0.3*LEFT+RIGHT*0.5+UP*0.12+DOWN*0.105).scale(0.5)
        
        ax = Axes(
            x_range=[0, 4.5],
            y_range=[0, 6],
            axis_config={"color": RED_B },
            tips=True,
        )
        equacao_vetorx = MathTex(r'Vx = Vcos(\theta)').scale(0.75).shift(LEFT*5.5+3.7*DOWN)
        equacao_vetory = MathTex(r'Vy = Vsen(\theta)').scale(0.75).shift(LEFT*5.5+4.4*DOWN)

        labels = ax.get_axis_labels(x_label="x", y_label="Y")
        grafico = ax.plot(lambda x: 4 * x - x ** 2, x_range=[0, 4], color=BLUE_C)

        moving_dot = Dot(ax.i2gp(0, grafico), color=RED)
        dot_inicial = Dot(ax.i2gp(0, grafico))  
        dot_final = Dot(ax.i2gp(4, grafico))  
        velocidade_vetorx = Arrow(start=moving_dot.get_center(), end=moving_dot.get_center() + RIGHT, color=YELLOW)
        velocidade_vetory = Arrow(start=moving_dot.get_center(), end=moving_dot.get_center() + UP, color=RED)
        nome_vetorx = Tex('Vx').next_to(velocidade_vetorx).scale(0.5)
        nome_vetory = Tex('Vy').next_to(velocidade_vetory).scale(0.5)
        self.play(Write(titulo))
        self.play(Write(instagram))
        self.wait(1)
        self.play(Transform(titulo, ax))
        self.play(Write(labels))
        self.play(Create(grafico))
        self.play(Create(angulo), Write(angulo_nome))
        self.wait(1)
        self.add(dot_inicial, dot_final, moving_dot)
        self.add(velocidade_vetorx, velocidade_vetory, nome_vetorx, nome_vetory)
        self.play(self.camera.frame.animate.scale(0.6).move_to(dot_inicial))
        self.play(Write(equacao_vetorx))
        self.play(Write(equacao_vetory))
        self.wait(1)

        self.play(self.camera.frame.animate.move_to(moving_dot))
        self.remove(equacao_vetorx, equacao_vetory)
        def update_vectors(mob):
            pos = moving_dot.get_center()
            
            t = pos[0] / 16  
            vy = 0.01*np.sin(np.radians(45)) - 9.81 * t 
            velocidade_vetorx.put_start_and_end_on(moving_dot.get_center(), moving_dot.get_center() + RIGHT)
            velocidade_vetory.put_start_and_end_on(moving_dot.get_center(), moving_dot.get_center() + UP * (vy / 5))  # Normaliza para visualização
            nome_vetorx.move_to(velocidade_vetorx.get_end() + RIGHT * 0.2)
            nome_vetory.move_to(velocidade_vetory.get_end() + UP * 0.2)
            
            if vy <= 0:
                return True 

            return False
        velocidade_vetorx.add_updater(update_vectors)
        velocidade_vetory.add_updater(update_vectors)
        nome_vetorx.add_updater(update_vectors)
        nome_vetory.add_updater(update_vectors)
    
        def curva_atualizada(mob):
            mob.move_to(moving_dot.get_center())
        
        self.camera.frame.add_updater(curva_atualizada)
        

        self.play(MoveAlongPath(moving_dot, grafico, rate_func=linear), run_time=7, stop_at_point=2)


        self.camera.frame.remove_updater(curva_atualizada)
        velocidade_vetorx.remove_updater(update_vectors)
        velocidade_vetory.remove_updater(update_vectors)
        nome_vetorx.remove_updater(update_vectors)
        nome_vetory.remove_updater(update_vectors)
        
        self.play(Restore(self.camera.frame))
        self.remove(velocidade_vetorx, velocidade_vetory, nome_vetorx, nome_vetory)
        
        #2 PARTE

        ponto = Dot(ax.i2gp(2, grafico), color = RED)
      
        
        x_value = 2
        y_value = 4 * x_value - x_value ** 2 
        
        linha_altura = ax.get_vertical_line(ax.c2p(x_value, y_value), color=YELLOW)
        nome_altura = MathTex('Hmax', color = YELLOW).next_to(linha_altura, RIGHT)
        self.play(Create(linha_altura))
        self.play(Write(nome_altura))
        self.wait(1)
        self.play(Create(ponto))
        self.play(self.camera.frame.animate.scale(0.6).move_to(ponto))
        self.wait(1)
        equacao_1 = Tex('Vy = 0').next_to(ponto, UP).scale(0.5)
        equacao2 = Tex('Vx = constante ').next_to(ponto, 2.5*UP).scale(0.5)
        self.play(Write(MathTex(r'Vx = Vcos(\theta)').shift(3.2*UP+LEFT*3.7).scale(0.5)))
        self.play(Write(MathTex(r'Vy = Vsen(\theta)').shift(2.8*UP+LEFT*3.7).scale(0.5)))
        self.play(Write(equacao_1))
        self.wait(2)
        self.remove(equacao_1)
        equacao_3 = MathTex(r'Torricelli: 'r'v_{y}^2 - v^2sen^2(\theta )= -2gy').next_to(ponto, 2.5*UP).scale(0.5)
        texto = Tex('Quando y = Hmax, Vy = 0 , então:').next_to(ponto, 2.5*UP).scale(0.5)
        equacao_4 = MathTex(r'Hmax = \frac{V^2sen^2(\theta )}{2g}').next_to(ponto, 2*UP).scale(0.5)
        texto2= Tex('Calculando a altura máxima(Hmax):').next_to(ponto, 2.5*UP).scale(0.5)
        framebox1 = SurroundingRectangle(equacao_4, buff = .1)
        self.play(Write(texto2))
        self.wait(1)
        self.play(ReplacementTransform(texto2, equacao_3))
        self.wait(1.3)
        self.play(ReplacementTransform(equacao_3, texto))
        self.wait(1)
        self.play(ReplacementTransform(texto, equacao_4))
        self.play(Create(framebox1))
        self.wait(1)
        self.play(Restore(self.camera.frame))

        #3 PARTE
        alcance = Line(dot_inicial, dot_final)
        nome_altura = MathTex('A', color = WHITE).next_to(alcance, DOWN)
        self.play(Create(alcance), Write(nome_altura))
        self.play(self.camera.frame.animate.shift(DOWN * 2.5), run_time=2)
        texto3= Tex('Para calcular o alcance, precisamos determinar o tempo total da trajetória.').shift(4.4*DOWN).scale(0.5)
        texto4 = Tex('Igualando a equação horária da posição (MRUV) a zero:').shift(4.4*DOWN).scale(0.5)
        equacao5 = MathTex(r'y(t) = Vsen(\theta )t - \frac{gt^2}{2} = 0').shift(LEFT*0.5+4.5*DOWN).scale(0.5)
        equacao6 = MathTex(r't=\frac{2Vsen(\theta)}{g}').shift(LEFT*0.5+4.5*DOWN).scale(0.5)
        equacao7 = MathTex(r'A = \frac{2Vsen(\theta)cos(\theta)}{g}=\frac{V^2sen(2\theta)}{g}').shift(LEFT*0.5+6*DOWN).scale(0.4)
        texto5 = Tex(r'Substituindo $t$ em $x(t) = V \cos(\theta) t$').shift(+LEFT*0.5+5.2 * DOWN).scale(0.4)
        framebox2 = SurroundingRectangle(equacao6, buff = .1)
        framebox3 = SurroundingRectangle(equacao7, buff = .1, color = BLUE)
        framebox1 = SurroundingRectangle(equacao_4, buff = .1)
        self.play(Write(texto3))
        self.play(self.camera.frame.animate.scale(0.6).move_to(texto3))
        self.wait(1)
        self.play(ReplacementTransform(texto3, texto4))
        self.wait(1)
        self.play(ReplacementTransform(texto4, equacao5))
        self.wait(1)
        self.play(ReplacementTransform(equacao5, equacao6))
        self.play(Create(framebox2))
        self.play(Write(texto5))
        self.wait(1)
        self.play(Write(equacao7))
        self.play(Create(framebox3))
        self.wait(1)
        



        
