# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked the AI assistant to help me improve the terminal output for the recommender so it would be easier to read and more useful for documentation.

**Prompts used:**

- “Help me format the top recommendations in the terminal as a readable table that includes the score and explanation for each song.”
- “Keep the change simple and make sure it works with the existing recommender output.”

**What did the agent generate or change?**

The assistant suggested a simple ASCII table format and helped structure a helper function in the CLI runner so each recommendation prints as a row with rank, title, score, and explanation.

**What did you verify or fix manually?**

I verified that the table printed correctly in the terminal and made sure the output still matched the existing ranking logic. I also adjusted the formatting so the explanations did not break the layout.

---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

<!-- e.g., Strategy, Factory, Observer, etc. -->

**How did AI help you brainstorm or implement it?**

<!-- Describe the conversation or suggestions that led to your decision -->

**How does the pattern appear in your final code?**

<!-- Point to the relevant class or method -->
