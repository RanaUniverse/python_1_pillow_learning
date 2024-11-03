"""
I want to make Images using pillow just for checking how 
to make python funcions and moduels for me 
so here i have some logics on how to use funcions
"""

# This below fun will generate the Image obj of Pillow library
from my_own_module.image_making_fun import make_a_circle_in_square


def main():
    print("A image will generated from pillow library")
    color_of_outside = (255, 255, 0)
    color_of_inside_circle = (0, 0, 255)
    color_of_border = (40, 190, 60)
    im = make_a_circle_in_square(
        size=2000,
        # radius=500,
        background_color=color_of_outside,
        circle_color=color_of_inside_circle,
        boundary_color=color_of_border,
        boundary_width=50
    )
    im.show()


if __name__ == "__main__":
    main()
