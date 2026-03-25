# CISC 322/326 — QUIZ 1 ULTIMATE STUDY GUIDE (Winter 2026)

## EXAM LOGISTICS (from your slides)
- **Format:** In-person, closed-book
- **Cheat sheet:** ONE 2-sided letter-size (8.5"x11")
- **Duration:** ~120 minutes
- **Coverage:** onQ material Weeks 1–3 in detail + design exercises (Weeks 4/5) + UML tutorial
- **EXCLUDED (per Quiz1Revision slide):** Interpreter and Process-Control patterns (if not yet covered in class — confirm this!)
- **Structure:** 100 marks total = Q1 Short Answers (50) + Q2 Design Exercise (50)

---

## PATTERN ANALYSIS: WHAT WILL BE ON YOUR QUIZ

I analyzed **3 past quizzes** (F2018, W2021, W2023). Here's the guaranteed pattern:

### QUIZ STRUCTURE (100% consistent across all 3 years):

| Section | Marks | What It Is |
|---------|-------|------------|
| **Q1: Short Answers** | **50** | 3-5 sub-questions testing theory, definitions, true/false with explanation, NFRs, views, styles |
| **Q2: Design Exercise** | **50** | A real-world system scenario where you design its architecture from scratch |

### Q1 SHORT ANSWERS — What Gets Asked Every Time:

| Topic | F2018 | W2021 | W2023 | **Prediction** |
|-------|-------|-------|-------|----------------|
| NFR identification & explanation | ✅ (8 marks) | ✅ (10 marks) | ✅ (15 marks) | **100% — WILL appear** |
| True/False with explanation | ✅ (18 marks) | ✅ (10 marks) | ✅ (15 marks) | **100% — WILL appear** |
| Architecture vs Design / definitions | ✅ (8 marks) | — | — | 50% chance |
| Stakeholder vs User | ✅ (8 marks) | ✅ (part of req.) | — | 60% chance |
| Good Requirements criteria | ✅ (8 marks) | — | — | 40% chance |
| Waterfall / dev process | ✅ (8 marks) | — | — | 30% chance |
| Triple constraints (scope/time/cost) | ✅ (18 marks) | — | — | 30% chance |
| Architectural Views matching | — | ✅ (5 marks) | ✅ (15 marks) | **90% — Very likely** |
| Style comparison (pros/cons for scenario) | — | ✅ (10 marks) | ✅ (5 marks) | **80% — Very likely** |
| Conceptual vs Concrete architecture | — | ✅ (true/false) | — | 50% chance |

### Q2 DESIGN EXERCISE — Exact Same Format Every Time (50 marks):

You get a **real-world system description** + a **specific use case**. Then:

| Sub-question | Marks | What to do |
|--------------|-------|------------|
| 2.1 NFRs | **5** | Give 2 non-functional requirements with CONCRETE examples for this system |
| 2.2 Style selection | **10** | Pick 1-2 architectural styles, explain WHY they fit this system's NFRs |
| 2.3 Sequence diagram | **15** | Draw sequence diagram for the given use case |
| 2.4 Boxes-and-arrows | **20** | Draw conceptual architecture, explain each component, map to styles |

**Past scenarios:** Web Grocer (F2018), Video Editor (W2021), clangd/LSP (W2023)  
**Prediction for W2026:** Could be any system — social media app, streaming service, game engine, smart home, ride-sharing, healthcare, etc.

---

## SECTION 1: THE BIG PICTURE — WHAT IS SOFTWARE ARCHITECTURE?

### Definition
> "The software architecture of a system is the structure(s) of the system, comprising software components, their externally visible properties, and the relationships between them."

### Architecture ≠ Design (4 Key Differences — asked directly in F2018!)
| Architecture | Design |
|-------------|--------|
| High-level structure (components, connectors) | Low-level details (classes, methods, algorithms) |
| Focuses on NFRs (quality attributes) | Focuses on functional requirements |
| Hard/expensive to change later | Easier to change |
| Multiple views of the system | Single detailed blueprint |

