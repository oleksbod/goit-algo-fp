import turtle

def draw_pifagor_tree(branch_length, level):
    if level == 0:
        return
    # draw the branch
    turtle.forward(branch_length)
    turtle.right(45)
    draw_pifagor_tree(0.7 * branch_length, level - 1)
    turtle.left(90)
    draw_pifagor_tree(0.7 * branch_length, level - 1)
    turtle.right(45)
    turtle.backward(branch_length)

def main():
    # Отримання рівня від користувача
    level = int(input("Enter the recursion depth: "))

    # Setup
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    turtle.color("green")
   
    turtle.speed(0)
    turtle.left(90)
 
    draw_pifagor_tree(100, level)

    turtle.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()