# Example usage
from autohedge.main import AutoFund
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
print("Environment variables loaded successfully.")

# Define the stocks to analyze
stocks = ["NVDA"]

# Initialize the trading system with the specified stocks
trading_system = AutoFund(
    name="swarms-fund",
    description="Private Hedge Fund for Swarms Corp",
    stocks=stocks,
)

# Define the task for the trading cycle
task = "As BlackRock, let's evaluate AI companies for a portfolio with $500 million in allocation, aiming for a balanced risk-reward profile."

# Run the trading cycle and print the results
print(trading_system.run(task=task))
