import pickle
import os
import shutil


def spilt(path, files_path, spilt_path, Kfold=10):
    """
    Split a labeled trajectory dataset into K folds of train/val/test
    subsets, using a pre-computed division stored in a .pkl file.

    Parameters
    ----------
    path : str
        Path to the pre-trained division model (.pkl file), e.g.
        'paddy_data_split.pkl' or 'wheat_1_data_split.pkl'.
    files_path : str
        Path to the directory containing the raw trajectory files
        to be split.
    spilt_path : str
        Output directory where the K-fold train/val/test subfolders
        will be created.
    Kfold : int, optional
        Number of folds to create (default: 10).
    """
    with open(path, 'rb') as file:
        data = pickle.load(file, encoding='latin1')
        train = data['train']
        valid = data['valid']
        test = data['test']

        # Overview of the full split
        print('train:', len(train))
        print('valid:', len(valid))
        print('test:', len(test))

        for i in range(Kfold):
            fold_path = spilt_path + "/" + str(i)
            if not os.path.exists(fold_path):
                os.mkdir(fold_path)
            if not os.path.exists(fold_path + "/train"):
                os.mkdir(fold_path + "/train")
            if not os.path.exists(fold_path + "/val"):
                os.mkdir(fold_path + "/val")
            if not os.path.exists(fold_path + "/test"):
                os.mkdir(fold_path + "/test")

            for j in train[i]:
                shutil.copyfile(files_path + "/" + j, fold_path + "/train/" + j)
            for j in valid[i]:
                shutil.copyfile(files_path + "/" + j, fold_path + "/val/" + j)
            for j in test[i]:
                shutil.copyfile(files_path + "/" + j, fold_path + "/test/" + j)

            print('len train:', len(train[i]))
            print('train:', train[i])
            print('len valid:', len(valid[i]))
            print('valid:', valid[i])
            print('len test:', len(test[i]))
            print('test:', test[i])
            print('+++++++++++++++++++++++++++++++++++++++++++++++')


if __name__ == "__main__":
    # Path to the pre-trained division model for the dataset you want to split.
    # Choose one of the following:
    path = 'wheat_1_data_split.pkl'
    # path = 'paddy_data_split.pkl'

    # Path to the directory containing the raw trajectory files to be split.
    # Replace this with the actual local path to your dataset.
    files_path = "/path/to/your/raw_trajectory_files"  # TODO: set this path
    spilt_path = files_path + "_10fold"

    if not os.path.exists(spilt_path):
        os.mkdir(spilt_path)

    spilt(path, files_path, spilt_path, Kfold=10)