### Why Architecture Matters
1. **Communication** among stakeholders (customers, managers, devs)
2. **Documentation** of early design decisions (constrains implementation)
3. **Reuse** — transferable abstraction to similar systems

### System Perspective Diagram
- Shows the **boundary** of your system
- Shows **external entities** that interact with your system
- Shows **connections** between external entities and your system
- Example: Online Flower Shop → Azure cloud (environment), customer, PayPal, Twitter, parent company

---

## SECTION 2: REQUIREMENTS (MODULE 2) — HIGH PRIORITY

### Functional Requirements (FR)
- WHAT the system should do
- Examples: "User can create a document", "System processes payments"

### Non-Functional Requirements (NFR) / Quality Attributes — THE MOST TESTED TOPIC

#### Performance NFRs:
| NFR | Definition | Example |
|-----|-----------|---------|
| **Response Time** | How fast system responds to a request | "Page loads in < 2 seconds" |
| **Throughput** | Amount of work per unit time | "Process 1000 transactions/sec" — BUT must specify average vs. peak! |
| **Deadline** | Hard time constraint | "Stock trade must execute within 100ms" |
| **Request Load** | How many concurrent users/requests | "Support 10,000 simultaneous users" |

#### Scalability NFRs (HEAVILY TESTED — W2023 ChatGPT question!):
| Approach | What It Is |
|----------|-----------|
| **Scale Up** (vertical) | Use a more powerful server |
| **Scale Out** (horizontal) | Add more servers |
| **Key insight:** For massive user loads (like ChatGPT), scaling OUT is better because even the most powerful single server will eventually max out |

#### Security NFRs:
| NFR | Definition |
|-----|-----------|
| **Authentication** | Verifying identity (WHO are you?) |
| **Authorization** | Verifying permissions (WHAT can you do?) — these are DIFFERENT! |
| **Non-repudiation** | Cannot deny an action (e.g., placing an order is a commitment) |
| **Encryption** | Protecting data (HTTPS, etc.) |

#### Other NFRs:
- **Availability** — system uptime
- **Usability** — ease of use
- **Modifiability** — how easily you can change the system
- **Portability** — runs on different platforms

### CRITICAL NFR Rules (these come up as True/False):
1. **NFRs can CONTRADICT each other** (e.g., stronger encryption → slower response time)
2. **You can't focus on ALL NFRs equally** — too expensive + contradictions
3. **NFRs must be PRECISE** — "process $5,000/sec" is BAD because it doesn't specify average vs. peak
4. **NFRs should be: verifiable, traceable, ranked for importance, ranked for stability**

### Stakeholder vs. User (asked in F2018!)
- **Stakeholder** = anyone with interest in the system (users, developers, managers, regulators, etc.)
- **User** = a SUBSET of stakeholders — only those who directly USE the system
- All users are stakeholders, but NOT all stakeholders are users

### "Environment" of a System
- Encompasses ALL factors impacting a system — both **technical** (cloud, hardware, OS) AND **non-technical** (policies, regulations, business rules)
- This was a True/False in W2023 — answer is TRUE

---

## SECTION 3: ARCHITECTURAL VIEWS — HIGH PRIORITY

### Rozanski & Woods' 6 Viewpoints:

| View | What It Captures | Keywords to Identify |
|------|-----------------|---------------------|
| **Functional** | Components, responsibilities, interactions, dependencies between components | "component should not directly depend on...", "shielding", subsystem responsibilities |
| **Information** | Static data structures, information flow | "valid telephone number", data formats, database schema |
| **Concurrency** | Concurrent processes, coordination, synchronization | Thread management, parallel processing, async operations |
| **Development** | Code organization, build, testing tools | Source code structure, file naming conventions, Git, CI/CD tools, BDD tools like Cucumber |
| **Deployment** | Physical machines, network topology, where things run | "hosted on different machine", servers, physical separation, tiers |
| **Operational** | Runtime management, upgrades, monitoring | "graceful restart", release strategy, KPIs, version transitions |

