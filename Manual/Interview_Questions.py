# #smoke testing = Testing the build stability for further testing
# #tests critical functionalities only
# #it will be performed on every new build
#
# #sanity testing = To verify specific bug fixes or features
# #tests only on specific areas
# #performed on modified build
#
# #severity = It tells how bad is that bug in terms of its impact on the application
# #crirtical, high,medium and low
#
# #priority = it tells how soon should the bug be fixed based on business needs
# #high ,medium and low
#
# #key factors to prioritize bugs
# # 1.Impact on functionality
# # ->Login feature = showstopper
# # ->issue in admin analytics - medium/low
# #
# # 2.Frequency of occurrence
# #
# # 3.Severity of bug
# #
# # 4.Business impact
# #
# # 5.Customer visibility
# #
# # 6.deadlines and release schedule
#
# #Q1: How do you handle issues in a page or framework?
#
# 🛠 Common Page Issues & Solutions
# Issue	Solution
# ❌ Element not found	✅ Use dynamic waits (WebDriverWait, expected_conditions)
# ❌ StaleElementReferenceException	✅ Re-locate element after page reload
# ❌ Click intercepted	✅ Use ActionChains or JavaScript click
# ❌ Dynamic locators	✅ Use relative XPath/CSS or regex in locators
# ❌ Pop-ups/alerts	✅ Handle with driver.switch_to.alert
# ❌ Frames/IFrames	✅ Switch to frame: driver.switch_to.frame()
#
#  Common Framework Issues & Solutions
# Issue	Solution
# ❌ Driver compatibility	✅ Use WebDriverManager or match browser/driver versions
# ❌ Library dependency errors	✅ Pin versions in requirements.txt
# ❌ Configuration issues	✅ Validate config.yaml/.env files
# ❌ Parallel execution failures	✅ Check thread-safety of framework components
#
# Q2: How do you debug automation failures?
# 🔥 Step 1: Check the Failure Logs
# Review the stack trace in the test report (HTML report, Jenkins console).
#
# Identify if it’s:
#
# Framework failure (setup issue).
#
# Test script failure (code/logic issue).
#
# Application issue (UI changes, server error).
#
# 🔥 Step 2: Rerun Test Locally
# Run the failing test locally in debug mode.
#
# Add breakpoints (in PyCharm or VSCode) and use step-through debugging.
#
# 🔥 Step 3: Isolate the Problem
# Is it reproducible every time?
#
# ✅ Yes → Code or application issue.
#
# ❌ No → Possible flaky test (network, timing issues).
#
# 🔥 Step 4: Common Fixes for Failures
# Failure Type	Fix
# ❌ Element not interactable	✅ Add explicit waits (WebDriverWait)
# ❌ Timeout errors	✅ Increase wait time or optimize locator strategy
# ❌ Locator failures	✅ Update locators after UI changes
# ❌ Test data issues	✅ Validate test data source (Excel, DB, API)
# ❌ Browser compatibility issues	✅ Test on multiple browsers using cross-browser setup
#
# 🔥 Step 5: Review Framework Hooks/Config
# Check:
#
# Setup/teardown methods
#
# Test fixtures
#
# Parallel execution settings
#
# 🔥 Step 6: Collaboration
# If the issue is with the app (e.g., backend API fails), report to the dev team with:
#
# Logs
#
# Screenshots
#
# Steps to reproduce
#

#Perfect! This is a classic interview question for QA/automation testers. They want to see if you can think broadly and deeply about testing a Login Page.

# Here’s a complete real-world answer that covers:
# ✔️ Positive test cases
# ✔️ Negative test cases
# ✔️ Boundary, edge, security, and UI considerations
# ✔️ Both manual & automation perspective 👇

#High Priority and low severity
# issue = A typo error in the company name
# severity = Low severity as it doesnt break any functionality
# priority = high priority as it affects brand reputation and needs to be fixed before production

#Low priority and high severity
# issue = Export to excel button is not working
# severity = High severity as is causes data loss
# priority = rarely used by stakeholders can be fixed in a future sprint

#High priority and hign severity
# issue = payment gateway not working
# severity = high severity as users cant make payment
# priority = direct revenue loss must be fixed asap
#
# #low priority and low severity
# issue = misaligned text or minor UI changes
# severity = no impact on functionality
# priority = doesnt effect end users.

# 1.What is the difference between Verification and Validation?
# Verification is about the process how we can do
# validation is about the product what we are doing.
#
# 2. What are the different levels of testing?
# 1.unit testing = done by developers on individual functions/modules
# 2.Integration testing = Checking data flow b/w modules
# 3.system testing = End to end testing on the whole application
# 4.Acceptence testing = Ensures software meets business requirements(UAT)

# 3. What is a Test Case and What Should It Include?
# A test case is a set of actions to verify a specific feature or functionality
# 1.Test Case id
# 2.Test Scenario/objective
# 3.Preconditions
# 4.Test Steps
# 5.expected result
# 6.Actual result
# 7.status
# 8.priority
# 9.comments
#
# 5. How do you ensure the quality of testing in your project?
# 1.Writing clear and detailed test cases
# 2.Regular reviewing test cases with peers
# 3.Using check list for test coverage
# 4.Reporting bugs with proper steps and logs
# 5.Testing both positive and negative Scenarios
# 6.Retesting and regression testing throughly
# 7.Coordinating closely with developers and BA,
