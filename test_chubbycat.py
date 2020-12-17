import pytest
import pygame
import ChubbyCatCollector
import math

pygame.init()


@pytest.fixture
def model():
    return ChubbyCatCollector.Model([600, 600])


two_points = [
    # Calculate the distance when all the coordinates are positive.
    ([[2, 3], [7, 15]], 13),
    # Calculate the distance when one or both of the coordinate is [0,0].
    ([[0, 0], [3, 0]], 3),
    ([[3, 0], [0, 0]], 3),
    ([[0, 0], [0, 0]], 0),
    # Calculate the distance of positive and negative coordinates.
    ([[-4, 0], [0, 3]], 5),
    ([[-3, 2], [5, -4]], 10),
    # Calculate when the distance is a float.
    ([[0, 5], [4, 0]], math.sqrt(41)),
]


@pytest.fixture(params=two_points)
def coord_points(request):
    return request.param


def test_distance(model, coord_points):
    """
    Test that the distance function correctly returns the
    distance betweeen two points.

    Args:
        model: The Model Class instance of the game.
        coord_points: A tuple where the first element is a list of
            coordinates of two points, and the second element is a number
            representing the distance between them.
    """
    points, result = coord_points
    assert model.distance(points[0], points[1]) == result


def test_icecream_list(model):
    """
    Test that the ice cream list is generated properly.

    Args:
        model: The Model Class instance of the game.
    """
    assert len(model.get_icecreamlist()) == model.icecream.icecream_num


def test_icecream_list_type(model):
    """
    Test the type of the ice cream list.

    Args:
        model: The Model Class instance of the game.
    """
    for coord in model.get_icecreamlist():
        assert type(coord) == list
