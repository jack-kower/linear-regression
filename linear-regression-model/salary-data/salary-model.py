# this imports the whole pandas library and renames it to pd
import pandas as pd

# this imports the matplotlib library's module pyplot and renames it to plt
from matplotlib import pyplot as plt

# this imports the LinearRegression class from the scikit-learn library's module linear_model
from sklearn.linear_model import LinearRegression, LogisticRegression
# allows data to be seperated into training and testing sets
from sklearn.model_selection import train_test_split

# this imports the mean_squared_error class from the scikit-learn library's module metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Specify the file path of the CSV file
file_path = 'salary-data-2022.csv'

# Read the CSV file and store it in a DataFrame
df = pd.read_csv(file_path)

# data frame of just minimum wage, unemployment rate, and mean salary
my_df = pd.DataFrame(df, columns=['minimum wage', "unemployment rate", "mean salary"])

# Since our target to train is mean salary, we will use it as our target and drop it

# sees all columns that are not the target column. The features
X = my_df.drop('mean salary', axis=1)
# sees only the target column
y = my_df['mean salary']

# splits the data into training and testing sets
# the larger the test size, the slower the model will run
# The ideal test size is 0.2 to 0.3
# The train size is 1-test_size
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=1)

### Starting here is the Linear Regression Model ###
# This sets an alias for the LinearRegression class called linr
linr = LinearRegression()
logr = LogisticRegression()

# fits the model to the training data
linr.fit(X_train, y_train)
logr.fit(X_train, y_train)
# Prediction of mean salary based on minimum wage and unemployment rate
y_pred = linr.predict(X_test)
y_pred2 = logr.predict(X_test)

# prints the accuracy of the model
r2 = r2_score
mse = mean_squared_error
mae = mean_absolute_error
intercept = linr.intercept_
intercept2 = logr.intercept_
# prints the prediction of target.
print("USING LINEAR REGRESSION: ")
print("predicted mean salary is: ", y_pred)

print("R2 Score: ", r2(y_test, y_pred))
print("Mean Squared Error: ", mse(y_test, y_pred))
print("Mean Absolute Error: ", mae(y_test, y_pred))
print("Intercept: ", intercept)


print("USING LOGISTIC REGRESSION: ")

print("predicted mean salary is: ", y_pred2)

print("R2 Score: ", r2(y_test, y_pred2))
print("Mean Squared Error: ", mse(y_test, y_pred2))
print("Mean Absolute Error: ", mae(y_test, y_pred2))
print("Intercept: ", intercept2)

#graphing both linear and logistic regression
#make it a scatter plot
plt.scatter(y_test, y_pred, color='blue', alpha=0.4)
plt.scatter(y_test, y_pred2, color='green', alpha=0.4)
#Makes key for blue and green dots
plt.legend(['Linear Regression', 'Logistic Regression'])
#plot a line
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red')
plt.title('actual mean salary vs predicted mean salary')
plt.xlabel('actual mean salary')
plt.ylabel('predicted mean salary')
#shows the graph
plt.show()
#downloads a png file of the graph
plt.savefig('salary-pred-regressions.png')
