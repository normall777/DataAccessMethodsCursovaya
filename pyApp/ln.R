fun.ln<-function()
{
  data <- read.csv("kc_house_data.csv", header=TRUE, sep=",");
  data <- data[,-c(1,2)];
  data <- data[data$sqft_living<13000,];
  data<- data[data$price<2*10^6,];
  data$avgZipCodePrice <- ave(data$price,data$zipcode);
  lm.data.in <- lm(price~sqft_living+yr_built+grade+waterfront+avgZipCodePrice, data = data);
  return (unique(data$zipcode));
  #return (c(lm.data.in, data$zipcode));

}

