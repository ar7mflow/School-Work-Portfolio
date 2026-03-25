# CISC 322 MIDTERM — ONE-PAGE CHEAT SHEET (Print Double-Sided)
## Ultra-Condensed Reference for 2-Hour Exam

---

## SIDE 1: Q1 MASTERY (Short Answers - 50 marks)

### A. NFR CATEGORIES — Q1 Worth 15 marks (GUARANTEED)

| **Category** | **Type** | **Good Example** | **Bad Example** |
|--------------|----------|------------------|-----------------|
| **Performance** | Response Time | "Page loads <2s on 10Mbps" | "Fast" |
| | Throughput | "1000 tx/sec **avg**, 5000 **peak**" | "$5K/sec" ❌ no avg/peak |
| | Deadline | "Trade executes <100ms" | "Quick" |
| **Scalability** | Request Load | "10K concurrent users" | "Many users" |
| | Scale Up | More powerful server (simpler) | |
| | Scale Out | More servers (better for massive loads) | |
| **Security** | Authentication | WHO you are (login/password) | |
| | Authorization | WHAT you can do (permissions) | ≠ Authentication! |
| | Encryption | Protect data (HTTPS/TLS) | |
| | Non-repudiation | Can't deny action (binding order) | |
| **Other** | Availability | 99.9%=8.76hr/yr down, 99.99%=52.6min/yr | |
| | Portability | "Windows, Mac, Linux, iOS, Android" | |
| | Usability | "New user creates doc <1 min" | |
| | Modifiability | "Add file format in 2 days" | |

**NFR MUST be:** Verifiable, Traceable, Ranked by importance, Ranked by stability  
**NFR TRAP:** Throughput without avg vs peak = INCOMPLETE (Black Friday spike!)
**Why can't focus on all NFRs?** (1) Limited resources (2) NFRs contradict (security↔performance)

---

### B. ARCHITECTURAL VIEWS MATCHING — Q1 Worth 15 marks

| **View** | **Shows** | **Keywords → This View** |
|----------|-----------|-------------------------|
| **Functional** | Components, responsibilities, interactions | "depends on", "shielding", "component should not", responsibility |
| **Information** | Data structures, constraints, flow | "valid format", "schema", "phone #", "decimal", "constraint" |
| **Concurrency** | Threads, sync, parallel processing | "thread", "async", "parallel", "sync", "concurrent", "lock" |
| **Development** | Code org, build tools, testing | "Git", "Cucumber", "convention", "file naming", "header files" |
| **Deployment** | Physical machines, network, where runs | "machine", "server", "hosted", "tier", "network topology" |
| **Operational** | Runtime mgmt, upgrades, monitoring | "restart", "upgrade", "monitor", "rollback", "release", "KPI" |

**CRITICAL:** Need ALL 3 (Functional + Information + Concurrency) for "software structure" — complementary!

---

### C. TRUE/FALSE GREATEST HITS — Q1 Worth 15 marks

| **Statement** | **T/F** | **Why (2-3 sentences)** |
|---------------|---------|------------------------|
| "$5K/sec throughput for Amazon" | **F** | Doesn't specify avg vs peak (spikes 10-100×!) |
| "Pub-sub: unaware identities = opposite OO" | **T** | Pub-sub uses event bus; OO needs direct reference |
| "Environment = tech + non-tech" | **T** | HW/cloud/OS + policies/regulations/business |
| "One view (Func/Info/Concur) enough" | **F** | Need ALL 3 — complementary info |
| "3 layers, 1 tier possible" | **T** | Layer=logical, Tier=physical. All on 1 machine OK |
| "Conceptual arch from source code" | **F** | Conceptual=docs/mental. CONCRETE=code |
| "Controller receives msgs, calls in order" | **T** | Exactly what controller does |
| "nginx has C++ classes Master/Worker" | **F** | nginx is C — conceptual names not literal |
| "MVC is architectural style" | **F** | MVC = DESIGN PATTERN in layer |
| "Focus equally on all NFRs" | **F** | Resource limits + NFRs contradict |
| "Authentication only, no authorization" | **F** | BOTH needed — WHO ≠ WHAT |
| "Blackboard = Repository exactly" | **F** | Blackboard ⊆ Repository (collaborative subset) |
| "Pipe-Filter can share state" | **F** | NO shared state = key invariant! |
| "Scale Up better for massive loads" | **F** | Scale OUT better (no physical limit) |

---

