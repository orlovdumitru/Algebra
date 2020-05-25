import math

class VectorCalculator:

    def __init__(self):
        pass


    def vector_add(self, v, w):
        '''Vector additions formula => V + W = [ V1 + W1, V2 + W2 + ... + Vn + Wn'''
        result = []
        for idx, v_item in v:
            result.append( float(v) + float(w[idx]) )
        return result


    def vector_sub(self, v, w):
        '''Vector additions formula => V + W = [ V1 + W1, V2 + W2 + ... + Vn + Wn'''
        result = []
        for idx, v_item in enumerate(v):
            result.append( float(v_item) - float(w[idx]) )
        return result


    def vector_scalar_mul(self, elem, v):
        '''Calculate scalar multiplication formula => m = 2(V) => 2*V1, 2*V2, ... V*n
            takes and element and list
            return a float nr
        '''
        return [float(elem) * float(e) for e in v]


    def vector_magnitude(self, v):
        '''Calculate magnitude formula => ||V|| = sqrt( (V1)**2 + (V2)**2 + ... + (Vn)**2 )'''
        nr = 0
        for item in v:
            nr += (float(item) ** 2)
        return math.sqrt(nr)


    def vector_normalization(self, v):
        ''' Calculate vector normalization fromula => (1/||v||) * v  
        takes a list
        return list []
        '''
        v_mag = self.vector_magnitude(v)
        result = []
        for item in v:
            result.append((1/v_mag) * float(item))
        return result


    def vector_inner_prod(self, v, w):
        '''Calculate vector innert product(dot product) formula => V * W = V1 * W1 + V2 * W2 + ... + Vn * Wn, return float number'''
        product = 0
        for idx, elem in enumerate(v):
            product += float(elem) * float(w[idx])
        return product


    def vector_angle(self, v, w, get_degree=False):
        ''' Get vector angle formula => θ = arccos( (V * W)/(||V|| * ||W||) ) '''
        inner_produs = self.vector_inner_prod(v, w)
        v_mag = self.vector_magnitude(v)
        w_mag = self.vector_magnitude(w)
        radians = math.acos(inner_produs / (v_mag * w_mag))
        degree = radians * (180.0 / math.pi)
        
        if get_degree:
            return degree
        else:
            return radians


    def check_equality(self, max_arr, min_arr):
        ''' Check for vector equality by deviding all by a number '''
        n = round(abs(float(max_arr[0])) / abs(float(min_arr[0])), 1)
        for i in range(len(max_arr)):
            if round(abs(float(max_arr[i])) / abs(float(min_arr[i])), 1) != n:
                return False
        return True


    def vector_is_orthogonal(self, v, w):
        ''' Check if a vecto is Orthogonal '''
        v_prod_w = self.vector_inner_prod(v, w)
        if abs(round(v_prod_w, 3)) == 0:
            return True
        
        if max([float(i) for i in v]) > max([float(i) for i in w]):
            if self.check_equality(v, w):
                return True
        else:
            if self.check_equality(w, v):
                return True
        return False


    def vector_is_paralel(self, v, w):
        '''Check if vectors are paralel'''
        if ((self.vector_magnitude(v)) ** 2) == 0:
            return True
        if ((self.vector_magnitude(w)) ** 2) == 0:
            return True
        for elem in v:
            if self.vector_scalar_mul(elem, w) == v:
                return True
        return False


    def projection(self, v, b):
        '''Projection b formula V = (v * Ub) * Ub
        takes in a vector and a b projection
        returns a vector '''
        b_norm = self.vector_normalization(b)
        v_prod_b = self.vector_inner_prod(v, b_norm)
        b_projection = self.vector_scalar_mul(v_prod_b, b_norm)
        return b_projection


    def orthogonal_vector(self, v, b):
        '''Get Orthogonal vector, V->1
        takes main vector, and parallel vector,
        returns orthogonal vector'''
        projection = self.projection(v, b)
        return self.vector_sub(v, projection)


    def find_vector_paral(self, v, b):
        '''find Vector from subtracting paralled v from paralel v
        takes vector v and b (v is projected on b)
        return vector''' 
        proj_b = self.projection(v, b)
        vect_proj = self.vector_sub(v, proj_b)
        return vect_proj


    def find_vector_ortog(self, v, b):
        '''find Vector from subtracting orthogonal v from orthogonal v
        takes vector v and b (v is projected on b)
        return vector''' 
        ortog_b = self.orthogonal_vector(v, b)
        vect_proj = self.vector_sub(v, ortog_b)
        return vect_proj


    def cross_product(self, v, w):
        result = {'x': 0, 'y': 0, 'z': 0}
        ref_arr = ['x', 'y', 'z', 'x', 'y']
        v.extend(v[:-1])
        w.extend(w[:-1])
        v = [float(i) for i in v]
        w = [float(i) for i in w]
        pp = 0
        pn = len(ref_arr) - 1
        while(pp < 3):
            result[ref_arr[pp]] += v[pp + 1] * w[pp + 2]
            result[ref_arr[pn]] -= v[pn - 1] * w[pn - 2]
            pp += 1
            pn -= 1
        return list(result.values())


    def parallelogram_area(self, v, w):
        '''calculates paralelogram area based on 2 vectors
        takes in 2 vectors
        return area of paralologram formula cross multiplication of 2 vectors result = sqrt(a1**2 + a2**2 + ... + an**2)
        '''
        cr_prod = self.cross_product(v, w)
        result = cr_prod[0] ** 2
        for i in range(1, len(cr_prod)):
            result += (cr_prod[i] ** 2)
        return math.sqrt(result)


    def triangle_area(self, v, w):
        main_area = self.parallelogram_area(v, w)
        return main_area / 2


if __name__ == '__main__':

    vec = VectorCalculator()

    v = input('Vector 1 separated by space: \n').split(' ')
    w = input('Vector 2 separated by space: \n').split(' ')

    # print('=> ', vec.vector_magnitude(v))
    # print('=> ', vec.vector_normalization(v))

    # print('=> ', vec.vector_inner_prod(v, w))
    # print('=> ', vec.vector_angle(v, w, True)) # True to get degree

    # print('Orthogonal => ', vec.vector_is_orthogonal(v, w))
    # print('Paralel => ', vec.vector_is_paralel(v, w))

    # print('=> ', vec.projection(v, w))
    # print('=> ', vec.orthogonal_vector(v, w))
    # print('=> ', vec.find_vector_paral(v, w))
    # print('=> ', vec.find_vector_ortog(v, w))

    # print('=> ', vec.cross_product(v, w))
    # print('=> ', vec.parallelogram_area(v, w))
    # print('=> ', vec.triangle_area(v, w))
