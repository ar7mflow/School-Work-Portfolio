# CISC 322 A2 Team Blueprint (Concrete Architecture Report)

**Date:** February 27, 2026  
**Course:** CISC/CMPE 322 Software Architecture  
**Project:** Gemini CLI  
**Team:** Group 5 — It Compiles (Sometimes)

---

## 1) Goal of A2 (What We Must Deliver)

Recover the **concrete architecture** of Gemini CLI from source code using Understand, then compare it against A1 conceptual architecture and explain divergences with evidence.

**Core idea:**
- A1 = what we thought architecture should be (conceptual)
- A2 = what the code actually is (concrete)
- Reflexion analysis = compare both, explain differences

---

## 2) Rubric-to-Action Checklist (What to Do for Full Marks)

## High-Level Concrete Architecture Diagram
- Produce one box-and-arrow diagram at the right abstraction level.
- Every component and dependency must be explained.
- Link and align with course reference architecture expectations.

## Architecture Derivation Process
- Explicitly show process:
  1. Start from A1 conceptual architecture.
  2. Iteratively map files/folders to components in Understand.
  3. Generate dependency graph.
  4. Refine mapping and justify updates.

## Detailed Subsystem Decomposition
- Pick one subsystem and decompose both:
  - conceptual inner architecture
  - concrete inner architecture
- Include at least 4 sub-components.

## Two Use Cases + Sequence Diagrams
- Two sequence diagrams aligned to concrete architecture.
- Label edges with **concrete method/function calls** (not abstract labels).

## Reflexion Analysis (High Level)
- Compare A1 conceptual vs recovered concrete architecture.
- Identify convergences and divergences.
- Explain divergences with facts, including git-based evidence.

## Reflexion Analysis (Second Level)
- Repeat same comparison process for the chosen subsystem’s internal decomposition.

## Conceptual Architecture Revisit
- Re-present conceptual architecture (about ~10 components total is acceptable range).
- If changed from A1, explain why clearly.

## Lessons Learned
- Specific to Gemini CLI and this team’s process.
- Avoid generic course-level statements.

## Presentation Quality
- Keep labels and naming consistent across all diagrams.
- Use readable Understand screenshots (or redraw cleanly).
- Keep layouts comparable between conceptual and concrete diagrams.

## Report Quality + AI Collaboration
- Strong abstract, clear organization, references, and explained figures.
- Include AI teammate model choice, prompting protocol, quality control, and impact reflection.

---

## 3) Concrete Mapping Starter (A1 Subsystems → Code Areas)

## 1) CLI Frontend
- `packages/cli/src/`
- `commands/`, `core/`, `ui/`, `services/`, `config/`, `utils/`

## 2) Core Backend
- `packages/core/src/core/`
- likely files: `geminiChat.ts`, `contentGenerator.ts`, `turn.ts`, `client.ts`, `prompts.ts`, `coreToolScheduler.ts`

## 3) Tool Execution Layer
- `packages/core/src/tools/`
- includes file tools (`read-file.ts`, `write-file.ts`, `edit.ts`, `glob.ts`, `ls.ts`, `grep.ts`), shell, web tools, memory, todo, registry

## 4) MCP Integration Layer
- tool-side: `packages/core/src/tools/mcp-client.ts`, `mcp-client-manager.ts`, `mcp-tool.ts`
- auth-side: `packages/core/src/mcp/` (OAuth/auth providers)

## 5) Context Manager
- `packages/core/src/prompts/`, `packages/core/src/resources/`, `packages/core/src/config/`

## 6) Safety/Approval Layer
- `packages/core/src/safety/`, `packages/core/src/confirmation-bus/`, `packages/core/src/policy/`

---

## 4) Likely Divergences to Investigate (Strong Candidates)

1. **MCP boundary mismatch**
- Conceptually separate subsystem, but concrete MCP tool execution files are inside `tools/`.

