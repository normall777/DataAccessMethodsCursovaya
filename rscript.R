my.f<-function(sqft_living, view, yr_built, grade, lat){
  data <- read.csv("kc_house_data.csv", header=TRUE, sep=",")
  data <- data[,-c(1,2)]
  data <- data[data$sqft_living<13000,]
  data<- data[data$price<2*10^6,]
  lm.data.in <- lm(price~sqft_living+view+yr_built+grade+lat, data = data)
  #data.predict.out <- predict(lm.data.in, c(sqft_living, view, yr_built, grade, lat))
  ret <- coef(lm.data.in)[1] + coef(lm.data.in)[2]*sqft_living + coef(lm.data.in)[3]*view +coef(lm.data.in)[4]*yr_built + coef(lm.data.in)[5]*grade + coef(lm.data.in)[6]*lat
  return (as.numeric(ret))
}
my.f(2570, 0, 1951, 7, 47.721)

