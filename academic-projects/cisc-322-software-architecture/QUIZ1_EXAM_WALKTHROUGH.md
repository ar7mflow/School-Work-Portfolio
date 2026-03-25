# CISC 322 QUIZ 1 — FROM ZERO TO HERO (ELI5 + Step-by-Step Exam Solutions)

**Philosophy:** This guide teaches you ONLY what you need to answer exam questions. Each section walks you through from basic concepts to completing an actual exam question.

---

## PART 1: THE EXAM STRUCTURE (What You're Actually Facing)

Your exam has **2 questions, 100 marks total**:

### Question 1: Short Answers (50 marks) — 40-50 minutes
You'll get 3-5 sub-questions testing theory. Based on actual past exams:
- Identifying Non-Functional Requirements (NFRs) with examples
- True/False statements you must explain why
- Matching architectural information to the correct "view"
- Comparing architectural styles for a scenario

### Question 2: Design Exercise (50 marks) — 60-70 minutes
You get a real-world system description (like "Web Grocer" or "Video Editing Software") with a specific use case (like "customer places an order"). You must:
- Identify 2 NFRs (marks vary: 5-6)
- Pick architectural styles and explain why (marks vary: 10)
- Draw a sequence diagram (marks vary: 14-15)
- Draw a boxes-and-arrows diagram with explanations (marks vary: 20)

**Cheat sheet:** ONE double-sided letter page (8.5"×11")

---

## PART 2: Q1 SUB-QUESTION TYPE #1 — NON-FUNCTIONAL REQUIREMENTS (NFRs)

### What You'll See On The Exam:
> "Google Docs is an online platform allowing anyone to create documents that can be shared with up to 100 collaborators. Provide 3 relevant non-functional requirements."

### Building Block #1: What ARE Requirements? (ELI5)

Imagine you're asking someone to build you a treehouse.

**Functional Requirements** = WHAT it should do
- "It should have a ladder to climb up"
- "It should have a roof to keep rain out"
- "It should fit 3 kids"

**Non-Functional Requirements** = HOW WELL it should do those things
- "The ladder should hold 200 pounds" ← that's about STRENGTH
- "The roof should not leak even in heavy rain" ← that's about QUALITY
- "It should be built in 2 weeks" ← that's about TIME

In software, NFRs are the same — they're about qualities like speed, security, reliability, not about features.

### Building Block #2: The NFR Categories You MUST Know

The exam expects you to identify NFRs and categorize them. Here are the types that appear on exams:

#### Category 1: PERFORMANCE — "How fast/much?"

| Type | What it means | Bad example (too vague) | Good example (specific) |
|------|--------------|------------------------|------------------------|
| **Response Time** | How quickly the system responds to ONE request | "The system should be fast" | "Page loads within 2 seconds" |
| **Throughput** | How much work per unit of time | "Process lots of transactions" | "Process 1000 transactions per second on average, 5000 at peak" |
| **Deadline** | Hard time limit (often real-time systems) | "Be quick" | "Stock trade executes within 100 milliseconds" |

**Critical exam trap:** If you say "process $5,000 worth of transactions per second" for throughput, you MUST specify "average" or "peak" — otherwise it's incomplete!

#### Category 2: SCALABILITY — "Can it handle growth?"

| Type | What it means | Example |
|------|--------------|---------|
| **Request Load** | How many simultaneous users/requests | "Support 10,000 concurrent users" |
| **Data Size** | How much data it can handle | "Store 100TB of documents" |

**Two ways to scale (exam loves this):**
- **Scale Up** (vertical) = Buy a bigger, more powerful server
- **Scale Out** (horizontal) = Buy more servers and split the work

**Which to choose?** Scale Out is better for massive user loads (like ChatGPT) because even the most powerful single server will eventually max out.

#### Category 3: SECURITY — "Is it safe?"

| Type | What it means | Example |
|------|--------------|---------|
| **Authentication** | Proving WHO you are | "User logs in with password" |
| **Authorization** | Proving WHAT you can do | "Only admins can delete files" |
| **Encryption** | Protecting data in transit/storage | "All connections use HTTPS" |
| **Non-repudiation** | Can't deny you did something | "Placing an order creates a binding commitment" |

**Exam trap:** Authentication ≠ Authorization. They're DIFFERENT. Both matter.

#### Category 4: OTHER COMMON ONES

| Type | What it means | Example |
|------|--------------|---------|
| **Availability** | System uptime % | "99.9% uptime (3.65 days downtime per year)" |
| **Portability** | Runs on different platforms | "Works on Windows, Mac, Linux, iOS, Android" |
| **Usability** | Easy to use | "New user can create document in under 1 minute" |
| **Modifiability** | Easy to change | "Can add new file format support in 2 days" |