### KEY EXAM QUESTIONS — Match the statement to the view:
- "Database on different machine than app server" → **Deployment** (or Information)
- "nginx graceful restart" → **Operational**
- "Valid telephone number for every customer" → **Information**
- "Use Cucumber for acceptance testing" → **Development**
- "Client GUI should not directly depend on database" → **Functional**
- "System has 3 tiers" → **Deployment**
- "Dispatch component sends async messages to queue" → **Functional** (describes component interaction)
- "C++ classes should have header/implementation files" → **Development**
- "Opening braces coding convention" → **Development**
- "Weekly encrypted data dump" → **Operational**

### Views & NFRs Relationship:
- NFRs are described by **perspectives** which **crosscut** views
- Each perspective addresses different quality concerns across multiple views
- You need ALL of Functional + Information + Concurrency to cover "Software Structure" (NOT just one — this was a True/False in W2023!)

### Layers vs. Tiers (TESTED in W2023!):
- **Layer** = LOGICAL partition of functionality at different abstraction levels
- **Tier** = PHYSICAL partition across different servers/machines
- **YES, you CAN have 3 layers and 1 tier** (all layers on one machine) — TRUE

---

## SECTION 4: ARCHITECTURAL STYLES — THE CORE OF THE COURSE

### Style Overview Table (PUT THIS ON YOUR CHEAT SHEET):

| Style | Components | Connectors | Best For | Advantages | Disadvantages |
|-------|-----------|------------|----------|------------|---------------|
| **Repository** | Central data store + independent operators | Procedure calls, memory access | Complex shared data (IDEs, compilers, AI) | Efficient storage, sharing via schema, centralized mgmt | Must agree on schema upfront, hard to distribute, evolution expensive |
| **Pipe & Filter** | Filters (transformers) | Pipes (data streams) | Sequential data processing (compilers, Unix) | Easy composition, reuse, maintenance, supports concurrency | Bad for interactive systems, parsing overhead |
| **Object-Oriented** | Objects (encapsulated data+ops) | Method invocations | Data protection, modularity | Hidden representation, autonomous agents | Must know other object's identity, side effects |
| **Pub-Sub (Implicit Invocation)** | Event announcers/listeners | Event bus/broadcast system | Loose coupling, plugins, notifications | Strong reuse, easy evolution | No control over response order, can't rely on responses |
| **Layered** | Layer groups of procedures | Procedure calls (restricted visibility) | Hierarchical services (OS, networks, web apps) | Abstraction levels, easy enhancement/reuse | Not all systems fit, performance concerns |
| **Client-Server** | Clients + Servers | Network | Distributed systems | Easy distribution, transparent location, heterogeneous | Network dependent, complex design |
| **Peer-to-Peer** | Peers (both client & server) | Direct network connections | Decentralized (file sharing, games) | No single point of failure, resilient, scalable | Cliques disconnect, need peer lists, no guaranteed response |
| **Interpreter** | Execution engine + memories | Procedure calls, memory access | Virtual machines, scripting | Hardware simulation, portability | Complex to implement, slower execution |
| **Process-Control** | Process + Controller + Sensors | Data flow | Real-time control (cruise control, nuclear) | Continuous feedback | Highly specialized |

### CRITICAL Style Knowledge (True/False favorites):

1. **Implicit invocation (pub-sub):** Components DON'T know each other's identities → OPPOSITE of OO style where you MUST know the target object's identity. **TRUE** (W2023)

2. **Pipe & Filter invariants:** Filters DON'T share state, DON'T know identity of upstream/downstream filters

3. **Repository = "Blackboard"** when multiple clients collaborate, accessing/processing/updating data for others

