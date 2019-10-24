# reading dataset
dataset=read.csv('diabetes_csv.csv')

#converting last column into factors
dataset$class=factor(dataset$class,levels=c('tested_positive',"tested_negative"),labels=c('0','1'))

#scaling the dataset
dataset[,-9]=scale(dataset[,-9])

#applying princomp function
pc_data=princomp(dataset[,-9])
summary(pc_data)

#abcd is a dataframe which contains pc_data$scores
abcd=data.frame(pc_data$scores)
plot(pc_data,type="line")

#libraries required for naive bayes and confusion matrix
library(caret)
library(e1071)

#naive bayes for normal dataset (accuracy for normal dataset is 76.17)
model_normal=naiveBayes(dataset[,1:8],dataset$class)
y_pred_normal=predict(model_normal,dataset[,1:8])
confusionMatrix(dataset$class,y_pred_normal)


#naive bayes after performing PCA (accuracy by considering 2 components is 72.01)
model_pca=naiveBayes(abcd[,1:2],dataset$class)
y_pred_pca=predict(model_pca,abcd[,1:2])
print(confusionMatrix(dataset$class,y_pred_pca))


#if you want to select only one component then you need to use data.frame function
model_pca=naiveBayes(data.frame(abcd[,1]),dataset$class)
y_pred_pca=predict(model_pca,data.frame(abcd[,1]))
confusionMatrix(dataset$class,y_pred_pca)


#accuracy after selecting only PC1 is 71.61
biplot(pc_data)
plot(pc_data)
screeplot(pc_data,type="line")



