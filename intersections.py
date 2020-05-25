
import re
import math

class Intersections(object):

    def __init__(self):
        pass


    def line_picker(self, line1, line2):
        '''get list 1 and list 2 from equation
        split by + and = use | => or, \ to escape + and = escape 
        remove x and y
        input format: 4.046x + 2.836y = 1.21
        return [x, y]
        '''
        a = [float(i) for i in (re.split('\+|\=|x|y', re.sub('x|y','',line1)))]
        b = [float(i) for i in (re.split('\+|\=|x|y', re.sub('x|y', '',line2)))]
        return a, b

    def line_intersect(self, line1, line2):
        '''return intersection of line1 and line2 
        return 'No intersection' if devider is 0 (zero)
        return [0.0, 0.0] if is the same line'''
        l1, l2 = self.line_picker(line1, line2)
        devide_by = (l1[0] * l2[1] - l1[1] * l2[0])
        if devide_by == 0:
            return 'No intersection'
        x = (l2[1] * l1[2] - l1[1] * l2[2]) / devide_by
        y = (-(l2[0]) * l1[2] + l1[0] * l2[2]) / devide_by
        return [x, y]


if __name__ == '__main__':

    inters = Intersections()

    line1 = input('Enter equation: \n')
    line2 = input('Enter equation: \n')

    print(inters.line_intersect(line1, line2))