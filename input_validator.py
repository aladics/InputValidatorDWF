import click
import pandas as pd
import logging
import numpy as np

def check_nan(df : pd.DataFrame):
    nan_column_names = df.columns[df.isna().any()].to_list()
    logging.info(f"The following columns contain NaN values: {nan_column_names}")

def check_zero_std(df : pd.DataFrame):
    df = df.select_dtypes(include=np.number)
    zero_std_columns = df.columns[df.std() == 0].to_list()
    logging.info(f"The following columns have zero std: {zero_std_columns}")

def check_inf(df : pd.DataFrame):
    df = df.select_dtypes(include=np.number)
    inf_columns = df.columns[df.isin([np.inf, -np.inf]).any()].to_list()
    logging.info(f"The following columns contain -Inf or Inf values: {inf_columns}")



@click.command()
@click.argument("input", type=click.Path(exists=True, readable=True))
@click.option("--log", default="INFO", help="Logging level. Default: INFO")
def main(input, log):
    """Check the csv file INPUT if it has any major problems data wise, for example: NaN values, features with zero std etc."""
    
    log_level = getattr(logging, log.upper(), None)
    if not isinstance(log_level, int):
        raise ValueError('Invalid log level: %s' % log)
    logging.basicConfig(level=log_level, format='%(asctime)s:%(levelname)s:  %(message)s')
    
    df = pd.read_csv(input)
    check_nan(df)
    check_zero_std(df)

    check_inf(df)

if __name__ == "__main__":
    main()