### Step-by-Step: How To Answer An NFR Question

**EXAM QUESTION (from W2021):**
> "Google Docs allows anyone to create documents shared with 100 collaborators. Provide 3 relevant non-functional requirements."

**STEP 1:** Read the scenario and identify what's SPECIAL about this system (2 minutes)
- It's ONLINE (not desktop)
- 100 COLLABORATORS can edit at the SAME TIME
- Must work across DIFFERENT devices

**STEP 2:** Match those special features to NFR categories (3 minutes)

| What's special | Why it matters | NFR category |
|---------------|----------------|-------------|
| Online | Internet speed varies, users expect quick load | **Response Time** |
| 100 collaborators at once | Many users at same time | **Scalability (Request Load)** |
| Different devices | Must work on phone, tablet, laptop | **Portability** |

**STEP 3:** Write your answer with CONCRETE examples (5 minutes)

❌ **BAD ANSWERS (too vague):**
- "The system should be fast"
- "It should be secure"
- "It should work on many devices"

✅ **GOOD ANSWERS (specific + tied to the scenario):**

**NFR 1: Response Time**
"Google Docs must load a document within 2 seconds on a standard broadband connection (10 Mbps). This is critical because collaborative editing is interactive — if users experience lag while typing, it disrupts the real-time collaboration experience."

**NFR 2: Scalability (Concurrent Users)**
"The system must support at least 100 simultaneous collaborators editing the same document without performance degradation. This requires handling high request loads (potentially 1000+ requests per second from 100 users making frequent edits) and updating all clients in near-real-time."

**NFR 3: Portability**
"Google Docs must function on all major platforms (Windows, macOS, Linux, iOS, Android) and browsers (Chrome, Firefox, Safari, Edge) without requiring platform-specific installations. Since it's accessed via web browser, it must work on any device with internet access."

**Why these are good:**
1. Each has a SPECIFIC, MEASURABLE target (2 seconds, 100 users, all major platforms)
2. Each explains WHY it matters FOR THIS SPECIFIC SYSTEM
3. Each connects to something mentioned in the scenario

---

## PART 3: Q1 SUB-QUESTION TYPE #2 — TRUE/FALSE WITH EXPLANATION

### What You'll See On The Exam:
> "For each statement, decide whether it is right or wrong, and motivate/explain your response."

Typically 5-7 statements worth 2-3 marks each. The explanation is MORE important than just "true" or "false"!

### Building Block: The Concept of "Architectural Views" (ELI5)

Imagine you're building a house. Different people need different drawings:

- **The homeowner** wants to see: "Where's the kitchen? How many bedrooms?" (functionality)
- **The electrician** wants to see: "Where do the wires go? Where are the outlets?" (electrical view)
- **The plumber** wants to see: "Where are the pipes? Where's the water heater?" (plumbing view)
- **The contractor** wants to see: "What order do we build things? What tools needed?" (construction view)

Software is EXACTLY the same! Different people (developers, operators, architects) need different "views" of the same system.

### The 6 Views You MUST Know (Rozanski & Woods)

| View | What it shows | Keywords to spot it | Example statement |
|------|--------------|---------------------|-------------------|
| **Functional** | Components and how they interact | "component depends on", "subsystem responsibilities", "shielding" | "The GUI should not directly access the database" |
| **Information** | Data structures and flow | "data format", "database schema", "valid phone number" | "Every customer must have a valid email" |
| **Concurrency** | Parallel processes, threads, synchronization | "async", "threads", "parallel", "synchronization" | "Messages sent asynchronously to queue" |
| **Development** | How code is organized for building | "file structure", "Git", "testing tools", "coding standards" | "Use Cucumber for acceptance testing" |
| **Deployment** | Physical machines, where things run | "different machine", "server", "3 tiers", "network topology" | "Database on separate server from app" |
| **Operational** | Runtime management, upgrades, monitoring | "restart", "release strategy", "monitoring", "KPIs" | "Use graceful restart for zero downtime" |

### Building Block: Common Architectural Styles (The Big 7)

Think of architectural styles like building styles for houses:

- **Ranch style** = all one floor, spread out
- **Victorian style** = multiple floors, ornate, complex
- **Modern style** = clean lines, open floor plan

Software architectural styles are patterns that work well for certain types of problems.

#### Style 1: **Repository** (The Central Database Pattern)

**ELI5:** Like a library. Everyone comes to ONE central place (the repository) to get information or add information.

**Components:** 
- Central data store (like the library building)
- Independent operators (like librarians, patrons, book delivery services)

