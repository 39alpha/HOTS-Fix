import netCDF4
import pandas as pd
import glob
import os

def get_dataframe_from_cdf(cdf_file):
    """ Convert the data from a netCDF file to a DataFrame.
        Ignore variables called ["dataDesc, "ros", "mtime"]
        
        Args: cdf_file - path to netcdf file
        Returns: this_df - DataFrame containing the data from the netcdf as columns
    """
    # Read the data
    data = netCDF4.Dataset(cdf_file)
    # Initialize the dataframe
    this_df = pd.DataFrame()
    # Iterate over variables
    for var in data.dimensions:
        # If they're not in the exclude list
        if var not in ["dataDesc", "ros", "mtime"]:
            this_df[var] = data[var][:]
    return this_df

def convert_all_cdf_to_csv(path):
    """ Convert all the .netCDF files in the path to a DataFrame.
    """
    # Find all the netcdf files in the path
    all_netcdf_files = glob.glob(path + "*.nc")
    # Get the first example
    first_df = get_dataframe_from_cdf(all_netcdf_files[0])
    # Concatenate the remaining data
    for net_cdf_file in all_netcdf_files[1:]:
        this_df = get_dataframe_from_cdf(net_cdf_file)
        first_df = pd.concat([first_df, this_df], ignore_index=False)
    # Write to file
    first_df.to_csv(path + "combined_data.csv")


def clean_hots(path):
    """Clean the raw data from HOTS to make sure it's suitable for training the prediction method.
    """
    # Read the combined data
    combined_data = pd.read_csv(os.path.join(path, "combined_data.csv"), index_col = 0)
    # we need these variables to exist
    minimum_data = combined_data.query("press > 0 & temp > 0 & dic > 0 & ph > 0")
    # We only ned to keep these variables (this is based on 39 Alpha needs)
    keeper_cols = ['crn','stn','cast','press',
                   'theta','sigma','temp',
                   'csal','coxy','dic','ph',
                   'alk','phos','nit','sil',
                   'doc']
    # Select the data columns
    keep_min_data = minimum_data[keeper_cols]
    # We need rows that all have data
    keep_min_data = keep_min_data[(keep_min_data > 0).all(1)]
    # Write these to file
    keep_min_data.to_csv("..\\data\parsed\\ideal-variables-2022.csv")

if __name__ == "__main__":
    convert_all_cdf_to_csv("..\\data\\raw-hots\\")
    clean_hots("..\\data\\raw-hots\\")