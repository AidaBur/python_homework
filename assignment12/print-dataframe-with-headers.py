import pandas as pd

class DFPlus(pd.DataFrame):

    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    def print_with_headers(self):
        num_rows = len(self)
        for i in range(0, num_rows, 10):
            print(self.columns.to_list())  
            print(super().iloc[i:i+10])
            print()
if __name__ == "__main__":
    dfp = DFPlus.from_csv("../csv/products.csv")
    dfp.print_with_headers()
