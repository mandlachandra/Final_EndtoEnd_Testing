# 1. What is Performance Testing?
# Performance Testing is a non functional testing that checks how an application behaves under
# expected and peak load conditions .
# It evaluates speed,scalability,reliability and resource usage

# 2. What are the types of Performance Testing?
# Load Testing = Test with expected load
# Stress Testing = Test beyond normal limits
# Spike Testing = Sudden increase or decrease in user load
# Endurance Testing = Run system under load for long duration
# Volume Testing = Test with large volumes of data
# Scalability Testing = Test how the system scales as load increases

# 3. What performance testing tools have you used?
# Apache Jmeter
# LoadRunner
#
# Example: I have used Apache JMeter to test REST APIs
# by simulating 1000 concurrent users and generating reports for average response time,
# throughput, and error rate.

# 4. What are some key performance metrics?
# Response Time
# Throughput (request/sec)
# Latency
# Error Rate
# CPU & Memory usage
# Hits per second
# Transactions per second(TPS)

# 6. What is the difference between response time and throughput?
# Response Time = Time taken for 1 request to complete
# Throughput = Total number of requests handled per second/Minute

# 7. How do you test an API's performance?
# Use JMeter or postman/Newman to send concurrent requests
# Simulate load using Thread groups
# Monitor response times, error %
# Analyze results with listeners like Summary report ,Aggregate Report

# 9. What is think time in performance testing?
# Think time is a pause b/w 2 user actions
# It simulates the real user behaviour where users take time to read and act
# In JMeter it is configured using Timers(eg.Constant Timer)

# 10. What are common challenges in performance testing?
# Creating realistic test scenarios
# Generating accurate user load
# Monitoring system level metrics
# Identifying bottlenecks
# data generation and test data management
# Correlation and parameterization in scripts




