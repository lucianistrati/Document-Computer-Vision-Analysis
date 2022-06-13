from sklearn.cluster import KMeans
from tqdm import tqdm
from matplotlib import pyplot as plt
import numpy as np
import cv2
import os

def main():
    images_folder = "data/azure_data_for_ocr/DA_SILOZ_images"
    all_images = []
    for i, file in enumerate(os.listdir(images_folder)):
        if i == 1000:
            break
        if i % 100 == 0:
            print(i)
        if file.endswith("_0.jpeg"):
            img = cv2.imread(os.path.join(images_folder, file))
            # print(img.shape)
            img = img[:img.shape[0] // 4, :, :]
            img = cv2.resize(img, dsize=(75, 200))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            all_images.append(img)
            # cv2.imshow("first page", img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

    all_images = np.array(all_images)
    np.save(file="data/azure_data_for_ocr/DA_SILOZ_images_numpy_arrays/half_of_first_image.npy", arr=all_images, allow_pickle=True)
    X = np.reshape(all_images, newshape=(all_images.shape[0], all_images.shape[1] * all_images.shape[2]))
    clusterizer = KMeans(n_clusters=4)
    clusterizer.fit(X)
    labels = clusterizer.labels_
    possible_labels = list(range(min(labels), max(labels) + 1))
    n_row = 3
    n_col = 3

    for label in possible_labels:
        cur_images = []

        for i, img in enumerate(all_images):
            if labels[i] == label:
                cur_images.append(img)
            if len(cur_images) == 9:
                break

        _, axs = plt.subplots(n_row, n_col, figsize=(7, 20))
        axs = axs.flatten()
        for img, ax in zip(cur_images, axs):
            ax.imshow(img)
        plt.show()


if __name__ == "__main__":
    main()
