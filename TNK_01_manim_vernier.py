##−∗−coding: utf−8−∗−
'''manim manim2.py Shapes -p -l'''
'''https://talkingphysics.wordpress.com/2018/06/25/more-graphing-manim-series-part-8/'''

from manimlib.imports import *
import numpy as np
import os
import pyclbr

class Scene1(Scene):
    def construct(self):
        rectangle = Rectangle(height=1, width=3.5, color = BLUE,fill_color=BLUE, fill_opacity=1)
        main_scale = MainScale()
        arrow = Arrow(DOWN,UP, color = RED)
        vernier_scale = VernierScale(color = GOLD)


        self.play(ShowCreation(rectangle))
        self.wait(1)
        self.play(ApplyMethod(rectangle.shift,0.5*DOWN+3.25*LEFT))
        self.play(ShowCreation(main_scale))
        arrow.next_to(rectangle, RIGHT)
        arrow.shift(0.4*LEFT+0.25*DOWN) ### put arrow at the right edge of the rectangle
        self.wait(1)
        self.play(ShowCreation(arrow))
        self.wait(1)
        self.play(FadeOut(rectangle))
        self.wait(1)
        self.play(ApplyMethod(arrow.shift,0.8*LEFT))
        self.wait(1)
        self.play(ApplyMethod(arrow.shift,1.2*RIGHT))
        self.wait(1)
        self.play(ApplyMethod(arrow.shift,0.4*LEFT))
        self.wait(1)
        vernier_scale.next_to(arrow)
        vernier_scale.shift(0.53*LEFT)
        self.play(FadeOut(arrow),ShowCreation(vernier_scale))
        self.wait(1)
        self.play(ApplyMethod(vernier_scale.shift,3.530*LEFT))
        self.wait(1)




class Scene2(ZoomedScene):

    CONFIG = {
        "camera_class": MultiCamera,
        "zoomed_display_height": 4,
        "zoomed_display_width": 6,
        "zoomed_display_center": None,
        "zoomed_display_corner": UP + RIGHT,
        "zoomed_display_corner_buff": DEFAULT_MOBJECT_TO_EDGE_BUFFER,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 2,
            "background_opacity": 1,
        },
        "zoomed_camera_image_mobject_config": {},
        "zoomed_camera_frame_starting_position": 4*LEFT,
        "zoom_factor": 0.1,
        "image_frame_stroke_width": 2,
        "zoom_activated": False,
    }

