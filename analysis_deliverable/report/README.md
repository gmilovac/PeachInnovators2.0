# Analysis Deliverable

Correlation between Watts and Speed: PearsonRResult(statistic=0.5075852543816257, pvalue=4.889500636668049e-65)
Correlation between Effective Length and Speed: PearsonRResult(statistic=0.16216358685065885,
pvalue=3.5168198665394844e-07)
Correlation between Length and Speed: PearsonRResult(statistic=0.06714991433005946, pvalue=0.03594846813703125)

## Hypothesis Testing

### Hypothesis 1

Higher Watts increase boat speed.

#### Results

statistic=0.5075852543816257
pvalue=4.889500636668049e-65

#### Why did we use this test?

We chose to test our hypothesis using linear regression. We considered using a non-linear regression to do so, but
ultimately chose to use a linear regression model as we felt we did not have enough data to successfully avoid
overfitting in our model. Additionally, we chose regression to test our hypotheses as we wanted to find the relationship
between our dependent variable (boat speed) and our various independent variables (in this case, watts).

We relied on our regression coefficient and p-value to measure success/failure, seeing a positive/negative coefficient (
based on our hypothesis) with a sufficiently small p-value as a signal of significant/successful results.

We did not have to do much cleaning - we had already done the majority of our cleaning for the data deliverable
component, however we did find a few rows that we had to remove from our data as they either omitted NULL values or
values so far outside the realm of reasonable expectations that they signaled a broken or maladjusted sensor.

#### Evaluation

The results of our regression of boat speed on Watts yielded a regression coefficient of approximately +0.51 with a
p-value of approximately 4.9e-65. This is a positive regression coefficient with an extremely small p-value, suggesting
significance of the finding that Watts are positively correlated with boat speed. This is what we hypothesized, and
given the significance of our p-value we accept the hypothesis that watts and boat speead are positively related.

Intuitively we are not surprised by our hypothesis being supported by the data - Watts are a measure of power output and
intuitively, more power should propel the boat at faster speeds. Additionally, stronger athletes tend to receive more
attention from coaches, thus improving their technical ability thus improving their ability to move boats quickly. We
are, however, surprised by the significance of the results. Our calculated p-value is extremely small, indicating high
significance of the Pearson coefficient, higher significance than we were expecting. We had initially expected a less
significant relationship.

### Hypothesis 2

Greater effective length increases boat speed.

#### Results

statistic=0.16216358685065885
pvalue=3.5168198665394844e-07

#### Why did we use this test?

We chose to test our hypothesis using linear regression. We considered using a non-linear regression to do so, but
ultimately chose to use a linear regression model as we felt we did not have enough data to successfully avoid
overfitting in our model. Additionally, we chose regression to test our hypotheses as we wanted to find the relationship
between our dependent variable (boat speed) and our various independent variables (in this case, effective length).

We relied on our regression coefficient and p-value to measure success/failure, seeing a positive/negative coefficient (
based on our hypothesis) with a sufficiently small p-value as a signal of significant/successful results.

We did not have to do much cleaning - we had already done the majority of our cleaning for the data deliverable
component, however we did find a few rows that we had to remove from our data as they either omitted NULL values or
values so far outside the realm of reasonable expectations that they signaled a broken or maladjusted sensor.

#### Evaluation

What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your
prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have.
Intuitively, how do you react to the results? Are you confident in the results?)

The results of our regression of boat speed on effective length yielded a regression coefficient of approximately +0.16
with a
p-value of approximately 3.52e-07. This is a positive regression coefficient with an extremely small p-value, suggesting
significance of the finding that effective length is positively correlated with boat speed. This is what we
hypothesized, and
given the significance of our p-value we accept the hypothesis that effective length and boat speed are positively
related.

Intuitively we are not surprised by our hypothesis being supported by the data, as effective length measures the arc of
the blade-path
for which the blade is 'connected' or produces at least a minimum threshold of watts, indicating that the blade is now
actively working
against the water. The longer the work is held on the blade, the more force that can be exerted to move the boat
forward. We are
confident in the results as the p-value is sufficiently small to be significant.

### Hypothesis 3

Greater raw length increases boat speed.

#### Results

statistic=0.06714991433005946
pvalue=0.03594846813703125

#### Why did we use this test?

