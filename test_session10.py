import pytest
import math
from polygon import Polygon
from polygon_sequence import Polygon_Sequence
abs_tol = 0.001
rel_tol = 0.001

def test_polygon_less_sides():
    with pytest.raises(ValueError):
        p = Polygon(2, 10)

def test_polygon_repr():
    n = 3
    R = 1
    p = Polygon(n, R)
    assert str(p) == 'Polygon(edges=3, circumradius=1)', f'actual: {str(p)}'


def test_polygon_vertice_assignment():
    n = 3
    R = 1
    p = Polygon(n, R)
    assert p.count_vertices == n, (f'actual: {p.count_vertices},'f' expected: {n}')

def test_polygon_edges_assignment():
    n = 3
    R = 1
    p = Polygon(n, R)
    assert p.count_edges == n, f'actual: {p.count_edges}, expected: {n}'

def test_polygon_circumradius_assignment():
    n = 3
    R = 1
    p = Polygon(n, R)
    assert p.circumradius == R, f'actual: {p.circumradius}, expected: {n}'

def test_polygon_interior_angle_assignment():
    n = 3
    R = 1
    p = Polygon(n, R)
    assert p.interior_angle == 60, (f'actual: {p.interior_angle},''expected: 60')


def test_polygon_all_properties_one():
    n = 4
    R = 1
    p = Polygon(n, R)
    assert p.interior_angle == 90, (f'actual: {p.interior_angle}, '
                                    ' expected: 90')
    assert math.isclose(p.area, 2, 
                        rel_tol=abs_tol, 
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                            ' expected: 2.0')

    assert math.isclose(p.side_length, math.sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.side_length},'
                                            f' expected: {math.sqrt(2)}')

    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                            f' expected: {4 * math.sqrt(2)}')

    assert math.isclose(p.apothem, 0.707,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                            ' expected: 0.707')

def test_polygon_all_properties_two():
    p = Polygon(6, 2)
    assert math.isclose(p.side_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)


def test_polygon_all_properties_three():
    p = Polygon(12, 3)
    assert math.isclose(p.side_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 150,
                        rel_tol=rel_tol, abs_tol=abs_tol)


def test_polygon_logical_properties():
    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)

    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5


def test_polygon_sequence_less_sides():
    with pytest.raises(ValueError):
        ps = Polygon_Sequence(2, 10)

def test_polygon_sequence_repr():
    ps = Polygon_Sequence(25,10)
    assert str(ps) == 'Polygon_Sequence(Largest Polygon Vertice Count=25, Common Circumradius=10)', f'actual: {str(ps)}'

def test_polygon_sequence_getitem():
    assert str(Polygon_Sequence(25,10).__getitem__(4))== 'Polygon(edges=7, circumradius=10)', f'getitem not working'

def test_polygon_sequence_len():
    assert Polygon_Sequence(25,10).__len__()==23, f'len not working'

def test_polygon_sequence_mep():
    assert str(Polygon_Sequence(25,10).max_efficiency_polygon)=='Polygon(edges=25, circumradius=10)', f'max_efficiency_polygon not working'