# Arham A2 Presentation Script (CISC 322)

Use this as your exact read-off script while recording.

Total Arham speaking target: 5:45 to 6:05.
If team timing slips, use the compression notes at the end.

---

## Quick Verification (One Final Check)

This script is aligned with:
- A2 presentation rubric requirements: concrete method-call labels, clear conceptual/concrete breakdown, derivation process, reflexion discussion, alternatives, limitations, readability and timing.
- A1 feedback risks: small unreadable figures, unclear methodology, weak alternatives discussion, implicit limitations, going over time.
- Your updated A2 report facts: subsystem names, dependency call chains, orchestration subcomponents, and reflexion points.

If you deliver this clearly and your slides stay readable and on-time, this is scoring-maximized.

---

## Delivery Rules (Read This Before Recording)

1. Speak in short, confident sentences. No rambling.
2. Start each slide with one thesis sentence.
3. Point at diagram arrows when saying method names.
4. Say the word "limitations" explicitly on Slide 13.
5. Keep pace around 135-145 words per minute.
6. Do not improvise new technical claims that are not in your report.
7. End your part by clearly handing off or closing.

Voice style:
- Tone: calm, technical, assertive.
- Emphasis words: "concrete", "method-call evidence", "derived", "validated", "rationale".

---

## Slide 5 Script (Concrete Architecture - High-Level)

### On-slide title
Concrete Architecture from Source Code

### Speak (about 1:20)
Now I will present the concrete architecture recovered directly from the TypeScript source.

We model six top-level subsystems and eight dependency relationships.
The key point is that these arrows are not conceptual guesses. They are tied to concrete method-call pathways in code.

From CLI Frontend to Orchestration Engine, useGeminiStream initiates GeminiClient.sendMessageStream for each conversational turn.

Inside Orchestration, GeminiClient.startChat registers tools through ToolRegistry.getFunctionDeclarations and builds session context using getCoreSystemPrompt with Config.getToolRegistry.

For tool execution, CoreToolScheduler routes calls through PolicyEngine.checkPolicy, then MessageBus.publish for approval flow, and finally ToolExecutor.execute.

Execution then crosses into Tool Execution Layer using tool.execute with params and signal.

Policy decisions also read configuration using Config.getApprovalMode and shell allowlist controls.

So this diagram is high-level by subsystem, but every major dependency shown is concretely grounded.

### How to say it
- Pause slightly after "not conceptual guesses".
- Point at 2-3 arrows while saying exact method names.
- Keep this slide precise, evidence-heavy, no extra stories.

---

## Slide 6 Script (Derivation Process)

### On-slide title
4-Stage Derivation Workflow

### Speak (about 0:55)
This architecture was derived through a four-stage process to avoid guesswork.

Stage one: we started from our A1 conceptual baseline as the initial hypothesis.

Stage two: we imported Gemini CLI into Understand and indexed the relevant source scope.

Stage three: we mapped real folders and files into subsystem clusters and traced dependencies.

Stage four: we resolved mismatches between conceptual intent and concrete implementation, then refined the architecture accordingly.

So our final model is code-derived and iteratively validated, not copied from documentation.

### How to say it
- Count stages on fingers or pointer motion: 1, 2, 3, 4.
- Keep wording crisp and procedural.

---

## Slide 7 Script (2nd-Level Conceptual - Orchestration Engine)

### On-slide title
Orchestration Engine: 2nd-Level Conceptual Breakdown

### Speak (about 0:55)
For second-level analysis, we selected the Orchestration Engine because it coordinates the full Reason-and-Act lifecycle.

Conceptually, this subsystem has four subcomponents.

Session Manager initializes and maintains context across turns.

Turn Executor runs the iterative turn loop and reacts to streamed events.

API Abstraction decouples orchestration logic from provider-specific model backends.

Tool Execution Gate enforces policy and scheduling constraints before tool execution.

This gives a clear responsibility split and prepares a direct conceptual-to-concrete mapping.

### How to say it
- One sentence per subcomponent, equal emphasis.
- Do not rush this slide; clarity is the scoring factor.

---

## Slide 8 Script (2nd-Level Concrete Mapping)

### On-slide title
Orchestration Engine: Concrete Mapping

### Speak (about 1:05)
Here is the concrete mapping from those conceptual blocks to implementation artifacts.

Session Manager maps to GeminiClient in client.ts, where session startup and context assembly are coordinated.

Turn Executor maps to turn.ts with stream progression through GeminiChat.sendMessageStream.

API Abstraction maps to the ContentGenerator interface and implementations, which support backend swaps without rewriting orchestration logic.

Tool Execution Gate maps to coreToolScheduler.ts, which performs policy checking, approval event publishing, and execution handoff.

A critical concrete behavior is serialized tool execution, which avoids unknown side effects between filesystem and shell operations.

So this subsystem is not only decomposed conceptually; it is directly verifiable in concrete code structure.

### How to say it
- Point at table row while reading each row.
- Stress "serialized tool execution" as a key design rationale.

---

## Slide 12 Script (Reflexion - 2nd Level)

### On-slide title
Reflexion Analysis: Orchestration Engine

### Speak (about 0:55)
At subsystem level, we observed one absence and two unexpected implementation characteristics.

Absence: there is no standalone Context Manager module as originally conceptualized.
Context responsibilities are distributed across orchestration and prompt/config artifacts.

Unexpected one: session compression behavior appears as a concrete mechanism with evolved threshold logic.

Unexpected two: a utility-style bypass path exists through generateJson, diverging from a strictly linear conversational pathway.

The reflexion takeaway is that implementation prioritizes modular operational behavior over clean monolithic conceptual boundaries.

### How to say it
- Keep this analytical, not defensive.
- Use "absence" and "unexpected" exactly as rubric language.

---

## Slide 13 Script (Alternatives + Limitations)

### On-slide title
Alternatives Considered and Limitations

### Speak (about 0:35)
We explicitly considered alternatives.

First, a standalone MCP execution subsystem, but the code implements MCP execution as a first-class tool type in a unified tool model.

Second, a monolithic safety module, but concrete code intentionally separates checking, policy, event transport, and execution orchestration.

Third, parallel tool execution, but current architecture prefers serialized execution to reduce side-effect risk.

Limitations: this analysis is primarily static-architecture focused, and runtime behavior across all operational modes is not exhaustively modeled.
Some design intentions are also inferred where explicit historical rationale is limited.

### How to say it
- Say "Limitations" clearly and slowly.
- Keep this section concise and mature.

---

## Optional Handoff Line (If You Need It)

If handing to Brian after Slide 13:
"That completes the concrete derivation and subsystem reflexion with alternatives and limitations; Brian will now close with final synthesis and lessons."

---

## Emergency Compression Version (If Time Is Running Late)

If you must cut to 4:45 total:
- Slide 5: mention only top 4 call chains.
- Slide 8: one line per row, no elaboration.
- Slide 12: one absence plus one unexpected.
- Slide 13: one alternative plus one limitation.

Never cut:
- Derivation stages on Slide 6.
- Explicit limitations statement on Slide 13.

---

## Final Record Checklist (Read Before Hitting Record)

1. Slides readable at full-screen recording resolution.
2. You state concrete method names at least 5 times across Slides 5 and 8.
3. You enumerate all four derivation stages.
4. You explicitly discuss alternatives and why rejected.
5. You explicitly state limitations.
6. You finish your part in <= 6:05.
7. No off-script facts added.

If all 7 are true, your section is rubric-maximized.