#class DrawLine(ZoomedScene):
#    CONFIG = {
#        "zoom_factor" : 3,
#    }
    def construct(self):
        #label for main scale#
        #label for vernier scale#
        # vernier_label = ["0","1","2","3","4","5","6","7","8","9","0"]
        # #vernier_label = ["0","1"]
        # '''put label at the correct position'''
        # vernier_label_object = []
        # i = 0
        # for x in vernier_label:
        #     i = i+1
        #     text = TextMobject(x,color = BLUE)
        #     text = text.shift(((i-1)*0.9-5)*RIGHT+1.3*DOWN)
        #     vernier_label_object.append(text)
        # vernier_label_field = VGroup(*vernier_label_object)

        # main_label = ["0","1","2","3","4","5","6","7","8","9","10"]
        # main_label_object = []
        # i = 0
        # for x in main_label:
        #     i = i+1
        #     text = TextMobject(x,color = WHITE)
        #     text = text.shift(((i-1)-5)*RIGHT+1.3*UP)
        #     main_label_object.append(text)
        # main_label_field = VGroup(*main_label_object)

        # points = np.array([x*RIGHT
        #     for x in np.arange(-5,5.5,1)
        #     ])
        # main_scale = []  #Empty list to use in for loop
        # for point in points:
        #     line = Line(np.array([0,0,0]),np.array([0,1,0]))   #Constant line
        #     result = line.shift(point)   #Create vector and shift it to grid point
        #     main_scale.append(result)   #Append to list
        # main_field = VGroup(*main_scale)

        # points = np.array([x*RIGHT
        #     for x in np.arange(-5,4.5,0.9)
        #     ])
        # vernier_scale = []  #Empty list to use in for loop
        # for point in points:
        #     line = Line(np.array([0,0,0]),np.array([0,-1,0]),color=BLUE)   #Constant line
        #     result = line.shift(point)   #Create vector and shift it to grid point
        #     vernier_scale.append(result)   #Append to list
        # vernier_field = VGroup(*vernier_scale)

        # self.vernier_set = VGroup(vernier_field,vernier_label_field)
        # self.main_set = VGroup(main_field,main_label_field)


        #self.play(ShowCreation(self.main_set))
        vernier_scale = VernierScale(color = GOLD)
        main_scale = MainScale()
        main_scale_label_th=TextMobject("\\tha สเกลหลัก (mm)")
        main_scale_label_en=TextMobject("main scale (mm)")
        main_scale_label_en.next_to(main_scale,UP)
        main_scale_label_th.next_to(main_scale_label_en,UP)

        vernier_scale_label_th=TextMobject("\\tha สเกลเวอร์เนียร์", color = GOLD)
        vernier_scale_label_en=TextMobject("vernier scale", color = GOLD)
        vernier_scale_label_th.next_to(vernier_scale,DOWN)
        vernier_scale_label_en.next_to(vernier_scale_label_th,DOWN)

        eq1=TextMobject("\\tha 10 ช่องเวอร์เนียร์ = 9 ช่องหลัก",color = GOLD)
        eq1.next_to(vernier_scale,DOWN)
        eq2=TextMobject("\\tha 1 ช่องเวอร์เนียร์กว้าง 0.9 mm",color = GOLD)
        eq2.next_to(eq1,DOWN)

        self.add(main_scale)
        self.add(vernier_scale)
        self.wait(1)
        self.play(ShowCreation(main_scale_label_en),ShowCreation(main_scale_label_th))
        #self.play(ShowCreation(vernier_field))
        #self.play(ShowCreation(vernier_label_field))
        
        self.play(ShowCreation(vernier_scale_label_en),ShowCreation(vernier_scale_label_th))
        self.wait(1)
        self.play(FadeOut(vernier_scale_label_en),FadeOut(vernier_scale_label_th),FadeOut(main_scale_label_en),FadeOut(main_scale_label_th))
        self.wait(1)
        self.play(ShowCreation(eq1))
        self.wait(1)
        self.play(ShowCreation(eq2))
        self.wait(1)
        self.play(FadeOut(eq1),FadeOut(eq2))
        self.wait(1)

        little_box = self.zoomed_camera
        big_box = self.zoomed_display

        #self.frame_height = 100
        #self.zoomed_camera_frame_starting_position = 2.25 * UP + 1.75 * LEFT
        #self.zoomfactor = 1
        #zoom_rect = self.big_rectangle
        little_box.frame.shift(LEFT)
        self.play(ShowCreation(little_box.frame))

        zd_rect = BackgroundRectangle(
            big_box,
            fill_opacity=0,
            buff=MED_SMALL_BUFF,
        )

        self.add_foreground_mobject(zd_rect)

        # animation of unfold camera
        unfold_camera = UpdateFromFunc(
            zd_rect,
            lambda rect: rect.replace(big_box)
        )

        self.activate_zooming()
        self.play(
            # You have to add this line
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera
        )
        #self.get_zoomed_display_pop_out_animation()
        self.wait(1)
        self.play(ApplyMethod(little_box.frame.shift,RIGHT))

        delta_1 = Rectangle(height=0.03, width=0.1, color = RED,fill_color=RED, fill_opacity=1)
        delta_1.shift(4.05*LEFT)

        delta_1_txt1=TextMobject("\\tha ห่างกัน", color = RED)
        delta_1_txt1.scale(0.1)
        delta_1_txt2=TextMobject("\\tha 1.0 mm - 0.9 mm", color = RED)
        delta_1_txt2.scale(0.1)
        delta_1_txt3=TextMobject("\\tha = 0.1 mm", color = RED)
        delta_1_txt3.scale(0.1)
        delta_1_txt1.next_to(delta_1,0.2*RIGHT)
        delta_1_txt2.next_to(delta_1_txt1,0.1*DOWN)
        delta_1_txt3.next_to(delta_1_txt2,0.1*DOWN)



        self.wait(1)
        self.play(FadeIn(delta_1),FadeIn(delta_1_txt1),FadeIn(delta_1_txt2),FadeIn(delta_1_txt3))
        self.wait(1)
        self.play(FadeOut(delta_1),FadeOut(delta_1_txt1),FadeOut(delta_1_txt2),FadeOut(delta_1_txt3))

        delta_2 = Rectangle(height=0.03, width=0.2, color = RED,fill_color=RED, fill_opacity=1)
        delta_2.shift(3.10*LEFT)

        delta_2_txt1=TextMobject("\\tha ห่างกัน", color = RED)
        delta_2_txt1.scale(0.1)
        delta_2_txt2=TextMobject("\\tha 2.0 mm - 1.8 mm", color = RED)
        delta_2_txt2.scale(0.1)
        delta_2_txt3=TextMobject("\\tha = 0.2 mm", color = RED)
        delta_2_txt3.scale(0.1)
        delta_2_txt1.next_to(delta_2,0.2*RIGHT)
        delta_2_txt2.next_to(delta_2_txt1,0.1*DOWN)
        delta_2_txt3.next_to(delta_2_txt2,0.1*DOWN)

        self.wait(1)
        self.play(ApplyMethod(little_box.frame.shift,RIGHT))
        self.wait(1)
        self.play(FadeIn(delta_2),FadeIn(delta_2_txt1),FadeIn(delta_2_txt2),FadeIn(delta_2_txt3))
        self.wait(1)
        self.play(FadeOut(delta_2),FadeOut(delta_2_txt1),FadeOut(delta_2_txt2),FadeOut(delta_2_txt3))

        self.wait(1)
        self.play(ApplyMethod(little_box.frame.shift,LEFT))
        self.wait(1)
        shift_vernier_txt=TextMobject("\\tha เลื่อนสเกลเวอร์เนียร์ไปทางขวา 0.1 mm", color = GOLD)
        shift_vernier_txt.next_to(vernier_scale,1.5*DOWN)
        self.play(ApplyMethod(vernier_scale.shift,RIGHT*0.1),FadeIn(shift_vernier_txt))

        yes_line = Rectangle(height=2, width=0.01, color = RED,fill_color=RED, fill_opacity=1)
        yes_line.shift(4.0*LEFT)
        self.play(FadeIn(yes_line))
        self.wait(1)
        self.play(FadeOut(yes_line))
        self.wait(1)
        self.play(ApplyMethod(little_box.frame.shift,RIGHT))
        self.wait(1)
        shift_vernier_txt2=TextMobject("\\tha เลื่อนสเกลเวอร์เนียร์ไปทางขวาอีก 0.1 mm", color = GOLD)
        shift_vernier_txt2_sub=TextMobject("\\tha รวมเป็น 0.2 mm", color = GOLD)
        shift_vernier_txt2.next_to(vernier_scale,1.5*DOWN)
        shift_vernier_txt2_sub.next_to(shift_vernier_txt2,1.0*DOWN)        
        self.play(ApplyMethod(vernier_scale.shift,RIGHT*0.1),Transform(shift_vernier_txt,shift_vernier_txt2),FadeIn(shift_vernier_txt2_sub))
        yes_line.shift(RIGHT)
        self.wait(1)
        self.play(FadeIn(yes_line))
        self.wait(1)
        #self.play(FadeOut(yes_line))
        #self.wait(1)
        self.play(FadeOut(little_box.frame),FadeOut(big_box.display_frame))
        self.wait(1)
        self.play(FadeOut(shift_vernier_txt),FadeOut(shift_vernier_txt2_sub))
        self.wait(1)
        self.play(FadeOut(yes_line))
        yes_line.shift(LEFT*2.0)
        self.play(ApplyMethod(vernier_scale.shift,LEFT*0.2))
        self.play(FadeIn(yes_line))
        self.wait(1)

