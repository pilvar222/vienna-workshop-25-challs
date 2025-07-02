# Lab Exercise 1: Web Application Security Basics

## Objective
Learn the fundamentals of web application security testing and common vulnerabilities.

## Prerequisites
- Basic understanding of HTTP/HTTPS protocols
- Familiarity with web browsers and developer tools
- Basic command line knowledge

## Lab Environment
- Target Application: Vienna Bootcamp Platform
- Tools: Browser Developer Tools, Burp Suite (optional)

## Exercise Steps

### 1. Information Gathering
- Explore the application structure
- Identify input fields and parameters
- Check for exposed files or directories

### 2. Parameter Testing
- Test URL parameters for unusual behavior
- Look for ways to access files outside intended directories
- Examine how the application handles different file paths

### 3. Input Validation Testing
- Try various input formats
- Test special characters and encoding
- Check for proper sanitization

### 4. Security Headers Analysis
- Examine response headers
- Check for security-related headers
- Document any missing protections

## Common Vulnerabilities to Look For
- Directory Traversal (Path Traversal)
- Local File Inclusion (LFI)
- Improper Input Validation
- Information Disclosure

## Questions for Discussion
1. What security measures does the application implement?
2. Are there any potential bypass techniques?
3. How effective is the path sanitization?
4. What additional security controls could be implemented?

## Deliverables
- Document all findings
- Provide proof-of-concept for any issues discovered
- Suggest remediation strategies

---
*Vienna Hacking Bootcamp - Advanced Web Application Security* 