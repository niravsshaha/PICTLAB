#Reading the dataset
dataset=read.csv('wine.data',sep=",",header=FALSE)

#changing order of columns
dataset=dataset[c(2:14,1)]
#scaling the dataset
dataset[,-14]=scale(dataset[,-14])

#giving names to columns
names(dataset)=c("Alcohol","Malic_acid","Ash","Alcalinity","Magnesium","Total_phenols",
                 "Flavanoids","Nonflavanoids","Proanthocyanins","Color_intensity",
                 "Hue","Od","Proline","Customer_segment")

#converting last column to factors
dataset$Customer_segment=factor(dataset$Customer_segment,levels = c('1','2','3'))

#creating principal comonents
pca_data=princomp(dataset[,-14])

#plotting principal components
biplot(pca_data)
plot(pca_data)

#summary of pca_data to find out principal components which are contributing the most
summary(pca_data)
screeplot(pca_data,type="line")

#libraries required for naive bayes and confusion matrix
library(caret)
library(e1071)

#naive bayes on normal dataset (Accuracy is 98.8%)
model1=naiveBayes(dataset[,1:13],dataset[,14])
predicted_values_normal=predict(model1,dataset[,1:13])
confusionMatrix(factor(dataset[,14]),factor(predicted_values_normal))


#naive bayes after performing PCA(Accuracy after considering 2 components is 97.19%)
model2=naiveBayes(pca_data$scores[,1:2],dataset[,14])
predicted_values_pca=predict(model2,pca_data$scores[,1:2])
confusionMatrix(factor(dataset[,14]),factor(predicted_values_pca))