4. **MVC is NOT an architectural style** — it's a DESIGN PATTERN used within the presentation LAYER of a layered architecture

5. **Compiler architecture evolution:** Started as Pipeline (1970s) → added Symbol Table → added Parse Tree (Repository) → now HYBRID (repository + pipeline elements)

### When to Recommend Which Style (EXAM PATTERN):

| Scenario | Recommended Style(s) | Reasoning |
|----------|---------------------|-----------|
| Web application (typical CRUD) | Client-Server + Layered | Users access central server, logic separated into layers |
| IDE / complex editor | Repository | Central AST/data model with many operations on it |
| Unix command-line data processing | Pipe & Filter | Sequential independent transformations |
| Game with multiplayer | Client-Server (or P2P for some aspects) | Central game server for consistency |
| Notification/event system | Pub-Sub | Loose coupling, dynamic subscribers |
| Small web app (lawn care) | Client-Server + Layered | NOT repository (overkill!), NOT pub-sub for main functionality |
| Video editor | Pipe & Filter + Repository | Batch processing pipeline + central media repository |
| Language server (clangd/LSP) | Client-Server + Repository | Client IDE contacts server, server manages AST repository |

---

## SECTION 5: UML DIAGRAMS — ESSENTIAL FOR 35 MARKS ON THE QUIZ

### Sequence Diagrams (THE most important — 15 marks on Q2!)

**Rules:**
- Maps 1-to-1 to ONE use case
- Read top-to-bottom = time flows downward
- **Elements:**
  - Actor (stick figure) — external entity
  - Object/Component (rectangle) — part of the system
  - Lifeline (dashed vertical line) — existence over time
  - Activation box (thin rectangle on lifeline) — active processing
  - Solid arrow → synchronous call (waits for reply)
  - Dashed arrow ← reply/return
  - Use `alt` box for conditional flow (if/else)
  - Use `loop` box for repeated actions

**How to draw one for the exam (step by step):**
1. Start with the Actor on the left
2. Identify the UI/entry point component
3. Walk through the use case step by step
4. Each "action" becomes an arrow between components
5. Include alt blocks for success/failure paths
6. End with the result going back to the Actor

**Example grading criteria (from W2023 marking scheme):**
- /3 for it being a valid sequence diagram (vertical elements, arrows, readable)
- /6 for having the right components with right responsibilities
- /6 for correct flows/interactions

### Boxes-and-Arrows Diagrams (20 marks on Q2!)

**Rules:**
- Boxes = components (subsystems)
- Arrows = dependencies/interactions (UNI-DIRECTIONAL, never bidirectional!)
- If A calls B in your sequence diagram → there MUST be an arrow from A to B
- Label each box with its purpose
- Show which components belong to which architectural style
- Include the client/external actor

**Grading criteria (from W2023):**
- /7 for having all components from sequence diagram + client
- /7 for having arrows matching all invocations in sequence diagram
- /6 for mapping components to chosen architectural styles

### Use Case Diagrams (may appear in short answers)

- System boundary (rectangle), Actors (stick figures), Use Cases (ovals)
- `<<include>>` = mandatory sub-use-case (always happens)
- `<<extend>>` = optional sub-use-case (sometimes happens)
- Primary actor (left) initiates, Secondary actor (right) reacts

---

## SECTION 6: CONCEPTUAL vs. CONCRETE ARCHITECTURE

### Conceptual Architecture
- How developers **think** of a system
- Derived from **documentation and mental models** (NOT from source code! — True/False trap!)
- Like a **blueprint** of a house
- Shows **essential relations**

### Concrete Architecture
- What **actually exists** in the source code
- Derived by **examining source code**
- Like the **actual house**
- Shows **all implementation-specific relations**

### Why They Don't Match (Linux case study):
1. **Missing relations** in conceptual — more functionality exists than documented
2. **Different mechanisms** used for efficiency (bypassing interfaces)
3. **Developer expediency** — code placed in convenient but wrong subsystems
4. Concrete has FAR more dependencies (37 vs. 19 at top level for Linux)

