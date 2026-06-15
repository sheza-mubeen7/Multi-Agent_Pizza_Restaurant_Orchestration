# 🍕 Multi-Agent Pizza Restaurant Orchestration

A lightweight, asynchronous implementation demonstrating the **Multi-Agent Hand-off & Context Routing Pattern** in Agentic AI workflows. 

---

## 🧠 Architectural Workflow & Learning Core

This repository serves as a foundational blueprint for multi-agent delegation frameworks, shifting away from standard monolithic prompts toward an optimized micro-agent layout.

### 👥 Agent Roles
1. **Welcome Agent (`welcome_agent`):** Handles client reception and onboarding. Contains zero menu-level parametric knowledge.
2. **Waiter Agent (`waiter_agent`):** Houses specific inventory data (pizzas, pricing matrices). Operates only upon receiving active handoff routing control.

### 🔄 Multi-Agent Routing Flow

The routing mechanism demonstrates how control passes between specialized agents dynamically based on context requirements:



1. **User Initiation:** User prompts the execution interface (`Runner.run`).
2. **Intent Evaluation:** The orchestration engine triggers the `Welcome Agent` to execute greeting routines.
3. **Dynamic Handoff Protocol:** Upon detecting completion parameters, control natively switches via the `handoffs` array to the `Waiter Agent`, instantly transforming the output generation persona without losing history vectors.

---

## 📂 Project Structure

```text
Multi-Agent-Pizza/
├── main.py             # Asynchronous runner loop and Agent topology definitions
├── tools/              # Core workflow configurations and operational setup
└── README.md           # Implementation blueprint and architecture analysis
