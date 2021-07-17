# Assignment 10 - Sequence Types
 
## Notes:
- This assignment was refactored after referring to the code shared in Session 11.
- Appropriate docstrings have been added, test cases written for polygon sequence and tested using github actions.
- @property function was added after reading it up.
    Please refer to this [link](https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work-in-python) and [here](https://docs.python.org/3/howto/descriptor.html#properties) is the python documentation to understand the property function/decorator.
## Objective 1 [pts:400]:
### Create a Polygon Class:
1. where initializer takes in:
    1. number of edges/vertices
    2. circumradius
2. that can provide these properties:
    1. num of edges
    2. num of vertices
    3. interior angle
    4. edge length
    5. apothem
    6. area
    7. perimeter
3. that has these functionalities:
    1. a proper __repr__ function
    2. implements equality (==) based on # vertices and circumradius (__eq__)
    3. implements > based on number of vertices only (__gt__)

    ### Code is below and saved as module - polygon.py

    ``` python
    import math

    class Polygon:
        '''
        Polygon Class that represents a regular strictly convex polygon.
        Input - Takes n=number of edges/vertices and R=circumradius of the polygon
                (Circumradius = radius of the circle that inscribes the polygon)
        Output - Provides the following properties:
            count_edges
            count_vertices
            interior_angle
            side_length
            apothem
            area
            perimeter
        '''
        def __init__(self, n, R):
            if n < 3:
                raise ValueError('Polygon must have at least 3 vertices.')
            self._n = n
            self._R = R

        def __repr__(self):
            return f'Polygon(edges={self._n}, circumradius={self._R})'

        @property
        def count_vertices(self):
            return self._n

        @property
        def count_edges(self):
            return self._n

        @property
        def circumradius(self):
            return self._R

        @property
        def interior_angle(self):
            return (self._n - 2) * 180 / self._n

        @property
        def side_length(self):
            return 2 * self._R * math.sin(math.pi / self._n)

        @property
        def apothem(self):
            return self._R * math.cos(math.pi / self._n)

        @property
        def area(self):
            return self._n / 2 * self.side_length * self.apothem

        @property
        def perimeter(self):
            return self._n * self.side_length

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return (self.count_edges == other.count_edges 
                        and self.circumradius == other.circumradius)
            else:
                return NotImplemented

        def __gt__(self, other):
            if isinstance(other, self.__class__):
                return self.count_vertices > other.count_vertices
            else:
                return NotImplemented
    ```

    ### Following test cases were written and tested using github actions.

    Test Name           | Description
    ------------------- | ------------
    test_polygon_less_sides(): | Test error for polygon with sides less than 3
    test_polygon_repr(): | Test for a proper repr
    test_polygon_vertice_assignment(): | Test for proper assignment - vertices
    test_polygon_edges_assignment(): | Test for proper assignment - edges
    test_polygon_circumradius_assignment(): | Test for proper assignment - circumradius
    test_polygon_interior_angle_assignment(): | Test for proper assignment - circumradius
    test_polygon_all_properties_one(): | Manual Test to check if the output is proper and within tolerance limits
    test_polygon_all_properties_two(): | Manual Test to check if the output is proper and within tolerance limits
    test_polygon_all_properties_three(): | Manual Test to check if the output is proper and within tolerance limits
    test_polygon_logical_properties(): | Test for proper logical properties - eq, gt etc.




## Objective 2 [pts:600]:
### Implement a Custom Polygon sequence type:
1.	where initializer takes in:
    1. number of vertices for largest polygon in the sequence
    2. common circumradius for all polygons
2.	that can provide these properties:
    1. max efficiency polygon: returns the Polygon with the highest area:perimeter ratio
3.	that has these functionalities:
    1. functions as a sequence type (__getitem__)
    2. supports the len() function (__len__)
    3. has a proper representation (__repr__)

    ### Code is below and saved as module - polygon.py

    ``` python
    from polygon import Polygon

    class Polygon_Sequence:
        """
        Returns max efficiency polygon, Polygon with the highest area:perimeter ratio.
        Input - Largest Polygon Vertice Count, Common Circumradius
        Method - max_efficiency_polygon - Returns Max Efficiency Polygon of Class Polygon
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
            return f'Polygon_Sequence(Largest Polygon Vertice Count={self._m},
            Common Circumradius={self._R})'

        def __getitem__(self, s):
            return self._polygons[s]

        @property
        def max_efficiency_polygon(self):
            """
            Returns the max efficiency polygon, which is the polygon
            with the highest area to perimeter ratio in the Polygon_Sequence
            """
            sorted_polygons = sorted(self._polygons, 
                                     key=lambda p: p.area/p.perimeter,
                                    reverse=True)
            return sorted_polygons[0]

    ```
    ### Following test cases were written and tested using github actions.

    Test Name           | Description
    ------------------- | ------------
    test_polygon_sequence_less_sides(): | Test error for polygon sequence with sides less than 3
    test_polygon_sequence_repr(): | Test for proper repr - sequence
    test_polygon_sequence_getitem(): | Test for proper getitem - polygon sequence
    test_polygon_sequence_len(): | Test for proper len - polygon sequence
    test_polygon_sequence_mep(): | Test for proper mep - polygon sequence
