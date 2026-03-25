# A2 Final Pack (95 Plus Marker Proof)

Group: It Compiles (Sometimes)
Course: CISC 322/CISC 326 Software Architecture
Deliverable: A2 Presentation (marker #2)
Date: March 13, 2026

## 1) Locked Runtime Plan (Safe Under 10.5)

Target total runtime: 10:20 (safe buffer below 10.5)
Hard stop rule: if timer hits 10:00 on slide 13, move to slide 14 immediately.

Slide timing and speaker split:

1. Slide 1 - Brian - 0:15
2. Slide 2 - Brian - 0:20
3. Slide 3 - Brian - 0:45
4. Slide 4 - Brian - 0:35
5. Slide 5 - Arham - 1:05
6. Slide 6 - Arham - 0:50
7. Slide 7 - Arham - 0:50
8. Slide 8 - Arham - 1:00
9. Slide 9 - Brian - 0:35
10. Slide 10 - Brian - 0:35
11. Slide 11 - Brian - 0:35
12. Slide 12 - Arham - 1:00
13. Slide 13 - Arham - 0:45
14. Slide 14 - Brian - 0:25

Spoken subtotal: 9:50
Handoff and transition buffer: ~0:30
Final target: ~10:20

Arham subtotal: 5:30 spoken, typically ~5:45 with natural pacing.
Brian subtotal: 4:20 spoken, typically ~4:35 with natural pacing.

## 2) Marker-Critical Non-Negotiables

Say these out loud, do not leave them only on slides:

1. Every key architecture and sequence edge must be spoken with concrete method names.
2. Derivation must be explained as a reproducible 4-stage process.
3. No diagram appears from nowhere: name source and reasoning before reading it.
4. Alternatives must be explicit and each must include why rejected.
5. Limitations must be explicit and audible.
6. Divergence rationale must reference facts from code history or repository evidence.
7. Keep readable visuals (large text, low density, zoom-safe screenshots).
8. Stay under 10.5 minutes.

## 3) Slide-by-Slide Final Content and Script

## Slide 1 - Title and Thesis (Brian, 0:15)

Put on slide:
- Title: Gemini CLI Concrete Architecture Recovery
- One sentence thesis:
  We recovered Gemini CLI concrete architecture from source code, validated it with tool-based evidence, and explained major divergences from A1.

Say:
- We recovered Gemini CLI concrete architecture from source code, validated it with evidence from analysis tools and file-level inspection, and explained every major divergence from our A1 conceptual model.

## Slide 2 - Why A2 Matters (Brian, 0:20)

Put on slide:
- A1 = conceptual intent
- A2 = concrete reality from code
- Goal = explain mismatch patterns and architectural evolution

Say:
- A1 captured intent. A2 proves what actually exists in code. Our focus is not just mapping modules, but explaining why conceptual and concrete structures differ.

## Slide 3 - Updated Conceptual Architecture (Brian, 0:45)

Put on slide:
- 6 subsystems with one short role each
- One line labeled A1 to A2 update rationale:
  safety became pipeline, MCP execution moved into tools, context flow clarified

Say:
- Here is the updated conceptual architecture with six subsystems and explicit roles.
- Compared to A1, we made three motivated updates: safety is treated as a pipeline, MCP execution is modeled in the tool layer, and context flow is clarified around prompt and config assembly.

## Slide 4 - Changes from A1 (Brian, 0:35)

Put on slide:
- Before/After table, 3 rows:
  - MCP subsystem -> MCP execution inside tool registry model
  - Single safety block -> distributed policy, confirmation, scheduler, checkers
  - Implicit context manager -> distributed context assembly

Say:
- These are the three concrete architecture updates from A1, each motivated by source structure and dependency tracing.
- Handoff: Arham will now show the concrete code-backed architecture and derivation method.

## Slide 5 - High-Level Concrete Architecture (Arham, 1:05)

Put on slide:
- 6 subsystem box-and-arrow diagram
- 8 dependencies with compact call labels:
  - useGeminiStream -> GeminiClient.sendMessageStream
  - GeminiClient.startChat -> ToolRegistry.getFunctionDeclarations
  - GeminiClient.startChat -> getCoreSystemPrompt, Config.getToolRegistry
  - CoreToolScheduler -> PolicyEngine.checkPolicy -> MessageBus.publish -> ToolExecutor.execute
  - ToolExecutor.execute -> tool.execute(params, signal)
  - PolicyEngine.checkPolicy -> Config.getApprovalMode and shell allowlist

Say:
- This concrete architecture is recovered directly from the TypeScript codebase.
- We model six top-level subsystems and eight dependencies.
- Each arrow is concrete, not abstract. For example, CLI to Orchestration is useGeminiStream invoking GeminiClient.sendMessageStream.
- Orchestration to tools is startChat invoking ToolRegistry.getFunctionDeclarations.
- Orchestration to context is startChat invoking getCoreSystemPrompt and Config.getToolRegistry.
- Tool calls are gated through PolicyEngine.checkPolicy, then MessageBus.publish, then ToolExecutor.execute.
- Execution crosses to implementations through tool.execute with params and signal.
- Policy reads Config.getApprovalMode and shell allowlist state.
- So this is subsystem-level architecture with function-level evidence on every key dependency.

## Slide 6 - Derivation Method (Arham, 0:50)

Put on slide:
- 4-stage workflow:
  1) A1 baseline
  2) import and index in Understand
  3) map folders/files to subsystem clusters
  4) resolve mismatches and refine
