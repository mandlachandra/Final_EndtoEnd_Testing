# Q1: What is an API?
# Answer:
# An API (Application Programming Interface) is a set of rules and protocols that allow different software systems to communicate with each other. APIs expose endpoints for performing operations like retrieving, creating, updating, or deleting resources.
# Example: A weather app uses an API to fetch data from a weather server.

# 2. Types of APIs: REST, SOAP, GraphQL
# Q2: What are the different types of APIs?
# Answer:
# The main types of APIs include:
#
# REST (Representational State Transfer) – Uses HTTP methods, stateless, and works with resources (URLs).
#
# SOAP (Simple Object Access Protocol) – XML-based, protocol-driven, and highly secure; used in enterprise systems.
#
# GraphQL – Query language for APIs, allows clients to request only the data they need.
#
# Q3: How is REST different from SOAP?
# Answer:
#
# Feature	REST	SOAP
# Format	JSON, XML	XML only
# Protocol	Uses HTTP	Uses HTTP, SMTP, TCP
# Flexibility	More flexible	More strict
# Performance	Faster, lightweight	Slower due to XML processing
# Security	OAuth, JWT	WS-Security (enterprise grade)

# Q4: What is GraphQL and how is it different from REST?
# Answer:
# GraphQL allows clients to request exactly the data they need in a single query, avoiding over-fetching
# or under-fetching. REST has multiple endpoints, while GraphQL typically has one endpoint.

# Q6: Difference between PUT and PATCH?
# Answer:
#
# PUT replaces the entire resource.
#
# PATCH updates only the fields provided.

#  What are HTTP status codes and their categories?
# Answer:
#
# Category	Meaning	Examples
# 1xx	Informational	100 Continue
# 2xx	Success	200 OK, 201 Created
# 3xx	Redirection	301 Moved Permanently, 302 Found
# 4xx	Client Error	400 Bad Request, 401 Unauthorized, 404 Not Found
# 5xx	Server Error	500 Internal Server Error, 503 Service Unavailable

# Q8: What does status code 201 mean?
# Answer:
# 201 Created indicates that a new resource has been successfully created using a POST request.
#
# Q9: What’s the difference between 401 and 403?
# Answer:
#
# 401 Unauthorized: Authentication is required or failed.
#
# 403 Forbidden: Authentication is provided but the user is not allowed to access the resource.

# Q10: What is the structure of an HTTP request?
# Answer:
# An HTTP request typically includes:
#
# Method (GET, POST, etc.)
#
# URL (Endpoint)
#
# Headers (Authentication, Content-Type)
#
# Query Parameters or Path Parameters
#
# Body (JSON/XML payload for POST/PUT)

# 11: What is the structure of an HTTP response?
# Answer:
# An HTTP response includes:
#
# Status Code
#
# Headers (Content-Type, Server info)
#
# Body (Response data in JSON/XML)

# Q12: What are request headers?
# Answer:
# Headers carry metadata in an HTTP request.
# Examples:
#
# Content-Type: application/json
#
# Authorization: Bearer <token>

# Q13: What is the difference between Query Params and Path Params?
# Answer:
#
# Feature	Query Params	Path Params
# Format	/users?id=123	/users/123
# Use	Optional filters or search	Identify a specific resource
# Sent in	URL after ?	Directly in the endpoint path
#
# Q14: What is the body in an API request?
# Answer:
# The body contains the actual data (payload) sent in POST, PUT, or PATCH requests, usually in JSON or XML format.
# {
#   "name": "John",
#   "email": "john@example.com"
# }