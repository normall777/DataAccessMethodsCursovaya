fun.zip<-function()
{
  data <- read.csv("kc_house_data.csv", header=TRUE, sep=",");
  data <- data[,-c(1,2)];
  data <- data[data$sqft_living<13000,];
  data<- data[data$price<2*10^6,];
  data$avgZipCodePrice <- ave(data$price,data$zipcode);
  return (unique(data$zipcode));

}

fun.predict<-function(sqft_living, yr_built, grade,  waterfront, zipcode){
  data <- read.csv("kc_house_data.csv", header=TRUE, sep=",");
  data <- data[,-c(1,2)];
  data <- data[data$sqft_living<13000,];
  data<- data[data$price<2*10^6,];
  data$avgZipCodePrice <- ave(data$price,data$zipcode)
  avg <-mean(data[data$zipcode==zipcode,]$price)
  lm.data.in <- lm(price~sqft_living+yr_built+grade+waterfront+avgZipCodePrice, data = data)
  ret <- coef(lm.data.in)[1] + coef(lm.data.in)[2]*sqft_living +
    coef(lm.data.in)[3]*yr_built + coef(lm.data.in)[4]*grade  +
    coef(lm.data.in)[5]*waterfront + coef(lm.data.in)[6]*avg;
  return (as.numeric(ret))
}