class Scene3(Scene):

#class DrawLine(ZoomedScene):
#    CONFIG = {
#        "zoom_factor" : 3,
#    }
    def construct(self):
        vernier_scale = VernierScale(color = GOLD)
        main_scale = MainScale()


        vernier_scale_label_th=TextMobject("\\tha เลื่อนสเกลเวอร์เนียร์ไปทางขวา", color = GOLD)
        vernier_scale_label_th.next_to(vernier_scale,DOWN)
        vernier_number=TextMobject("\\tha 0.0 mm", color = GOLD)
        vernier_number.next_to(vernier_scale_label_th,RIGHT)
        vernier_number.shift(DOWN*0.12)

        yes_line = Rectangle(height=2, width=0.01, color = RED,fill_color=RED, fill_opacity=1)
        yes_line.shift(5.0*LEFT)

        self.add(main_scale)
        self.add(vernier_scale)
        self.add(yes_line)
        self.play(FadeIn(vernier_scale_label_th),FadeIn(vernier_number))

        for i in range(9):

            self.wait(0.5)
            self.play(FadeOut(yes_line))
            yes_line.shift(RIGHT)
            text = "\\tha 0." + str(i+1)+ " mm"
            vernier_new_number = TextMobject(text, color = GOLD)
            vernier_new_number.next_to(vernier_scale_label_th,RIGHT)
            vernier_new_number.shift(DOWN*0.12)        
            self.play(ApplyMethod(vernier_scale.shift,RIGHT*0.1),Transform(vernier_number,vernier_new_number))
            self.play(FadeIn(yes_line))

        self.wait(0.5)
        self.play(FadeOut(yes_line))
        yes_line.shift(RIGHT)
        text = "\\tha 1.0 mm"
        vernier_new_number = TextMobject(text, color = GOLD)
        vernier_new_number.next_to(vernier_scale_label_th,RIGHT)
        vernier_new_number.shift(DOWN*0.12)        
        self.play(ApplyMethod(vernier_scale.shift,RIGHT*0.1),Transform(vernier_number,vernier_new_number))
        self.play(FadeIn(yes_line))

        self.wait(0.5)
        self.play(FadeOut(yes_line))
        yes_line.shift(9*LEFT)       
        self.play(FadeIn(yes_line))

        self.wait(0.5)
        self.play(FadeOut(yes_line))
        yes_line.shift(RIGHT)       
        text = "\\tha 1.1 mm"
        vernier_new_number = TextMobject(text, color = GOLD)
        vernier_new_number.next_to(vernier_scale_label_th,RIGHT)
        vernier_new_number.shift(DOWN*0.12)        
        self.play(ApplyMethod(vernier_scale.shift,RIGHT*0.1),Transform(vernier_number,vernier_new_number))
        self.play(FadeIn(yes_line))

        self.wait(0.5)
        self.play(FadeOut(yes_line))
        yes_line.shift(RIGHT)       
        text = "\\tha 1.2 mm"
        vernier_new_number = TextMobject(text, color = GOLD)
        vernier_new_number.next_to(vernier_scale_label_th,RIGHT)
        vernier_new_number.shift(DOWN*0.12)        
        self.play(ApplyMethod(vernier_scale.shift,RIGHT*0.1),Transform(vernier_number,vernier_new_number))
        self.play(FadeIn(yes_line))