**When to use:** When you have complex shared data that many different parts need to access/modify
- Examples: IDEs (code editors), databases, version control systems

**Key characteristic:** The central data store is the STAR of the show. Everything revolves around it.

#### Style 2: **Pipe & Filter** (The Assembly Line Pattern)

**ELI5:** Like a car assembly line. Each station does ONE job, then passes the work to the next station.

**Components:**
- Filters = stations that transform data (add wheels, paint car, install engine)
- Pipes = conveyor belt passing data between filters

**When to use:** Sequential data processing where each step is independent
- Examples: Unix commands (`cat file | grep word | sort`), compilers, video processing

**Key rules:**
- Filters DON'T share state (each does its own thing)
- Filters DON'T know who's before/after them
- Data flows in ONE direction

#### Style 3: **Layered** (The Hierarchy Pattern)

**ELI5:** Like an organization chart. The CEO talks to VPs. VPs talk to managers. Managers talk to workers. But the CEO doesn't directly talk to workers — you go through the chain.

**Components:**
- Layers = groups at the same level (Layer 1 = User Interface, Layer 2 = Business Logic, Layer 3 = Database)

**When to use:** When you have clear levels of abstraction
- Examples: Web applications (3-tier), Operating Systems, Network protocols (OSI model)

**Key rules:**
- Layer N can ONLY talk to Layer N-1 (the layer directly below)
- Lower layers don't know about upper layers

**Layers vs. Tiers (EXAM TRAP):**
- **Layer** = LOGICAL separation (in the code/design)
- **Tier** = PHYSICAL separation (different machines)
- You CAN have 3 layers on 1 tier (all layers on same server)

#### Style 4: **Client-Server** (The Restaurant Pattern)

**ELI5:** Like a restaurant. Customers (clients) ask for food. The kitchen (server) makes the food and sends it back.

**Components:**
- Clients = request services
- Server = provides services
- Network = how they talk

**When to use:** Distributed systems where many users access shared resources
- Examples: Web apps, email, databases

**Key characteristic:** Clients initiate requests. Server waits for requests and responds.

#### Style 5: **Pub-Sub / Implicit Invocation** (The News Broadcast Pattern)

**ELI5:** Like a newspaper or TV news. The news station BROADCASTS news. You SUBSCRIBE to channels you care about. The news station doesn't know/care who's watching.

**Components:**
- Publishers = announce events ("User logged in!", "File changed!")
- Subscribers = listen for events they care about
- Event bus = the broadcast system

**When to use:** Loose coupling, plugins, notifications — when you want components to not depend on each other
- Examples: GUI frameworks, plugin systems, notification systems

**Key rules (EXAM FAVORITE):**
- Publishers DON'T know who's listening
- Subscribers DON'T know who's publishing
- **OPPOSITE of Object-Oriented style** (in OO, you MUST know the target object's identity)

#### Style 6: **Object-Oriented** (The Message Passing Pattern)

**ELI5:** Like sending letters. If you want to send a letter to someone, you MUST know their address (identity).

**Components:** Objects (encapsulated data + operations)
**Connectors:** Method calls

**Key characteristic:** To call a method on Object B, Object A must KNOW Object B's identity

**EXAM TRAP:** In pub-sub, components DON'T know each other's identities. In OO, they MUST know each other's identities. **These are OPPOSITES.**

#### Style 7: **Peer-to-Peer** (The Potluck Dinner Pattern)

**ELI5:** Like a potluck where everyone brings food AND eats food. Everyone is equal — no one person is "in charge."

**Components:** Peers (act as BOTH client AND server)

**When to use:** When you want no central point of failure
- Examples: BitTorrent, Blockchain

**Client-Server vs. Peer-to-Peer:**
- Client-Server = One central authority (restaurant has one kitchen)
- Peer-to-Peer = Everyone equal (potluck has many cooks)

### Step-by-Step: How To Answer True/False Questions

**EXAM QUESTION (from W2023):**
> "In the implicit invocation architectural style, components communicate while being unaware of each other's identities, which is the opposite of the object oriented architectural style."

**STEP 1: Identify what concepts are being tested (30 seconds)**
- Implicit invocation (pub-sub) style
- Object-oriented style
- Whether they're opposites

**STEP 2: Recall the KEY CHARACTERISTIC of each style (1 minute)**
- **Pub-sub:** Publishers announce events, subscribers listen. Publishers DON'T know who's listening. Subscribers DON'T know who's publishing. ← Components DON'T know each other's identities
- **Object-Oriented:** Object A calls a method on Object B. To do this, A MUST know B's identity (like knowing someone's phone number to call them). ← Components MUST know each other's identities