### D. KEY DEFINITIONS (4-8 marks each)

**Architecture vs Design:**
| Architecture | Design |
|--------------|--------|
| High-level (components) | Low-level (classes/methods) |
| NFRs (quality) | FRs (functionality) |
| Hard to change | Easier to change |
| Multiple views | Detailed blueprint |

**Conceptual vs Concrete:**
| Conceptual | Concrete |
|------------|----------|
| Mental model (docs) | Actual code |
| Essential relations | ALL relations |
| Blueprint | Actual building |

**Why mismatch?** Missing docs, efficiency shortcuts, code in wrong places  
**Example:** Linux — 19 deps (conceptual) vs 37 deps (concrete)

**Stakeholder ⊃ User:**
- Stakeholder = ANYONE with interest (users, devs, managers, regulators, customers)
- User = Subset who directly USE system
- All users are stakeholders ≠ vice versa
- Draw Venn: Users inside Stakeholders circle

**Good Requirements 4 Criteria:**
1. **Verifiable:** Can test/measure ("load <2s" testable vs "be fast" not)
2. **Traceable:** Link to source (stakeholder) AND implementation (code)
3. **Ranked importance:** Limited resources → prioritize critical
4. **Ranked stability:** Unstable reqs → isolate behind interfaces

**Layer vs Tier:**
- Layer = LOGICAL partition (presentation, business, data layers)
- Tier = PHYSICAL partition (client machine, app server, DB server)
- **3 layers on 1 tier = VALID** (all layers same machine)

---

## SIDE 2: ARCHITECTURAL STYLES + Q2 DESIGN (50 marks)

### E. ARCHITECTURAL STYLES REFERENCE TABLE

| **Style** | **Components** | **Connectors** | **Best For** | **Advantages** | **Disadvantages** |
|-----------|----------------|----------------|--------------|----------------|-------------------|
| **Repository** | Central data store + operators | Procedures, memory | Complex shared data (IDE, compiler, AI) | Efficient storage, centralized, schema sharing | Must agree schema, hard to distribute |
| **Pipe & Filter** | Filters (transformers) | Pipes (data stream) | Sequential processing (Unix, compilers) | Reuse, composition, concurrency | Bad for interactive, parsing overhead |
| **Object-Oriented** | Objects (data+ops) | Method calls | Data protection, modularity | Hidden representation, autonomy | Must know other's identity, side effects |
| **Pub-Sub** | Publishers/Subscribers | Event bus | Loose coupling (notifications, plugins) | Strong reuse, easy evolution | No control over order, unreliable responses |
| **Layered** | Layers (proc groups) | Proc calls (restricted) | Hierarchical (OS, network, web apps) | Abstraction levels, easy enhance | Not all fit, performance hit |
| **Client-Server** | Clients + Servers | Network | Distributed (web, email, DB) | Easy distribution, transparent location | Network dependent, complex design |
| **Peer-to-Peer** | Peers (client+server) | Direct network | Decentralized (file share, games) | No single point failure, resilient | Cliques disconnect, no guaranteed response |
| **Interpreter** | Execution engine + memory | Procedures, memory | VMs, scripting | Hardware simulation, portability | Complex, slower execution |

**EXCLUDED FROM QUIZ 1:** Interpreter, Process-Control (per Quiz1Revision slide)

---

### F. STYLE SELECTION DECISION TREE

**Complex central data + many ops → Repository** (IDE, compiler, editor)  
**Sequential transformations → Pipe & Filter** (Unix, video, compilers)  
**Web/network users → Client-Server** (+ Layered for tiers)  
**Events/notifications/plugins → Pub-Sub** (NOT for CRUD!)  
**No central authority → Peer-to-Peer** (blockchain, file sharing)

**Common combos:**
- Web app: Client-Server + Layered
- IDE/LSP: Client-Server + Repository
- Video editor: Pipe & Filter + Repository
- Notification system: Pub-Sub

---

### G. STYLE INVARIANTS (True/False favorites)

**Pipe & Filter:**
1. Filters DON'T share state
2. Filters DON'T know upstream/downstream identity
3. Data flows ONE direction

**Pub-Sub:**
- Publishers DON'T know subscribers
- Subscribers DON'T know publishers
- **OPPOSITE of OO** (OO requires knowing identity)

**Repository:**
- Blackboard = when multiple clients COLLABORATE
- Clients access/modify shared data

---

### H. UML SEQUENCE DIAGRAM CHEATSHEET (15 marks Q2)

