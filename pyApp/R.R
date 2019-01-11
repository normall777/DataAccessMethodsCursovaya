# Функция получения списка потовых индексов
# Outputs: Возвращает уникальные номера почтовых индексов
# Для выполнения необходимо нахождение используемового набора данных в текущей директории 
fun.zip<-function()
{
  data <- read.csv("kc_house_data.csv", header=TRUE, sep=",");
  data <- data[,-c(1,2)];
  data <- data[data$sqft_living<13000,];
  data<- data[data$price<2*10^6,];
  data <- data[(data$grade<=12 & data$grade>3),]
  data$avgZipCodePrice <- ave(data$price,data$zipcode);
  return (unique(data$zipcode));

}

# Функция предсказания цены
# Inputs: sqft_living = площадь жилья
#         yr_built = год постройки здания
#         grade = оценка здания
#         waterfront = Наличие выхода к воде (0 - нет, 1 - да)
#         zipcode = почтовый индекс
# Outputs: Возвращает предсказанную цену
# Для выполнения необходимо нахождение набора данных в текущей директории
fun.predict<-function(sqft_living, yr_built, grade,  waterfront, zipcode){
  data <- read.csv("kc_house_data.csv", header=TRUE, sep=",");
  data <- data[,-c(1,2)];
  data <- data[data$sqft_living<13000,];
  data<- data[data$price<2*10^6,];
  data <- data[(data$grade<=12 & data$grade>3),]
  data$avgZipCodePrice <- ave(data$price,data$zipcode)
  avg <-mean(data[data$zipcode==zipcode,]$price)
  lm.data.in <- lm(price~sqft_living+yr_built+grade+waterfront+avgZipCodePrice, data = data)
  ret <- coef(lm.data.in)[1] + coef(lm.data.in)[2]*sqft_living +
    coef(lm.data.in)[3]*yr_built + coef(lm.data.in)[4]*grade  +
    coef(lm.data.in)[5]*waterfront + coef(lm.data.in)[6]*avg;
  return (as.integer(ret))
}