**STEP 3: Compare (30 seconds)**
- Pub-sub = NO knowledge of identity
- OO = MUST have knowledge of identity
- These ARE opposites!

**STEP 4: Write your answer (2 minutes)**

✅ **GOOD ANSWER:**
"**TRUE.** In pub-sub (implicit invocation), components communicate via an event bus. A publisher announces an event without knowing which subscribers (if any) will respond. Similarly, subscribers register for events without knowing which publisher will trigger them. They only need to know about the common event bus/channel.

In contrast, the object-oriented style requires explicit method invocations. For Object A to call a method on Object B, Object A must have a reference to (know the identity of) Object B. This is fundamentally opposite to pub-sub's anonymous communication model."

**Why this is good:**
1. Clear TRUE/FALSE at the start
2. Explains BOTH styles
3. Shows WHY they're opposites
4. Uses course terminology (event bus, method invocations, reference)

### More True/False Examples To Practice:

**QUESTION:** "It is possible to have an architecture consisting of 3 layers and 1 tier."

**ANSWER:** **TRUE.** Layers are LOGICAL partitions of functionality (e.g., presentation layer, business logic layer, data layer). Tiers are PHYSICAL partitions across different machines. All 3 layers can exist on ONE machine (1 tier), such as a small web application where the UI, backend logic, and database all run on the same server.

---

**QUESTION:** "The conceptual architecture can simply be derived by checking the source code implementation."

**ANSWER:** **FALSE.** The conceptual architecture represents how developers THINK about a system — it's derived from documentation, design discussions, and mental models. It's like a blueprint. The CONCRETE architecture is what actually exists in the source code. These often DON'T match because developers take shortcuts, add features not in the original design, or implement things differently than planned. The Linux kernel case study showed conceptual had 19 dependencies while concrete had 37 dependencies.

---

**QUESTION:** "'The system should be able to process $5,000 worth of transactions per second' could be sufficient to describe the throughput NFR for the Amazon webapp."

**ANSWER:** **FALSE.** This is incomplete because it doesn't specify whether $5,000/sec is the AVERAGE or PEAK throughput. During peak periods (Black Friday, Prime Day), Amazon might need 10x or 100x more capacity. Between special events, much lower. A proper NFR would state: "Process $5,000/sec average with $50,000/sec peak capacity during sale events."

---

## PART 4: Q1 SUB-QUESTION TYPE #3 — MATCHING STATEMENTS TO VIEWS

### What You'll See On The Exam:
> "Choose the architectural view that would be best suited to contain the following architectural information."

Then you get 5 statements and must match each to: Functional, Information, Concurrency, Development, Deployment, or Operational.

### The Keyword Cheat Sheet

**If the statement mentions...** | **It's probably this view**
---|---
Component responsibilities, interactions, dependencies | **Functional**
Data formats, schema, "valid X", database structure | **Information**
Threads, async, parallel, synchronization | **Concurrency**
File organization, Git, testing tools, coding standards | **Development**
Different machines, servers, network, tiers | **Deployment**
Restart, upgrades, monitoring, KPIs, releases | **Operational**

### Step-by-Step: Matching Practice

**EXAM QUESTION (from W2023):**

a) "When a new release of the nginx web server is available, we should use its graceful restart capabilities in order not to interrupt the running sessions."

**STEP 1: Find keywords (15 seconds)**
- "new release" = version management
- "restart" = runtime operation
- "not interrupt running sessions" = operational concern

**ANSWER:** **Operational** (manages runtime and upgrades)

---

b) "It is essential to have a valid telephone number registered for every customer and employee."

**STEP 1: Find keywords**
- "valid telephone number" = data constraint
- "for every customer" = data requirement

**ANSWER:** **Information** (data structures and constraints)

---

c) "We will use a behaviour-driven development tool like Cucumber to automate and execute our acceptance tests."

**STEP 1: Find keywords**
- "Cucumber" = development tool
- "execute tests" = development activity

**ANSWER:** **Development** (testing tools and processes)

---

d) "The web application's database should be hosted on a different machine than the one running the application server."

**STEP 1: Find keywords**
- "different machine" = physical separation
- "hosted" = where things run

**ANSWER:** **Deployment** (physical distribution)

---

e) "The client GUI should not directly depend on the database schema, nor be able to trigger automated purchase of supplies; there should be dedicated components shielding the client GUI from these."

**STEP 1: Find keywords**
- "should not directly depend" = component dependency rules
- "dedicated components" = component responsibilities
- "shielding" = separation of concerns

