#Sample Dataset
df <- data.frame(
  Price = c(300, 400, 350, 500, 250),
  Area = c(1500, 2200, 1800, 2500, 1200),
  Bedrooms = c(3, 4, 3, 5, 2),
  Age = c(10, 5, 8, 2, 15)
)
# Fit the model and display summary
model <- lm(Price ~ Area + Bedrooms + Age, data = df)
summary(model)
# Predict price for (Area=2000, Bedrooms=3, Age=5)
new_data <- data.frame(Area = 2000, Bedrooms = 3, Age = 5)
prediction <- predict(model, new_data)
print(paste("Predicted Price:", prediction))
# Plot actual vs predicted values
plot(df$Price, predict(model), xlab="Actual", ylab="Predicted", main="Actual vs Predicted")
abline(0, 1, col="red")