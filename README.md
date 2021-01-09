# Bikeshare Project
### Date created
2021/01/07

### Description
This is a project that analyzes bikeshare data from 3 different cities; Washington DC, Chicago and New York City. It does so through an interactive use of the terminal.

### Files used
* chicago.csv
* new_york_city.csv
* washington.csv

These are all files given through the Udacity _Programming for Data Science with Python Nanodegree Program_. These files have been supplied after they have gone through data wrangling and cleaning of the original raw data and presented in a CSV format ready to use.

### Requirements
- Anaconda
- Python 3
- Numpy
- Pandas

To run this successfully you will need to have Anaconda or PIP installed on your terminal. I have used anaconda throughout this project and will show examples of code through the use of anaconda.

To install anaconda on Linux [click here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)
To install anaconda on MacOS [click here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)

If you already have anaconda installed run this code in your terminal to determine which version you are running:
`conda -V`

If the terminal responds with a version number you are good to go.
If you have the following error code `bash: conda: command not found` then use this [link](https://discuss.codecademy.com/t/setting-up-conda-in-git-bash/534473) to set up conda in your terminal:

Next you will need to create a virtual environment that runs python 3 and to install Numpy and Pandas. If you already have some environments created you can type this code to list the ones you have:
`conda info --envs`

To enter an environment you want type:
`conda activate <name-of your-environment>`

If you dont have a virtual environment this [documentation](https://docs.conda.io/projects/conda/en/4.6.1/user-guide/tasks/manage-environments.html) can help you set one up

Finally to install the packages enter the following:

`conda install numpy`

`conda install pandas`

### How to interact with the program
Once your terminal is set up and you have Python3, NumPy and Pandas installed you need to open a directory that has the 3 required data files (Chicago, Washington DC and New York City) and save the bikshare.py program in the same directory. now make sure in your terminal you are "cd" into this directory

To run the program enter the following in your terminal:
`python bikeshare.py`

The program prompts form you to enter the name of the city you would like to analyze. Select from Chicago, NYC or Washington DC. You may also enter short hand names for these cities such as DC, D.C NYC, New York etc. If you have any other common short hand names for these cities reach out and create a pull request to update the code! :wink:

Next it will ask you if you would like to filter the data by month and prompts you to enter yes or no.
If you select yes it will ask you which month you would like to filter by. Note that the data *only* contains data for 6 months, from January to June.

After you enter your desired month it will ask you if you would also like to filter the data by the day of week.
If you select yes it will ask you to enter the day of the week such as Saturday, Tuesday, Friday etc...

After you entered these inputs the terminal will show you the results, showing you a few statistics about the data and then it is followed by a set of raw data. The terminal prompts if you would like to see the next 5 data points, display the next 5 and will do so until you select no.

Finally it will ask you if you would like to restart the program. If you type _yes_ then it will restart and ask you which city you would like to analyze for such as in the beginning



### Credits
I followed this documentation on how to install [Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)

I followed this [page](https://discuss.codecademy.com/t/setting-up-conda-in-git-bash/534473) to set up conda in my terminal
