

class Ship(object):
    """ This is the rudimentary ship object. Extend as required for application.

    You may thing of the ship as a coordinate plane, with the amidships as the y-axis,
    midships as the x-axis and the main deck as the z-axis.
    """

    units = 'meters'

    def __init__(self, sails: list=[], masts: list=[]):
        self.sails = sails


    class Mast(object):
        """ A mast object to pass to a sail

        Your implementation must provide:
         - a getter method that reads the geometry of the mast. It must return an equation that
            can be used to compute the geometry of a sail's attachment points in 3d space.
         - a setter method that updates the geometry of the mast.
        """

        _geometry = [
            (0, 0, 0),
            (0, -.5, .5),
            (0, .5, .5),
            (0, 0, 1),
        ]

        def get_base_coordinates(self):
            return


    class Sail(object):
        """ A sail object to pass to a ship

        Give it three mixins:
         - a mast that it's attached to
         - a polygon getter to use (must provide a `read` method)
         - a polygon setter to use (must provide a `set` method)
        """

        id = None
        angle = None

        _geometry = [
            (0, 0, 0),
            (0, -.5, .5),
            (0, .5, .5),
            (0, 0, 1),
        ]
        _sail_geometry = None
        _mast_geometry = None

        def __init__(self, sail_geometry):
            self._sail_geometry = sail_geometry

        def get_geometry(self):
            return self._sail_geometry

        def set_geometry(self, geometry):
            self._sail_geometry = geometry
