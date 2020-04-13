#required package
install.packages("openxlsx")
library(openxlsx)

#set wd
setwd("C:/Users/Haghish/Dropbox/Chase")

#name of the file
file = "./trials.xlsx"

#name of the text file
vectors = "VECTORS.txt"

#remove previous file
unlink(vectors)

#read the file
trials = read.xlsx(file, sheet=1, startRow = 3, colNames = T)
trials = trials[, 3:6] #drop the descriptions

#save the data frame to a file
a = paste(as.character(trials[,1]), collapse=",")
a = paste("trialType=", a, sep = "")
b = paste(as.character(trials[,2]), collapse=",")
b = paste("duration=", b, sep = "")
c = paste(as.character(trials[,3]), collapse=",")
c = paste("chaseAngle=", c, sep = "")
d = paste(as.character(trials[,4]), collapse=",")
d = paste("chaseRate=", d, sep = "")

write(a, file=vectors, append = TRUE)
write(b, file=vectors, append = TRUE)
write(c, file=vectors, append = TRUE)
write(d, file=vectors, append = TRUE)