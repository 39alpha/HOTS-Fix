import netCDF4
import pandas as pd
import glob

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
    all_netcdf_files = glob.glob(path + "*.nc")
    first_df = get_dataframe_from_cdf(all_netcdf_files[0])
    for net_cdf_file in all_netcdf_files[1:]:
        this_df = get_dataframe_from_cdf(net_cdf_file)
        first_df = pd.concat([first_df, this_df], ignore_index=False)
    
    first_df.to_csv(path + "combined_data.csv")

if __name__ == "__main__":
    convert_all_cdf_to_csv("..\\data\\raw-hots\\")
