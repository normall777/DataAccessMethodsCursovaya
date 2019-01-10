my.f<-function(sqft_living, yr_built, grade,  waterfront, zipcode, lm.data.in, data.zipcode){
  data <- data.zipcode
  data$price <- lm.data.in$model$price
  avg <-mean(data[data$zipcode==zipcode,]$price)
  ret <- coef(lm.data.in)[1] + coef(lm.data.in)[2]*sqft_living +
    coef(lm.data.in)[3]*yr_built + coef(lm.data.in)[4]*grade  + 
    coef(lm.data.in)[5]*waterfront + coef(lm.data.in)[6]*avg;
  return (as.numeric(ret))
}