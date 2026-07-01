# OpenAI Agents SDK Practice - Troubleshooting Notes

This file records the main test cases, the failures we encountered, and the reasons behind them while making the OpenAI Agents SDK example work.

## What was tested

1. Running the sample from the agents folder.
2. Running the sample from the worker folder.
3. Using the default OpenAI client path with no API credentials.
4. Using the Gemini-style OpenAI-compatible endpoint with a project .env file.
5. Running the script with Python 3.11 and then with Python 3.12.

## Main failures and reasons

### 1. ImportError: cannot import name AsyncOpenAI from openai
Reason:
- The installed OpenAI client package was not compatible with the SDK import pattern being used.
- This happened because the environment had a mismatched package combination.

Fix:
- Use a compatible SDK/runtime combination.
- In this project, Python 3.12 with the installed OpenAI Agents SDK and OpenAI client worked correctly.

### 2. KeyError: ~TContext while importing agents
Reason:
- This was caused by a deeper incompatibility in the installed SDK package under the earlier Python/runtime setup.
- In simple terms, the package version and Python typing behavior were not aligned.

Fix:
- Switch to Python 3.12 for the project.
- Use the SDK version already installed in that interpreter.

### 3. Missing credentials error
Error:
- openai.OpenAIError: Missing credentials

Reason:
- The agent was trying to use the default OpenAI credentials path.
- The project .env file was not being loaded from the expected location.

Fix:
- Load the environment variables from the project config folder.
- Use the Gemini API key from the project .env file.
- Configure the model client with the Gemini-compatible base URL.

### 4. The script was not using the configured model
Reason:
- The sample agent was created without explicitly attaching the configured model object.

Fix:
- Attach the configured model from config/sdk_client.py to the Agent instance.

## Final working setup

### Recommended interpreter
- Use Python 3.12

### Required packages
- openai-agents 0.17.7
- openai 2.44.0

### Environment file
- Place the API key in config/.env
- Example:
  - GEMINI_API_KEY=your_key_here

### Run command
From the project folder:

```powershell
py -3.12 .\worker\main.py
```

## Summary
The project started working once these three things were fixed:
1. The correct Python version was used.
2. The SDK and client package combination was aligned.
3. The Gemini API key was loaded from the project .env file and attached to the agent model.
