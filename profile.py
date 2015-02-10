import os
import matplotlib.pyplot as plt

class Profile():
    ''' Manage Temperature-Salinity profiles '''

    depth = []    # container for depth values
    temp  = []    # container for temperature values
    sal   = []    # container for salinity values
    nPoints = 0   # number of points

    def __init__(self, fileName):
        ''' Load data from input file

        The data is read from a file with three columns:
        depth, temperature, salinity (separated by spaces)

        Parameters
        ----------
            fileName : str
                name of the input file

        Modifies
        --------
            self.depth - list, values of depth
            self.temp  - list, values of temperature
            self.sal   - list, values of salinity
            self.nPoints  int, number of points
        '''

        # check if file is there
        if not os.path.exists(fileName):
            raise IOError('file %s does not exist' % fileName)

        # read data from file and keep data in self
        with open(fileName) as f:
            # loop through all lines in the file
            for line in f:
                # split by spaces (single or multiple)
                # and unpack into several float values
                d,t,s = map(float, line.split())

                # map(func, iterable) is equal to:
                # func(iterable[0])
                # func(iterable[1])
                # func(iterable[2])
                # ...
                # items = line.split() #-> ['0', '31.1', '35.1']
                # d = float(items[0])
                # t = float(items[1])
                # s = float(items[2])

                # add depth, temperature, salinity data to self
                self.depth.append(d)
                self.temp.append(t)
                self.sal.append(s)

        self.nPoints = len(self.depth)

    def get_ts_at_level(self, level):
        ''' Get values of temperature and salinity from given layer'''

        return self.temp[level], self.sal[level]

    def get_ts_at_depth(self, depth):
        ''' Get values of temperature and salinity at given depth '''

        # check if depth exists
        if not depth in self.depth:
            raise LookupError('Depth %d does not exist!')

        # find level of the given depth
        level = self.depth.index(depth)

        return self.get_ts_at_level(level)

    def get_mixed_layer_depth(self, threshold=.1):
        ''' Estimate the depth of the mixed layer '''

        mld = None

        # loop through all values except last
        for i in range(self.nPoints - 1):
            # get temperature gradient
            gradient = ((self.temp[i]  - self.temp[i+1]) /
                        (self.depth[i] - self.depth[i+1]))

            # break loop when gradient above threshold
            if abs(gradient) > threshold:
                mld = self.depth[i]
                break

        # MLD not found with that threshold
        if mld is None:
            raise LookupError('MLD not found with threshold %f!' % threshold)

        return mld

    def plot_ts(self):
        ''' Make a plot '''
        plt.plot(self.temp, self.depth, 'o-')
        plt.gca().invert_yaxis()
        plt.xlabel('temperature')
        plt.ylabel('depth')
