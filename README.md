# Yiğit Sarp Avcı

I am a Computer Engineering student at **Boğaziçi University**, Junior Consultant at **180 Degrees Consulting - Boğaziçi Branch**, and Backend Developer Intern at **DefineX | Consulting, Technology & Labs**, previously interning at **Akbank** (SRE) and **Smash Mate** (Software Engineering).

My focus spans the entire computing stack—from low-level systems programming and processor architecture to scalable enterprise backends and algorithmic FinTech platforms—combining strong theoretical computer science foundations with modern, AI-assisted product development.

---

### Education

- **Boğaziçi University** — B.Sc. in Computer Engineering *(09/2023 – Expected 06/2028)*
  - **Extracurriculars & Athletics:** Executive Board Member & DJ at Radyo Boğaziçi; Active Member at ESTIEM; Work and Travel USA; Student-Athlete (sailing, skiing & windsurfing).
  - **Volunteering & Mentorship:** Volunteering Division Member at Industrial Engineering Club (BÜYAK); Educational Mentor to high school students.
- **Kabataş Boys' High School** *(09/2018 – 06/2023 · GPA: 3.78/4.00)*
  - **Extracurriculars:** Debate, Model United Nations (MUN), Entrepreneurship, and Coding Clubs.
  - **Volunteering:** Community Involvement Projects Club and TOÇEV (Tüvana Okuma İstekli Çocuk Eğitim Vakfı).

---

### Experience

- **Junior Consultant** — **180 Degrees Consulting - Boğaziçi Branch** *(10/2026 – Present)*
  - Delivering strategic advisory for social enterprises and non-profits, uncovering growth opportunities via data-driven market research and stakeholder benchmarking.
  - Formulating operational roadmaps and financial impact models, optimizing resource allocation and project reach through qualitative and quantitative analyses.
- **Backend Developer Intern** — **DefineX | Consulting, Technology & Labs** *(09/2026 – Present)*
  - Developing internal data processing platforms and Model Context Protocol (MCP) integrations, streamlining operational workflows for corporate teams by automating enterprise data extraction and RESTful backend pipelines.
  - Leveraging AI-assisted engineering workflows to accelerate enterprise backend feature delivery, implementing schema validation and API throughput optimization.
- **Site Reliability Engineering Intern** — **Akbank** *(07/2026 – 09/2026)*
  - Maintained high availability for mission-critical core banking infrastructure by designing real-time observability dashboards and proactive alerting thresholds in Dynatrace and Grafana.
  - Engaged in Linux systems engineering, server health diagnostics, and log analysis to accelerate incident detection and root-cause resolution across high-throughput production nodes.
- **Software Engineering Intern** — **Smash Mate** *(06/2026 – 07/2026)*
  - Engineered player matchmaking, search discovery, and scoring microservices using Java (Quarkus), designing high-performance RESTful endpoints and core game-matching domain logic.
  - Developed responsive mobile interfaces in React Native and authored comprehensive unit and integration test suites, delivering a fully tested pre-launch release.

---

### Technical Skills

- **Programming Languages:** Python, Java, C (C11), C++ (C++17), TypeScript, JavaScript, SQL, Bash, Assembly (x86-64, RISC-V), SystemVerilog
- **Backend & Systems:** Quarkus, FastAPI, Express, Microservices Architecture, RESTful APIs, WebSockets, Linux Syscalls, POSIX IPC, Multithreading (Pthreads)
- **Frontend & Mobile:** Next.js (App Router), React, React Native, Expo, WebAssembly (WASM), Qt 6, Tailwind CSS, Zustand
- **Databases & Storage:** PostgreSQL, SQLite, Prisma ORM, TypeORM, SQLAlchemy
- **DevOps, Testing & Tools:** Docker, Docker Compose, Linux/Unix, Git/GitHub, CI/CD (GitHub Actions), Jest, Pytest, Grafana, CMake, Make, AI-Assisted Development

---

### Projects

#### Quantitative FinTech & Real-Time Trading

