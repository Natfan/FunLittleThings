
#

x1 <- read.csv("frank.txt", sep="\n")
#x2 <- paste(paste(x1[[1]], sep=" "),collapse=" ")
x2 <- paste(x1[[1]], collapse=" ")
splitstrings <- c("\\.","!","?",":",";")
splitstrings <- c(splitstrings, paste(splitstrings," ",sep=""))
x3 <- strsplit(as.character(x2[[1]]), splitstrings)
x3 <- gsub("\\n"," ",x3[[1]])
x3 <- gsub('"',"", x3)

trim.leading <- function (x)  { return(sub("^\\s+", "", x)) }
x4 <- trim.leading(x3)

write.csv(x4,"frank.csv",quote=FALSE,row.names=FALSE)