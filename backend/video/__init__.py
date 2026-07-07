"""
FlowMind Video Agent
Generates short videos from a text prompt using Google's Veo model
(via the Gemini API). Requires GEMINI_API_KEY in .env.

Video generation is a long-running operation on Google's side (it can
take a couple of minutes), so this polls until the job finishes rather
than returning immediately.
"""
