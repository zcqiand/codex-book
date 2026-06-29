---
name: pr-review
description: Review a PR branch for security risks, test coverage gaps, and maintainability issues. Trigger when the user asks for a structured code review.
---

Instructions

1. Check out the PR branch and run `git diff main...HEAD --stat`
2. For each changed file, assess: security, test coverage, maintainability
3. Output findings as a three-section report with severity labels