- **[Algorithmic Trading & Execution Engine](https://github.com/yigitsarpavci/algorithmic-trading-simulator)** — Real-Time Quantitative Trading Terminal & Execution Engine
  - Quantitative trading engine running a V8 Risk-First strategy on a 2-second simulation loop with Z-Score mean reversion, dynamic volatility-adjusted sizing, and a 4-state exit machine.
  - Streams real-time order book depth, execution logs, and P&L metrics to a Next.js terminal UI via full-duplex FastAPI WebSockets and Docker Compose, with a pytest suite and GitHub Actions CI.
  - **Tech Stack:** `Python 3.11+`, `FastAPI`, `Next.js 14`, `PostgreSQL`, `WebSockets`, `pytest`, `Z-Score Strategy`, `Docker`

- **[Financial Analytics Dashboard](https://github.com/yigitsarpavci/financial-analytics-dashboard)** — Personal Finance & Portfolio Risk Platform
  - Educational full-stack personal finance and portfolio risk platform built with Next.js 16 (App Router), FastAPI, SQLAlchemy, Alembic, PostgreSQL (`psycopg2`), and Docker Compose.
  - Implements categorical cash-flow analytics, weighted multi-asset diversification scoring, and context-aware AI advisory insights via OpenAI with deterministic rule fallbacks.
  - **Tech Stack:** `Next.js 16`, `FastAPI`, `Python`, `PostgreSQL (psycopg2)`, `SQLAlchemy`, `Docker / Docker Compose`, `OpenAI API`, `Recharts`

#### Biometric Telemetry & Sports Analytics

- **[Garmin Athlete Analytics Platform](https://github.com/yigitsarpavci/garmin-athlete-analytics-platform)** — Biometric Telemetry, Model Context Protocol (MCP) & Performance Analytics Engine
  - End-to-end biometric telemetry platform ingesting 93 days of raw Garmin Connect data, `1 Hz` binary `.fit` sensor streams, 5-min overnight HRV RMSSD, and Running Dynamics via the Model Context Protocol (MCP) with adaptive SSO keep-alive.
  - Combines Acute:Chronic Workload Ratio (ACWR) injury-risk modeling and flexible weekly quota periodization with a single-screen (`100vh`) deep-forest dark dashboard (`Chart.js`), LLM coaching fallbacks, synthetic demo mode, a native macOS desktop app, and a 99-test suite.
  - **Tech Stack:** `Python 3.12`, `Python HTTP Server`, `Model Context Protocol (MCP)`, `Binary .FIT Parser`, `NumPy / Pandas`, `Chart.js`, `Playwright`, `Unittest`

#### Full-Stack SaaS & Enterprise Backends

- **[Enterprise Operations & Knowledge Platform](https://github.com/yigitsarpavci/enterprise-admin-dashboard)** — Operations, Workforce Delegation & Knowledge Base Platform
  - Full-stack enterprise platform coupling workforce task delegation and work-logging with a decoupled Express 5 REST API and Knowledge Base (SOP/FAQ) engine.
  - Implements department productivity comparisons (Recharts), TypeORM DataMapper with in-memory SQLite isolation, SWR optimistic updates, and end-to-end Supertest API integration suites. The Express API is protected by the same signed session as the Next.js app (401 unauthenticated, 403 for non-admin writes).
  - **Tech Stack:** `Next.js 16`, `Express 5`, `TypeScript`, `TypeORM`, `Prisma`, `SWR`, `Jest`, `Supertest`, `Recharts`, `Tailwind CSS`, `jose (JWT)`

- **[Restaurant Operations & Table Management SaaS](https://github.com/yigitsarpavci/restaurant-floor-plan-saas)** — Multi-Tenant Table Management & Live-Ops Platform
  - Multi-tenant SaaS platform with slug-based tenant isolation (`/manage/[tenantSlug]`), interactive drag-and-drop floor plan builder (`react-rnd`), and real-time coordinate persistence.
  - Features a live-ops console for waitstaff with walk-in queues and multi-table merging, powered by Zustand global state and end-to-end Zod validation. Secured with signed httpOnly session cookies, bcrypt password hashing and per-action tenant authorization.
  - **Tech Stack:** `Next.js 16`, `TypeScript`, `Prisma`, `PostgreSQL`, `Zustand`, `Tailwind CSS`, `react-rnd`, `Zod`

#### Systems Programming & Computer Architecture

- **[Low-Level Systems & Computer Architecture Lab](https://github.com/yigitsarpavci/low-level-systems-lab)** — x86-64 Scheduler, Bare-Metal RISC-V, C11 Shell, CoreMark, Pipeline & Cache Hierarchy
  - Unified systems and architecture laboratory featuring a zero-libc x86-64 process scheduler (direct Linux syscalls), bare-metal RV32I flight pathfinding on Spike (`.ld` memory mapping), and a modular C11 Unix shell with grammar backtracking.
  - Combines CoreMark compiler optimization profiling (`-O0` to `-Ofast`) across Apple Silicon and RISC-V extensions with 5-stage RISC-V processor pipeline simulation (`Verilator`, `GTKWave`) and set-associative L1/L2 write-back cache hierarchy analysis.
  - Also includes the **[Linux IPC Game Subsystem](https://github.com/yigitsarpavci/low-level-systems-lab/tree/main/07-linux-ipc-game-subsystem)** (module 07): a real-time 60 FPS terminal game decoupled from its input controllers via non-blocking named pipes (`O_NONBLOCK` FIFOs), POSIX signals (`SIGUSR1`, `SIGTERM`), lock-free ring buffers and runtime `dlopen`/`dlsym` hot-swapping, verified by a dependency-free C test suite (443 checks) in CI.
  - **Tech Stack:** `x86-64 Assembly`, `RISC-V`, `C11`, `Linux Syscalls`, `POSIX IPC`, `Named Pipes`, `dlopen`, `Verilator`, `Spike Simulator`, `ARM64`, `Clang/LLVM`, `GNU Toolchain`

#### Mobile & WebAssembly

- **[Cross-Platform & WebAssembly Game Lab](https://github.com/yigitsarpavci/cross-platform-game-lab)** — C++/Qt6 WASM & React Native Mobile Architecture · [Live Demo](https://yigitsarpavci.github.io/cross-platform-game-lab/)
  - Unified game engineering lab featuring a cross-platform 2048 puzzle engine engineered in C++17/Qt 6 compiled to WebAssembly via Emscripten, and an Expo/React Native Minesweeper mobile application.
  - Implements directional grid normalization, an infinite undo history stack (`std::stack`) with deep-copy snapshots, non-recursive iterative BFS flood-fill preventing call-stack overflows, and hardware haptics.
  - **Tech Stack:** `C++17`, `Qt 6`, `WebAssembly (WASM)`, `CMake`, `Emscripten`, `React Native`, `Expo`, `TypeScript`, `Iterative BFS`

#### Algorithms & Data Structures

- **[Advanced Data Structures & Algorithms Suite](https://github.com/yigitsarpavci/data-structures-and-algorithms-suite)** — Graph Theory, Priority Allocators, AST Interpreter & Complexity Analysis
  - Curated algorithms and computational theory suite implementing Tarjan's Strongly Connected Components (SCC) and articulation points in $O(V + E)$ linear time, dynamic freelance matching via indexed max-heaps in $O(\log N)$ time, and a custom functional language interpreter with dual lexical/dynamic scoping.
  - Combines custom memory-efficient adjacency lists, open-addressing hash maps, and AST evaluation with closed-form asymptotic and probabilistic complexity modeling ($\Theta(n \log n)$ to $\Theta(n^3)$) verified via Monte Carlo and exhaustive $3^n$ benchmarks.
  - **Tech Stack:** `Java`, `Python`, `Graph Theory (Tarjan SCC)`, `Dynamic Max-Heaps`, `AST Tree Traversal`, `Complexity Modeling`

---

### Languages

- **Turkish:** Native · **English:** Advanced / Professional Working Proficiency · **German:** Beginner / Elementary

### Hobbies & Interests

- Wakeboarding, Kiteboarding, Surfing, Bouldering, Running, Traveling

### Resume

- **CV / Resume:** [View / Download (PDF)](./cv/cv.pdf)
