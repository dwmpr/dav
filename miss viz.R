library(ggplot2)
library(reshape2)

# Sample dataset
data <- data.frame(
  A = c(1, 2, NA, 4, 100),
  B = c(5, NA, 7, 8, 200)
)

# Heatmap for missing values
missing <- is.na(data)
melted <- melt(missing)

ggplot(melted, aes(x=Var2, y=Var1, fill=value)) +
  geom_tile() +
  scale_fill_manual(values=c("white","red")) +
  ggtitle("Missing Values Heatmap")

# Boxplot for outliers
boxplot(data, main="Outlier Detection")