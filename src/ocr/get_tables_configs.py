from typing import List
import cv2
class TableConfig():
    def __init__(self, n_rows: int, n_cols: int, rows_sizes: List[int], cols_sizes: List[int]):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.rows_sizes = rows_sizes
        self.cols_sizes = cols_sizes

def get_table_configs(img_filepath) -> List[TableConfig]:
    img = cv2.imread(img_filepath)

def main():
    pass

if __name__=='__main__':
    main()