# split the raw data 
# save it in data/processed folder
#import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params

def split_and_save_data(config_path):
    config = read_params(config_path)
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]
    target_col = config["base"]["target_col"]
    predictors_path = config["split_data"]["predictors_path"]
    taget_path = config["split_data"]["taget_path"]
    train_x_path = config["split_data"]["train_x_path"]
    train_y_path = config["split_data"]["train_y_path"]
    test_x_path = config["split_data"]["test_x_path"]
    test_y_path = config["split_data"]["test_y_path"]

    df = pd.read_csv(raw_data_path, sep=",")
    train, test =train_test_split(
        df,
        test_size=split_ratio,
        random_state=random_state
    )
    train.to_csv(train_data_path, index=False, encoding= "utf-8", sep= ",")
    test.to_csv(test_data_path, index=False, encoding= "utf-8", sep= ",")

    predictors = df.drop(target_col, axis=1)
    target = df[target_col]

    train_predictors = train.drop(target_col, axis=1)
    train_target = train[target_col]

    test_predictors = test.drop(target_col, axis=1)
    test_target = test[target_col]


    predictors.to_csv(predictors_path,index=False, encoding= "utf-8", sep=",")
    target.to_csv(taget_path,index=False, encoding= "utf-8", sep=",")

    train_predictors.to_csv(train_x_path,index=False, encoding= "utf-8", sep=",")
    train_target.to_csv(train_y_path,index=False, encoding= "utf-8", sep=",")

    test_predictors.to_csv(test_x_path,index=False, encoding= "utf-8", sep=",")
    test_target.to_csv(test_y_path,index=False, encoding= "utf-8", sep=",")


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    split_and_save_data(config_path=parsed_args.config)
