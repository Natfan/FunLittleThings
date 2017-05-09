#
#
# Generate weather forecast icons
#
#

source("weather_classifications.R")

#-----------------------------------------

x <- read.csv("./data/FC_latest.csv")
x$ws <- sqrt(x$u10^2 + x$v10^2)
x$t2m <- x$t2m - 273.15
x$tp <- x$tp * 1000 # (convert to mm)
x$sf <- x$sf * 1000 # (convert to mm)

classify_one <- function(value, x_bands) {
  if(all((x_bands-value) < 0)) { return(length(x_bands)+1) }
  else { return( min(which((x_bands-value) > 0)) ) }
}

classify <- function(input_data,bands,band_names) {
  out <- sapply(input_data, classify_one, x_bands=bands)
  out_band_name <- band_names[out]
}

classify_precip <- function(precip, snow,
                            precip_bands, snow_bands,
                            precip_band_names, sleet_band_names) {
  out <- sapply(precip, classify_one, x_bands=precip_bands)
  out_band_name <- rep(" ",length(out))
  snow_frames <- which(snow >= snow_bands[1])
  if(length(snow_frames) == 0) {
    out_band_name <- precip_band_names[out]
  } else {
    out_band_name[which(snow < snow_bands[1])] <- precip_band_names[out]
    out_band_name[which(snow >= snow_bands[1])] <- sleet_band_names[out]
  }
}

x$temperature <- classify(x$t2m,temp_bands,temp_band_names)
x$windspeed <-   classify(x$ws, wind_bands,wind_band_names)
x$cloudcover <-  classify(x$tcc,cloud_bands,cloud_band_names)
x$precip     <-  classify_precip(x$tp,x$sf,precip_bands,snow_bands,precip_band_names,sleet_band_names)

write.csv(x,"./data/FC_human.csv",row.names=FALSE)