# Sample rainfall data
rainfall <- c(200, 220, 250, 300, 280, 260, 270)

# Create time series
ts_data <- ts(rainfall, start=c(2020,1), frequency=12)

# Plot
plot(ts_data, main="Rainfall Trend", col="blue")

# Fit ARIMA model
model <- arima(ts_data, order=c(1,1,1))

# Forecast
forecast <- predict(model, n.ahead=5)

print(forecast)