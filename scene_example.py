from manim import *

class ManimCELogo(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN)
        self.add(logo)



class TextAlignment(Scene):
    def construct(self):
        title = Text("K-means clustering and Logistic Regression", color=WHITE)
        title.scale(0.75)
        self.add(title.to_edge(UP))

        t1 = Text("1. Measuring").set_color(WHITE)

        t2 = Text("2. Clustering").set_color(WHITE)

        t3 = Text("3. Regression").set_color(WHITE)

        t4 = Text("4. Prediction").set_color(WHITE)

        x = VGroup(t1, t2, t3, t4).arrange(direction=DOWN, aligned_edge=LEFT).scale(0.7).next_to(ORIGIN,DR)
        x.set_opacity(0.5)
        x.submobjects[1].set_opacity(1)
        self.add(x)

class FadeInExample(Scene):
    def construct(self):
        dot = Dot(UP * 2 + LEFT)
        self.add(dot)
        tex = Tex(
            "FadeIn with ", "shift ", " or target\_position", " and scale"
        ).scale(1)
        animations = [
            FadeIn(tex[0]),
            FadeIn(tex[1], shift=DOWN),
            FadeIn(tex[2], target_position=dot),
            FadeIn(tex[3], scale=1.5),
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))


class SimpsonTextAlignment(Scene):
    def construct(self):
        title = Text("辛普森悖论", color=WHITE)
        title.generate_target()
        animation_title=FadeIn(title,shift=UP)
        title.target.shift(3*UP+4*LEFT)
        self.play(animation_title)
        self.wait(2)
        self.play(MoveToTarget(title))

        announcement=(MarkupText('即在某个条件下的多组数据，<gradient from="RED" to="YELLOW">分别</gradient>讨论时都会满足某种性质', gradient=(BLUE, GREEN)),
                      MarkupText('可是一旦<gradient from="RED" to="YELLOW">合并</gradient>考虑，却可能导致相反的结论。',gradient=(BLUE, GREEN)))
        announcement[0].scale(0.6)
        announcement[1].scale(0.6)
        announcement[1].next_to(announcement[0],DOWN)
        announcement_animations=[
            FadeIn(announcement[0],shift=UP),
            FadeIn(announcement[1], shift=UP),
        ]
        self.play(AnimationGroup(*announcement_animations, lag_ratio=3.5))
        self.wait(2)
        self.play(Circumscribe(Group(announcement[0], announcement[1])))

