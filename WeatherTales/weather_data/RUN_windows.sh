#!/bin/bash

RSCRIPT="~/../../Program Files/R/R-3.3.2/bin/Rscript.exe"
# RSCRIPT="./Rscript.exe"

if [ -f "temp_input.txt" ]
then 
	rm "temp_input.txt"
fi

echo "=================================="
echo "  Setting up download parameters  "
echo "=================================="
~/../../Program\ Files/R/R-3.3.2/bin/Rscript.exe set_up_weather_data_download.R


echo "=================================="
echo "         Downloading data         "
echo "=================================="
python get_weather_data.py

echo "=================================="
echo "     Extracting location data"
echo "=================================="
~/../../Program\ Files/R/R-3.3.2/bin/Rscript.exe extract_data.R

echo "=================================="
echo "   Converting to human forecast"
echo "=================================="
~/../../Program\ Files/R/R-3.3.2/bin/Rscript.exe create_human_forecast.R
