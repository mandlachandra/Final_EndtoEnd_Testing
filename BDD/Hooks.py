# In BDD frameworks like Behave (Python) or Cucumber (Java),
# hooks are special methods that run before or after certain events in your test execution.
#
# They are like setup and teardown methods but specifically tailored for BDD.
#
# 🔹 Types of Hooks
#
# Before/After Scenario Hooks
#
# Run before or after every scenario.
#
# Example: Open browser before each scenario, close it after scenario.
#
# Before/After Step Hooks
#
# Run before or after every step.
#
# Example: Logging step execution.
#
# Before/After Feature Hooks
#
# Run before or after a feature file.
#
# Example: Database setup before a feature, cleanup after feature.
#
# Before/After All Hooks
#
# Run once before all tests and after all tests.
#
# Example: Initialize a global report, teardown report.
#
# 🔹 Hooks in Behave (Python Example)
#
# 📂 project structure
#
# features/
#    ├── steps/
#    │     └── step_definitions.py
#    ├── environment.py   ← Hooks go here
#    └── sample.feature
#
#
# 📌 environment.py
#
# from selenium import webdriver
#
# def before_all(context):
#     print("⚡ Before All: Initialize test environment")
#
# def after_all(context):
#     print("🛑 After All: Cleanup test environment")
#
# def before_feature(context, feature):
#     print(f"🚀 Starting Feature: {feature.name}")
#
# def after_feature(context, feature):
#     print(f"✅ Completed Feature: {feature.name}")
#
# def before_scenario(context, scenario):
#     print(f"🔹 Starting Scenario: {scenario.name}")
#     context.driver = webdriver.Chrome()  # launch browser
#
# def after_scenario(context, scenario):
#     print(f"🔸 Ending Scenario: {scenario.name}")
#     context.driver.quit()  # close browser
#
# def before_step(context, step):
#     print(f"➡️  Starting Step: {step.name}")
#
# def after_step(context, step):
#     print(f"⬅️  Finished Step: {step.name}")
#
# 🔹 Why Use Hooks?
#
# Browser setup/teardown → Open browser before a scenario, close it after.
#
# Test data management → Insert or cleanup data before/after a feature.
#
# Logging & Reporting → Capture logs/screenshots after failed steps.
#
# Reusability → Avoid repeating setup code in every step definition.
#
# ✅ Example use case in automation:
#
# before_scenario: Login to app.
#
# after_scenario: Logout and take screenshot if failed.
#
# before_feature: Load required test data.
#
# after_all: Generate and send HTML report.