class ZoomedSceneExample(ZoomedScene):
    CONFIG = {
        "zoom_factor": 0.3,
        "zoomed_display_height": 1,
        "zoomed_display_width": 6,
        "image_frame_stroke_width": 20,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 3,
        },
    }

    def construct(self):
        # Set objects
        dot = Dot().shift(UL*2)

        image=ImageMobject(np.uint8([[ 0, 100,30 , 200],
                                     [255,0,5 , 33]]))
        image.set_height(7)
        frame_text=TextMobject("Frame",color=PURPLE).scale(1.4)
        zoomed_camera_text=TextMobject("Zommed camera",color=RED).scale(1.4)

        self.add(image,dot)

        # Set camera
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(dot)
        frame.set_color(PURPLE)

        zoomed_display_frame.set_color(RED)
        zoomed_display.shift(DOWN)

        # brackground zoomed_display
        zd_rect = BackgroundRectangle(
            zoomed_display,
            fill_opacity=0,
            buff=MED_SMALL_BUFF,
        )

        self.add_foreground_mobject(zd_rect)

        # animation of unfold camera
        unfold_camera = UpdateFromFunc(
            zd_rect,
            lambda rect: rect.replace(zoomed_display)
        )

        frame_text.next_to(frame,DOWN)

        self.play(
            ShowCreation(frame),
            FadeInFromDown(frame_text)
        )

        # Activate zooming
        self.activate_zooming()

        self.play(
            # You have to add this line
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera
        )

        zoomed_camera_text.next_to(zoomed_display_frame,DOWN)
        self.play(FadeInFromDown(zoomed_camera_text))

        # Scale in     x   y  z
        scale_factor=[0.5,1.5,0]

        # Resize the frame and zoomed camera
        self.play(
            frame.scale,                scale_factor,
            zoomed_display.scale,       scale_factor,
            FadeOut(zoomed_camera_text),
            FadeOut(frame_text)
        )

        # Resize the frame
        self.play(
            frame.scale,3,
            frame.shift,2.5*DOWN
        )

        # Resize zoomed camera
        self.play(
            ScaleInPlace(zoomed_display,2)
        )


        self.wait()

        self.play(
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera,
            # -------> Inverse
            rate_func=lambda t: smooth(1-t),
        )
        self.play(
            Uncreate(zoomed_display_frame),
            FadeOut(frame),
        )
        self.wait()