**ANSWER:** **Functional** (component interactions and responsibilities)

---

## PART 5: Q2 — THE DESIGN EXERCISE (50 MARKS)

This is where you design an architecture from scratch. Let me walk you through the COMPLETE process using a real example.

### Example Scenario (Similar to Past Exams):

> **Video Editing Software**
> 
> Video editing software allows users to select source material, cut out bloopers, apply visual effects and titles in real-time. However, transforming videos (adding effects) and compressing for different devices is CPU-heavy batch processing, not real-time.
>
> **USE CASE:** "User should be able to apply and preview visual effects on an input video file, before rendering the results into a new, compressed video file."

You must answer 4 sub-questions. Let me show you how to tackle each one.

---

### SUB-QUESTION 1: Provide 2 NFRs (~5 marks)

**WHAT THEY'RE TESTING:** Can you identify quality attributes specific to THIS system that influence architecture design?

**STEP 1: Read the scenario and highlight what's SPECIAL (2 minutes)**
- "real-time preview" vs. "batch processing rendering"
- "CPU-heavy"
- "different target devices"

**STEP 2: Think about problems this system faces (2 minutes)**
- Users want INTERACTIVE editing (quick feedback)
- But video processing is SLOW
- Need to handle LARGE video files
- Final output must work on MANY devices

**STEP 3: Match to NFR categories (2 minutes)**

| Problem | NFR Category | Specific Requirement |
|---------|-------------|---------------------|
| Interactive editing needs quick feedback | Response Time | Preview effects in < 100ms |
| Slow batch processing | Throughput | Render 1080p video at 30fps minimum |
| Many output devices | Portability | Export to common formats (MP4, MOV, AVI) |
| Large files | Scalability (Data) | Handle 4K videos up to 2 hours |

**STEP 4: Write 2 complete NFRs (5 minutes)**

**NFR #1: Response Time (Interactive Editing)**
"The system must apply and preview visual effects within 100 milliseconds of the user's action (e.g., adjusting a color filter slider). This is critical because video editing is an iterative, interactive process — if there's lag between adjusting an effect and seeing the result, the user experience suffers and editors cannot work efficiently. To achieve this, the preview may use lower resolution or simplified rendering."

**NFR #2: Throughput (Batch Rendering)**
"The final rendering engine must process and compress 1080p video at minimum 30 frames per second (real-time) on standard hardware (4-core CPU). For a 10-minute video, full processing should complete within 30 minutes. This ensures reasonable wait times for users exporting final projects, even though it's a batch operation separate from the interactive editing phase."

**WHY THESE ARE GOOD:**
- Specific + measurable (100ms, 30fps)
- Explain WHY it matters
- Connect to the specific system features (interactive vs batch)
- Address the challenge mentioned (real-time vs slow processing)

---

### SUB-QUESTION 2: Which architectural styles? (~10 marks)

**WHAT THEY'RE TESTING:** Can you pick appropriate styles and explain HOW they address your NFRs?

**STEP 1: Review your NFRs and think about what each style is good for (3 minutes)**

My NFRs:
- Response time for preview ← need fast access to video data + effects
- Throughput for rendering ← need sequential processing pipeline

Style options:
- **Repository:** Good for complex shared data accessed by many operations → Video data is complex (frames, audio, metadata) and many operations (cut, effect, render)
- **Pipe & Filter:** Good for sequential transformations → Rendering is sequential (decode → apply effects → encode)
- **Layered:** Good for separation of concerns → Could separate UI from processing
- **Client-Server:** Good if distributed, but this is likely one machine

**STEP 2: Pick 2 styles that work together (2 minutes)**

Best combo: **Repository + Pipe & Filter**

**STEP 3: Write your explanation connecting styles to NFRs (8 minutes)**

**Style 1: Repository Architecture (for managing video data and interactive editing)**

"I select the Repository style for the core video data management and interactive editing components. The repository (central store) contains:
- The video file's data structure (frames, audio tracks, metadata)
- The current project state (edit timeline, applied effects, markers)

Multiple independent components operate on this repository:
- Preview Generator (reads data, applies effects for quick preview)
- Timeline Manager (tracks cuts and edits)
- Effect Processors (read video data, apply transformations)

**How it addresses NFRs:**
- **Response Time (100ms previews):** The repository keeps all video data and effects in memory/cache, allowing fast access. The Preview Generator can quickly read a subset of frames, apply effects at lower resolution, and display results without waiting for full rendering. This centralized, in-memory access pattern enables the interactive editing experience.
- **Data Management:** Video data is complex with many operations needed. Repository excels at this — IDE architectures use repositories for similarly complex code data."

