import turtle
def draw_triangle():
    window=turtle.Screen();
    window.bgcolor("red");
    brad =turtle.Turtle();
    for i in range(1,3):
        brad.forward(100);
        brad.right(60)
    brad.right(90)
    brad.forward(170)
    sid=turtle.Turtle();
    sid.shape("turtle");
    sid.color('yellow');
    sid.circle(100);
    window.exitonclick();

draw_triangle();   
