# Load built-in dataset
data("AirPassengers")

# Convert to time series (already a ts object, but safe to show)
ts_data <- AirPassengers

# Plot the data
plot(ts_data, main="Air Passengers Data", col="blue")

# Fit ARIMA model
model <- arima(ts_data, order = c(1,1,1))

# Display model
model

# Forecast next 12 months
forecast <- predict(model, n.ahead = 12)

# Print forecast values
forecast$pred