**Style 2: Pipe & Filter Architecture (for final rendering and export)**

"I select Pipe & Filter for the final rendering pipeline. The filters are sequential processing stages:
- Decoder Filter (reads source video file)
- Effect Application Filter (applies all effects in order)
- Resolution Scaler Filter (scales for target device)
- Encoder/Compressor Filter (outputs MP4/MOV/AVI)

**How it addresses NFRs:**
- **Throughput (30fps rendering):** Pipe & Filter supports concurrent execution — while Filter 1 decodes frame N+1, Filter 2 applies effects to frame N, Filter 3 encodes frame N-1. This pipelining increases throughput. Unix compilers use this pattern for the same reason.
- **Modularity:** Each filter is independent. We can swap the encoder filter to support new formats without changing other filters."

**WHY THIS IS GOOD:**
- Names 2 specific styles
- Defines the components/connectors for each
- Explicitly connects EACH style to the NFRs
- Shows understanding of WHY these styles work (not just definitions)
- References course examples (IDE for repository, compilers for pipe & filter)

---

### SUB-QUESTION 3: Sequence Diagram (~15 marks)

**WHAT THEY'RE TESTING:** Can you translate a use case into a sequence of component interactions?

**THE PROCESS (The Most Important Thing):**

A sequence diagram is NOT about drawing rectangles and arrows randomly. It's a conversation between components to accomplish the use case. Let me show you the system for creating one.

**STEP 1: Break down the use case into micro-steps (5 minutes)**

USE CASE: "User applies and previews visual effects, then renders final compressed video"

Micro-steps:
1. User selects effect (e.g., "Sepia filter")
2. System applies effect to preview
3. System shows preview to user
4. [User is happy with preview]
5. User clicks "Render"
6. System processes full video with effects
7. System compresses video
8. System saves final file

**STEP 2: Identify components based on responsibilities (5 minutes)**

Ask yourself: "Who should handle each step?"

| Step | Component Needed | Why |
|------|-----------------|-----|
| User interacts | **User** (actor) | External to system |
| User sees interface | **UI / Editor Window** | Presentation layer |
| Manages effects | **Effect Manager** | Knows available effects, manages parameters |
| Quick preview | **Preview Renderer** | Fast, low-quality rendering |
| Stores video data | **Video Repository** | Central data store |
| Full render | **Rendering Pipeline** | Batch processing |
| Compression | **Codec Engine** | Format conversion |

**STEP 3: Draw the sequence diagram structure (2 minutes)**

Left to right: User → UI → Effect Manager → Preview Renderer → Video Repository

Below: Rendering Pipeline → Codec Engine

**STEP 4: Add the messages/arrows (3 minutes)**

```
User → UI: SelectEffect("Sepia")
UI → EffectManager: ApplyEffect("Sepia", videoData)
EffectManager → VideoRepository: GetFrameData(currentFrame)
VideoRepository → EffectManager: frameData
EffectManager → PreviewRenderer: RenderPreview(frameData, "Sepia")
PreviewRenderer → EffectManager: previewImage
EffectManager → UI: previewImage
UI → User: DisplayPreview()

[User happy with preview]

User → UI: ClickRender()
UI → RenderingPipeline: StartRender(videoData, effects[])
RenderingPipeline → VideoRepository: GetAllFrames()
VideoRepository → RenderingPipeline: allFrames
loop for each frame
  RenderingPipeline → EffectManager: ApplyAllEffects(frame, effects[])
  EffectManager → RenderingPipeline: processedFrame
end
RenderingPipeline → CodecEngine: Compress(processedFrames, "MP4")
CodecEngine → RenderingPipeline: compressedVideo
RenderingPipeline → UI: RenderComplete(fileName)
UI → User: ShowNotification("Export complete!")
```

**GRADING CRITERIA (from actual exams):**
- /3 for valid sequence diagram syntax (vertical lifelines, arrows between them, readable)
- /6 for having components with appropriate responsibilities
- /6 for correct flow/interactions matching the use case

