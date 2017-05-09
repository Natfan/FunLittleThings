# Extract data from a netcdf file

library(RNetCDF)

#----------------------------

GetPointDataNetCDF <- function(filename, vars) {

  data <- open.nc(filename,write=FALSE)
  x <- read.nc(data)
  
  if(var.inq.nc(ncfile = data,var=0)$name != "longitude") {
    stop("Longitude data not found :O")
  }
  if(var.inq.nc(ncfile = data,var=1)$name != "latitude") {
    stop("Latitude data not found :O")
  }
  if(var.inq.nc(ncfile = data,var=2)$name != "time") {
    stop("Time data not found :O")
  }
  
  #if(var.inq.nc(ncfile = data,var=5)$name != "t2m") {
  #  stop("2m temp not found :O")
  #}
  
  out <- list()

  # CODE GOES HERE FOR DATE SUBSETTING
  # Convert time coordinate from hours since 1900 to date
  # and filter
  
  # Loop through the gridded data layers
  for (i in 3:length(x)) {
    varname <- var.inq.nc(ncfile = data,variable=(i-1))$name

    # If this variable is in our list
    if (sum(vars %in% varname)>0) {
      
      # Find which variable we're looking at
      which_vars <- which(vars %in% varname)
      if(length(which_vars) > 1 ) { stop("ERROR!! Too many variable name matches") }
      var_now <- vars[which_vars][[1]]
      print(paste("Looking at ",varname,sep=""))
      
      # Subset the data at the location we care about
      var_data <- x[[i]]                       # nc data
      var_ts   <- var_data[ , , ,]   # subset by lon, lat, time
      
      # Store output
      out[[var_now]] <- var_ts
    }
  }
  
  if(length(out)==0) { print("WARNING - no data found") }

  close.nc(data)
  
  return(out)
}

input <- read.csv("temp_input.txt",header=FALSE,sep=" ")
source("set_up_weather_data_download.R") # Grabs input parameters
if(nchar(MONTH)<2) {  MONTH <- paste("0",MONTH,sep="") }
if(nchar(DAY)<2)   {  DAY <-   paste("0",DAY,sep="") }
file_input <- paste("./data/ERAInt_forecast_",YEAR,"-",MONTH,"-",DAY,".nc",sep="")

output <- GetPointDataNetCDF(file_input,LAT,LON,VARS)
print(output)