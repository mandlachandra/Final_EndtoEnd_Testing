# 1. What is Functional Testing?
#
# Answer:
# Functional testing is a type of software testing where we verify that the application functions according to the requirements. It focuses on what the system does rather than how it does it.
# Example: In Michaels’ e-commerce site, testing that a user can search for a product, add it to the cart, and successfully complete checkout.
#
# 2. What are the types of Functional Testing?
#
# Answer:
#
# Unit Testing – testing individual functions/modules.
#
# Smoke Testing – basic check to ensure critical flows work.
#
# Sanity Testing – quick checks after fixes.
#
# Regression Testing – ensure new changes don’t break existing features.
#
# Integration Testing – testing data flow between modules.
#
# System Testing – end-to-end application testing.
#
# User Acceptance Testing (UAT) – validation by business users.
#
# 3. What is the difference between Functional and Non-Functional Testing?
#
# Answer:
#
# Functional → tests business logic & features (login, checkout).
#
# Non-functional → tests performance, security, usability, etc.
#
# 4. What is the process you follow in Functional Testing?
#
# Answer:
#
# Understand requirements (BRD, user stories).
#
# Prepare test scenarios & test cases.
#
# Identify test data.
#
# Execute test cases.
#
# Log defects in Jira.
#
# Retest & regression after fixes.
#
# Provide test reports.
#
# 5. What techniques do you use to design test cases for Functional Testing?
#
# Answer:
#
# Equivalence Partitioning (EP) → dividing inputs into valid/invalid classes.
#
# Boundary Value Analysis (BVA) → testing edge values (min, max).
#
# Decision Table Testing → combinations of inputs → outputs.
#
# State Transition Testing → checking system behavior in different states.
#
# Error Guessing → based on experience, guessing where app may fail.
#
# 6. Can you explain an example of Functional Testing you did in Michaels?
#
# Answer:
# “In Michaels’ site, one functional test was verifying the checkout process:
#
# Login → Search Product → Add to Cart → Apply Coupon → Make Payment.
# We created positive test cases (valid card payment) and negative test cases (expired card, invalid coupon). We also did boundary testing (max cart limit) and regression testing after new discounts were introduced.”
#
# 7. What are entry and exit criteria in Functional Testing?
#
# Answer:
#
# Entry Criteria: Requirements finalized, environment ready, test cases prepared.
#
# Exit Criteria: All planned test cases executed, critical defects closed, test reports published.
#
# 8. How do you ensure all requirements are covered in Functional Testing?
#
# Answer:
# We prepare a Requirement Traceability Matrix (RTM) that maps each requirement → test cases → test results. This ensures full coverage.
#
# 9. How do you decide whether testing is complete?
#
# Answer:
#
# 100% critical test cases executed.
#
# No Sev-1 / Sev-2 defects open.
#
# Test coverage achieved.
#
# Stakeholder sign-off.
#
# 10. How do you handle regression testing in Functional Testing?
#
# Answer:
#
# Identify impacted areas after new code changes.
#
# Automate frequently used regression test cases with Selenium + Pytest.
#
# Run regression suite in Jenkins before each release.
#
# 11. What challenges have you faced in Functional Testing?
#
# Answer:
#
# Incomplete requirements → clarified with BA/PO.
#
# Frequent requirement changes → handled by maintaining modular test cases.
#
# Test data dependency → used SQL queries & automation scripts to prepare data.
#
# 12. Difference between Smoke and Sanity Testing?
#
# Answer:
#
# Smoke → Build Verification → “Is the build stable enough to test?”
#
# Sanity → Small scope → “Does the fix/new functionality work as expected?”
#
# 13. Have you automated any functional tests?
#
# Answer:
# “Yes. In Michaels automation, functional test cases like login, product search, add-to-cart, and checkout were automated using Selenium with Python. We used Pytest for execution and Jenkins for CI/CD. Reports were generated via Allure/HTML reports.”
#
# 14. What tools have you used for Functional Testing?
#
# Answer:
#
# Manual Testing → Jira, TestRail (test management).
#
# Automation → Selenium with Python, Pytest, Allure, Jenkins.
#
# API Functional Testing → Postman, Rest Assured (Python requests).
#
# 15. What’s the role of Functional Testing in Agile?
#
# Answer:
# In Agile, functional testing is performed in every sprint. As soon as a user story is developed, we write and execute functional tests. We also run regression tests before the sprint ends to ensure nothing else is broken.
#
# ✅ Short Interview Tip: Since you have both Manual + Automation experience, frame your answers like:
#
# “We first test manually → then automate high-priority regression cases.”
#
# “In Michaels, we followed Agile; functional testing was done sprint-wise, and automated tests were integrated with Jenkins.”