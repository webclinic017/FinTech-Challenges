# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains helper functions for loading and saving CSV files.

"""
import csv

def save_csv(data, csvpath):
    """Saves data to a csv file at path
    Args:
        csvpath (Path): Desired CSV File path
        data (List): List of desired data you wish to save to said file.
    Returns:
        None
    """
    with open(csvpath, "w") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter="\n")
        csvwriter.writerow(data)

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data
