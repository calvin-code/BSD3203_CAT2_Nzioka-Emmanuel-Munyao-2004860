# BSD 3203 CAT 2 FOR 20/04860 NZIOKA EMMANUEL MUNYAO(R)
# The code of this CAT, below, was written and edited on Notepad++ v8.7.8 64 bit and tested and run on R 4.4.2 GUI 64 bit.
# All the steps are highlighted and labelled correctly
# The machine used for this CAT  supports displaying date and time in the long format however, 
#  R code was used to display the current date and time for every question heading. The Machine name is Emmanuel-Rogger(Emmanuel Nzioka).
# In case of any problems, the author of this script can be reached through +254791971305 or 2004860@students.ac.ke
										# Section A: R Programming (20 Marks)
										# Question 1: Data Manipulation with dplyr (6 Marks)
# Get current date and time
current_datetime <- Sys.time()
# Get machine name
machine_name <- Sys.info()["nodename"]
# Print the results
print(paste("Current Date and Time:", current_datetime))
print(paste("Machine Name:", machine_name))
# Load necessary libraries
library(dplyr)
# Create sales_data dataframe
sales_data <- data.frame(
  Product = c("Laptop", "Phone", "Tablet", "Laptop", "Phone"),
  Region = c("Region A", "Region B", "Region A", "Region B", "Region A"),
  Sales = c(7000, 4500, 8000, 3000, 6500),
  Date = as.Date(c("2024-01-10", "2024-01-12", "2024-01-15", "2024-01-18", "2024-01-20"))
)
# Save dataset to CSV
write.csv(sales_data, "sales_data.csv", row.names = FALSE)
# Load dataset from CSV
sales_data <- read.csv("sales_data.csv")
# Display only Product and Sales columns
sales_data %>% select(Product, Sales)
# Filter rows where Sales is greater than 5000
sales_data %>% filter(Sales > 5000)
# Group data by Region and calculate total sales per region
region_sales <- sales_data %>%
  group_by(Region) %>%
  summarise(Total_Sales = sum(Sales))
head(region_sales)
# Save to CSV
write.csv(region_sales, "region_sales.csv", row.names = FALSE)
										# Question 2: Data Visualization with ggplot2 (6 Marks)
# Get current date and time
current_datetime <- Sys.time()
# Get machine name
machine_name <- Sys.info()["nodename"]
# Print the results
print(paste("Current Date and Time:", current_datetime))
print(paste("Machine Name:", machine_name))
# Load necessary library
library(ggplot2)
# Create a bar chart showing total sales for each Product
ggplot(sales_data, aes(x = Product, y = Sales, fill = Product)) +
  geom_bar(stat = "identity") +
  ggtitle("Total Sales per Product") +
  theme_minimal()
# Create a line plot showing sales trends over time for Region A
sales_data$Date <- as.Date(sales_data$Date)  # Convert Date column to Date format
region_a_sales <- filter(sales_data, Region == "Region A")
ggplot(region_a_sales, aes(x = Date, y = Sales, group = 1)) +
  geom_line(color = "blue") +
  geom_point() +
  ggtitle("Sales Trend Over Time for Region A") +
  theme_minimal()
											# Question 3: Statistical Analysis (8 Marks)
# Get current date and time
current_datetime <- Sys.time()
# Get machine name
machine_name <- Sys.info()["nodename"]
# Print the results
print(paste("Current Date and Time:", current_datetime))
print(paste("Machine Name:", machine_name))
# Summary statistics for Sales column
summary(sales_data$Sales)
# Perform t-test comparing mean Sales between Region A and Region B
sales_region_a <- filter(sales_data, Region == "Region A")$Sales
sales_region_b <- filter(sales_data, Region == "Region B")$Sales
t_test_result <- t.test(sales_region_a, sales_region_b, var.equal = TRUE)
t_test_result
# Interpretation of p-value
if (t_test_result$p.value < 0.05) {
  print("The difference in mean sales between Region A and Region B is statistically significant.")
} else {
  print("The difference in mean sales between Region A and Region B is not statistically significant.")
}
