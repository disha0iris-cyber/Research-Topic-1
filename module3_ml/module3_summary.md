Questions  & Answers

What forecasting methods are appropriate? • When are simple methods sufficient? Simple methods such as Moving Average or ARIMA are sufficient for short-term forecasting of stable services.
• When do you need deep learning? Deep learning models (LSTM, Transformers) are required to capture long-range dependencies and complex temporal patterns.

• Trade-off between complexity and accuracy More complex models offer higher accuracy but require more data, computational resources, and careful tuning.

How accurate can predictions be? • Metrics used Accuracy is evaluated using MAE, RMSE, and MAPE.
• Variation by service and time API traffic achieves higher accuracy, while video traffic is more error-prone during peak periods.

• Realistic forecast horizon Reliable predictions are limited to short horizons; accuracy deteriorates for long-term forecasts.

What happens when predictions are wrong? Prediction errors directly affect allocation decisions, leading to congestion or wasted capacity.
• Quantifying uncertainty Uncertainty is quantified using historical prediction errors and confidence intervals.

• Why ML alone is insufficient ML lacks guarantees under worst-case scenarios, making it unreliable without robustness mechanisms.

How can uncertainty be characterized? Uncertainty can be represented through prediction intervals derived from model errors, which are later incorporated into optimization models.
