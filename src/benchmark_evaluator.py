from benchmark_reader import TruthTable

class BenchmarkEvaluator:

    def evaluate(self, x, y, compressed=False, chunk_size = None):
        assert len(x) == len(y)

        if not compressed:
            return self.hamming_distance(x, y)
        else:
            return self.hamming_distance(x, y, compressed=compressed, chunk_size=chunk_size)

    def hamming_distance(self, x, y, compressed=False, chunk_size = None):
        dist = 0
        if compressed:
            for xi, yi in zip(x,y):
                cmp = ~(xi | yi)
                for i in range(chunk_size):
                   dist += (cmp >> 1) & 1
        else:
            for xi, yi in zip(x, y):
                if xi != yi:
                    dist += 1


