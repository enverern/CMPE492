library(readxl)
library(ggparty)
library(openxlsx)

categoric_sku_based_data <- read_excel("categoric_sku_based_data.xlsx",
                                       col_types = c(
                                         "skip", "numeric", "numeric",
                                         "numeric", "numeric", "numeric",
                                         "numeric", "numeric", "numeric", "numeric",
                                         "numeric", "numeric", "numeric", "numeric", "numeric",
                                         "numeric", "numeric", "numeric", "numeric",
                                         "numeric", "numeric", "numeric"
                                       )
)

categoric_sku_based_data$direct_discount_percentage <- categoric_sku_based_data$scaled_direct_discount / categoric_sku_based_data$scaled_original_unit_price
#categoric_sku_based_data <- na.omit(categoric_sku_based_data)
# Calculate IQR
Q1 <- quantile(categoric_sku_based_data$total_quantity, 0.03, na.rm = TRUE)
Q3 <- quantile(categoric_sku_based_data$total_quantity, 0.998, na.rm = TRUE)
IQR <- Q3 - Q1

# Define bounds
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Filter outliers
categoric_sku_based_data <- categoric_sku_based_data[categoric_sku_based_data$total_quantity >= lower_bound & categoric_sku_based_data$total_quantity <= upper_bound, ]


write.xlsx(categoric_sku_based_data, "used_categorical_sku_based_data.xlsx")




total_quantity_tree <- lmtree(total_quantity ~ direct_discount_percentage |
    type + attribute1 + attribute2 + repeatable + first_order_month + user_level + plus + gender + age + marital_status + education + city_level + purchase_power + categoric_original_price,
    data = categoric_sku_based_data,weights = click_count, caseweights = TRUE)

#summary(total_quantity_tree)


p <- ggparty(total_quantity_tree,
             terminal_space = 0.5,
             add_vars = list(p.value = "$node$info$p.value")) +
  geom_edge() +
  geom_edge_label() +
  geom_node_splitvar() +
  geom_node_plot(gglist = list(geom_point(aes(x = direct_discount_percentage,
                                              y = total_quantity,
  ),
  alpha = 0.8),
  theme_bw (base_size = 10)),
  scales = "fixed",
  id = "terminal",
  shared_axis_labels = TRUE,
  shared_legend = TRUE,
  legend_separator = TRUE,
  predict = "direct_discount_percentage",
  predict_gpar = list(col = "blue",
                      size = 1.2)
  )

ggsave(file=paste0("/Users/envereren/Desktop/totaltree", 5,".png"), plot = p, width = 24, height = 20, units = "in", dpi = 300)