**Elements:**
- Actor (stick figure) — external entity
- Component (rectangle) — system part
- Lifeline (dashed line) — time flows DOWN
- Activation box (thin rect on lifeline) — active processing
- Solid arrow → sync call (waits for reply)
- Dashed arrow ← return/reply
- `alt` box — if/else conditional
- `loop` box — repeated actions
- `par` box — parallel execution

**Grading:** /3 valid structure, /6 right components, /6 correct flows

**MUST:** Map 1-to-1 to use case, include return to Actor at end

---

### I. BOXES-AND-ARROWS DIAGRAM RULES (20 marks Q2)

**CRITICAL RULES:**
1. **UNI-DIRECTIONAL arrows ONLY** (if A calls B → arrow A→B, NEVER ↔)
2. **ALL components from sequence diagram MUST appear** + client/actor
3. **Every interaction in sequence = arrow in boxes**
4. Label each box's purpose
5. Show which boxes belong to which style (group/mark)

**Grading:** /7 all components, /7 arrows match sequence, /6 map to styles

---

### J. REFERENCE ARCHITECTURES (Know subsystems)

**Compiler:**
Source → Scanner → Parser → Semantic Analyzer → Code Generator → Binary  
(+ Symbol Table, Parse Tree shared repository)

**Web Server (5 subsystems):**
1. Request Handling (accept connections)
2. Authentication/Authorization
3. Static/Dynamic Content
4. Logging
5. Configuration

**Linux Kernel (5 subsystems):**
1. Process Scheduler (SCHED) — most central
2. Memory Manager (MM)
3. Virtual File System (VFS) — uses Facade pattern
4. Network Interface (NET)
5. Inter-Process Communication (IPC)

---

### K. Q2 DESIGN EXERCISE TIME MANAGEMENT (50 marks, 60-70 min)

**Read scenario:** 3 min  
**2.1 NFRs (5 marks):** 5 min — Pick 2, be SPECIFIC with numbers  
**2.2 Styles (10 marks):** 8 min — Name 2, define briefly, WHY for THIS system  
**2.3 Sequence (15 marks):** 15-20 min — Walk through use case step-by-step  
**2.4 Boxes-arrows (20 marks):** 15-20 min — All components, uni-directional arrows, map styles  
**Review:** 5 min

**Generic components for ANY system:**
1. Client/UI — user interacts
2. Request Handler/Controller — receives, routes
3. Business Logic/Engine — core processing
4. Data Store/Repository — data lives
5. External System Interface — talks to outside
6. + 1-2 domain-specific

---

### L. QUICK REFERENCE: EXAM PATTERN (100% consistent)

**Q1: Short Answers (50 marks) — 40-50 minutes**
- NFRs identification: 15 marks (100% appears)
- True/False with explanation: 15 marks (100% appears)
- Views matching: 15 marks (90% appears)
- Definitions/other: 5 marks (varies)

**Q2: Design Exercise (50 marks) — 60-70 minutes**
- 2.1 NFRs: 5-6 marks
- 2.2 Style selection: 10 marks
- 2.3 Sequence diagram: 14-15 marks
- 2.4 Boxes-and-arrows: 20 marks

**Cheat sheet allowed:** ONE 2-sided letter (8.5"×11")  
**Format:** Closed-book, in-person, 120 minutes

---

### M. LAST-MINUTE MEMORY HOOKS

**NFR reminder:** "Performance Scales Securely Available" (Perf, Scale, Sec, Avail)  
**Views:** "FIDDeO" (Func, Info, Dev, Deploy, Operational) + Concurrency  
**Pub-Sub vs OO:** "Anonymous bus vs direct phone call"  
**Layers vs Tiers:** "Logical cake layers vs physical wedding cake tables"  
**Scale Out vs Up:** "Clone army vs Hulk" (many vs one powerful)  
**Pipe invariants:** "No sharing, No knowing, One way" (state, identity, flow)

---

**EXAM STRATEGY:**
✅ Do NOT write until you've read ENTIRE question
✅ For NFRs: ALWAYS include numbers/measurable criteria tied to scenario  
✅ For T/F: 2-3 sentences MINIMUM explaining WHY  
✅ For sequence: Walk through use case literally step-by-step  
✅ For boxes: Count components in sequence, ensure ALL appear + arrows match  
✅ Cite course terminology (event bus, facade, abstraction layer, quality attributes, etc.)

**GOOD LUCK! 🚀**