**COMMON MISTAKES TO AVOID:**
- ❌ Missing the alt/loop boxes for conditional logic
- ❌ Having too few components (need 5-7, not 2-3)
- ❌ Not showing returns (dashed arrows back)
- ❌ Components doing too much (one component shouldn't do everything)

---

### SUB-QUESTION 4: Boxes-and-Arrows Diagram (~20 marks)

**WHAT THEY'RE TESTING:** Can you create a structural view showing how components are organized and connected?

**THE GOLDEN RULE:** Your boxes-and-arrows diagram should have ALL the same components as your sequence diagram, just reorganized to show structure instead of time.

**STEP 1: List all components from your sequence diagram (2 minutes)**

From my sequence diagram:
1. User (external)
2. UI / Editor Window
3. Effect Manager
4. Preview Renderer
5. Video Repository
6. Rendering Pipeline
7. Codec Engine

**STEP 2: Group components by architectural style (3 minutes)**

**Repository Style Group:**
- Video Repository (the central data)
- Effect Manager (operates on repository)
- Preview Renderer (operates on repository)
- Rendering Pipeline (operates on repository)

**Pipe & Filter Style Group:**
- Rendering Pipeline → Codec Engine (sequential pipeline)

**STEP 3: Draw the diagram (10 minutes)**

```
[User]
  |
  ↓
[ UI / Editor Window ]
  |
  ↓
┌─────────────────────────────────────┐
│  REPOSITORY ARCHITECTURE            │
│                                     │
│  ┌──────────────────┐              │
│  │ Effect Manager   │              │
│  └──────────────────┘              │
│         ↕                           │
│  ┌──────────────────┐              │
│  │ Video Repository │ ← CENTRAL    │
│  │ (stores frames,  │    STORE     │
│  │  effects, state) │              │
│  └──────────────────┘              │
│         ↕                           │
│  ┌──────────────────┐              │
│  │ Preview Renderer │              │
│  └──────────────────┘              │
└─────────────────────────────────────┘
         ↓
         (for final export)
         ↓
┌─────────────────────────────────────┐
│  PIPE & FILTER ARCHITECTURE         │
│                                     │
│  [Rendering Pipeline] →             │
│    [Codec Engine] →                 │
│      [File Output]                  │
│                                     │
└─────────────────────────────────────┘
```

**STEP 4: Write explanations for each component (7 minutes)**

**Component Explanations:**

1. **UI / Editor Window** (Functional View)
   - Handles all user interactions
   - Displays video timeline and preview
   - Sends user commands to appropriate components

2. **Effect Manager** (Repository Operator)
   - Maintains catalog of available effects (Sepia, Blur, Sharpen, etc.)
   - Applies effects to video data by reading from repository
   - Manages effect parameters (intensity, timing)

3. **Video Repository** (Central Data Store — Repository Style)
   - Stores ALL video project data: raw frames, audio, metadata, edit timeline
   - Provides centralized access for all components
   - Keeps frequently-accessed data in memory for fast preview performance

4. **Preview Renderer** (Repository Operator)
   - Generates low-resolution, real-time previews
   - Reads small frame subset from repository
   - Optimized for speed over quality (100ms NFR)

5. **Rendering Pipeline** (Pipe & Filter — Filter 1)
   - Batch processes entire video with all effects
   - Reads all frames from repository sequentially
   - Applies effects at full quality (slower but thorough)

6. **Codec Engine** (Pipe & Filter — Filter 2)
   - Receives processed frames from pipeline
   - Compresses to target format (MP4, MOV, AVI)
   - Outputs final file

**Interaction Explanations:**

- UI ↔ Effect Manager: UI sends user effect selections, Effect Manager returns preview
- Effect Manager ↔ Repository: Reads video data, writes effect metadata
- Preview Renderer ↔ Repository: Fast reads of small frame sets
- Rendering Pipeline ↔ Repository: Batch reads of all frames
- Rendering Pipeline → Codec Engine: Sequential pipe passing processed frames

**Mapping to Styles:**

**Repository Architecture** includes:
- Video Repository (the shared data store)
- Effect Manager, Preview Renderer (independent operators on the repository)

**Pipe & Filter Architecture** includes:
- Rendering Pipeline → Codec Engine (sequential filters with data flowing through pipes)

These styles work together:
- Repository handles the interactive editing phase (fast access needed)
- Pipe & Filter handles the batch export phase (throughput needed)

**GRADING CRITERIA (from actual exams):**
- /7 for having all boxes from sequence diagram + client/user
- /7 for having arrows/connections matching all invocations from sequence diagram
- /6 for explaining components and mapping to chosen architectural styles

**CRITICAL RULES:**
- Arrows are UNI-DIRECTIONAL (A → B, not A ↔ B)
- If A calls B in sequence diagram, there MUST be an arrow A → B
- Use visual grouping (boxes, dashed lines) to show which components belong to which style

---

## PART 6: RAPID-FIRE KNOWLEDGE DUMPS (For Your Cheat Sheet)

### The Styles Comparison Table (MUST HAVE ON CHEAT SHEET)

| Style | Components | Connectors | One-line Use Case | #1 Pro | #1 Con |
|-------|-----------|------------|-------------------|--------|--------|
| Repository | Central store + operators | Memory/calls | Complex shared data w/ many ops | Efficient sharing via schema | Must agree on schema upfront |
| Pipe & Filter | Filters (transformers) | Pipes (streams) | Sequential data transformations | Easy to understand as composition | Bad for interactive systems |
| Layered | Layer groups | Restricted calls | Hierarchical abstraction levels | Easy enhancement/reuse | Performance penalties |
| Client-Server | Clients + servers | Network | Distributed systems | Transparent location | Network dependent |
| Pub-Sub | Publishers + subscribers | Event bus | Loose coupling / plugins | Strong reuse, easy evolution | No control over order/responses |
| OO | Objects | Method calls | Data encapsulation | Hidden representation | Must know other's identity, side effects |
| P2P | Peers | Direct connections | No central authority | No single failure point | Cliques can disconnect |

### TRUE/FALSE Killer List

| Statement | Answer | One-sentence Why |
|-----------|--------|------------------|
| $5K/sec throughput is sufficient NFR | FALSE | Must specify average vs. peak |
| Pub-sub components don't know identities (opposite of OO) | TRUE | Pub-sub uses event bus, OO requires direct reference |
| Environment includes technical + non-technical factors | TRUE | Policies, regulations, cloud, hardware all count |
| Need all 3 of Functional + Information + Concurrency for software structure | TRUE | They're complementary, not alternatives |
| Can have 3 layers, 1 tier | TRUE | Layers = logical, tier = physical |
| Conceptual arch from source code | FALSE | It's from docs/mental model; CONCRETE arch from code |
| Controller receives external messages, calls others | TRUE | That's exactly a controller's role |
| Every NFR in every view | FALSE | NFRs crosscut via perspectives, but not all in all |
| Only authentication matters, not authorization | FALSE | BOTH matter — who you are vs. what you can do |

### View Matching Speed Sheet

**If statement says...** → **View is...**
- "different machine / server / tier" → Deployment
- "restart / upgrade / release" → Operational
- "valid data / schema / format" → Information
- "component depends / shields / interacts" → Functional
- "async / threads / parallel" → Concurrency
- "Git / testing tool / file structure" → Development

---

## PART 7: YOUR 60-MINUTE EXAM BATTLE PLAN

### Time Allocation (for 120min exam):

| Section | Time | Strategy |
|---------|------|----------|
| Q1.1 NFRs | 10 min | 2 min read, 3 min identify categories, 5 min write |
| Q1.2 True/False (5 statements) | 15 min | 3 min each: 30s identify concept, 1m recall facts, 1.5m write |
| Q1.3 View matching | 10 min | 2 min per statement (5 statements) |
| Q1.4 Other short answer | 15 min | Depends on question |
| Q2.1 NFRs | 9 min | 2 min identify special features, 2 min match to categories, 5 min write |
| Q2.2 Styles | 13 min | 3 min review NFRs/recall styles, 2 min pick, 8 min explain |
| Q2.3 Sequence diagram | 25 min | 5 min micro-steps, 5 min identify components, 3 min structure, 10 min draw, 2 min review |
| Q2.4 Boxes-and-arrows | 20 min | 2 min list components, 3 min group by style, 10 min draw, 5 min write explanations |
| **Buffer** | 3 min | For review/overflow |

### The Night Before:

1. **Create your cheat sheet** with the tables above
2. **Practice drawing** one sequence diagram and one boxes-and-arrows diagram from scratch
3. **Memorize** the 6 views and their keywords
4. **Memorize** the True/False greatest hits
5. Get sleep — you're prepared

### The Morning Of:

- Eat breakfast (your brain needs glucose)
- Bring 2 pens (in case one dies)
- Bring your cheat sheet
- Arrive 10 minutes early

### During The Exam:

1. **First 5 minutes:** Read ENTIRE exam, identify easiest questions, plan time allocation
2. **Q1:** Do easiest sub-questions first to build confidence
3. **Q2:** Read scenario 3 times, highlight key phrases
4. **For sequence diagrams:** FIRST write the micro-steps list, THEN draw
5. **For boxes-and-arrows:** FIRST list all components, THEN organize by style, THEN draw
6. **Last 5 minutes:** Review for missing labels, unclear arrows, incomplete explanations

---

## YOU'RE READY.

This exam is NOT about memorizing 200 pages of slides. It's about:
1. Identifying NFRs with concrete examples
2. Picking architectural styles that match NFRs
3. Drawing sequence diagrams that show interactions
4. Drawing boxes-and-arrows that show structure

You now know how to do all 4. Practice each one ONCE tonight, then rest. See you on the other side with that A.