2. **`mcp/` folder role mismatch**
- Mostly authentication/provider code, not full MCP orchestration.

3. **Distributed safety logic**
- Safety concerns split across multiple folders rather than a single clean module.

4. **Distributed context logic**
- Context functionality spread across prompts/resources/config.

5. **Potential cross-layer dependencies**
- Check whether CLI or tools directly depend on internals that bypass intended layering.

---

## 5) Reflexion Analysis Template (Use This in Report)

For each observed relation:

| Relation | In A1 Conceptual? | In Concrete? | Type | Evidence | Interpretation |
|---|---|---|---|---|---|
| A -> B | Yes/No | Yes/No | Convergence/Divergence | Understand graph + code refs + git facts | Why this happened and what it means |

Interpretation guidance:
- If divergence appears accidental or architectural drift: propose refactor.
- If divergence is justified by implementation realities: update conceptual architecture rationale.

---

## 6) Sequence Diagram Upgrade Rules (A1 → A2)

In A2, edge labels must be concrete calls.

Use this style:
- `CLI.processInput()`
- `GeminiChat.sendMessage()`
- `ContentGenerator.generateContent()`
- `ToolRegistry.executeTool()`
- `WriteFileTool.execute()`

Do **not** use labels like “Forward request” or “Execute operation” without concrete method names.

---

## 7) Work Plan (March 1–13)

## Phase A: Recovery (Mar 1–4)
- Open Understand project.
- Build architecture mapping from A1 subsystems.
- Generate first high-level concrete dependency graph.

## Phase B: Analysis (Mar 4–8)
- Identify high-level convergences/divergences.
- Select one subsystem for second-level decomposition.
- Build inner conceptual + concrete diagrams.

## Phase C: Use Cases & Evidence (Mar 7–10)
- Update two sequence diagrams with concrete method calls.
- Collect git evidence to explain major divergences.

## Phase D: Writing & Integration (Mar 10–13)
- Draft final report sections.
- Run consistency pass on names/legends.
- Final screenshot/diagram readability pass.
- Submit before deadline.

---

## 8) Team Task Split (Suggested)

- **Arham:** Understand mapping, diagram pipeline, integration pass
- **Edward:** Derivation narrative + high-level reflexion analysis
- **Junoh:** Sequence diagrams with concrete method calls
- **Faizan:** Subsystem decomposition + second-level reflexion analysis
- **Ajwaad/Brian:** Conceptual revisit, abstract/introduction/conclusion, references
- **All:** AI collaboration section + quality control evidence

---

## 9) Git Evidence Quick Commands

Use these to support divergence explanations:

```bash
git log --oneline -- packages/core/src/tools/
git log --follow --oneline -- packages/core/src/tools/mcp-client.ts
git blame packages/core/src/tools/tool-registry.ts
git log -p -S "import" -- packages/core/src/
```

Use outputs to support statements such as:
- when dependency was introduced
- who introduced it
- whether change aligns with architecture intent

---

## 10) Final Pre-Submission Check

- [ ] High-level concrete diagram included and explained
- [ ] Derivation process clearly documented (A1 -> Understand mapping -> refinement)
- [ ] One subsystem decomposed (conceptual + concrete, >=4 sub-components)
- [ ] Two sequence diagrams included
- [ ] Sequence edges use concrete method/function names
- [ ] Reflexion analysis completed at high level
- [ ] Reflexion analysis completed at second level
- [ ] Divergences supported with evidence (including git where needed)
- [ ] Consistent labels/legends across all visuals
- [ ] Understand screenshots readable
- [ ] References complete and cited
- [ ] AI collaboration section complete with quality control and impact

---

## 11) Key Reminder

A2 is not just “draw concrete diagrams.”
A2 is primarily about proving that we can:
1) recover architecture from code, and
2) critically explain how and why it differs from our conceptual model.

If we execute reflexion analysis rigorously with evidence, this report can score at the top band.
