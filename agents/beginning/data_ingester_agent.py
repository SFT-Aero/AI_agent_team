# Receives and prepares the webscrappers output to be interpreted by agent team
# Makes sure that all downstream agents receive clean, consistent data regardless of source
# This agent will:
    # Standardize categories: ("Tech" → "Technology")
    # Fix dates: parse strings into datetime.date objects or standardized strings
    # Fallbacks: fill missing fields with defaults ('No teaser found')
    # Clean HTML: remove tags from body/teaser fields

from crewai import Agent