class AddingText(Scene):
    #Adding text on the screen
    def construct(self):
        my_first_text=TextMobject("\\tha สวัสดี")
        #my_first_text.scale(3)
        second_line=TextMobject("\\tha วันนี้เราจะมาเรียนเรื่อง")
        second_line.next_to(my_first_text,DOWN)
        third_line=TextMobject("\\tha ที่สำคัญมาก")
        third_line.next_to(my_first_text,DOWN)
 
        self.add(my_first_text, second_line)
        self.wait(2)
        self.play(Transform(second_line,third_line))
        #self.wait(2)
        #second_line.shift(3*DOWN)
        #self.play(ApplyMethod(my_first_text.shift,3*UP))

class MainScale(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs) ### must have
        main_label = ["0","1","2","3","4","5","6","7","8","9","10"]
        main_label_object = []
        i = 0
        for x in main_label:
            i = i+1
            text = TextMobject(x,color = WHITE)
            text = text.shift(((i-1)-5)*RIGHT+1.3*UP)
            main_label_object.append(text)
        main_label_field = VGroup(*main_label_object)

        points = np.array([x*RIGHT
            for x in np.arange(-5,5.5,1)
            ])
        main_scale = []  #Empty list to use in for loop
        for point in points:
            line = Rectangle(height=1, width=0.01, color = self.color,fill_color=self.color, fill_opacity=1)
            #line = Line(np.array([0,0,0]),np.array([0,1,0]),stroke_width = 5) #Constant line
            result = line.shift(point+0.5*UP)   #Create vector and shift it to grid point
            main_scale.append(result)   #Append to list
        main_field = VGroup(*main_scale)

        main_set = VGroup(main_field,main_label_field)
        self.add(main_set)

class VernierScale(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        vernier_label = ["0","1","2","3","4","5","6","7","8","9","0"]
        #vernier_label = ["0","1"]
        '''put label at the correct position'''
        vernier_label_object = []
        i = 0
        for x in vernier_label:
            i = i+1
            text = TextMobject(x,color = self.color)
            text = text.shift(((i-1)*0.9-5)*RIGHT+1.3*DOWN)
            vernier_label_object.append(text)
        vernier_label_field = VGroup(*vernier_label_object)

        points = np.array([x*RIGHT
            for x in np.arange(-5,4.5,0.9)
            ])
        vernier_scale = []  #Empty list to use in for loop
        for point in points:
            line = Rectangle(height=1, width=0.01, color = self.color,fill_color=self.color, fill_opacity=1)
            #line = Line(np.array([0,0,0]),np.array([0,-1,0]),color=self.color,stroke_width = 5)   #Constant line
            result = line.shift(point+0.5*DOWN)   #Create vector and shift it to grid point
            vernier_scale.append(result)   #Append to list
        vernier_field = VGroup(*vernier_scale)

        vernier_set = VGroup(vernier_field,vernier_label_field)
        self.add(vernier_set)
