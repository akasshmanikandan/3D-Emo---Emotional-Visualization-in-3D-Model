#Install and load the necessary packages
install.packages("readxl")
library(readxl)

#Loading the Excel file 
data <- read_excel("C:\\Users\\Akassh Manikandan\\OneDrive\\Desktop\\Dissertation\\Data Analysis\\3d_EMO_User_Analysis.xlsx", sheet = "Cleaned Data")
accuracy <- read_excel("C:\\Users\\Akassh Manikandan\\OneDrive\\Desktop\\Dissertation\\Data Analysis\\3d_EMO_User_Analysis.xlsx", sheet = "Expanded Accuracy")

#View loaded data
View(data)
View(accuracy)

# Summary of user response dataset
summary(data)

# Bar plot of expanded accuracy
barplot(accuracy$`Expanded Accuracy (%)`,
        names.arg = accuracy$Emotion,
        col = "steelblue",
        main = "Expanded Accuracy per Emotion",
        ylab = "Accuracy (%)",
        las = 2)
install.packages("ggplot2")

library(ggplot2)

ggplot(accuracy, aes(x = Emotion, y = `Expanded Accuracy (%)`)) +
  geom_col(fill = "skyblue3") +
  theme_minimal() +
  labs(title = "Emotion Recognizability (Expanded Accuracy)",
       x = "Emotion",
       y = "Accuracy (%)") +
  coord_flip()

install.packages("tidyr")

library(readxl)
library(tidyr)
library(dplyr)

# Load the Excel sheet
data <- read_excel("C:\\Users\\Akassh Manikandan\\OneDrive\\Desktop\\Dissertation\\Data Analysis\\3d_EMO_User_Analysis.xlsx", sheet = "Cleaned Data")

# Define accepted answers
accepted_answers <- list(
  Q1 = c("smile", "happy"),
  Q2 = c("sad", "disappointed"),
  Q3 = c("fear", "shock"),
  Q4 = c("surprise", "amazed"),
  Q5 = c("disgust", "uncomfortable"),
  Q6 = c("angry", "rage"),
  Q7 = c("fake smile", "evil smile"),
  Q8 = c("sad", "tired"),
  Q9 = c("mesmerized", "amazed"),
  Q10 = c("annoyed", "tense")
)

#  Identify question columns by full text
response_cols <- grep("^Q[0-9]+: ", names(data), value = TRUE)

#  Create mapping: long column names -> Q1...Q10
short_names <- paste0("Q", 1:10)
names_map <- setNames(response_cols, short_names)

#  Rename columns for easier pivoting
names(data)[match(response_cols, names(data))] <- short_names

#  Pivot to long format and evaluate
long_data <- data %>%
  pivot_longer(cols = all_of(short_names), 
               names_to = "Question", 
               values_to = "Response") %>%
  mutate(Response = tolower(trimws(Response)),
         Emotion = case_when(
           Question == "Q1" ~ "Smile",
           Question == "Q2" ~ "Sad",
           Question == "Q3" ~ "Fear",
           Question == "Q4" ~ "Surprise",
           Question == "Q5" ~ "Disgust",
           Question == "Q6" ~ "Angry",
           Question == "Q7" ~ "Fake Smile",
           Question == "Q8" ~ "Melancholy",
           Question == "Q9" ~ "Mesmerized",
           Question == "Q10" ~ "Annoyed"
         )) %>%
  rowwise() %>%
  mutate(Correct = ifelse(Response %in% accepted_answers[[Question]], 1, 0)) %>%
  ungroup()

# Preview
head(long_data)

anova_result <- aov(Correct ~ Emotion, data = long_data)
summary(anova_result)
TukeyHSD(anova_result)

library(ggplot2)
ggplot(long_data, aes(x = Emotion, y = Correct)) +
  geom_boxplot(fill = "skyblue") +
  theme_minimal() +
  labs(title = "Variation of Emotion Recognizability",
       x = "Emotion", y = "Correct (0 or 1)") +
  coord_flip()

plot(TukeyHSD(anova_result))

# Run pairwise t-tests with Bonferroni correction
pairwise_t <- pairwise.t.test(long_data$Correct, long_data$Emotion, 
                              p.adjust.method = "bonferroni")

# View t-test results
print(pairwise_t)

install.packages("reshape2")
# Convert your t-test results to matrix
p_matrix <- as.matrix(pairwise_t$p.value)

# Convert to tidy long format
library(reshape2)
p_long <- melt(p_matrix, na.rm = TRUE)

# Plot heatmap of p-values
library(ggplot2)
ggplot(p_long, aes(Var1, Var2, fill = value)) +
  geom_tile(color = "white") +
  scale_fill_gradient(low = "red", high = "white", name = "p-value") +
  geom_text(aes(label = sprintf("%.3g", value)), color = "black", size = 3) +
  labs(title = "Pairwise t-test Significance (Bonferroni)", x = "Emotion 1", y = "Emotion 2") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

