"""
FlowMind Deployment Agent
Pulls the latest code from GitHub and installs dependencies on the
server FlowMind is running on. Restricted to a fixed, whitelisted set
of commands — it does not execute arbitrary shell input from chat
messages, for safety.
"""