- Footer: iterative mapping plus manual code verification

Say:
- To avoid guesswork, we used a four-stage derivation workflow.
- Stage one: start from A1 conceptual architecture as hypothesis.
- Stage two: import and index source in Understand.
- Stage three: map folders and files to subsystem clusters and trace dependencies.
- Stage four: identify mismatches and refine architecture.
- This is reproducible and evidence-driven, not copied from documentation.

## Slide 7 - 2nd-Level Conceptual Subsystem (Arham, 0:50)

Put on slide:
- Title: Orchestration Engine as 2nd-Level Focus
- 4 subcomponents:
  - Session Manager
  - Turn Executor
  - API Abstraction
  - Tool Execution Gate
- Rationale line: chosen because it coordinates full reason-and-act lifecycle

Say:
- We selected Orchestration Engine for second-level analysis because it coordinates the full lifecycle.
- Session Manager maintains and prepares chat context.
- Turn Executor runs iterative turn progression.
- API Abstraction isolates provider-specific model calls.
- Tool Execution Gate enforces policy and scheduling constraints before execution.

## Slide 8 - 2nd-Level Concrete Mapping (Arham, 1:00)

Put on slide:
- 3-column table: Subcomponent | Concrete artifacts | Responsibility
- Mappings:
  - Session Manager | GeminiClient in client.ts | start, reset, compression flow
  - Turn Executor | turn.ts plus GeminiChat.sendMessageStream | event loop and tool requests
  - API Abstraction | ContentGenerator interface plus implementations | backend swap with stable contract
  - Tool Execution Gate | coreToolScheduler.ts with ToolExecutor delegate | policy-check, publish, execute, serialized calls

Say:
- This table maps conceptual subcomponents to concrete artifacts.
- Session Manager maps to GeminiClient in client.ts.
- Turn Executor maps to turn.ts and stream handling via GeminiChat.sendMessageStream.
- API Abstraction maps to ContentGenerator and implementations.
- Tool Execution Gate maps to CoreToolScheduler with delegation to ToolExecutor.
- Tool calls are serialized to avoid unknown side effects across filesystem and shell operations.

## Slide 9 - Use Case 1 Sequence (Brian, 0:35)

Put on slide:
- Sequence with concrete calls only:
  shouldConfirmExecute -> checkPolicy -> publish -> execute
- Components in sequence must match concrete architecture boxes

Say:
- Use Case 1 traces file and shell execution with concrete calls: shouldConfirmExecute, checkPolicy, publish, and execute.
- The sequence boundaries align exactly with the concrete subsystem model shown earlier.

## Slide 10 - Use Case 2 Sequence (Brian, 0:35)

Put on slide:
- Sequence with concrete calls only:
  sendMessageStream -> Turn processing -> ToolCallRequest scheduling -> execution return path

Say:
- Use Case 2 traces web-search and todo flow through sendMessageStream, turn processing, tool-call scheduling, and response return.
- Again, sequence participants and edges match the concrete subsystem decomposition.

## Slide 11 - Reflexion High-Level (Brian, 0:35)

Put on slide:
- Divergences:
  - MCP in tools
  - distributed safety pipeline
  - UI scheduler hooks
- Convergences:
  - CLI/Core boundary holds
  - tool grouping largely preserved

Say:
- High-level reflexion found three divergences and two convergences.
- The key result is that architecture evolution is structured, not accidental, and can be explained with concrete evidence.

## Slide 12 - Reflexion 2nd-Level with Rationale (Arham, 1:00)

Put on slide:
- Absence: no standalone context-manager module
- Unexpecteds:
  - tryCompressChat threshold behavior and evolution
  - utility bypass path through generateJson
- Evidence line: rationale grounded in repository history and code-level inspection