class TreatmentTable(Scene):
    def construct(self):

        # support_data=Title("Subpopulation Data")
        # self.add(support_data)
        men_title=Text("Men")

        men=IntegerTable(
            [[6,81,87],
             [36,234,270]],
            row_labels=[Text("吃药"),Text("不吃药")],
            col_labels=[Text("没有康复"),Text("康复"),Text("总数")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=False,
            line_config={"stroke_width":1,"color":YELLOW}
        )
        # men.remove(men.get_vertical_lines()[1])

        women_title=Text("Women")
        women=IntegerTable(
            [[71,192,263],
             [25,55,80]],
            row_labels=[Text("吃药"),Text("不吃药")],
            col_labels=[Text("没有康复"),Text("康复"),Text("总数")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=False,
            line_config={"stroke_width":1,"color":YELLOW},
        )
        # women.remove(women.get_vertical_lines()[1])
        men_title.shift(UP*4)
        men.next_to(men_title,DOWN)
        women_title.next_to(men,DOWN)
        women.next_to(women_title,DOWN)

        g=Group(men_title,men,women_title, women).scale(0.7).arrange(DOWN)
        # self.add(g)
        self.play(Write(g[0]))
        self.wait()
        self.play(g[1].create())
        self.wait()
        self.play(Write(g[2]))
        self.wait()
        self.play(g[3].create())

        g.generate_target()
        g.target.shift(2*LEFT).scale(0.7)
        self.play(MoveToTarget(g))


        # ======================================= 1 ==========================================
        self.play(Circumscribe(men.get_rows()[1][2:],fade_in=True))
        self.wait()
        self.play(men[0][6].animate.set_color(BLUE),men[0][7].animate.set_color(ORANGE))
        self.wait(1)
        num_81=men[0][6].copy()
        num_87=men[0][7].copy()
        num_87.generate_target()
        num_81.target.scale(0.7).move_to(RIGHT*3 + UP)
        num_87.target.scale(0.7).move_to(RIGHT*3.5 + UP)

        self.play(MoveToTarget(num_81), MoveToTarget(num_87))
        self.wait(1)
        # 创建公式
        equation_1 = MathTex("{{81}}/{{87}}={{0.93}}").scale(0.7).shift(UP+RIGHT*4)
        equation_1.set_color_by_tex("81", BLUE)
        equation_1.set_color_by_tex("87", ORANGE)
        equation_1.set_color_by_tex("0.93", RED_B)

        #将数字替换到公式中
        self.play(FadeIn(equation_1[0]), ReplacementTransform(num_81, equation_1[0]))
        self.play(FadeIn(equation_1[2]), ReplacementTransform(num_87, equation_1[2]))

        #补充公式符号
        self.play(FadeIn(equation_1[1]), FadeIn(equation_1[3]), FadeIn(equation_1[4]))
        self.wait(2)

        # 添加橙色序号 ①
        number_1 = Text("①").scale(0.7).next_to(equation_1, RIGHT, buff=0.5)
        number_1.set_color(YELLOW_A)
        self.play(Write(number_1))
        self.wait(1)
        # ====================================== 2 ==========================================
        self.play(Circumscribe(men.get_rows()[2][2:],fade_out=True))
        self.wait()
        self.play(men[0][10].animate.set_color(BLUE),men[0][11].animate.set_color(ORANGE))
        self.wait(1)
        num_81=men[0][10].copy()
        num_87=men[0][11].copy()
        num_87.generate_target()

        # 创建公式
        equation_2 = MathTex("{{234}}/{{270}}={{0.87}}").scale(0.7).shift(UP+RIGHT*4)
        equation_2.next_to(equation_1, DOWN)
        equation_2.set_color_by_tex("234", BLUE)
        equation_2.set_color_by_tex("270", ORANGE)
        equation_2.set_color_by_tex("0.87", RED_C)

        num_81.target.move_to(equation_2[0].get_center())
        num_87.target.move_to(equation_2[2].get_center())

        self.play(MoveToTarget(num_81), MoveToTarget(num_87))
        self.wait(1)

        #将数字替换到公式中
        self.play(FadeIn(equation_2[0]), ReplacementTransform(num_81, equation_2[0]))
        self.play(FadeIn(equation_2[2]), ReplacementTransform(num_87, equation_2[2]))

        #补充公式符号
        self.play(FadeIn(equation_2[1]), FadeIn(equation_2[3]), FadeIn(equation_2[4]))
        self.wait(2)

        # 添加橙色序号 ①
        number_2 = Text("②").scale(0.7).next_to(equation_2, RIGHT, buff=0.5)
        number_2.set_color(ManimColor("#ffa502"))
        self.play(Write(number_2))
        self.wait(1)



        # ======================================= 3 ==========================================
        self.play(Circumscribe(women.get_rows()[1][2:],fade_in=True))
        self.wait()
        self.play(women[0][6].animate.set_color(BLUE),women[0][7].animate.set_color(ORANGE))
        self.wait(1)
        num_81=women[0][6].copy()
        num_87=women[0][7].copy()
        num_87.generate_target()
        num_81.target.scale(0.7).move_to(RIGHT*3 + DOWN)
        num_87.target.scale(0.7).move_to(RIGHT*3.5 + DOWN)

        self.play(MoveToTarget(num_81), MoveToTarget(num_87))
        self.wait(1)
        # 创建公式
        equation_3 = MathTex("{{192}}/{{263}}={{0.73}}").scale(0.7).shift(DOWN+RIGHT*4)
        equation_3.set_color_by_tex("192", BLUE)
        equation_3.set_color_by_tex("263", ORANGE)
        equation_3.set_color_by_tex("0.73", RED_B)

        #将数字替换到公式中
        self.play(FadeIn(equation_3[0]), ReplacementTransform(num_81, equation_3[0]))
        self.play(FadeIn(equation_3[2]), ReplacementTransform(num_87, equation_3[2]))

        #补充公式符号
        self.play(FadeIn(equation_3[1]), FadeIn(equation_3[3]), FadeIn(equation_3[4]))
        self.wait(2)

        # 添加橙色序号 ①
        number_3 = Text("③").scale(0.7).next_to(equation_3, RIGHT, buff=0.5)
        number_3.set_color(YELLOW_B)
        self.play(Write(number_3))
        self.wait(1)
        # ====================================== 4 ==========================================
        self.play(Circumscribe(women.get_rows()[2][2:],fade_out=True))
        self.wait()
        self.play(women[0][10].animate.set_color(BLUE),women[0][11].animate.set_color(ORANGE))
        self.wait(1)
        num_81=women[0][10].copy()
        num_87=women[0][11].copy()
        num_87.generate_target()

        # 创建公式
        equation_4 = MathTex("{{55}}/{{80}}={{0.69}}").scale(0.7).shift(DOWN+RIGHT*4)
        equation_4.next_to(equation_3, DOWN)
        equation_4.set_color_by_tex("55", BLUE)
        equation_4.set_color_by_tex("80", ORANGE)
        equation_4.set_color_by_tex("0.69", RED_C)

        num_81.target.move_to(equation_4[0].get_center())
        num_87.target.move_to(equation_4[2].get_center())

        self.play(MoveToTarget(num_81), MoveToTarget(num_87))
        self.wait(1)

        #将数字替换到公式中
        self.play(FadeIn(equation_4[0]), ReplacementTransform(num_81, equation_4[0]))
        self.play(FadeIn(equation_4[2]), ReplacementTransform(num_87, equation_4[2]))

        #补充公式符号
        self.play(FadeIn(equation_4[1]), FadeIn(equation_4[3]), FadeIn(equation_4[4]))
        self.wait(2)

        # 添加橙色序号 ①
        number_4 = Text("④").scale(0.7).next_to(equation_4, RIGHT, buff=0.5)
        number_4.set_color(YELLOW_C)
        self.play(Write(number_4))
        self.wait(1)
        
        