"""
Here i will have some fun which will do
some image generateion of Geometrical Shapes
"""

from PIL import Image, ImageDraw


def create_square_image(size, color):
    """
    Here the size will the one side length of square in px
    color is tuple of 3 int or solid color name
    """
    im = Image.new("RGB", (size, size), color)
    return im


def create_square_with_diagonals(
    size=1024,
    background_color="white",
    line_color="blue",
    line_width=10,
):
    im = Image.new("RGB", (size, size), background_color)
    draw = ImageDraw.Draw(im)

    top_left = (0, 0)
    bottom_right = (size, size)
    top_right = (size, 0)
    bottom_left = (0, size)

    draw.line([top_left, bottom_right], fill=line_color, width=line_width)
    draw.line([top_right, bottom_left], fill=line_color, width=line_width)

    return im


def make_a_circle_in_square(
    size=1024,
    radius=None,
    background_color="white",
    circle_color="black",
    boundary_color="red",
    boundary_width=10,
    dot_radius=5,
):
    # im = Image.new("RGB", (size, size), background_color)
    # im = create_square_image(size, background_color)
    im = create_square_with_diagonals(size, line_width=boundary_width)

    draw = ImageDraw.Draw(im)

    center = (size // 2, size // 2)
    if radius is None:
        radius = size // 2
    draw.circle(
        xy=center,
        radius=radius,
        fill=circle_color,
        outline=boundary_color,
        width=boundary_width,
    )

    dot_radius = 25
    if radius == 0:
        dot_radius =0
        pass
    draw.circle(center, dot_radius, fill=background_color)
    print("size is: ", size)
    print(center)
    print("radius is", radius)

    return im


if __name__ == "__main__":

    image = make_a_circle_in_square(
        size=1000,

        radius=99,
        boundary_color="green",
        circle_color=(255, 0, 0),
        boundary_width=10,
    )
    image.show()