We chose to test our hypothesis using linear regression. We considered using a non-linear regression to do so, but
ultimately chose to use a linear regression model as we felt we did not have enough data to successfully avoid
overfitting in our model. Additionally, we chose regression to test our hypotheses as we wanted to find the relationship
between our dependent variable (boat speed) and our various independent variables (in this case, length).

We relied on our regression coefficient and p-value to measure success/failure, seeing a positive/negative coefficient (
based on our hypothesis) with a sufficiently small p-value as a signal of significant/successful results.

We did not have to do much cleaning - we had already done the majority of our cleaning for the data deliverable
component, however we did find a few rows that we had to remove from our data as they either omitted NULL values or
values so far outside the realm of reasonable expectations that they signaled a broken or maladjusted sensor.

#### Evaluation

What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your
prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have.
Intuitively, how do you react to the results? Are you confident in the results?)

The results of our regression of boat speed on effective length yielded a regression coefficient of approximately +0.07
with a
p-value of approximately 0.036. This is a positive regression coefficient with a significant p-value (though not as
significant
as our other hypothesis tests), suggesting significance of the finding that overall length is positively correlated with
boat
speed. This is what we hypothesized, and given the significance of our p-value we accept the hypothesis that overall
length
and boat speed are positively related.

Intuitively we are not surprised by our hypothesis being supported by the data, as length measures the arc of the
blade-path
through each stroke. The longer the stroke length, the longer the oar is spent propelling the boat forwards. We are
confident in the results as the p-value is sufficiently small to be significant.

## Machine Learning

### Model 1

#### Model specifics

Multiple regression of boat speed on length, catch slip, and watts. The purpose of this test is to see which variables
impact boat
speed and the magnitude to which each impacts boat speed.

#### Results

#### Why did we use this model?

#### Evaluation

(Why did you use this statistical test or ML algorithm? Which other tests did you consider or evaluate? What metric(s)
did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model?
Did you have to clean or restructure your data? What is your interpretation of the results? Do you accept or deny the
hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you
got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the
results?)

We used a multiple regression because we wanted to find the relationship of multiple variables with our dependent
variable
(boat speed). To measure success/failure of the model we use t-statistic, confidence interval and sign/size of the
coefficient
of each variable. A multiple regression seemed like an intuitive way to measure the impact of multiple variables on boat
speed
at the same time while controlling the bias introduced by each other variable. As before, we had to clean only a small
portion
of the data that we did not previously clean in the data deliverable so that we could run our data through the
regression with no
errors or significant outliers that suggested a broken sensor reading.

Our results of the model are as follows: Length (coeff: 0.0016, p-value: 0.4), catch slip (coeff: -0.0064, p-value: 0.101), watts (coeff: 0.0042, p-value: 0.000). These results suggest that once we consider watts, catch slip and length as independent variables on boat speed, watts is the only statistically significant variable related to boat speed. This is highly surprising given our previous consideration of length as fundamental to the rowing stroke. Although these results are highly statistically significant (for watts but not the other two metrics), the data that we are working with has some serious limitations (control for direction, wind, water conditions, etc.) so althought the p-value may be very significant, it is important to consider these results in the context of our data being limited in scope.
### Model 2

#### Model specifics

The second model is a deep learning neural network developed using TensorFlow and Keras, designed to predict boat speed
from
various input features like Watts, Piece Number, and Effective Length. It incorporates multiple dense layers with ReLU
activation and regularization to manage overfitting, optimized using Adam with a focus on minimizing the mean squared
error (MSE). Despite employing cross-validation to ensure robustness and prevent model bias, the RMSE of approximately
13.16% of the mean boat speed suggests the model still requires refinement to enhance its predictive accuracy and
reliability.

#### Results

Mean Boat Speed: 5.458852459016393 m/s

Variance of Boat Speed: 0.16183556839559257

**Overall performance:**

Average MSE across all folds: 0.633944496512413

Standard Deviation MSE across all folds: 0.49534558462948314

Average RMSE across all folds: 0.7188324928283691

#### Evaluation

The deep learning model using TensorFlow and Keras was selected for its ability to handle nonlinear relationships and
interactions between multiple input features. Given the complex nature of factors influencing boat speed, a neural
network can learn these intricate patterns effectively, which might not be easily captured by simpler linear models.

