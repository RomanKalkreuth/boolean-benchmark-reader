"""
Provides an evaluator that can be used for the evalution of the benchmarks of the
General Boolean Function Benchmark Suite (GBFS):
https://dl.acm.org/doi/abs/10.1145/3594805.3607131
"""

__author__ = "Roman Kalkreuth"

class BenchmarkEvaluator:
    """ Evaluator class that evaluates compressed and uncompressed output pairs
    by calculating the the hamming distance. """

    def evaluate(self, x, y, compressed=False, chunk_size = None):
        """
        Triggers the evaluation with the Hamming distance. DIstiguishes between compressed and uncompressed
        output pairs that are passed to the function.
        """
        if len(x) != len(y):
            raise ValueError("Dimensions do not match.")

        if not compressed:
            return self.hamming_distance(x, y)
        else:
            return self.hamming_distance(x, y, compressed=compressed, chunk_size=chunk_size)

    def hamming_distance(self, x, y, compressed=False, chunk_size = None):
        """
        Calculates the hamming distance which is defined as
        the number of different bits between x and y.

        :param x:
        :param y:
        :compressed:
        :chunk_size:
        """
        dist = 0
        if compressed:
            for xi, yi in zip(x,y):
                # Bitwise XOR the chunks to identify dissimilar bits
                cmp = xi ^ yi
                for i in range(chunk_size):
                    # Sum up the number of 1s then
                    dist += cmp & 1
                    cmp = cmp >> 1
        else:
            for xi, yi in zip(x, y):
                if xi != yi:
                    dist += 1
        return dist