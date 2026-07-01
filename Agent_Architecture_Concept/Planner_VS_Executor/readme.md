# Planner vs Executor in AI Agents

## Overview

In agent systems, Planner and Executor are two different
responsibilities.

A Planner decides **what needs to be done** and creates a strategy.

An Executor performs **the actual actions** required to complete the
plan.

------------------------------------------------------------------------

# Planner

## Definition

A Planner is responsible for reasoning, breaking complex tasks into
smaller steps, and creating an execution strategy.

The Planner focuses on:

-   Understanding user goals
-   Creating task plans
-   Deciding the sequence of actions
-   Selecting required tools or agents

------------------------------------------------------------------------

## Planner Responsibilities

-   Analyze the user request
-   Decompose large tasks into smaller tasks
-   Decide the order of operations
-   Create a plan for execution
-   Handle dependencies between tasks

------------------------------------------------------------------------

## Planner Flow

    User Request
          |
          ↓
    Planner
          |
          ↓
    Task Plan
          |
          ↓
    Executor

------------------------------------------------------------------------

# Executor

## Definition

An Executor is responsible for carrying out the plan created by the
Planner.

The Executor focuses on:

-   Running actions
-   Calling tools
-   Executing tasks
-   Returning results

------------------------------------------------------------------------

## Executor Responsibilities

-   Execute planned steps
-   Use available tools
-   Communicate with external systems
-   Handle tool results
-   Report completion

------------------------------------------------------------------------

## Executor Flow

    Task Plan
         |
         ↓
    Executor
         |
         ↓
    Tools / APIs / Actions
         |
         ↓
    Final Result

------------------------------------------------------------------------

# Planner vs Executor Comparison

  Feature          Planner                  Executor
  ---------------- ------------------------ -------------------
  Main purpose     Create strategy          Perform actions
  Focus            Reasoning and planning   Execution
  Output           Task plan                Completed result
  Responsibility   Decide what to do        Do the work
  Uses tools       Usually selects tools    Executes tools
  Handles          Complex decisions        Actual operations

------------------------------------------------------------------------

# Single Agent vs Planner-Executor Architecture

## Single Agent

One agent handles:

-   Planning
-   Reasoning
-   Tool usage
-   Execution

Simple but can become difficult for complex workflows.

------------------------------------------------------------------------

## Planner-Executor System

Multiple specialized responsibilities:

    User
     |
     ↓
    Planner Agent
     |
     ↓
    Execution Plan
     |
     ↓
    Executor Agent
     |
     ↓
    Tools
     |
     ↓
    Result

Advantages:

-   Better organization
-   Easier debugging
-   More control
-   Suitable for complex tasks

------------------------------------------------------------------------

# When to Use Planner-Executor Pattern

Use this architecture when:

-   Tasks have multiple steps
-   Workflows are complex
-   Different tools are required
-   Reliability is important
-   You need better control over agent behavior

------------------------------------------------------------------------

# Interview Answer

Planner-Executor architecture separates decision-making from execution.
The Planner agent analyzes the user request and creates a step-by-step
plan, while the Executor agent performs those steps using tools and
external systems. This separation improves reliability, scalability, and
control in complex AI agent workflows.

------------------------------------------------------------------------

# Summary

    Planner
     |
     |-- Understand goal
     |-- Break task into steps
     |-- Create plan
     |
     ↓

    Executor
     |
     |-- Execute steps
     |-- Call tools
     |-- Produce result
