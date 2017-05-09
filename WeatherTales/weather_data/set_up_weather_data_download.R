
#
# GET AND PROCESS WEATHER DATA
# 

YEAR  = 2016
MONTH = 10
DAY   = 3

LAT = 18.5
LON = -74.3

VARS = c("t2m","u10","v10","tcc","tp","sf")

#---------------------------------------------------

conversions = list(
  t2m = "167.128",  # 2m temp
  u10 = "165.128",  # u 10m
  v10 = "166.128",  # v 10m
  tcc = "164.128",  # total cloud cover
  tp = "228.128",   # total precip
  sf = "144.128"    # snowfall
)

vars_in <- as.character(conversions[VARS])
if(sum(is.na(vars_in))>0) { print("Error: some variables not recognised") }

write.csv(paste(c(YEAR,MONTH,DAY,vars_in),collapse=" "),
          "temp_input.txt",
          row.names=FALSE, quote=FALSE)

#GetWeatherLocationData <- function(year,month,day,lat,lon) {
#
#  # Download the data
#  setwd("~")
#  print(paste("python ~/Documents/WeatherTales/weather_data/get_weather_data.py"))
#  print(paste("python ~/Documents/WeatherTales/weather_data/get_weather_data.py"))
#  system(paste("python get_weather_data.py"))
#
#}


#GetWeatherLocationData(YEAR,MONTH,DAY,LAT,LON)

#GetWeatherMapData

