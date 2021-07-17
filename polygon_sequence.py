from polygon import Polygon

class Polygon_Sequence:
    """
    Returns the max efficiency polygon:which is the Polygon with the highest area:perimeter ratio.
    Input - Largest Polygon Vertice Count, Common Circumradius
    Method max_efficiency_polygon - Returns Max Efficiency Polygon of Class Polygon
    """
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._polygons = [Polygon(i, R) for i in range(3, m+1)]

    def __len__(self):
        return self._m - 2

    def __repr__(self):
        return f'Polygon_Sequence(Largest Polygon Vertice Count={self._m}, Common Circumradius={self._R})'
    
    def __getitem__(self, s):
        return self._polygons[s]

    @property
    def max_efficiency_polygon(self):
        """
        Returns the max efficiency polygon, which is the polygon with the highest area to perimeter ratio in the Polygon_Sequence
        """
        sorted_polygons = sorted(self._polygons, 
                                 key=lambda p: p.area/p.perimeter,
                                reverse=True)
        return sorted_polygons[0]