### What To Do About Mismatches:
1. Restructure to remove unexpected dependencies
2. Refine conceptual architecture to better reflect reality

---

## SECTION 7: REFERENCE ARCHITECTURES

### What Is a Reference Architecture?
- Architecture **template** for ALL systems in a domain
- A product architecture is an **instantiation** of the reference arch
- Benefits: documents proven designs, common vocabulary, aids comparison, improves reuse

### Compiler Reference Architecture:
```
Source → Scanner → Parser → Semantic Analyzer → Code Generator → Binary
                    ↕
              Symbol Table
              Parse Tree (AST)
```

### Web Server Reference Architecture (5 subsystems):
1. **Request Handling** — accepts/manages client connections
2. **Authentication/Authorization** — who can access what
3. **Static/Dynamic Content** — serving files vs. executing scripts
4. **Logging** — recording requests/errors
5. **Configuration** — server settings management

### Web Browser Reference Architecture (8 subsystems):
1. User Interface
2. Browser Engine
3. Rendering Engine
4. Networking
5. JavaScript Interpreter
6. Display Backend
7. Data Persistence
8. Plugin System

### Linux Kernel (5 subsystems — for case study questions):
1. **Process Scheduler (SCHED)** — most central, controls CPU access
2. **Memory Manager (MM)** — virtual memory, swapping
3. **Virtual File System (VFS)** — uses Facade design pattern
4. **Network Interface (NET)** — BSD sockets → INET → TCP/UDP → IP
5. **Inter-Process Communication (IPC)** — signals, pipes, semaphores, shared memory

---

## SECTION 8: DESIGN EXERCISE STRATEGY (50 MARKS)

### Step-by-step approach for Q2:

**Step 1: Read the scenario carefully (2 min)**
- Identify what the system DOES
- Identify the specific USE CASE they give you
- Identify any external systems mentioned

**Step 2: NFRs (5 marks) — MUST be concrete (3 min)**
- Pick 2 NFRs that IMPACT THE ARCHITECTURE
- Always tie them to the SPECIFIC system, not generic
- Common winners: response time, scalability, throughput, integration, accuracy
- Bad answer: "The system should be fast" ← too vague
- Good answer: "Response time — the IDE developer expects code completion suggestions within 200ms of typing, otherwise the interactive experience suffers"

**Step 3: Architectural Styles (10 marks) — Pick 2 styles (5 min)**
- Almost ALWAYS one of these combos:
  - Client-Server + Layered (web apps)
  - Client-Server + Repository (IDEs, complex data systems)
  - Pipe & Filter + Repository (media processing, compilers)
- Explain HOW each style addresses your NFRs
- Don't just define the style — explain WHY it fits THIS system

**Step 4: Sequence Diagram (15 marks) — (15 min)**
- Choose 5-7 components based on the use case
- Walk through the use case step by step
- Include alt/loop where appropriate
- EVERY component should have a clear responsibility

**Step 5: Boxes-and-Arrows (20 marks) — (15 min)**
- Transfer ALL components from sequence diagram into boxes
- Add the client/external actor
- Draw arrows for EVERY interaction in the sequence diagram
- Label each box's purpose
- Clearly indicate which boxes belong to Style 1 vs Style 2
- Use visual grouping (e.g., dashed boundary for layers, or central DB for repository)

### Practice: Generic Template

For ANY system, you likely need these components:
1. **Client/UI** — what the user interacts with
2. **Request Handler / Controller** — receives requests, routes them
3. **Business Logic / Engine** — core processing
4. **Data Store / Repository** — where data lives
5. **External System Interface** — talks to outside services
6. **Plus 1-2 domain-specific** components

---

## SECTION 9: TRUE/FALSE GREATEST HITS (from all 3 quizzes)

Practice these — the exam WILL have them:

