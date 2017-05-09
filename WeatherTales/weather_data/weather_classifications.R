#
#
# WEATHER CLASSIFICATIONS
#
#

temp_bands <- seq(-5,25,5)
n_tbands <- length(temp_bands)
temp_band_names <- c(paste("<",temp_bands[1]),
                     paste(temp_bands[1:n_tbands-1]," to ",temp_bands[2:n_tbands]),
                     paste(">",temp_bands[n_tbands]))

wind_bands <- c(5,15)
n_wbands <- length(wind_bands)
wind_band_names <- c("calm","gusty","gales")

cloud_bands <- c(0.1,0.8)
n_cbands <- length(cloud_bands)
cloud_band_names <- c("clear","cloudy","overcast")

precip_bands <- c(0.5,4)
snow_bands <- c(0.5)
n_pbands <- length(precip_bands)
precip_band_names <- c("dry","light rain","heavy rain")
sleet_band_names  <- c("snow","sleet","heavy sleet")
all_precip_band_names <- c(precip_band_names,sleet_band_names)