The primary metrics used were Mean Squared Error (MSE) and Root Mean Squared Error (RMSE). MSE is sensitive to large
errors and provides a clear indication of model performance in terms of average squared error, making it suitable for
regression tasks. RMSE converts these errors back to the original units of the target variable (speed), offering a more
interpretable measure of average error magnitude. Additionally, comparing RMSE to the mean speed allows for assessing
model errors relative to actual speed values.

Complications in creating model:

- Variance in model performance across different folds, indicated by a standard deviation in MSE. This suggests model
  sensitivity to the specific splits of the data, possibly due to underlying variability or outliers within the dataset.
- Ensuring model robustness to different data distributions, which was addressed through K-Fold cross-validation.
- Interpreting error metrics in a meaningful way, especially relating RMSE to practical applications in the context of
  boat speed.

The data did not need to be significantly cleaned or restructured for this model, as the preprocessing steps from the
data deliverable were sufficient.

With an average RMSE of 0.719 m/s, the model's error is significant, particularly when considering the mean boat speed
of 5.459 m/s and the relatively low variance in boat speed (0.162 m/s²). The RMSE represents approximately 13.16% of the
mean boat speed, which may be considered high in contexts requiring high precision. The RMSE also surpasses the square
root of the variance (about 0.402 m/s), indicating that the prediction error is larger than the typical variability of
boat speed in the dataset. This suggests the model may not be capturing all relevant factors or interactions
effectively.

The average RMSE being greater than the square root of the variance indicates that the model’s predictions are less
accurate than desired, and the high standard deviation in MSE across folds suggests variability in model performance.
This variability can reduce confidence in the model's robustness and its generalizability to unseen data. To increase
confidence, further investigations into feature engineering, alternative model architectures, or additional data sources
could be beneficial. Optimizations such as tuning hyperparameters and incorporating regularization techniques might also
help reduce the prediction error and stabilize performance across different subsets of data.

In summary, while the initial model setup and cross-validation efforts provide a good starting point, the model requires
significant improvements to achieve a level of accuracy that is dependable and useful in actually predicting boat speed.

## Final Evaluation

The results of our analysis were largely in line with our initial beliefs about the data. We hypothesized that Watts and
Effective Length would have a positive correlation with boat speed, and that Length would have a positive correlation
with boat speed. Our results did not support these hypotheses, with Watts having a strong positive correlation with boat
speed and both Effective Length and Length having a weak negative correlation with boat speed. This was surprising to us,
as we had expected that the longer the stroke length, the more force that could be exerted to move the boat forward. We
had also expected that the longer the work is held on the blade, the more force that can be exerted to move the boat
forward.

The tools for analysis that we chose were appropriate for the data we had. We used linear regression to test our
hypotheses, as we wanted to find the relationship between our dependent variable (boat speed) and our various independent
variables (Watts, Effective Length, and Length). We used a deep learning neural network to predict boat speed from
various input features like Watts, Piece Number, and Effective Length. We chose these tools because they were well-suited
to the type of data we had and the questions we wanted to answer.

The data was adequate for our analysis, but there were some aspects of the data that were problematic. We had to clean
the data to remove rows that omitted NULL values or values so far outside the realm of reasonable expectations that they
signaled a broken or maladjusted sensor. We could have remedied this by being more thorough in our initial data cleaning
process.

```angular2html
Variance of MSE across all folds: 0.0003205489023127002
OLS Regression Results
==============================================================================
Dep. Variable:                  Speed   R-squared:                       0.260
Model:                            OLS   Adj. R-squared:                  0.258
Method:                 Least Squares   F-statistic:                     113.9
Date:                Wed, 24 Apr 2024   Prob (F-statistic):           3.16e-63
Time:                        18:04:54   Log-Likelihood:                -321.42
No. Observations:                 976   AIC:                             650.8
Df Residuals:                     972   BIC:                             670.4
Df Model:                           3
Covariance Type:            nonrobust
==============================================================================
coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          3.9411      0.186     21.219      0.000       3.577       4.306
Length         0.0016      0.002      0.842      0.400      -0.002       0.005
Catch Slip    -0.0064      0.004     -1.644      0.101      -0.014       0.001
Watts          0.0042      0.000     16.701      0.000       0.004       0.005
==============================================================================
Omnibus:                       44.862   Durbin-Watson:                   0.553
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               50.209
Skew:                          -0.551   Prob(JB):                     1.25e-11
Kurtosis:                       2.851   Cond. No.                     6.02e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 6.02e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```