| Statement | Answer | Explanation |
|-----------|--------|-------------|
| "$5,000/sec throughput" is sufficient for Amazon's NFR | **WRONG** | Doesn't specify average vs. peak |
| In pub-sub, components don't know each other's identities (opposite of OO) | **TRUE** | In OO you must know the target object's identity to invoke a method |
| "Environment" includes both technical dependencies AND business policies | **TRUE** | Environment = ALL factors impacting the system |
| One view (functional, information, or concurrency) is enough for software structure | **WRONG** | You need ALL 3 — they provide complementary information |
| You can have 3 layers and 1 tier | **TRUE** | Layers are logical, tiers are physical — all layers can be on one machine |
| Conceptual architecture is derived from source code | **WRONG** | It's from documentation/mental models. CONCRETE arch comes from source code |
| A controller receives external messages and calls other components in order | **TRUE** | That's exactly what a controller does |
| nginx source code contains C++ classes named "Master, Worker, etc." | **WRONG** | nginx is written in C, those are conceptual names, not literal classes |
| Every NFR must be in every architectural view | **WRONG** | NFRs crosscut views via perspectives, but not every NFR is in every view |
| Only authentication matters, not authorization | **WRONG** | Both matter — authentication = who are you, authorization = what can you do |
| Sequence diagram = concurrency view | **WRONG** | Sequence diagram is behavioral/interaction, not the concurrency view |
| "Old people everywhere" is an architectural style | **WRONG** | It's a joke — not a real style |

---

## SECTION 10: WHAT TO PUT ON YOUR CHEAT SHEET

### MUST include:
1. **Architectural Styles table** (Section 4 table above — components, connectors, pros, cons)
2. **Rozanski & Woods views** with keywords for matching (Section 3)
3. **NFR categories** with definitions (performance, security, scalability)
4. **Layers vs. Tiers** quick note
5. **Conceptual vs. Concrete** definitions
6. **UML sequence diagram notation** (arrow types, alt/loop boxes)
7. **Boxes-and-arrows rules** (uni-directional arrows!)
8. **Reference architecture** subsystems (compiler, web server, Linux kernel)
9. **True/False greatest hits** (Section 9)

### Probably DON'T need:
- History of programming languages
- Detailed building architecture analogies
- Full paper texts
- Process-Control and Interpreter details (if excluded per revision slide)

---

## SECTION 11: LAST-MINUTE QUICK-FIRE REVIEW

### Q: What's the difference between architecture and design?
A: Architecture = high-level structure (components + connectors), focuses on NFRs, hard to change. Design = low-level details (classes, methods), focuses on FRs, easier to change.

### Q: Name 2 NFRs for [any system] that impact architecture.
A: Pick from: response time, scalability (request load), throughput, availability, security (authentication/authorization), portability, accuracy. ALWAYS give concrete examples tied to the specific system.

### Q: Why can't you focus on all NFRs equally?
A: (1) Too expensive — not enough resources/budget. (2) NFRs contradict each other — e.g., stronger encryption increases response time.

### Q: When to use Repository vs. Layered?
A: Repository = complex central data model with MANY different operations (IDE, compiler, AI). Layered = hierarchical services at different abstraction levels (web apps). If it's a simple CRUD web app, repository is OVERKILL.

### Q: When would pub-sub work/not work?
A: WORKS for: notifications, event handling, plugin systems. DOESN'T WORK for: on-demand data retrieval, main CRUD operations.

### Q: What's a reference architecture?
A: A template/blueprint for ALL systems in a domain. A product arch is an instantiation of it. Examples: compiler ref arch, web server ref arch, OS ref arch.

### Q: How to go from use case → architecture?
A: Use case → Sequence Diagram (identify components + interactions) → Boxes-and-Arrows (structural view of same components)

---

**YOU'VE GOT THIS. The quiz is formulaic — same structure every year. Nail the NFRs, know your styles, draw clean diagrams, and ALWAYS explain WHY.**