Say:
- At second level, we observed one absence and two unexpecteds.
- Absence: no standalone context manager class; context assembly is distributed.
- Unexpected one: compression behavior includes explicit threshold-driven handling.
- Unexpected two: generateJson introduces a utility bypass path diverging from a strictly linear conversational pipeline.
- Reflexion conclusion: implementation prioritizes modular flexibility over cleaner single-module boundaries from the original conceptual view.

## Slide 13 - Alternatives and Limitations (Arham, 0:45)

Put on slide:
- Alternatives considered and rejected:
  - standalone MCP execution subsystem -> rejected due to unified tool registry implementation
  - monolithic safety module -> rejected due to split responsibilities for maintainability
  - parallel tool execution -> rejected due to side-effect risk
- Limitations:
  - analysis is primarily static-architecture focused
  - runtime variation not exhaustively modeled
  - strongest rationale for major divergences, weaker for some internal intent

Say:
- We explicitly considered three alternatives and rejected each based on concrete implementation tradeoffs.
- Limitation one: this analysis emphasizes static architecture over exhaustive runtime profiling.
- Limitation two: historical rationale is strongest for major divergences and weaker for some internal design intentions.

## Slide 14 - Lessons and Final Takeaway (Brian, 0:25)

Put on slide:
- Lessons tied to your method and this system
- One-sentence close

Say:
- Our key lesson is that architecture quality improves when conceptual models are continuously reconciled with concrete evidence.
- Final takeaway: the recovered architecture is reproducible, code-grounded, and explains both what exists and why it evolved.

## 4) AI Teammate Criteria Shield (High-Risk Rubric Fix)

Add one micro-block to slide 6 or 12 footer and say in 15 to 20 seconds:

Put on slide:
- AI workflow protocol:
  - model selection reason
  - task split and verification loop
  - quantitative impact summary

Say:
- We used an explicit AI protocol: model chosen for code-structure extraction, task-split by artifact type, and human verification at each stage.
- Quantitatively, AI accelerated first-pass extraction while all final architecture claims were human-validated against source files and dependency traces.

If asked for numbers in Q and A, provide your actual values only.
Do not invent metrics.

## 5) Readability and Delivery Rules

1. Minimum 28 to 32 pt body text on architecture slides.
2. Maximum 8 lines per text block.
3. Diagram labels must remain readable at back-row distance.
4. No screenshot where text is not readable when projected.
5. Speak one sentence explaining source and intent before each technical figure.

## 6) Website Criterion Closure Checklist

Before submission, website must include:

1. A2 slide deck and A2 report.
2. At least one additional maintained background artifact (method notes, architecture mapping notes, or supporting references).
3. Brief update note showing current A2 cycle maintenance.

Do not leave website at A2-only state if you want max score safety.

## 7) Rehearsal Protocol (Fast, Reliable)

Run this exactly:

1. One full run at normal speed with timer.
2. One run at 0.9x speed focusing on clear transitions and call names.
3. Final run with hard time cuts at slide 13 if timer exceeds 10:00.

Pass criteria:

1. Runtime <= 10:25
2. All major edges spoken with concrete methods
3. Derivation stages spoken in order without hesitation
4. Alternatives and limitations both spoken explicitly

## 8) Marker-Facing Self-Check Grid (Go/No-Go)

Mark each item Pass before final recording:

1. Sequence diagrams exist and match concrete architecture.
2. Sequence edges use concrete method names.
3. Updated conceptual architecture includes explicit A1 update rationale.
4. High-level concrete architecture has clear decomposition and dependencies.
5. One 2nd-level subsystem includes conceptual and concrete mapping with >= 4 subcomponents.
6. Reflexion includes high-level and 2nd-level divergences.
7. Divergence rationale is fact-based (history or code evidence).
8. Derivation method is explicit, logical, and reproducible.
9. Alternatives discussed with rejection rationale.
10. Limitations spoken clearly.
11. Figures readable.
12. Runtime below 10.5.
13. Website includes A2 deliverables and maintained extra material.
14. AI teammate process and impact clearly and honestly explained.

If any item is No-Go, fix before final recording.

## 9) Emergency Cut Plan (If Time Runs Long)

If behind time, cut in this order:

1. Slide 2 to 0:12
2. Slide 11 to 0:25
3. Slide 14 to 0:15

Never cut:

1. Slide 6 derivation stages
2. Slide 5 concrete call evidence
3. Slide 13 alternatives plus limitations

## 10) Final One-Line Closing to Use

We did not just redraw architecture; we reconstructed it from source evidence, validated it against concrete calls and sequences, and explained exactly where and why reality diverged from our A1 model.
