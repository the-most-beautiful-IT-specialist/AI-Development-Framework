# AI Development Framework: Engineering Skeleton v1.0
A professional framework for integrating LLMs into the SDLC with strict API contracts and quality metrics.

This repository presents an **engineering framework** for integrating Large Language Models (LLMs) into the Software Development Life Cycle (SDLC). 

Unlike simple text-based policies, this project provides a concrete "skeleton" — a set of technical API contracts, reusable software modules, and quality control metrics.

---

## 🏗 Architecture and Data Flow (SDLC Workflow)

The framework divides the development process into 4 controlled phases. At each stage, the developer is provided with a specific tool:

| Phase | Framework Tool | Expected Outcome |
| :--- | :--- | :--- |
| **1. Requirements** | "The 6 Critical Questions" | Risk assessment and AI viability evaluation |
| **2. Design** | API Contract Templates | Strict JSON schemas (hallucination prevention) |
| **3. Implementation** | Human-in-the-loop Wrapper | Code with built-in human validation requirements |
| **4. Testing** | Manual Fix Rate Calculator | Quantitative assessment of AI performance |

---

## 🛠 Technical Components (Core Modules)

Reusable software components are implemented in the `/src` directory:

1. **`llm_client.py`**: A universal client for OpenAI and Anthropic API. Enforces strict data contracts to prevent unstructured outputs.
2. **`metrics_calculator.py`**: A tool for calculating code generation efficiency based on Prof. Shlomo Mark's methodology.

### Example of a Strict API Contract (JSON):
The framework guarantees that the AI returns data exactly in the requested format, allowing for safe integration into production code:
```json
{
  "tasks": [
    { "title": "Setup OAuth", "hours": 2 },
    { "title": "Database Schema", "hours": 3 }
  ]
}

## 📈 Quality Metrics (AI Specific Metrics)

The central element of quality control in this framework is the **Manual Fix Rate (MFR)**.

**Formula:** `MFR = (Number of manually fixed lines / Total number of AI-generated lines) * 100%`

* **Green Zone (<15%):** Prompt and model are working effectively.
* **Yellow Zone (15-30%):** Prompt refactoring is required (add context).
* **Red Zone (>30%):** Using AI is inefficient. Architecture redesign is required.

## 🚀 Quick Start

To see the framework in action, run the demonstration script (converting a User Story into technical tasks):

```bash
python examples/story_to_tasks.py
```

### Input-Output Logic Example:
* **Input (User):** "As a user, I want to reset my password via email."
* **Process:** Executing `get_strict_json()` through our framework wrapper.
* **Output:** A structured JSON array of technical tasks for Jira/Trello.


## 📝 Why is this a "Framework" and not a "Document"?

1. **It is reusable code:** Developers import classes from `src/` instead of writing API calls from scratch.
2. **It is a methodology:** The framework enforces a secure SDLC structure through specific steps and Guardrails.
3. **It is scalable:** New models (e.g., Llama, Gemini) can be easily integrated without changing the core application logic.
