# Read the file
mydata <- read.csv("pca_gsp.csv")

# attach function attaches dataset to R search file
attach(mydata)

# Returns names of attributes
names(mydata)

# cbind function takes sequence of vector,matrix, or data-frame arguments and combine by columns or rows respectively
X <- cbind(Ag,Mining,Constr,Manuf,Manuf_nd,Transp,Comm,Energy,TradeW,TradeR,RE,Services,Govt)
summary(X)

# cor() function will calculate the correlation between two vectors, or will create a correlation matrix when given a matrix
cor(X)

# princomp performs a principal components analysis on the given numeric data matrix and returns the results as an object of class princomp
pcal <- princomp(X,scores = TRUE, cor = TRUE)
summary(pcal)
# Importance of components:
#                          Comp.1    Comp.2    Comp.3    Comp.4
# Standard deviation     1.7987525 1.4954801 1.3999420 1.1663403
# Proportion of Variance 0.2488854 0.1720354 0.1507567 0.1046423
# Cumulative Proportion  0.2488854 0.4209209 0.5716776 0.6763199
#                         Comp.5     Comp.6     Comp.7     Comp.8
# Standard deviation     1.07583525 0.93184458 0.85116719 0.78471605
# Proportion of Variance 0.08903242 0.06679495 0.05572966 0.04736764
# Cumulative Proportion  0.76535232 0.83214726 0.88787692 0.93524456
#                         Comp.9   Comp.10    Comp.11    Comp.12
# Standard deviation     0.5641253 0.4851322 0.38943836 0.36945813
# Proportion of Variance 0.0244798 0.0181041 0.01166633 0.01049995
# Cumulative Proportion  0.9597244 0.9778285 0.98949478 0.99999473
#                         Comp.13
# Standard deviation     8.279806e-03
# Proportion of Variance 5.273476e-06
# Cumulative Proportion  1.000000e+00

# loadings() function prints loadings in factor analysis
loadings(pcal)
#                 Comp.1 Comp.2 Comp.3 Comp.4 Comp.5 Comp.6 Comp.7 Comp.8
# SS loadings     1.000  1.000  1.000  1.000  1.000  1.000  1.000  1.000
# Proportion Var  0.077  0.077  0.077  0.077  0.077  0.077  0.077  0.077
# Cumulative Var  0.077  0.154  0.231  0.308  0.385  0.462  0.538  0.615
#                 Comp.9 Comp.10 Comp.11 Comp.12 Comp.13
# SS loadings     1.000   1.000   1.000   1.000   1.000
# Proportion Var  0.077   0.077   0.077   0.077   0.077
# Cumulative Var  0.692   0.769   0.846   0.923   1.000

plot(pcal)







screeplot(pcal,type = "line",main = "Screen Plot")


biplot(pcal)

pcal$scores[1:10,]
